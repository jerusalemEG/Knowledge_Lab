"""
Knowledge Lab - Unified Quranic Cosmic Architecture Engine (v5.0 Ultimate Synthesis)
Merges knowledge_graph_viewer and Prophetic_Cosmic_Atlas into a single supreme engine
anchored completely in the Holy Quran, connecting all 12 master manuscripts,
the 7 Heavenly Spheres, the Universal Throne Sphere, the 12 Zodiac Signs,
and the Five Arch-Prophets (Ulul Azm).
"""

import os
import re
import json
import sys
from pathlib import Path

# Force UTF-8 on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

VAULT_DIR = Path(__file__).resolve().parent.parent / "02_vault"
OUTPUT_JSON = Path(__file__).resolve().parent / "knowledge_graph.json"
OUTPUT_HTML_1 = Path(__file__).resolve().parent.parent / "knowledge_graph_viewer.html"
OUTPUT_HTML_2 = Path(__file__).resolve().parent.parent / "Prophetic_Cosmic_Atlas.html"
OUTPUT_HTML_WEB = Path(__file__).resolve().parent.parent / "website" / "index.html"

WIKILINK_PATTERN = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
TAG_PATTERN = re.compile(r"(?:^|\s)#([a-zA-Z0-9_\u0600-\u06FF]+)")


def parse_frontmatter(content):
    meta = {}
    fm_match = FRONTMATTER_PATTERN.match(content)
    if not fm_match:
        return meta, content
    fm_text = fm_match.group(1)
    body = content[fm_match.end():]
    current_key = None
    is_list = False
    for line in fm_text.splitlines():
        line_clean = line.strip()
        if not line_clean or line_clean.startswith("#"):
            continue
        if line_clean.startswith("- ") and current_key and is_list:
            item = line_clean[2:].strip().strip('"').strip("'")
            meta[current_key].append(item)
            continue
        if ":" in line:
            parts = line.split(":", 1)
            k = parts[0].strip()
            v = parts[1].strip()
            if not v:
                meta[k] = []
                current_key = k
                is_list = True
            else:
                current_key = k
                is_list = False
                meta[k] = v.strip('"').strip("'")
    return meta, body


def categorize_node(nd_type, relpath):
    path_lower = relpath.lower()
    if "prophet" in path_lower or "ulul_azm" in path_lower or nd_type in ["prophet_archetype", "master_sphere"]:
        return "أولو العزم من الرسل", "prophets", "#f59e0b"
    elif "00_index" in path_lower or "quranic" in path_lower or nd_type in ["index", "master_blueprint"]:
        return "الهيكل القرآني والمصفوفات", "index", "#ff4d6d"
    elif "09_zodiac" in path_lower or nd_type == "zodiac_sign":
        return "دائرة البروج الاثني عشر", "zodiac", "#ff9f1c"
    elif "01_cycles" in path_lower or nd_type == "cycle":
        return "الدورات الكونية والفلك", "astronomy", "#00b4d8"
    elif "02_eras" in path_lower or nd_type == "era":
        return "العصور والرسالات التاريخية", "eras", "#e11d48"
    elif "03_esoteric" in path_lower or nd_type == "system":
        return "الميلوثيسيا وتصريف القوى", "esoteric", "#9d4edd"
    elif "07_hermetic" in path_lower or "alchemy" in path_lower:
        return "الهرمسية والكيمياء القديمة", "alchemy", "#06d6a0"
    elif "08_sacred" in path_lower or "geometry" in path_lower:
        return "الهندسة المقدسة والرياضيات", "geometry", "#fb8500"
    elif "04_sources" in path_lower or "06_extracted" in path_lower or nd_type in ["scholar", "text", "school", "source_manuscript"]:
        return "المخطوطات والحكماء", "sources", "#70e000"
    elif "05_synthesis" in path_lower or nd_type in ["matrix", "master_matrix"]:
        return "الهيكل القرآني والمصفوفات", "matrix", "#ff4d6d"
    else:
        return "مفاهيم عامة", "concept", "#3a86ff"


def scan_vault():
    nodes = {}
    links = []
    md_files = list(VAULT_DIR.rglob("*.md"))
    
    for f in md_files:
        if ".obsidian" in str(f):
            continue
        name = f.stem
        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue
            
        meta, body = parse_frontmatter(content)
        title = meta.get("title", name.replace("_", " "))
        raw_type = meta.get("type", "concept")
        relpath = str(f.relative_to(VAULT_DIR))
        
        category_name, group_id, color = categorize_node(raw_type, relpath)
        
        tags = meta.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        body_tags = TAG_PATTERN.findall(body)
        all_tags = list(set(tags + body_tags))
        
        snippet = ""
        for line in body.splitlines():
            line_str = line.strip()
            if line_str and not line_str.startswith("#") and not line_str.startswith(">"):
                snippet = line_str[:180]
                break
                
        nodes[name] = {
            "id": name,
            "label": title,
            "filename": f.name,
            "relpath": relpath,
            "type": raw_type,
            "category": category_name,
            "group": group_id,
            "color": color,
            "tags": all_tags,
            "snippet": snippet,
            "raw_content": content,
            "body_markdown": body,
            "connections": []
        }

    for name, node in nodes.items():
        content = node["raw_content"]
        wikilinks = WIKILINK_PATTERN.findall(content)
        seen_targets = set()
        for target, _alias in wikilinks:
            clean_target = target.strip()
            if clean_target in nodes and clean_target not in seen_targets and clean_target != name:
                seen_targets.add(clean_target)
                node["connections"].append(clean_target)
                links.append({
                    "source": name,
                    "target": clean_target
                })

    return nodes, links


def generate_unified_html(nodes, links):
    nodes_list = []
    degrees = {nid: 0 for nid in nodes}
    for l in links:
        degrees[l["source"]] = degrees.get(l["source"], 0) + 1
        degrees[l["target"]] = degrees.get(l["target"], 0) + 1

    for nid, nd in nodes.items():
        deg = degrees.get(nid, 0)
        size = 14 + min(deg * 2.8, 32)
        if nd["group"] in ["prophets", "index", "matrix"]:
            size += 10

        nodes_list.append({
            "id": nid,
            "label": nd["label"],
            "title": f"<b>{nd['label']}</b><br>التصنيف: {nd['category']}<br>الروابط: {deg}",
            "group": nd["group"],
            "category": nd["category"],
            "color": {
                "background": nd["color"],
                "border": "#ffffff",
                "highlight": { "background": "#ffffff", "border": nd["color"] },
                "hover": { "background": "#ffffff", "border": nd["color"] }
            },
            "size": size,
            "degree": deg,
            "tags": nd["tags"],
            "snippet": nd["snippet"],
            "relpath": nd["relpath"],
            "body": nd["body_markdown"]
        })

    edges_list = []
    for l in links:
        edges_list.append({
            "from": l["source"],
            "to": l["target"],
            "color": {
                "color": "rgba(90, 105, 120, 0.35)",
                "highlight": "#00f5d4",
                "hover": "#ffffff"
            },
            "width": 1.3
        })

    graph_data_json = json.dumps({"nodes": nodes_list, "edges": edges_list}, ensure_ascii=False)

    html_template = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl" style="background-color: #111823; color-scheme: dark;">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="color-scheme" content="dark">
    <meta name="theme-color" content="#111823">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <title>أطلس الكوزمولوجيا القرآنية وشبكة المعرفة الشاملة — Quranic Cosmic Atlas</title>
    <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        :root {{
            color-scheme: dark !important;
            --bg-space: #111823;
            --void-black: #111823;
            --panel-bg: rgba(30, 41, 59, 0.95);
            --border-glass: rgba(148, 163, 184, 0.2);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --gold: #64748b;
            --gold-glow: rgba(148, 163, 184, 0.35);
            --cyan: #38bdf8;
            --rose: #fb7185;
            --purple: #c084fc;
            --emerald: #34d399;
        }}
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            scrollbar-color: rgba(148, 163, 184, 0.35) #111823 !important;
        }}
        html {{
            background-color: #111823 !important;
            color-scheme: dark !important;
        }}
        body {{
            background-color: #111823 !important;
            color: var(--text-main);
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(56, 189, 248, 0.05) 0%, transparent 45%),
                radial-gradient(circle at 90% 80%, rgba(148, 163, 184, 0.05) 0%, transparent 45%);
            min-height: 100vh;
            color-scheme: dark !important;
        }}
        ::-webkit-scrollbar {{
            width: 8px !important;
            height: 8px !important;
        }}
        ::-webkit-scrollbar-track {{
            background: #111823 !important;
        }}
        ::-webkit-scrollbar-thumb {{
            background: rgba(148, 163, 184, 0.35) !important;
            border-radius: 6px !important;
            border: 2px solid #111823 !important;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: rgba(148, 163, 184, 0.65) !important;
        }}
        
        /* Master Header */
        header {{
            background: rgba(11, 15, 23, 0.9);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border-glass);
            padding: 16px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 8px 30px rgba(0,0,0,0.6);
        }}
        .brand-title {{
            font-size: 1.45rem;
            font-weight: 800;
            color: var(--gold);
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .brand-subtitle {{
            font-size: 0.78rem;
            color: var(--text-muted);
            margin-top: 3px;
        }}

        .nav-tabs {{
            display: flex;
            gap: 6px;
            background: rgba(0, 0, 0, 0.5);
            padding: 4px;
            border-radius: 12px;
            border: 1px solid var(--border-glass);
        }}
        .nav-btn {{
            background: none;
            border: none;
            color: var(--text-muted);
            padding: 8px 16px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.86rem;
            font-weight: 600;
            transition: all 0.25s ease;
            white-space: nowrap;
        }}
        .nav-btn:hover {{
            color: #fff;
            background: rgba(255, 255, 255, 0.06);
        }}
        .nav-btn.active {{
            background: var(--gold);
            color: #05070b;
            font-weight: bold;
            box-shadow: 0 0 16px var(--gold-glow);
        }}

        /* Container Sections */
        main {{
            max-width: 1500px;
            margin: 0 auto;
            padding: 25px 20px 80px 20px;
        }}
        .tab-section {{
            display: none;
            animation: fadeIn 0.4s ease;
        }}
        .tab-section.active {{
            display: block;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(8px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* Hero */
        .hero {{
            text-align: center;
            padding: 20px 20px 40px 20px;
            max-width: 1000px;
            margin: 0 auto;
        }}
        .quran-ayah {{
            background: rgba(244, 180, 26, 0.08);
            border: 1px solid rgba(244, 180, 26, 0.3);
            border-radius: 12px;
            padding: 14px 24px;
            color: var(--gold);
            font-size: 1.15rem;
            font-weight: 600;
            margin-bottom: 16px;
            display: inline-block;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }}
        .hero h1 {{
            font-size: 2.2rem;
            font-weight: 800;
            background: linear-gradient(135deg, #fff 30%, var(--gold) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 12px;
        }}
        .hero p {{
            font-size: 1.05rem;
            color: var(--text-muted);
            line-height: 1.8;
        }}

        /* 1. Fullscreen Interactive Force Network View */
        #graph-fullscreen-wrapper {{
            width: 100%;
            height: 760px;
            background: radial-gradient(circle at center, #0e1422 0%, #05070b 100%);
            border: 1px solid var(--border-glass);
            border-radius: 20px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 16px 45px rgba(0,0,0,0.7);
        }}
        #cosmic-network-canvas {{
            width: 100%;
            height: 100%;
        }}

        /* Topbar Controls within Graph */
        .graph-top-filters {{
            position: relative;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
            z-index: 10;
            background: rgba(11, 15, 23, 0.9);
            backdrop-filter: blur(16px);
            padding: 10px 16px;
            border-radius: 14px;
            border: 1px solid var(--border-glass);
            margin-bottom: 12px;
            flex-wrap: wrap;
        }}
        .pills-container {{
            display: flex;
            gap: 6px;
            overflow-x: auto;
        }}
        .filter-pill {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-glass);
            color: var(--text-muted);
            padding: 5px 12px;
            border-radius: 16px;
            font-size: 0.78rem;
            cursor: pointer;
            transition: all 0.2s;
            white-space: nowrap;
        }}
        .filter-pill:hover {{
            background: rgba(255, 255, 255, 0.12);
            color: #fff;
        }}
        .filter-pill.active {{
            background: var(--cyan);
            color: #000;
            font-weight: bold;
            border-color: var(--cyan);
            box-shadow: 0 0 12px rgba(0, 240, 255, 0.4);
        }}
        .search-box {{
            width: 200px;
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid var(--border-glass);
            padding: 6px 12px;
            border-radius: 16px;
            color: #fff;
            font-size: 0.8rem;
            outline: none;
        }}

        .graph-bottom-controls {{
            position: absolute;
            bottom: 20px;
            right: 20px;
            display: flex;
            gap: 8px;
            z-index: 10;
        }}
        .g-btn {{
            background: rgba(11, 15, 23, 0.9);
            border: 1px solid var(--border-glass);
            color: #fff;
            padding: 8px 14px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.82rem;
            transition: all 0.2s;
        }}
        .g-btn:hover {{
            background: var(--gold);
            color: #000;
        }}

        /* Sliding Markdown Reader Drawer */
                /* BACKDROP & ENHANCED DRAWER (MOBILE & DESKTOP) */
        .drawer-backdrop {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
            z-index: 1400;
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
            transition: opacity 0.3s ease, visibility 0.3s ease;
        }}
        .drawer-backdrop.active {{
            opacity: 1;
            visibility: visible;
            pointer-events: auto;
        }}

        #reader-drawer {{
            position: fixed;
            top: 80px;
            left: 20px;
            bottom: 20px;
            width: 540px;
            max-width: 90vw;
            background: rgba(7, 11, 20, 0.96);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(148, 163, 184, 0.35);
            border-radius: 16px;
            z-index: 1500;
            box-shadow: 0 16px 50px rgba(0,0,0,0.85);
            display: flex;
            flex-direction: column;
            transform: translateX(-580px);
            transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease, visibility 0.3s ease;
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
        }}
        #reader-drawer.open {{
            transform: translateX(0);
            opacity: 1;
            visibility: visible;
            pointer-events: auto;
        }}

        @media (max-width: 768px) {{
            #reader-drawer {{
                top: auto !important;
                bottom: 0 !important;
                left: 0 !important;
                right: 0 !important;
                width: 100% !important;
                max-width: 100% !important;
                height: 82vh !important;
                max-height: 82vh !important;
                border-radius: 20px 20px 0 0 !important;
                border-bottom: none !important;
                border-left: none !important;
                border-right: none !important;
                border-top: 2px solid var(--gold) !important;
                transform: translateY(100%) !important;
            }}
            #reader-drawer.open {{
                transform: translateY(0) !important;
            }}
        }}

        /* GRAPH DUAL MODE: THEORY VS CANVAS */
        .graph-mode-toggle-bar {{
            display: flex;
            flex-direction: column;
            gap: 6px;
            margin-bottom: 12px;
        }}
        .mode-toggle-buttons {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}
        .mode-toggle-btn {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            border-radius: 10px;
            font-size: 0.84rem;
            font-weight: 700;
            cursor: pointer;
            background: rgba(15, 23, 42, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #94a3b8;
            transition: all 0.2s ease;
            font-family: 'Tajawal', sans-serif;
        }}
        .mode-toggle-btn:hover {{
            color: #fff;
            background: rgba(255, 255, 255, 0.05);
        }}
        .mode-toggle-btn.active {{
            background: linear-gradient(135deg, rgba(6, 214, 160, 0.25), rgba(6, 214, 160, 0.08));
            border-color: #06d6a0;
            color: #a7f3d0;
            box-shadow: 0 0 14px rgba(6, 214, 160, 0.25);
        }}
        .mode-hint-text {{
            font-size: 0.76rem;
            color: #94a3b8;
        }}

        /* THEORY CARDS GRID */
        .theory-cards-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
            gap: 14px;
            margin-top: 14px;
            max-height: calc(100vh - 270px);
            overflow-y: auto;
            padding-bottom: 30px;
            -webkit-overflow-scrolling: touch;
        }}
        @media (max-width: 768px) {{
            .theory-cards-grid {{
                grid-template-columns: 1fr;
                max-height: none;
            }}
        }}
        .theory-node-card {{
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            padding: 16px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .theory-node-card:hover {{
            border-color: rgba(148, 163, 184, 0.4);
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
        }}
        .theory-card-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 8px;
        }}
        .theory-card-cat {{
            font-size: 0.72rem;
            padding: 3px 8px;
            border-radius: 6px;
            font-weight: 600;
        }}
        .theory-card-links {{
            font-size: 0.7rem;
            color: #94a3b8;
        }}
        .theory-card-title {{
            font-family: 'Amiri', serif;
            font-size: 1.15rem;
            font-weight: 700;
            color: #f8fafc;
            margin-bottom: 6px;
        }}
        .theory-card-snippet {{
            font-size: 0.82rem;
            color: #94a3b8;
            line-height: 1.6;
            margin-bottom: 12px;
        }}
        .theory-card-btn {{
            font-size: 0.78rem;
            color: var(--gold);
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-weight: 700;
        }}
        .drawer-header {{
            padding: 16px 20px;
            border-bottom: 1px solid var(--border-glass);
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(255, 255, 255, 0.02);
        }}
        .drawer-title {{
            font-size: 1.15rem;
            color: var(--gold);
            font-weight: 700;
        }}
        .close-btn {{
            background: none;
            border: none;
            color: var(--text-muted);
            font-size: 1.3rem;
            cursor: pointer;
        }}
        .close-btn:hover {{ color: #fff; }}
        .drawer-meta {{
            padding: 10px 20px;
            background: rgba(0,0,0,0.3);
            border-bottom: 1px solid var(--border-glass);
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            font-size: 0.78rem;
        }}
        .meta-tag {{
            background: rgba(255, 255, 255, 0.08);
            padding: 2px 8px;
            border-radius: 10px;
            color: var(--cyan);
        }}
        .drawer-body {{
            padding: 20px;
            overflow-y: auto;
            flex: 1;
            font-size: 0.92rem;
            line-height: 1.7;
            color: var(--text-main);
        }}
        .drawer-body h1, .drawer-body h2, .drawer-body h3 {{
            color: var(--cyan);
            margin: 16px 0 8px 0;
            font-size: 1.1rem;
        }}
        .drawer-body p {{ margin-bottom: 12px; }}
        .drawer-body blockquote {{
            border-right: 3px solid var(--gold);
            padding-right: 12px;
            color: #a0aec0;
            margin: 12px 0;
        }}
        .drawer-connections {{
            padding: 12px 20px;
            background: rgba(0, 0, 0, 0.4);
            border-top: 1px solid var(--border-glass);
        }}
        .conn-title {{
            font-size: 0.78rem;
            color: var(--text-muted);
            margin-bottom: 6px;
            font-weight: 600;
        }}
        .conn-pills {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }}
        .conn-pill {{
            background: rgba(0, 240, 255, 0.12);
            color: var(--cyan);
            border: 1px solid rgba(0, 240, 255, 0.25);
            padding: 3px 8px;
            border-radius: 10px;
            font-size: 0.75rem;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .conn-pill:hover {{
            background: var(--cyan);
            color: #000;
        }}

        /* 2. Spheres Ascension Ladder */
        .spheres-container {{
            display: grid;
            grid-template-columns: 380px 1fr;
            gap: 30px;
            align-items: start;
        }}
        .ladder-list {{
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        .sphere-card {{
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            border-radius: 14px;
            padding: 16px 20px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 16px;
            transition: all 0.25s ease;
            position: relative;
            overflow: hidden;
        }}
        .sphere-card::before {{
            content: '';
            position: absolute;
            right: 0;
            top: 0;
            bottom: 0;
            width: 5px;
            background: var(--sphere-color, var(--gold));
            opacity: 0.6;
        }}
        .sphere-card:hover, .sphere-card.active {{
            background: rgba(255, 255, 255, 0.05);
            border-color: var(--sphere-color, var(--gold));
            transform: translateX(-6px);
            box-shadow: 0 8px 24px rgba(0,0,0,0.5);
        }}
        .sphere-card.active::before {{ width: 8px; opacity: 1; }}
        .sphere-rank {{
            font-size: 1.4rem;
            font-weight: 800;
            color: var(--sphere-color, var(--gold));
            min-width: 35px;
        }}
        .sphere-info h3 {{
            font-size: 1.05rem;
            color: #fff;
            margin-bottom: 4px;
        }}
        .sphere-info span {{
            font-size: 0.82rem;
            color: var(--text-muted);
        }}

        .sphere-detail-panel {{
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            border-radius: 20px;
            padding: 35px;
            box-shadow: 0 16px 40px rgba(0,0,0,0.6);
            position: sticky;
            top: 95px;
        }}
        .detail-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border-glass);
            padding-bottom: 20px;
            margin-bottom: 24px;
        }}
        .detail-header h2 {{ font-size: 1.7rem; color: var(--gold); }}
        .detail-badge {{
            background: rgba(244, 180, 26, 0.15);
            color: var(--gold);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            border: 1px solid rgba(244, 180, 26, 0.3);
        }}

        .prophet-banner {{
            background: rgba(0, 0, 0, 0.35);
            border: 1px solid var(--border-glass);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            gap: 20px;
        }}
        .prophet-avatar {{
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--gold), #ff3366);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
            color: #fff;
        }}
        .prophet-desc h4 {{ font-size: 1.2rem; color: #fff; margin-bottom: 4px; }}
        .prophet-desc p {{ font-size: 0.9rem; color: var(--text-muted); line-height: 1.5; }}

        .specs-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
            margin-bottom: 25px;
        }}
        .spec-box {{
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--border-glass);
            border-radius: 10px;
            padding: 14px;
        }}
        .spec-label {{ font-size: 0.75rem; color: var(--text-muted); margin-bottom: 4px; }}
        .spec-value {{ font-size: 0.92rem; color: #fff; font-weight: 600; }}

        .textual-proof {{
            background: rgba(0, 240, 255, 0.04);
            border-right: 3px solid var(--cyan);
            padding: 16px;
            border-radius: 8px;
            font-size: 0.9rem;
            line-height: 1.7;
            color: #d0d7de;
        }}

        /* Luxury Treatise & Compendium Styles for Door 02 */
        .spheres-compendium {{
            margin-bottom: 40px;
            background: rgba(11, 17, 33, 0.7);
            border: 1px solid var(--border-glass);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.5);
        }}
        .compendium-header {{
            text-align: center;
            margin-bottom: 30px;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
        }}
        .compendium-badge {{
            display: inline-block;
            background: rgba(148, 163, 184, 0.15);
            color: var(--gold);
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 700;
            border: 1px solid rgba(148, 163, 184, 0.35);
            margin-bottom: 12px;
        }}
        .compendium-header h2 {{
            font-size: 1.8rem;
            color: #fff;
            margin-bottom: 10px;
        }}
        .compendium-header p {{
            font-size: 0.95rem;
            color: var(--text-muted);
            line-height: 1.8;
        }}
        .compendium-cards-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }}
        .treatise-card {{
            background: rgba(15, 23, 42, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 24px;
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        .treatise-card:hover {{
            border-color: rgba(148, 163, 184, 0.4);
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
        }}
        .treatise-card-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            padding-bottom: 12px;
        }}
        .t-badge {{
            background: rgba(0, 240, 255, 0.12);
            color: var(--cyan);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.78rem;
            font-weight: 700;
            white-space: nowrap;
        }}
        .treatise-card-header h3 {{
            font-size: 1.15rem;
            color: #94a3b8;
            margin: 0;
        }}
        .treatise-card-body {{
            font-size: 0.92rem;
            line-height: 1.85;
            color: #475569;
        }}
        .treatise-card-body p {{
            margin-bottom: 12px;
        }}
        .treatise-card-body p:last-child {{
            margin-bottom: 0;
        }}
        .treatise-card-body strong {{
            color: #fff;
        }}
        .treatise-card-body em {{
            color: #93c5fd;
            font-style: normal;
        }}

        /* Enhanced Detail Panel Items */
        .hadith-box {{
            background: rgba(16, 185, 129, 0.06);
            border-right: 4px solid #10b981;
            padding: 18px 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            font-size: 0.95rem;
            line-height: 1.85;
            color: #e2e8f0;
        }}
        .hadith-box-header {{
            display: flex;
            align-items: center;
            gap: 8px;
            color: #10b981;
            font-weight: 700;
            font-size: 0.88rem;
            margin-bottom: 8px;
        }}
        .secret-box {{
            background: rgba(168, 85, 247, 0.07);
            border-right: 4px solid #a855f7;
            padding: 18px 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            font-size: 0.93rem;
            line-height: 1.85;
            color: #e2e8f0;
        }}
        .secret-box-header {{
            display: flex;
            align-items: center;
            gap: 8px;
            color: #c084fc;
            font-weight: 700;
            font-size: 0.88rem;
            margin-bottom: 8px;
        }}
        .orbit-box {{
            background: rgba(59, 130, 246, 0.06);
            border-right: 4px solid #3b82f6;
            padding: 16px 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            font-size: 0.92rem;
            line-height: 1.8;
            color: #475569;
        }}
        .orbit-box-header {{
            display: flex;
            align-items: center;
            gap: 8px;
            color: #60a5fa;
            font-weight: 700;
            font-size: 0.88rem;
            margin-bottom: 8px;
        }}
        .quran-box {{
            background: rgba(148, 163, 184, 0.06);
            border: 1px dashed rgba(148, 163, 184, 0.35);
            padding: 16px 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            font-size: 0.95rem;
            line-height: 1.85;
            color: #fef08a;
            text-align: center;
        }}

        /* Global Civilizational Consensus Box */
        .global-consensus-box {{
            background: rgba(15, 23, 42, 0.75);
            border: 1px solid rgba(148, 163, 184, 0.35);
            border-radius: 14px;
            padding: 22px;
            margin-bottom: 25px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        }}
        .consensus-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 16px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 12px;
            flex-wrap: wrap;
            gap: 10px;
        }}
        .consensus-header h4 {{
            font-size: 1.15rem;
            color: var(--gold);
            margin: 0;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .consensus-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 14px;
        }}
        @media (max-width: 768px) {{
            .consensus-grid {{
                grid-template-columns: 1fr !important;
            }}
        }}
        .civ-card {{
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: 10px;
            padding: 14px;
            transition: all 0.25s ease;
        }}
        .civ-card:hover {{
            background: rgba(255, 255, 255, 0.04);
            border-color: rgba(0, 240, 255, 0.35);
        }}
        .civ-card-title {{
            font-size: 0.88rem;
            font-weight: 700;
            color: var(--cyan);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .civ-card-text {{
            font-size: 0.86rem;
            line-height: 1.75;
            color: #475569;
        }}

        /* Panoramic Matrix Table Styles */
        .panoramic-matrix-wrapper {{
            margin-top: 50px;
            background: rgba(11, 17, 33, 0.7);
            border: 1px solid var(--border-glass);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6);
        }}
        .matrix-table-header {{
            text-align: center;
            margin-bottom: 25px;
        }}
        .matrix-tag {{
            display: inline-block;
            background: rgba(0, 240, 255, 0.12);
            color: var(--cyan);
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 0.82rem;
            font-weight: 700;
            border: 1px solid rgba(0, 240, 255, 0.3);
            margin-bottom: 10px;
        }}
        .matrix-table-header h3 {{
            font-size: 1.6rem;
            color: #fff;
            margin-bottom: 8px;
        }}
        .matrix-table-header p {{
            font-size: 0.9rem;
            color: var(--text-muted);
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.7;
        }}
        .matrix-responsive-table {{
            width: 100%;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
        }}
        .panoramic-spheres-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.88rem;
            text-align: right;
            white-space: nowrap;
        }}
        .panoramic-spheres-table th {{
            background: rgba(15, 23, 42, 0.95);
            color: var(--gold);
            padding: 14px 16px;
            border-bottom: 1px solid rgba(148, 163, 184, 0.3);
            font-weight: 700;
            position: sticky;
            top: 0;
            z-index: 2;
        }}
        .panoramic-spheres-table td {{
            padding: 12px 16px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            color: #475569;
        }}
        .panoramic-spheres-table tr:hover td {{
            background: rgba(255, 255, 255, 0.03);
            color: #fff;
        }}
        .badge-hz {{
            display: inline-block;
            background: rgba(59, 130, 246, 0.15);
            color: #60a5fa;
            padding: 3px 8px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.8rem;
            border: 1px solid rgba(59, 130, 246, 0.3);
        }}

        /* Odyssey Universal Synthesis Styles */
        .odyssey-wrapper {{
            margin-top: 50px;
            margin-bottom: 50px;
            background: radial-gradient(ellipse at top, rgba(16, 24, 48, 0.9) 0%, rgba(5, 8, 16, 0.98) 100%);
            border: 1px solid rgba(244, 180, 26, 0.35);
            border-radius: 24px;
            padding: 35px 25px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7), 0 0 40px rgba(244, 180, 26, 0.08);
            position: relative;
            overflow: hidden;
        }}
        .odyssey-header {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .odyssey-header h2 {{
            font-size: 1.85rem;
            color: #fff;
            margin-bottom: 12px;
            background: linear-gradient(135deg, #94a3b8, #fff, #00f0ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .odyssey-header p {{
            font-size: 0.96rem;
            color: #94a3b8;
            max-width: 900px;
            margin: 0 auto;
            line-height: 1.8;
        }}
        .odyssey-nav-bar {{
            display: flex;
            gap: 10px;
            overflow-x: auto;
            padding: 8px 4px 18px 4px;
            -webkit-overflow-scrolling: touch;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            margin-bottom: 25px;
        }}
        .odyssey-nav-btn {{
            flex: 0 0 auto;
            background: rgba(15, 23, 42, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #475569;
            padding: 10px 16px;
            border-radius: 14px;
            cursor: pointer;
            font-size: 0.86rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .odyssey-nav-btn:hover {{
            background: rgba(255, 255, 255, 0.06);
            border-color: rgba(0, 240, 255, 0.4);
            transform: translateY(-2px);
        }}
        .odyssey-nav-btn.active {{
            background: linear-gradient(135deg, rgba(244, 180, 26, 0.25), rgba(0, 240, 255, 0.15));
            border-color: var(--gold);
            color: #fff;
            box-shadow: 0 0 20px rgba(244, 180, 26, 0.25);
            transform: translateY(-2px);
        }}
        .odyssey-stage-card {{
            background: rgba(11, 17, 33, 0.65);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 30px;
            animation: fadeIn 0.4s ease;
        }}
        .odyssey-stage-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 15px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 20px;
            margin-bottom: 25px;
        }}
        .odyssey-title-group h3 {{
            font-size: 1.5rem;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 6px;
        }}
        .odyssey-title-group span {{
            font-size: 0.88rem;
            color: var(--text-muted);
        }}
        .odyssey-essence-callout {{
            background: rgba(244, 180, 26, 0.08);
            border-right: 4px solid var(--gold);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 25px;
            font-size: 1.05rem;
            line-height: 1.9;
            color: #fef08a;
            box-shadow: inset 0 0 25px rgba(244, 180, 26, 0.04);
        }}
        .odyssey-essence-callout strong {{
            color: var(--gold);
            display: block;
            margin-bottom: 6px;
            font-size: 0.9rem;
            letter-spacing: 0.5px;
        }}
        .odyssey-symphony-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin-bottom: 25px;
        }}
        @media (max-width: 900px) {{
            .odyssey-symphony-grid {{ grid-template-columns: 1fr; }}
        }}
        .sym-card {{
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: 14px;
            padding: 20px;
            transition: all 0.25s ease;
        }}
        .sym-card:hover {{
            border-color: rgba(0, 240, 255, 0.35);
            background: rgba(255, 255, 255, 0.035);
        }}
        .sym-card-title {{
            font-size: 0.95rem;
            font-weight: 700;
            color: var(--cyan);
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .sym-card-content {{
            font-size: 0.9rem;
            line-height: 1.8;
            color: #475569;
        }}
        .odyssey-epiphany-box {{
            background: radial-gradient(circle at center, rgba(0, 240, 255, 0.08) 0%, rgba(15, 23, 42, 0.4) 100%);
            border: 1px solid rgba(0, 240, 255, 0.3);
            border-radius: 14px;
            padding: 22px;
            text-align: center;
            margin-top: 10px;
        }}
        .odyssey-epiphany-ayah {{
            font-size: 1.15rem;
            color: var(--gold);
            font-weight: 700;
            margin-bottom: 8px;
            line-height: 1.8;
        }}
        .odyssey-epiphany-wisdom {{
            font-size: 0.92rem;
            color: #e2e8f0;
            line-height: 1.8;
            max-width: 800px;
            margin: 0 auto;
        }}
        .odyssey-nav-controls {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 25px;
            padding-top: 15px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
        }}
        .odyssey-ctrl-btn {{
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #fff;
            padding: 8px 18px;
            border-radius: 12px;
            cursor: pointer;
            font-size: 0.88rem;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s;
        }}
        .odyssey-ctrl-btn:hover {{
            background: var(--gold);
            color: #000;
            border-color: var(--gold);
        }}

        /* Zodiac Celestial Wheel & High-Tech Hologram */
        .zodiac-wheel-canvas {{
            position: relative;
            width: 100%;
            max-width: 380px;
            height: 380px;
            margin: 15px auto;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .zodiac-wheel-svg {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            filter: drop-shadow(0 0 20px rgba(0, 240, 255, 0.25));
            pointer-events: none;
            animation: slow-rotate 240s linear infinite;
        }}
        @keyframes slow-rotate {{
            from {{ transform: rotate(0deg); }}
            to {{ transform: rotate(360deg); }}
        }}
        .zodiac-wheel-node {{
            position: absolute;
            width: 44px;
            height: 44px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 6;
            transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            background: rgba(11, 15, 23, 0.95);
            border: 2px solid var(--border-glass);
            box-shadow: 0 0 15px rgba(0,0,0,0.8);
            font-size: 1.3rem;
            color: #fff;
            transform: translate(-50%, -50%);
        }}
        .zodiac-wheel-node:hover, .zodiac-wheel-node.active {{
            transform: translate(-50%, -50%) scale(1.35);
            border-color: #fff;
            box-shadow: 0 0 30px currentColor, inset 0 0 10px currentColor;
        }}
        .z-pill-btn {{
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: #475569;
            padding: 7px 12px;
            border-radius: 12px;
            cursor: pointer;
            font-size: 0.78rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.25s ease;
            white-space: nowrap;
        }}
        .z-pill-btn:hover {{
            background: rgba(255, 255, 255, 0.06);
            transform: translateY(-2px);
        }}
        .z-pill-btn.active {{
            border-color: currentColor;
            box-shadow: 0 0 15px currentColor;
            transform: translateY(-2px);
            color: #fff;
            background: rgba(255, 255, 255, 0.08);
        }}

        /* 3. 12 Zodiac Wheel */
        .zodiac-filter-bar {{
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }}
        .z-filter-btn {{
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            color: var(--text-muted);
            padding: 8px 18px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 0.85rem;
            font-weight: 600;
            transition: all 0.2s;
        }}
        .z-filter-btn:hover, .z-filter-btn.active {{
            background: var(--cyan);
            color: #000;
            border-color: var(--cyan);
            box-shadow: 0 0 12px rgba(0, 240, 255, 0.3);
        }}
        .zodiac-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 24px;
        }}
        .zodiac-card {{
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            border-radius: 18px;
            padding: 24px;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            overflow: hidden;
        }}
        .zodiac-card:hover {{
            transform: translateY(-5px);
            border-color: var(--gold);
            box-shadow: 0 14px 35px rgba(244, 180, 26, 0.15);
        }}
        .zodiac-card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }}
        .zodiac-glyph {{ font-size: 2.2rem; color: var(--gold); }}
        .zodiac-element {{
            font-size: 0.75rem;
            padding: 4px 10px;
            border-radius: 12px;
            font-weight: 600;
        }}
        .elem-fire {{ background: rgba(239, 68, 68, 0.15); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.3); }}
        .elem-earth {{ background: rgba(245, 158, 11, 0.15); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.3); }}
        .elem-air {{ background: rgba(6, 182, 212, 0.15); color: #06b6d4; border: 1px solid rgba(6, 182, 212, 0.3); }}
        .elem-water {{ background: rgba(59, 130, 246, 0.15); color: #3b82f6; border: 1px solid rgba(59, 130, 246, 0.3); }}

        .z-prop-list {{
            display: flex;
            flex-direction: column;
            gap: 8px;
            background: rgba(0, 0, 0, 0.3);
            padding: 12px 14px;
            border-radius: 10px;
            border: 1px solid var(--border-glass);
            font-size: 0.84rem;
            margin: 12px 0;
        }}
        .z-prop-row {{ display: flex; justify-content: space-between; }}
        .z-prop-lbl {{ color: var(--text-muted); }}
        .z-prop-val {{ color: var(--cyan); font-weight: 600; }}

        /* 4. Timeline View & Precession Engine */
        .timeline-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 26px;
        }}
        .age-card {{
            background: rgba(13, 17, 23, 0.88);
            backdrop-filter: blur(14px);
            border: 1px solid var(--border-glass);
            border-radius: 20px;
            padding: 26px;
            transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            cursor: pointer;
        }}
        .age-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, transparent, var(--gold), transparent);
            opacity: 0.3;
            transition: opacity 0.3s ease;
        }}
        .age-card:hover {{
            transform: translateY(-6px);
            border-color: var(--cyan);
            box-shadow: 0 16px 36px rgba(0, 240, 255, 0.16), 0 0 20px rgba(148, 163, 184, 0.1);
        }}
        .age-card:hover::before {{
            opacity: 1;
            background: linear-gradient(90deg, var(--rose), var(--gold), var(--cyan));
        }}
        .age-card.active-era {{
            border-color: var(--gold);
            box-shadow: 0 0 25px rgba(148, 163, 184, 0.35);
        }}
        .age-card-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }}
        .age-glyph-badge {{
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(148, 163, 184, 0.4);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.4rem;
            color: var(--gold);
            box-shadow: 0 0 15px rgba(148, 163, 184, 0.15);
        }}
        .age-era {{ font-size: 0.85rem; color: var(--gold); font-weight: 700; letter-spacing: 0.5px; }}
        .age-title {{ font-size: 1.35rem; color: #fff; margin-bottom: 8px; font-weight: 700; }}
        .polarity-tag {{
            background: rgba(255, 51, 102, 0.12);
            color: #ff7597;
            padding: 5px 12px;
            border-radius: 10px;
            font-size: 0.78rem;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            margin-bottom: 14px;
            border: 1px solid rgba(255, 51, 102, 0.35);
            font-weight: 600;
        }}
        .age-meta-pills {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 14px;
        }}
        .age-pill {{
            font-size: 0.75rem;
            padding: 3px 9px;
            border-radius: 6px;
            background: rgba(0, 240, 255, 0.08);
            border: 1px solid rgba(0, 240, 255, 0.25);
            color: var(--cyan);
        }}
        .age-pill.prophet-pill {{
            background: rgba(16, 185, 129, 0.1);
            border-color: rgba(16, 185, 129, 0.3);
            color: #34d399;
        }}
        .age-pill.monument-pill {{
            background: rgba(245, 158, 11, 0.1);
            border-color: rgba(245, 158, 11, 0.3);
            color: #fbbf24;
        }}
        .age-desc {{ font-size: 0.9rem; color: #475569; line-height: 1.7; margin-bottom: 16px; text-align: justify; }}
        .age-shadow-box {{
            background: rgba(0, 0, 0, 0.35);
            border-right: 3px solid var(--rose);
            padding: 8px 12px;
            border-radius: 0 8px 8px 0;
            font-size: 0.8rem;
            color: #fca5a5;
            margin-bottom: 14px;
            line-height: 1.5;
        }}
        .age-symbols {{
            border-top: 1px solid var(--border-glass);
            padding-top: 12px;
            font-size: 0.82rem;
            color: #94a3b8;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        /* Precession Wheel & Polar Axis Canvas */
        .precession-wheel-canvas {{
            position: relative;
            width: 100%;
            max-width: 400px;
            height: 400px;
            margin: 15px auto;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .precession-wheel-svg {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            filter: drop-shadow(0 0 25px rgba(148, 163, 184, 0.2));
            pointer-events: none;
        }}
        .precession-node {{
            position: absolute;
            width: 46px;
            height: 46px;
            border-radius: 50%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-size: 1.25rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            transform: translate(-50%, -50%);
            background: rgba(13, 17, 23, 0.92);
            border: 2px solid;
            box-shadow: 0 4px 15px rgba(0,0,0,0.6);
            z-index: 10;
        }}
        .precession-node:hover {{
            transform: translate(-50%, -50%) scale(1.18);
            box-shadow: 0 0 25px currentColor;
            z-index: 15;
        }}
        .precession-node.active {{
            transform: translate(-50%, -50%) scale(1.25);
            box-shadow: 0 0 35px currentColor, inset 0 0 15px currentColor;
            background: rgba(255, 255, 255, 0.12);
            z-index: 20;
        }}
        .precession-node-label {{
            font-size: 0.58rem;
            position: absolute;
            bottom: -15px;
            white-space: nowrap;
            color: #fff;
            background: rgba(0,0,0,0.7);
            padding: 1px 4px;
            border-radius: 4px;
            pointer-events: none;
        }}

        /* Era Filter Buttons */
        .era-filter-bar {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
            margin-bottom: 30px;
        }}
        .e-filter-btn {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-glass);
            color: var(--text-muted);
            padding: 8px 18px;
            border-radius: 12px;
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.25s ease;
        }}
        .e-filter-btn:hover, .e-filter-btn.active {{
            background: linear-gradient(135deg, rgba(148, 163, 184, 0.2), rgba(0, 240, 255, 0.2));
            border-color: var(--gold);
            color: #fff;
            box-shadow: 0 0 20px rgba(148, 163, 184, 0.25);
        }}

        /* 5. Matrix Table & Multi-Dimensional Console */
        .matrix-console-box {{
            background: rgba(13, 17, 23, 0.85);
            backdrop-filter: blur(14px);
            border: 1px solid var(--border-glass);
            border-radius: 20px;
            padding: 24px;
            margin-bottom: 30px;
            display: flex;
            flex-direction: column;
            gap: 18px;
            box-shadow: 0 16px 40px rgba(0,0,0,0.6);
        }}
        .matrix-search-wrapper {{
            display: flex;
            gap: 14px;
            align-items: center;
            flex-wrap: wrap;
        }}
        .matrix-search-input {{
            flex: 1;
            min-width: 260px;
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(0, 240, 255, 0.3);
            border-radius: 12px;
            padding: 12px 18px;
            color: #fff;
            font-size: 0.95rem;
            outline: none;
            transition: all 0.3s ease;
        }}
        .matrix-search-input:focus {{
            border-color: var(--cyan);
            box-shadow: 0 0 18px rgba(0, 240, 255, 0.25);
        }}
        .matrix-mode-bar {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }}
        .m-mode-btn {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-glass);
            color: var(--text-muted);
            padding: 8px 16px;
            border-radius: 10px;
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.25s ease;
        }}
        .m-mode-btn:hover, .m-mode-btn.active {{
            background: linear-gradient(135deg, rgba(0, 240, 255, 0.2), rgba(148, 163, 184, 0.2));
            border-color: var(--cyan);
            color: #fff;
            box-shadow: 0 0 16px rgba(0, 240, 255, 0.2);
        }}
        .matrix-ranks-bar {{
            display: flex;
            gap: 8px;
            overflow-x: auto;
            padding-bottom: 4px;
        }}
        .m-rank-btn {{
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border-glass);
            color: #475569;
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 600;
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .m-rank-btn:hover, .m-rank-btn.active {{
            background: rgba(148, 163, 184, 0.15);
            border-color: var(--gold);
            color: #fff;
            box-shadow: 0 0 15px rgba(148, 163, 184, 0.25);
        }}
        .table-wrapper {{
            background: rgba(13, 17, 23, 0.9);
            border: 1px solid var(--border-glass);
            border-radius: 20px;
            overflow-x: auto;
            box-shadow: 0 20px 50px rgba(0,0,0,0.6);
            margin-top: 25px;
        }}
        table {{ width: 100%; border-collapse: collapse; text-align: right; min-width: 1350px; }}
        th, td {{ padding: 14px 18px; border-bottom: 1px solid var(--border-glass); font-size: 0.88rem; vertical-align: top; }}
        th {{ background: rgba(0, 0, 0, 0.6); color: var(--gold); font-weight: 700; white-space: nowrap; position: sticky; top: 0; z-index: 10; }}
        tr.active-matrix-row {{ background: rgba(0, 240, 255, 0.08) !important; border-right: 4px solid var(--cyan); }}
        tr:hover {{ background: rgba(255, 255, 255, 0.03); cursor: pointer; }}

        /* 6. Books Grid */
        .books-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
            gap: 25px;
        }}
        .book-card {{
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            border-radius: 16px;
            padding: 26px;
            transition: all 0.3s;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .book-card:hover {{
            border-color: var(--gold);
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(244, 180, 26, 0.12);
        }}
        .book-author {{ color: var(--cyan); font-size: 0.85rem; font-weight: 600; margin-bottom: 6px; }}
        .book-name {{ font-size: 1.25rem; color: #fff; margin-bottom: 12px; }}
        .book-summary {{ font-size: 0.88rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 18px; }}
        .book-chapters {{ background: rgba(0, 0, 0, 0.3); border: 1px solid var(--border-glass); border-radius: 8px; padding: 12px; font-size: 0.8rem; color: var(--gold); }}

        /* 7. Critique & Discrepancies Grid */
        .critique-grid {{
            display: flex;
            flex-direction: column;
            gap: 24px;
        }}
        .critique-card {{
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            border-radius: 18px;
            padding: 26px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
            border-right: 4px solid var(--gold);
        }}
        .critique-card.urgent {{
            border-right-color: #ff3366;
        }}
        .critique-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 14px;
        }}
        .critique-title {{
            font-size: 1.3rem;
            color: #fff;
            font-weight: 700;
        }}
        .critique-tag {{
            background: rgba(255, 51, 102, 0.15);
            color: #ff3366;
            border: 1px solid rgba(255, 51, 102, 0.3);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.78rem;
            font-weight: 600;
        }}
        .critique-sections {{
            display: flex;
            flex-direction: column;
            gap: 16px;
            margin-top: 14px;
        }}
        .c-step-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 0.82rem;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 6px;
            margin-bottom: 8px;
        }}
        .c-step-quran {{ background: rgba(0, 240, 255, 0.15); color: var(--cyan); border: 1px solid rgba(0, 240, 255, 0.3); }}
        .c-step-manuscript {{ background: rgba(255, 51, 102, 0.15); color: #ff3366; border: 1px solid rgba(255, 51, 102, 0.3); }}
        .c-step-murshid {{ background: rgba(244, 180, 26, 0.15); color: var(--gold); border: 1px solid rgba(244, 180, 26, 0.3); }}

        .c-box {{
            padding: 18px 20px;
            border-radius: 12px;
            font-size: 0.92rem;
            line-height: 1.8;
        }}
        .c-box.quran-box {{
            background: rgba(0, 240, 255, 0.04);
            border: 1px solid rgba(0, 240, 255, 0.25);
            color: #e0fbfc;
            border-right: 4px solid var(--cyan);
        }}
        .c-box.manuscript-box {{
            background: rgba(255, 51, 102, 0.04);
            border: 1px solid rgba(255, 51, 102, 0.25);
            color: #ffe5ec;
            border-right: 4px solid #ff3366;
        }}
        .c-note-murshid {{
            background: rgba(244, 180, 26, 0.08);
            border: 1px solid var(--gold);
            border-right: 4px solid var(--gold);
            padding: 18px 20px;
            border-radius: 12px;
            color: #94a3b8;
            font-size: 0.92rem;
            line-height: 1.8;
        }}
        .murshid-decision-box {{
            margin-top: 12px;
            padding-top: 12px;
            border-top: 1px dashed rgba(244, 180, 26, 0.4);
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
        }}
        .decision-status-pill {{
            font-size: 0.78rem;
            padding: 4px 10px;
            border-radius: 14px;
            background: rgba(244, 180, 26, 0.2);
            color: var(--gold);
            font-weight: 600;
        }}

        /* 8. Chakras & Prophetic Body Cosmos Styles */
        .chakras-container {{
            display: grid;
            grid-template-columns: 440px 1fr;
            gap: 30px;
            align-items: start;
            margin-top: 25px;
        }}
        @media (max-width: 1024px) {{
            .chakras-container {{ grid-template-columns: 1fr; }}
        }}
        .body-silhouette-wrapper {{
            background: radial-gradient(ellipse at center, #0f172a 0%, #030712 100%);
            border: 1px solid rgba(0, 240, 255, 0.35);
            border-radius: 24px;
            padding: 25px 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            box-shadow: 0 20px 50px rgba(0,0,0,0.8), 0 0 35px rgba(0, 240, 255, 0.12);
            overflow: hidden;
        }}
        .chakra-pills-bar {{
            display: flex;
            gap: 6px;
            overflow-x: auto;
            max-width: 100%;
            padding: 4px 6px 12px 6px;
            -webkit-overflow-scrolling: touch;
            margin-bottom: 15px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            width: 100%;
            justify-content: flex-start;
        }}
        .c-pill-btn {{
            flex: 0 0 auto;
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: #475569;
            padding: 7px 12px;
            border-radius: 12px;
            cursor: pointer;
            font-size: 0.78rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.25s ease;
        }}
        .c-pill-btn:hover {{
            background: rgba(255, 255, 255, 0.06);
            transform: translateY(-2px);
        }}
        .c-pill-btn.active {{
            border-color: currentColor;
            box-shadow: 0 0 15px currentColor;
            transform: translateY(-2px);
            color: #fff;
            background: rgba(255, 255, 255, 0.08);
        }}
        .silhouette-canvas {{
            width: 100%;
            max-width: 340px;
            height: 540px;
            position: relative;
            display: flex;
            justify-content: center;
            margin: 0 auto;
        }}
        .human-figure-svg {{
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            height: 100%;
            filter: drop-shadow(0 0 20px rgba(0, 240, 255, 0.35));
            pointer-events: none;
        }}
        .central-sushumna-line {{
            display: none; /* Replaced by rich SVG line */
        }}
        .chakra-point-btn {{
            position: absolute;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 44px;
            height: 44px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 5;
            transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: 2px solid rgba(255,255,255,0.85);
            box-shadow: 0 0 20px currentColor;
            background: rgba(11, 15, 23, 0.9);
            font-size: 1.15rem;
            color: #fff;
        }}
        .chakra-point-btn:hover, .chakra-point-btn.active {{
            transform: translate(-50%, -50%) scale(1.35);
            border-color: #ffffff;
            box-shadow: 0 0 35px currentColor, inset 0 0 14px currentColor;
        }}
        .chakra-point-btn::after {{
            content: '';
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            border: 2px solid currentColor;
            animation: pulse-ring 2.2s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
        }}
        @keyframes pulse-ring {{
            0% {{ transform: scale(0.95); opacity: 0.8; }}
            50% {{ transform: scale(1.6); opacity: 0; }}
            100% {{ transform: scale(1.6); opacity: 0; }}
        }}

        /* Detail Panel */
        .chakra-detail-card {{
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 16px 45px rgba(0,0,0,0.5);
            transition: all 0.35s ease;
        }}
        .chakra-main-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border-glass);
            padding-bottom: 20px;
            margin-bottom: 24px;
        }}
        .chakra-names h2 {{
            font-size: 1.6rem;
            color: #fff;
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .chakra-sub-names {{
            font-size: 0.92rem;
            color: var(--text-muted);
        }}
        .chakra-prophet-badge {{
            background: linear-gradient(135deg, rgba(244, 180, 26, 0.2), rgba(255, 51, 102, 0.2));
            border: 1px solid var(--gold);
            padding: 8px 18px;
            border-radius: 24px;
            color: var(--gold);
            font-weight: 700;
            font-size: 0.95rem;
        }}
        .chakra-specs-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            margin-bottom: 25px;
        }}
        @media (max-width: 768px) {{
            .chakra-specs-grid {{ grid-template-columns: 1fr; }}
        }}
        .c-spec-item {{
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--border-glass);
            border-radius: 12px;
            padding: 14px 16px;
        }}
        .c-spec-label {{
            font-size: 0.76rem;
            color: var(--text-muted);
            margin-bottom: 4px;
        }}
        .c-spec-val {{
            font-size: 0.95rem;
            color: #fff;
            font-weight: 600;
        }}
        .chakra-deep-desc {{
            background: rgba(0, 0, 0, 0.3);
            border: 1px solid var(--border-glass);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            line-height: 1.8;
            font-size: 0.94rem;
            color: #e2e8f0;
        }}
        .chakra-proof-quote {{
            background: rgba(0, 240, 255, 0.04);
            border-right: 4px solid var(--cyan);
            border-radius: 8px;
            padding: 16px;
            line-height: 1.8;
            font-size: 0.9rem;
            color: #94a3b8;
        }}

        /* 9. Security Password Gate Overlay */
        #portal-auth-gate {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at center, #0e172a 0%, #03060a 100%);
            z-index: 99999;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            backdrop-filter: blur(25px);
            transition: opacity 0.5s ease, visibility 0.5s ease;
        }}
        #portal-auth-gate.unlocked {{
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
        }}
        .auth-card {{
            background: rgba(11, 15, 23, 0.92);
            border: 1px solid rgba(244, 180, 26, 0.35);
            border-radius: 24px;
            max-width: 440px;
            width: 100%;
            padding: 40px 30px;
            text-align: center;
            box-shadow: 0 25px 60px rgba(0,0,0,0.8), 0 0 40px rgba(244, 180, 26, 0.15);
            position: relative;
        }}
        .auth-logo-icon {{
            font-size: 3.5rem;
            margin-bottom: 15px;
            display: inline-block;
            filter: drop-shadow(0 0 20px rgba(244, 180, 26, 0.6));
            animation: pulse-ring 2.5s infinite;
        }}
        .auth-title {{
            font-size: 1.5rem;
            color: #fff;
            font-weight: 800;
            margin-bottom: 8px;
        }}
        .auth-subtitle {{
            font-size: 0.88rem;
            color: var(--text-muted);
            line-height: 1.6;
            margin-bottom: 24px;
        }}
        .auth-input-group {{
            margin-bottom: 20px;
            position: relative;
        }}
        .auth-password-input {{
            width: 100%;
            background: rgba(0, 0, 0, 0.6);
            border: 1px solid var(--border-glass);
            border-radius: 12px;
            padding: 14px 20px;
            font-size: 1.05rem;
            color: #fff;
            outline: none;
            text-align: center;
            letter-spacing: 3px;
            transition: all 0.25s;
        }}
        .auth-password-input:focus {{
            border-color: var(--gold);
            box-shadow: 0 0 15px var(--gold-glow);
        }}
        .auth-submit-btn {{
            width: 100%;
            background: linear-gradient(135deg, var(--gold), #64748b);
            border: none;
            color: #05070b;
            padding: 14px;
            border-radius: 12px;
            font-size: 1rem;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.25s;
            box-shadow: 0 8px 25px var(--gold-glow);
        }}
        .auth-submit-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 12px 30px rgba(244, 180, 26, 0.5);
        }}
        .auth-error-msg {{
            color: #ff3366;
            font-size: 0.84rem;
            margin-top: 12px;
            display: none;
        }}
        .auth-hint {{
            font-size: 0.78rem;
            color: var(--text-muted);
            margin-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.06);
            padding-top: 14px;
        }}

        /* 10. Comprehensive Mobile Responsiveness */
        @media (max-width: 860px) {{
            header {{
                flex-direction: column;
                gap: 12px;
                padding: 12px 16px;
            }}
            .brand-title {{
                font-size: 1.15rem;
                justify-content: center;
            }}
            .brand-subtitle {{
                text-align: center;
                font-size: 0.72rem;
            }}
            .nav-tabs {{
                width: 100%;
                overflow-x: auto;
                justify-content: flex-start;
                padding: 6px;
                -webkit-overflow-scrolling: touch;
            }}
            .nav-btn {{
                padding: 7px 12px;
                font-size: 0.78rem;
                flex-shrink: 0;
            }}
            main {{
                padding: 15px 10px 60px 10px;
            }}
            .hero h1 {{
                font-size: 1.5rem;
            }}
            .quran-ayah {{
                font-size: 0.95rem;
                padding: 10px 16px;
            }}
            #graph-fullscreen-wrapper {{
                height: 520px;
            }}
            #reader-drawer {{
                width: calc(100% - 30px);
                left: 15px;
                right: 15px;
                top: 60px;
                bottom: 15px;
                transform: translateY(110%);
            }}
            #reader-drawer.open {{
                transform: translateY(0);
            }}
            .silhouette-canvas {{
                width: 100%;
                max-width: 320px;
                height: 540px;
            }}
            .specs-grid {{
                grid-template-columns: 1fr;
            }}
            .books-grid {{
                grid-template-columns: 1fr;
            }}
            .zodiac-grid {{
                grid-template-columns: 1fr;
            }}
            .table-wrapper table {{
                font-size: 0.78rem;
            }}
            .spheres-container {{
                grid-template-columns: 1fr !important;
            }}
            .sphere-detail-panel {{
                position: static !important;
                top: auto !important;
            }}
            .compendium-cards-grid {{
                grid-template-columns: 1fr !important;
            }}
        }}
    </style>
</head>
<body>

    <!-- SECURITY PASSWORD GATE OVERLAY -->
    <div id="portal-auth-gate">
        <div class="auth-card">
            <div class="auth-logo-icon">🌌</div>
            <h2 class="auth-title">بوابة المعرفة الكوزمولوجية</h2>
            <p class="auth-subtitle">أطلس الكوزمولوجيا القرآنية وشبكة النبوات والمخطوطات العالمية. هذه المنظومة محمية ومخصصة للمعاينة الخاصة.</p>
            
            <form onsubmit="handlePortalAuth(event)">
                <div class="auth-input-group">
                    <input type="password" id="auth-pass-input" class="auth-password-input" placeholder="أدخل كلمة المرور..." autofocus autocomplete="off">
                </div>
                <button type="submit" class="auth-submit-btn">🔓 دخول المنظومة واستعراض البيانات</button>
                <div id="auth-error-msg" class="auth-error-msg">⚠️ كلمة المرور غير صحيحة، يرجى المحاولة مرة أخرى.</div>
            </form>

            <div class="auth-hint">
                🔒 كلمة المرور الافتراضية للمعاينة: <code style="color:var(--gold); font-weight:bold; font-size:0.95rem;">1234</code>
            </div>
        </div>
    </div>

    <header>
        <div>
            <div class="brand-title">🌌 أطلس الكوزمولوجيا القرآنية وشبكة المعرفة الشاملة</div>
            <div class="brand-subtitle">The Grand Unified Quranic Cosmology & Prophetic Knowledge Engine</div>
        </div>

        <nav class="nav-tabs">
            <button class="nav-btn active" onclick="switchTab('graph')">الشبكة الكونية الكبرى 🕸️</button>
            <button class="nav-btn" onclick="switchTab('spheres')">سلم الأفلاك والأنبياء 🪐</button>
            <button class="nav-btn" style="border: 1px solid #00f0ff; color: #00f0ff;" onclick="switchTab('chakras')">مجسم التشاكرات والأنبياء 🧘</button>
            <button class="nav-btn" onclick="switchTab('zodiac')">دائرة البروج الاثني عشر ♈</button>
            <button class="nav-btn" onclick="switchTab('timeline')">تعاقب العصور (2,160 سنة) ⏳</button>
            <button class="nav-btn" onclick="switchTab('matrix')">المصفوفة المعمارية الشاملة 🏛️</button>
            <button class="nav-btn" onclick="switchTab('manuscripts')">أمهات المخطوطات والكتب 📜</button>
            <button class="nav-btn" style="border: 1px solid #ff3366; color: #ff3366;" onclick="switchTab('critique')">ميزان القرآن ورصد التناقضات (للمرشد) ⚖️</button>
        </nav>
    </header>

    <main>

        <!-- TAB 1: FULLSCREEN MASTER FORCE GRAPH & THEORY VIEW -->
        <section id="tab-graph" class="tab-section active">
            <div id="graph-fullscreen-wrapper">
                <!-- MODE TOGGLE BAR: MOBILE THEORY VS DESKTOP CANVAS -->
                <div class="graph-mode-toggle-bar">
                    <div class="mode-toggle-buttons">
                        <button id="btn-mode-theory" class="mode-toggle-btn active" onclick="switchGraphMode('theory')">
                            <i class="fa-solid fa-book-open"></i> أطلس المفاهيم النظرية (موصى به للهاتف 📱)
                        </button>
                        <button id="btn-mode-canvas" class="mode-toggle-btn" onclick="switchGraphMode('canvas')">
                            <i class="fa-solid fa-circle-nodes"></i> شبكة الجراف البصرية ثلاثية الأبعاد (للكمبيوتر 💻)
                        </button>
                    </div>
                    <div class="mode-hint-text">
                        💡 تم تصميم الوضع النظري ليعمل على أي هاتف بسرعة فائقة وسلاسة تامة دون أي بطء أو تجميد للشاشة.
                    </div>
                </div>

                <div class="graph-top-filters">
                    <div class="pills-container">
                        <button class="filter-pill active" onclick="filterGraphCategory('ALL')">الكل 🌐</button>
                        <button class="filter-pill" style="border-color:#94a3b8; color:#94a3b8;" onclick="filterGraphCategory('أولو العزم من الرسل')">أولو العزم من الرسل 👑</button>
                        <button class="filter-pill" onclick="filterGraphCategory('دائرة البروج الاثني عشر')">دائرة البروج (12) ♈</button>
                        <button class="filter-pill" onclick="filterGraphCategory('الهيكل القرآني والمصفوفات')">الهيكل القرآني والمصفوفات 🔴</button>
                        <button class="filter-pill" onclick="filterGraphCategory('الدورات الكونية والفلك')">الدورات الفلكية 🔵</button>
                        <button class="filter-pill" onclick="filterGraphCategory('العصور والرسالات التاريخية')">العصور والرسالات 🟡</button>
                        <button class="filter-pill" onclick="filterGraphCategory('الميلوثيسيا وتصريف القوى')">الميلوثيسيا والطب 🟣</button>
                        <button class="filter-pill" onclick="filterGraphCategory('الهرمسية والكيمياء القديمة')">الخيمياء والهرمسية 🟢</button>
                        <button class="filter-pill" onclick="filterGraphCategory('الهندسة المقدسة والرياضيات')">الهندسة والرياضيات 🟠</button>
                        <button class="filter-pill" onclick="filterGraphCategory('المخطوطات والحكماء')">المخطوطات والحكماء 🌿</button>
                    </div>

                    <input type="text" id="graph-search-input" class="search-box" placeholder="🔍 ابحث في المفاهيم والروابط..." oninput="handleGraphSearch(this.value)">
                </div>

                <!-- 1. THEORY CARDS VIEW (DEFAULT ON MOBILE) -->
                <div id="graph-theory-container">
                    <div class="theory-cards-grid" id="theory-cards-grid">
                        <!-- Populated dynamically via JS -->
                    </div>
                </div>

                <!-- 2. CANVAS VIEW (DEFAULT ON DESKTOP) -->
                <div id="graph-canvas-container" style="display:none; position:relative; width:100%; height:100%;">
                    <div id="cosmic-network-canvas"></div>
                    <div class="graph-bottom-controls">
                        <button class="g-btn" onclick="if (cosmicNetwork) cosmicNetwork.fit({{animation: {{duration: 700}}}})">🔍 ضبط المشهد</button>
                        <button class="g-btn" id="physics-toggle-btn" onclick="toggleCosmicPhysics()">⏸ تثبيت / تحريك</button>
                        <button class="g-btn" onclick="resetFocus()">✨ إعادة تركيز</button>
                    </div>
                </div>

                <!-- BACKDROP FOR MOBILE DRAWER -->
                <div class="drawer-backdrop" id="drawer-backdrop" onclick="closeDrawer()"></div>

                <!-- SLIDING READER DRAWER / BOTTOM SHEET -->
                <div id="reader-drawer">
                    <div class="drawer-header">
                        <div class="drawer-title" id="drawer-title">عنوان المفهوم</div>
                        <button class="close-btn" onclick="closeDrawer()" title="إغلاق">✕</button>
                    </div>
                    <div class="drawer-meta" id="drawer-meta"></div>
                    <div class="drawer-body" id="drawer-body"></div>
                    <div class="drawer-connections">
                        <div class="conn-title">الروابط المتقاطعة مباشرة في الجراف:</div>
                        <div class="conn-pills" id="drawer-connections-pills"></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- TAB 2: SPHERES ASCENSION LADDER & UNIVERSAL THRONE -->
        <section id="tab-spheres" class="tab-section">
            <div class="hero">
                <div class="quran-ayah">«سَنُرِيهِمْ آيَاتِنَا فِي الْآفَاقِ وَفِي أَنفُسِهِمْ حَتَّىٰ يَتَبَيَّنَ لَهُمْ أَنَّهُ الْحَقُّ ۗ أَوَلَمْ يَكْفِ بِرَبِّكَ أَنَّهُ عَلَىٰ كُلِّ شَيْءٍ شَهِيدٌ» [فصلت: 53]</div>
                <h1>سلم الصعود الباطني: الأفلاك السبعة وعرش الرحمن</h1>
                <p>الموسوعة الكوزمولوجية الكبرى لمعراج الأرواح ومقامات الأنبياء: دراسة مضاهاة جامعة بين نصوص الوحي المحكم (القرآن وصحيحي البخاري ومسلم)، والفيزياء المدارية المعاصرة (Hans Cousto & Kepler)، وكشوفات أئمة العرفان والفلك الإسلامي (ابن عربي، ابن سينا، السهروردي، وإخوان الصفا).</p>
            </div>

            <!-- ANALYTICAL COSMOLOGICAL COMPENDIUM (6 MASTER WORLD MODULES) -->
            <div class="spheres-compendium">
                <div class="compendium-header">
                    <span class="compendium-badge">الموسوعة التحقيقية العالمية الكبرى • إجماع الحضارات والأديان والفلسفات</span>
                    <h2>معراج الأرواح وهندسة الأكوان السبعة وسدرة المنتهى عبر حضارات العالم</h2>
                    <p>ستة مباحث تأسيسية مفصلة تشهد فيها حضارات الأرض قاطبة بناموس الصعود السباعي: من نصوص الوحي المحكم (القرآن وصحيحي البخاري ومسلم)، إلى حكمة الصين الطاوية وعناصر وو شينغ، والفيدا الهندوسية، وزقورات بابل السومرية، وميثولوجيا وفلسفة اليونان (أفلاطون وأرسطو وأفلوطين)، والمتون الهرمسية (Poimandres)، والفيزياء المدارية الحديثة.</p>
                </div>

                <div class="compendium-cards-grid">
                    <!-- Treatise 1 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الأول 🏛️</span>
                            <h3>هندسة السماوات السبع وعرش الرحمن بين الوحي والفيزياء</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p><strong>التأسيس القرآني المحكم:</strong> تكرر ذكر السماوات السبع في القرآن في سبعة مواضع صريحة، أصلها قوله تعالى: <em>«الَّذِي خَلَقَ سَبْعَ سَمَاوَاتٍ طِبَاقًا ۖ مَّا تَرَىٰ فِي خَلْقِ الرَّحْمَٰنِ مِن تَفَاوُتٍ»</em> [الملك: 3]، وقوله: <em>«اللَّهُ الَّذِي خَلَقَ سَبْعَ سَمَاوَاتٍ وَمِنَ الْأَرْضِ مِثْلَهُنَّ يَتَنَزَّلُ الْأَمْرُ بَيْنَهُنَّ»</em> [الطلاق: 12].</p>
                            <p><strong>النسبة الهندسية الكونية (مقياس الكرسي والعرش):</strong> روى ابن حبان والبيهقي في 'الأسماء والصفات' عن أبي ذر الغفاري رضي الله عنه أن النبي ﷺ قال: <em>«ما السماوات السبع في الكرسي إلا كحلقة ملقاة بأرض فلاة، وفضل العرش على الكرسي كفضل تلك الفلاة على تلك الحلقة»</em>. يثبت هذا النص النبوي استحالة حصر الوجود في المادة المنظورة؛ فعالم الأجرام الفيزيائي المرئي بأضخم التلسكوبات (Hubble & James Webb) ليس سوى ذرة في فضاء الكرسي، والكرسي ذرة في فضاء العرش المحيط الأعظم.</p>
                            <p><strong>سماء الرؤية وسماء الملكوت:</strong> فرّق ابن سينا في <em>'رسالة المعراج'</em> والغزالي في <em>'مشكاة الأنوار'</em> بين 'السماء الفلكية المشاهدة' و'السماء الملكوتية المجردة'؛ حيث تمثل كل سماء رتبة وجودية وطاقية متصاعدة من التجرد الروحي، تتطابق مع الأبعاد الإضافية الملتفة (Extra Dimensions) في فيزياء الأوتار الفائقة (M-Theory).</p>
                        </div>
                    </div>

                    <!-- Treatise 2 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الثاني 🌌</span>
                            <h3>الجغرافيا الملكوتية: سدرة المنتهى، البيت المعمور، والأنهار الأربعة</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p><strong>سدرة المنتهى (شجرة الوجود الكبرى):</strong> تقع في أفق السماء السابعة وفوقها؛ قال تعالى: <em>«عِندَ سِدْرَةِ الْمُنتَهَىٰ * عِندَهَا جَنَّةُ الْمَأْوَىٰ * إِذْ يَغْشَى السِّدْرَةَ مَا يَغْشَىٰ»</em> [النجم: 14-16]. وفي صحيح مسلم عن ابن مسعود: <em>«إليها ينتهي ما يُعرج به من الأرض فيُقبض منها، وإليها ينتهي ما يُهبط به من فوقها فيُقبض منها»</em>. نبقها كقلال هجر وورقها كآذان الفيلة؛ وهي حد انتهاء النواميس الفيزيائية وبداية أنوار الجبروت الأحدي.</p>
                            <p><strong>البيت المعمور وتناظر الكعبة:</strong> في السماء السابعة مسنداً ظهره إليه أبو الأنبياء إبراهيم الخليل عليه السلام. يدخله كل يوم سبعون ألف ملك للتعبد لا يعودون إليه إلى يوم القيامة. وفي مستدرك الحاكم عن علي بن أبي طالب: <em>«هو بيت في السماء بحيال الكعبة، لو سقط لسقط عليها»</em>؛ مما يبرهن وجود محور رنيني كوني عمودي يربط مركز الأرض المشرفة (الكعبة) بمركز السماء السابعة (البيت المعمور) بالعرش الأعلى.</p>
                            <p><strong>الأنهار الكونية الأربعة (الفيض المزدوج):</strong> أخرج البخاري (3207) ومسلم (162): <em>«يخرج من أصلها نهران باطنان ونهران ظاهران، فقلت: ما هذان يا جبريل؟ قال: أما الباطنان فنهران في الجنة، وأما الظاهران فالنيل والفرات»</em>. فسر ابن حجر في <em>'فتح الباري'</em> وابن عربي في الباب 167 هذا المشهد بأن جريان النيل والفرات هو فيض البركة المادية والحياة العضوية لاستقرار الخلافة الإنسانية، بينما النهران الباطنان هما فيض العلم اللدني والحياة الأبدية الروحية.</p>
                        </div>
                    </div>

                    <!-- Treatise 3 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الثالث ⚖️</span>
                            <h3>سر الترتيب النبوي السباعي وفلسفة المعراج الروحي</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p><strong>1. فلك القمر (آدم - الأولى):</strong> أبو البشر وقالب الطين. يستقبل الروح الصاعدة من الأرض لأن منه تفرعت الأجساد، وعن يمينه نسم السعداء وشماله نسم الأشقياء.</p>
                            <p><strong>2. فلك عطارد (يحيى وعيسى - الثانية):</strong> اجتماع ابني الخالة؛ يحيى (سر الحياة الدائمة والطهارة) وعيسى (سر الكلمة والتزكية)، لتطهير العقل من سموم الشك قبل سماء الجمال.</p>
                            <p><strong>3. فلك الزهرة (يوسف - الثالثة):</strong> مقام شطر الحسن والجمال الإلهي المنعكس، وتأويل الرؤى؛ فالخيال المطلق هو البرزخ الجامع بين المعاني المجردة والصور الحسية.</p>
                            <p><strong>4. فلك الشمس (إدريس - الرابعة):</strong> قطب السماء ووسط الأفلاك. <em>«وَرَفَعْنَاهُ مَكَانًا عَلِيًّا»</em>؛ مقام هرمس الهرامسة وأول من خط بالقلم، متطابقاً مع توسط الشمس للمنظومة كقلب العالم النابض.</p>
                            <p><strong>5. فلك المريخ (هارون - الخامسة):</strong> مقام الألفة والمحبة الكهنوتية الحاكمة لحدة القهر؛ لتسكين نار المريخ بسكينة الود النبوي.</p>
                            <p><strong>6. فلك المشتري (موسى - السادسة):</strong> فلك التشريع والعدل الأكبر، وكليم الله صاحب التوراة والصعق، الممهد مباشرة لقمة التوحيد الخالص.</p>
                            <p><strong>7. فلك زحل (إبراهيم - السابعة):</strong> باني الكعبة، شيخ الأنبياء؛ مسنداً ظهره إلى البيت المعمور في فلك أقصى الثبات والتجرد والأبدية.</p>
                            <p><strong>8. سدرة المنتهى والعرش (محمد ﷺ - الفلك المحيط):</strong> تجاوز المقامات كلها <em>«فَكَانَ قَابَ قَوْسَيْنِ أَوْ أَدْنَىٰ»</em> حيث وقف جبريل قائلاً: <em>«لو تقدمت قيد أنملة لاحترقت بالأنوار»</em>.</p>
                        </div>
                    </div>

                    <!-- Treatise 4 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الرابع 🎵</span>
                            <h3>الترددات المدارية الكونية وقانون الأوكتاف (Hans Cousto & Kepler)</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p><strong>موسيقى الأفلاك (Musica Universalis):</strong> منذ يوهانس كبلر في كتابه التاريخي <em>Harmonices Mundi (1619)</em>، ثم التطبيق الرياضي والفيزيائي للعالم السويسري هانز كوستو في كتاب <em>The Cosmic Octave (1978)</em>، ثبت رياضياً أن لكل كوكب تردداً دورانياً ومدارياً ناتجاً عن زمن دورته حول الشمس وفق قوانين الميكانيكا الكلاسيكية (Kepler's Laws)، وبمضاعفة التردد بأوكتافات صوتية (f × 2^n) تتحول حركة الكواكب إلى نغمات مسموعة مقاسة بالهرتز (Hz).</p>
                            <p><strong>التناغم الرنيني والجسد البشري:</strong> إن ترددات الأفلاك السبعة تتوافق بدقة مذهلة مع ترددات مراكز الرنين الحيوي (الشاكرات والغدد الصماء - Melothesia)، حيث رصدت أبحاث الكيمياء الحيوية أن الرنين الكهرومغناطيسي للمنظومة الشمسية يترك أثراً حيوياً على الإيقاع اليومي (Circadian Rhythm) وإفرازات الهرمونات في الإنسان.</p>
                            <p><strong>مصفوفة الترددات المدارية المعتمدة:</strong> فلك القمر (210.42 Hz) • فلك عطارد (141.27 Hz) • فلك الزهرة (221.23 Hz) • فلك الشمس (126.22 Hz) • فلك المريخ (144.72 Hz) • فلك المشتري (183.58 Hz) • فلك زحل (147.85 Hz) • العرش المحيط (432 Hz / 528 Hz).</p>
                        </div>
                    </div>

                    <!-- Treatise 5 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الخامس 🌏</span>
                            <h3>سلم الصعود في حضارات الشرق: الصين الطاوية، الفيدا، وبابل</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p><strong>الصين الطاوية ونظام (Qi Zheng & Wuxing):</strong> في علم الفلك الصيني التراثي وكتاب <em>'هوانغدي نيجينغ' (Huangdi Neijing)</em>، تُعرف الكواكب الخمسة مع الشمس والقمر باسم الحكام السبعة 'تشي تشنغ' (Qi Zheng 七政). يرتبط كل كوكب بأحد العناصر الخمسة (وو شينغ Wuxing) وأحد الأعضاء الحيوية الخمسة: زحل (عنصر الأرض والرسوخ والطحال)، المشتري (عنصر الخشب والتوسع والكبد)، المريخ (عنصر النار والقلب والبأس)، الزهرة (عنصر المعدن والنقاء والرئتين)، وعطارد (عنصر الماء والذكاء والسيولة والكليتين). كما تحكم النجوم السبعة لدب الشمال (Beidou 北斗七星) بوابات الطاقة والمصائر الكونية في معراج الروح الطاوي.</p>
                            <p><strong>الهند والكونيات الفيدية (Sapta Loka & Meru):</strong> في نصوص الفيدا والأوبانيشاد وكتاب <em>'سوريا سيدهانتا' (Surya Siddhanta)</em>، يُقسم الكون إلى سبع طبقات عليا متصاعدة (Sapta Loka सप्तलोक): تبدأ من بهور لوكا (عالم الأرض والقمر)، وبهوفار، وسفار، وماهار، وجانا، وتاباس (سماء التجرد والزهد لزحل)، وصولاً إلى ساتيا لوكا (سماء الحقيقة المطلقة المقابلة لسدرة المنتهى). ويقوم الكون على محور جبل ميرو (Mount Meru) الذي تتطابق درجاته السبع مع الشاكرات السبع (من مولادارا إلى ساهاسرارا) في كتاب <em>Sat-Chakra-Nirupana</em>.</p>
                            <p><strong>بابل وسومر (زقورة الطبقات السبع Etemenanki):</strong> في بلاد الرافدين، شُيدت الزقورات المدرجة (مثل برج بابل وزقورة بورسيبا) من سبع طبقات مكسوة بألوان ومعادن الأفلاك السبعة تقديساً لحركة الآلهة الكوكبية: سين (القمر - الفضة)، نابو (عطارد - الأزرق الفاتح)، عشتار (الزهرة - الأخضر والذهب)، شمش (الشمس - صفائح الذهب)، نيرغال (المريخ - الآجر الأحمر)، مردوخ (المشتري - البرتقالي)، ونينورتا (زحل - الأسود الداكن)؛ لتمثل معراجاً معمارياً يربط الأرض بأعلى نقطة في سماء آنو.</p>
                        </div>
                    </div>

                    <!-- Treatise 6 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث السادس 🏛️</span>
                            <h3>سلم الأفلاك في الفلسفة اليونانية، الهرمسية، وميثرا</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p><strong>اليونان وأفلاطون وأرسطو:</strong> في ختام كتاب <em>'الجمهورية' (Republic - Book X)</em>، يروي أفلاطون 'أسطورة إير' (Myth of Er) واصفاً 'مغزل الضرورة' (Spindle of Necessity) المكون من ثماني دوائر كوكبية متداخلة تدور بنغمات متوافقة تصنع سيمفونية الكون. وفي كتاب <em>'في السماء' (De Caelo)</em> لأرسطو، تتراكب الأفلاك البلورية المتحدة المركز يقودها 'المحرك الأول الذي لا يتحرك'. وفي الأفلاطونية المحدثة عند أفلوطين (Plotinus) وبرقلس (Proclus)، تهبط النفس عبر الأفلاك السبعة متلبسة بجلابيب الكواكب، ثم ترتقي في المعراج العرفاني (Anagoge) متجردة من كثافة الكواكب لتعود للواحد الأحد (The One).</p>
                            <p><strong>المتون الهرمسية (Corpus Hermeticum - Poimandres):</strong> في الفصل الأول من متون هرمس، يصف المعلم هرمس الهرامسة صعود الروح عقب مفارقة الجسد عبر المناطق الكوكبية السبع؛ حيث تسلّم في كل سماء رذيلة أرضية اكتسبتها في النزول: تسلّم للقمر الغرائز والتغير، ولعطارد الحيل والمكر، وللزهرة الشهوة الزائفة، وللشمس حب السيادة، وللمريخ الجرأة الطائشة، وللمشتري الطمع، ولزحل المكر والحدود؛ حتى تدخل الفلك الثامن (Ogdoad) مجردة نقية لتندمج في نور الأنوار الإلهي.</p>
                            <p><strong>سلم ميثرا ذو الدرجات السبع وأسفار أخنوخ:</strong> وثّق الفيلسوف كلسوس (Celsus) في كتابه الذي رد عليه أوريجانوس (<em>Contra Celsum</em>) أن الطقوس الميثرائية تعتمد على سلم صعود ذي سبع درجات مصنوعة من سبعة معادن: الرصاص (زحل)، النحاس (الزهرة)، البرونز (المشتري)، الحديد (المريخ)، سبيكة الفضة (عطارد)، الفضة (القمر)، والذهب (الشمس). وهو ذات النمط المكرر في <em>'كتاب أخنوخ الثاني' (2 Enoch)</em> الذي يصف ارتقاء النبي إدريس (أخنوخ) عبر السماوات السبع وتلقيه أسرار الخلق وسفيرة التاج (Keter) في قبالاه <em>'سفر يتسيراه'</em>.</p>
                        </div>
                    </div>

                    <!-- Treatise 7: Master Synthesis -->
                    <div class="treatise-card" style="grid-column: 1 / -1; border-color: rgba(244, 180, 26, 0.4); background: radial-gradient(circle at top, rgba(244, 180, 26, 0.06), rgba(11, 17, 33, 0.95));">
                        <div class="treatise-card-header">
                            <span class="t-badge" style="background: rgba(244,180,26,0.2); color: var(--gold); border-color: var(--gold);">المبحث السابع 🌟 سيمفونية التوحيد الأكبر</span>
                            <h3>ملحمة الترابط الكوني: كيف تلاقت بصائر الإنسانية في شهادة واحدة لعظمة الخالق؟</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p><strong>سر الرقم (7) والناموس الوجودي:</strong> لماذا اتفقت الحضارات على السبعية؟ سبع سماوات، سبع أراضين، سبعة أيام للأسبوع، سبعة أبحر، سبع دورات طواف حول الكعبة، سبعة ألوان للطيف المرئي (Newton's Spectrum)، سبع نغمات للأوكتاف الموسيقي، سبعة معادن كيميائية كلاسيكية، وسبع شاكرات في علم الوظائف الحيوية؟ إن الرقم (7) في الهندسة المقدسة (Sacred Geometry) يمثل 'حد الاكتمال الدوري' في عالم الشهادة المادي والزماني، بينما الرقم (8) يمثل قفزة الانبعاث والعرش (Ogdoad / حملة العرش ثمانية)، والرقم (9) يمثل الفلك الأطلس المحيط بالكل. لقد صُمم الكون بنظام أوكتاف محكم يتكرر في كل مستوى وجودي.</p>
                            <p><strong>التناظر المذهل بين الإنسان الصغير والكون الكبير:</strong> أجمع حكماء الإسلام (إخوان الصفا، الغزالي، وابن عربي)، وحكماء الشرق (الطاوية والفيدا)، وفلاسفة اليونان (فيثاغورس وأفلاطون) على قاعدة: 'الإنسان نسخة مختصرة من العالم، والعالم إنسان كبير'. فالسماوات السبع بأفلاكها وتردداتها ونغماتها ليست أجراماً غريبة عنك؛ بل هي مطبوعة في مراكز طاقتك، وغددك الصماء، ومسارات تنفسك. حين يعرج الوعي الإنساني، فإنه لا يسافر في فراغ خارجي، بل يرتقي في درجات نفسه متحرراً من غلظة التراب ليدرك شرف نفخة الروح الأزلية.</p>
                            <p><strong>حل شفرة الخلاف الظاهري ووحدة الأصل النبوي:</strong> إن تطابق رمزية الكواكب والمعادن والطبقات السبع بين بابل ومصر والهند والصين واليونان ليس مصادفة عمياء؛ بل هو شاهد تاريخي حاسم على قوله تعالى: <em>«وَإِن مِّنْ أُمَّةٍ إِلَّا خَلَا فِيهَا نَذِيرٌ»</em> [فاطر: 24]. لقد انطلقت البشرية من مشكاة نبوية قديمة واحدة (بدأت بآدم وإدريس ونوح)، ثم توارثت الأمم هذه المعارف الكوزمولوجية وصاغتها بألسنتها وثقافاتها، حتى جاء الوحي القرآني الخاتم فصحح ما اعترى تلك الرموز من تحريف وشرك، وأعاد توجيه البوصلة كلها نحو الواحد الأحد الفرد الصمد: <em>«سَنُرِيهِمْ آيَاتِنَا فِي الْآفَاقِ وَفِي أَنفُسِهِمْ حَتَّىٰ يَتَبَيَّنَ لَهُمْ أَنَّهُ الْحَقُّ»</em> [فصلت: 53].</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- INTERACTIVE LADDER & DOSSIER PANEL -->
            <div class="spheres-container">
                <div class="ladder-list" id="spheres-list"></div>
                <div class="sphere-detail-panel" id="sphere-detail"></div>
            </div>

            <!-- GRAND COSMIC ODYSSEY & CIVILIZATION SYNTHESIS (THE LIVING JOURNEY) -->
            <div class="odyssey-wrapper" id="odyssey-experience">
                <div class="odyssey-header">
                    <span class="matrix-tag" style="background:rgba(244,180,26,0.15); color:var(--gold); border-color:rgba(244,180,26,0.35);">خلاصة الخلاصات وسيمفونية التوحيد الأكبر</span>
                    <h2>أوديسة الروح ومعراج الكينونة: السيمفونية الكونية الكبرى وعظمة خلق الله</h2>
                    <p>هنا ينحل لغز آلاف السنين، وتذوب الفروق الظاهرية بين لغات الأمم ورموزها؛ لترى كيف اجتمعت نصوص الوحي المعصوم، ومخطوطات الصين الطاوية، وتراتيل الفيدا الهندية، وزقورات بابل، ومثالية أفلاطون، وهرمسية الإسكندرية، في سيمفونية واحدة تعزف تسبيح الخالق الأعظم، لتدرك أنك لست مجرد متفرج على الكون.. بل أنت الكون متجسداً في وعي يسعى إلى معراجه الأبدي.</p>
                </div>

                <!-- Navigation Tabs for the 8 Gates -->
                <div class="odyssey-nav-bar" id="odyssey-nav"></div>

                <!-- Active Stage Dynamic Canvas -->
                <div id="odyssey-stage-container"></div>
            </div>

            <!-- PANORAMIC COMPARATIVE MATRIX TABLE -->
            <div class="panoramic-matrix-wrapper">
                <div class="matrix-table-header">
                    <span class="matrix-tag">المصفوفة الكوزمولوجية الكبرى</span>
                    <h3>جدول المضاهاة البانورامية الشاملة للأفلاك السبعة وعرش الرحمن</h3>
                    <p>مقارنة أفقية وعمودية دقيقة تلخص النواميس الكونية السبعة وما وراءها: الأنبياء المقيمون، النصوص المسندة، الترددات المدارية بالهرتز (Hz)، التشاكرات، الغدد الصماء، المعادن الخيميائية، الملائكة، والمبادئ الهرمسية الحاكمة.</p>
                </div>
                <div class="matrix-responsive-table">
                    <table class="panoramic-spheres-table">
                        <thead>
                            <tr>
                                <th>الفلك والكوكب</th>
                                <th>السماء والمقام</th>
                                <th>النبي الحاكم</th>
                                <th>التردد المداري (Hz)</th>
                                <th>المعدن الخيميائي</th>
                                <th>الشاكرا واللطيفة</th>
                                <th>الغدة الصماء</th>
                                <th>الملاك الموكل</th>
                                <th>الصين والطاوية (Wuxing)</th>
                                <th>الفيدا والهندوسية</th>
                                <th>بابل واليونان الفلسفية</th>
                                <th>الهرمسية وأخنوخ والقبالاه</th>
                                <th>السر العرفاني الوجودي</th>
                            </tr>
                        </thead>
                        <tbody id="panoramic-spheres-tbody"></tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- TAB CHAKRAS: PROPHETIC BODY & 7 CHAKRAS HOLOGRAPHIC VISUALIZER -->
        <section id="tab-chakras" class="tab-section">
            <div class="hero">
                <div class="quran-ayah">«وَفِي أَنفُسِكُمْ ۚ أَفَلَا تُبْصِرُونَ» [الذاريات: 21] — «لَقَدْ خَلَقْنَا الْإِنسَانَ فِي أَحْسَنِ تَقْوِيمٍ» [التين: 4]</div>
                <h1 style="color: #00f0ff;">مجسم التشاكرات السبعة واللطائف ومقامات الأنبياء (العالم الصغير)</h1>
                <p>الموسوعة التشريحية الكبرى للإنسان الكامل: دراسة مضاهاة جامعة بين اللطائف الصوفية السبع، الشاكرات الفيدية (Sat-Chakra-Nirupana)، الدانتيان ومسارات التشي الصينية (Jing-Luo)، شجرة الحياة الكابالية، ومحور الغدد الصماء والضفائر العصبية الحديث (Neuro-Endocrine Axis).</p>
            </div>

            <!-- ANALYTICAL COMPENDIUM FOR CHAKRAS & MICROCOSM (4 MASTER TREATISES) -->
            <div class="spheres-compendium" style="margin-bottom: 40px;">
                <div class="compendium-header">
                    <span class="compendium-badge">الموسوعة التحقيقية للعالم الصغير • الإنسان الكامل وتشريح النور</span>
                    <h2>هندسة مراكز الروح والجسد الأثيري ومطابقة المقامات عبر حضارات الأرض</h2>
                    <p>أربعة مباحث تأسيسية متعمقة تشهد فيها الفلسفة الإسلامية، والطب الفلكي القديم، ونصوص الفيدا، والطاوية الصينية، والبيولوجيا العصبية المعاصرة بأن الإنسان هو النسخة الجامعة للكون الأكبر، وأن مراكز طاقته هي بوابات معراج الوعي.</p>
                </div>

                <div class="compendium-cards-grid">
                    <!-- Treatise 1 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الأول 🧘</span>
                            <h3>نظرية الإنسان الكامل والعالم الصغير (Microcosm) في العرفان الإسلامي</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p><strong>تطابق الأكوان في القبضة الإنسانية:</strong> أجمع حكماء الإسلام وأئمة العرفان - من الإمام علي في بيته المشهور: <em>«أتزعم أنك جرم صغير وفيك انطوى العالم الأكبر؟»</em>، إلى عبد الكريم الجيلي في كتابه <em>'الإنسان الكامل في معرفة الأواخر والأوائل'</em> وابن عربي في <em>'الفتوحات المكية' (الباب 361)</em> - على أن الإنسان هو الثمرة المقصودة من شجرة الوجود. فكل فلك كوكبي في السماء، وكل عنصر طبيعي، وكل صفة إلهية، لها مركز مطابق في باطن التركيب الإنساني، بحيث صار جسد الإنسان خريطة حية لكامل أبعاد الملك والملكوت.</p>
                            <p><strong>النفخة الإلهية وقالب الطين:</strong> يمثل الجسد الترابي قاعدة الهرم (شاكرا الجذر / سماء آدم)، بينما تمثل الروح القدسية قمة الهرم وسدرة المنتهى (شاكرا التاج والهالة المحمدية). وبين القاع والقمة تمتد قناة النور (الصراط الباطني)، فكلما ترقى الإنسان بتزكية نفسه عبر مقامات الأنبياء، انفتحت له بوابات الفهم الكوني وتطهرت لطائفه من كثافة التراب.</p>
                        </div>
                    </div>

                    <!-- Treatise 2 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الثاني ⚡</span>
                            <h3>فسيولوجيا النور: مطابقة الشاكرات مع الغدد الصماء والضفائر العصبية</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p><strong>المحور العصبي والغدي (Neuro-Endocrine-Vagal Axis):</strong> كشفت العلوم الطبية الحديثة عن تطابق تام بين مواقع مراكز الطاقة القديمة ومراكز التحكم الفسيولوجي الأعمق في الجسم البشري: فشاكرا التاج تطابق الغدة الصنوبرية (إفراز الميلاتونين وحفظ الإيقاع الحيوي)، وشاكرا الجبين تطابق الغدة النخامية (سيدة الغدد الصماء Master Gland)، وشاكرا الحنجرة تطابق الغدة الدرقية المنظمة للأيض، وشاكرا القلب تطابق غدة التيموس (مركز المناعة الخلوية) والضفيرة القلبية، وشاكرا الضفيرة تطابق البنكرياس والضفيرة البطنية (Celiac Plexus)، وشاكرا العجز تطابق الغدد التناسلية، وشاكرا الجذر تطابق غدتي الكظر (الأدرينالين ومواجهة الخطر).</p>
                            <p><strong>ترددات الأوكتاف الكوني والنبض الحيوي (Hz):</strong> وفق أبحاث الفيزياء الحيوية وقوانين هانز كوستو، تهتز كل شاكرا وكل عضو بتردد رنيني محدد بالهرتز يطابق بدقة الترددات الصوتية الناتجة عن دوران الكواكب، مما يثبت أن صحة الإنسان الجسدية والنفسية تعتمد على تناغمه الرنيني مع السيمفونية الكونية المحيطة به.</p>
                        </div>
                    </div>

                    <!-- Treatise 3 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الثالث 🌏</span>
                            <h3>الإجماع الحضاري: اللطائف الصوفية، الشاكرات الفيدية، ومسارات التشي الصينية</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p><strong>اللطائف الصوفية السبع (طريق السلوك النقشبندي):</strong> يقابل العرفان الإسلامي الشاكرات الفيدية بما يُعرف بـ 'اللطائف السبع': لطيفة القالب (الجسد)، لطيفة النفس (تحت السرة)، لطيفة القلب (يسار الصدر)، لطيفة الروح (يمين الصدر)، لطيفة السر (فوق القلب)، لطيفة الخفي (فوق الروح)، ولطيفة الأخفى (وسط الصدر وأعلى الرأس). يترقى السالك بالذكر القلبي لتطهير كل لطيفة حتى يشرق نور الأحدية.</p>
                            <p><strong>الصين والطاوية (حقول الدانتيان ومسارات Jing-Luo):</strong> في الطب الصيني التقليدي وكتاب <em>'هوانغدي نيجينغ'</em>، لا يُنظر للجسد ككتلة مادية، بل كشبكة من 12 مساراً رئيسياً لسريان طاقة التشي (Qi)، تتجمع في ثلاثة حقول كبرى تسمى الدانتيان (Dan Tian): الدانتيان السفلي (مركز طاقة الحياة والجوهر Jing في أسفل البطن)، الدانتيان الأوسط (مركز التنفس والمشاعر Qi في الصدر)، والدانتيان العلوي (مركز الروح والوعي الاستناري Shen في الجبين بين الحاجبين).</p>
                        </div>
                    </div>

                    <!-- Treatise 4 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الرابع 🏛️</span>
                            <h3>علم الميلوثيسيا الطبية والطب الفلكي القديم (ابن سينا والبيروني)</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p><strong>التشريح الفلكي للأعضاء والأمزجة:</strong> فصّل الشيخ الرئيس ابن سينا في كتابه الخالد <em>'القانون في الطب'</em>، وأبو الريحان البيروني في <em>'التفهيم لأوائل صناعة التنجيم'</em>، وأطباء الإسكندرية واليونان (أبقراط وجالينوس)، علم 'الميلوثيسيا' (Melothesia) وهو مطابقة أعضاء الجسد البشري بالبروج الاثني عشر والكواكب السبعة: فالرأس للحمل، والحنجرة للثور، والصدر للسرطان، والقلب للأسد والشمس، والعمود الفقري للميزان، وصولاً للأقدام عند الحوت.</p>
                            <p><strong>توازن الأخلاط الأربعة واستشفاء الروح:</strong> قرر هذا العلم أن المرض هو اضطراب في ميزان الأخلاط الأربعة (الدم، البلغم، الصفراء، والسوداء) الناتجة عن طبائع العناصر الكونية (الحرارة، البرودة، الرطوبة، واليبوسة). والعلاج الكامل لا يقتصر على العقاقير الكيميائية وحدها، بل يشمل موازنة الرنين الطاقي وتصحيح مسار التنفس وتطهير الخيال بالتوحيد والسكينة الروحية.</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="chakras-container">
                <!-- Human Silhouette Hologram -->
                <div class="body-silhouette-wrapper">
                    <div style="font-size: 0.95rem; font-weight: 700; color: var(--gold); margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
                        <span>🧘 مجسم الجسد الأثيري ومسار الشوشومنا (قناة النور)</span>
                    </div>

                    <!-- Interactive Quick Selector Pills -->
                    <div class="chakra-pills-bar" id="chakra-pills-bar"></div>

                    <div class="silhouette-canvas" id="silhouette-canvas">
                        <!-- High-Tech Sacred Meditating Human Hologram SVG -->
                        <svg class="human-figure-svg" viewBox="0 0 320 540" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <defs>
                                <linearGradient id="bodyGrad" x1="0" y1="0" x2="0" y2="540" gradientUnits="userSpaceOnUse">
                                    <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.35" />
                                    <stop offset="50%" stop-color="#00f0ff" stop-opacity="0.22" />
                                    <stop offset="100%" stop-color="#ef4444" stop-opacity="0.35" />
                                </linearGradient>
                                <linearGradient id="spineRainbow" x1="0" y1="30" x2="0" y2="480" gradientUnits="userSpaceOnUse">
                                    <stop offset="0%" stop-color="#ffffff" />
                                    <stop offset="12%" stop-color="#a855f7" />
                                    <stop offset="25%" stop-color="#3b82f6" />
                                    <stop offset="40%" stop-color="#00f0ff" />
                                    <stop offset="55%" stop-color="#10b981" />
                                    <stop offset="70%" stop-color="#f59e0b" />
                                    <stop offset="85%" stop-color="#f97316" />
                                    <stop offset="100%" stop-color="#ef4444" />
                                </linearGradient>
                                <radialGradient id="auraGlow" cx="160" cy="95" r="90" gradientUnits="userSpaceOnUse">
                                    <stop offset="0%" stop-color="#fbbf24" stop-opacity="0.65" />
                                    <stop offset="60%" stop-color="#00f0ff" stop-opacity="0.25" />
                                    <stop offset="100%" stop-color="#000000" stop-opacity="0" />
                                </radialGradient>
                                <filter id="glowFilt" x="-20%" y="-20%" width="140%" height="140%">
                                    <feGaussianBlur stdDeviation="3" result="blur" />
                                    <feComposite in="SourceGraphic" in2="blur" operator="over" />
                                </filter>
                            </defs>

                            <!-- Glowing Aura Background -->
                            <circle cx="160" cy="95" r="85" fill="url(#auraGlow)" />
                            
                            <!-- Sacred Geometry Halo behind Head -->
                            <circle cx="160" cy="95" r="75" stroke="rgba(251, 191, 36, 0.7)" stroke-width="1.8" stroke-dasharray="6 4" />
                            <circle cx="160" cy="95" r="60" stroke="rgba(0, 240, 255, 0.5)" stroke-width="1.2" />
                            <circle cx="160" cy="95" r="45" stroke="rgba(168, 85, 247, 0.6)" stroke-width="1.2" stroke-dasharray="3 3" />
                            <!-- Radiating Rays -->
                            <line x1="160" y1="15" x2="160" y2="35" stroke="#fbbf24" stroke-width="2.5" />
                            <line x1="160" y1="155" x2="160" y2="175" stroke="#fbbf24" stroke-width="2" />
                            <line x1="80" y1="95" x2="100" y2="95" stroke="#fbbf24" stroke-width="2" />
                            <line x1="220" y1="95" x2="240" y2="95" stroke="#fbbf24" stroke-width="2" />
                            <line x1="105" y1="40" x2="118" y2="53" stroke="rgba(251, 191, 36, 0.8)" stroke-width="1.8" />
                            <line x1="215" y1="40" x2="202" y2="53" stroke="rgba(251, 191, 36, 0.8)" stroke-width="1.8" />

                            <!-- Meditating Human Silhouette Contour (Lotus Pose) -->
                            <circle cx="160" cy="95" r="28" fill="url(#bodyGrad)" stroke="#00f0ff" stroke-width="1.8" />
                            <path d="M152,122 L150,135 L170,135 L168,122" fill="url(#bodyGrad)" stroke="#00f0ff" stroke-width="1.5" />
                            <path d="M150,135 C138,138 112,148 95,165 C78,182 66,215 62,250 C58,285 64,310 75,325 C84,337 96,335 105,320 C114,305 118,275 125,235 C130,205 136,175 145,160 L145,260 C138,295 132,340 120,370 C108,400 78,430 52,455 C35,472 40,498 70,505 C108,512 140,512 160,512 C180,512 212,512 250,505 C280,498 285,472 268,455 C242,430 212,400 200,370 C188,340 182,295 175,260 L175,160 C184,175 190,205 195,235 C202,275 206,305 215,320 C224,335 236,337 245,325 C256,310 262,285 258,250 C254,215 242,182 225,165 C208,148 182,138 170,135 Z" 
                                  fill="url(#bodyGrad)" stroke="#00f0ff" stroke-width="1.8" filter="url(#glowFilt)" />

                            <!-- Meditating Hands in Mudra over Lap -->
                            <ellipse cx="160" cy="425" rx="36" ry="16" fill="rgba(0, 240, 255, 0.12)" stroke="rgba(0, 240, 255, 0.5)" stroke-width="1.5" />

                            <!-- Sacred Heart Geometry (Merkabah) at Heart Center -->
                            <polygon points="160,230 182,268 138,268" stroke="rgba(16, 185, 129, 0.45)" stroke-width="1.2" fill="none" />
                            <polygon points="160,280 182,242 138,242" stroke="rgba(16, 185, 129, 0.45)" stroke-width="1.2" fill="none" />
                            <circle cx="160" cy="255" r="24" stroke="rgba(244, 180, 26, 0.3)" stroke-width="1" stroke-dasharray="2 2" fill="none" />

                            <!-- Sushumna (Central Spine Rainbow Light Channel) -->
                            <line x1="160" y1="45" x2="160" y2="480" stroke="url(#spineRainbow)" stroke-width="4.5" stroke-linecap="round" />

                            <!-- Ida (Left Lunar Channel - Cyan) -->
                            <path d="M160,470 C135,435 135,415 160,395 C185,360 185,345 160,325 C135,290 135,275 160,255 C185,225 185,210 160,195 C135,165 135,155 160,140 C185,110 185,100 160,85" 
                                  stroke="#00f0ff" stroke-width="2" stroke-dasharray="4 3" fill="none" opacity="0.75" />

                            <!-- Pingala (Right Solar Channel - Radiant Luminous Gold) -->
                            <path d="M160,470 C185,435 185,415 160,395 C135,360 135,345 160,325 C185,290 185,275 160,255 C135,225 135,210 160,195 C185,165 185,155 160,140 C135,110 135,100 160,85" 
                                  stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="4 3" fill="none" opacity="0.9" />
                        </svg>

                        <!-- 8 Chakra Pulsating Interactive Nodes on Body -->
                        <div class="chakra-point-btn" id="chakra-node-8" style="top: 38px; color: #fbbf24; border-color: #fbbf24; background: rgba(251, 191, 36, 0.35); box-shadow: 0 0 25px #fbbf24;" onclick="selectChakra(8)" title="الهالة المحيطة — النبي محمد ﷺ">👑</div>
                        <div class="chakra-point-btn" id="chakra-node-7" style="top: 85px; color: #a855f7; border-color: #a855f7;" onclick="selectChakra(7)" title="شاكرا التاج — إبراهيم الخليل">🟣</div>
                        <div class="chakra-point-btn" id="chakra-node-6" style="top: 140px; color: #3b82f6; border-color: #3b82f6;" onclick="selectChakra(6)" title="شاكرا العين الثالثة — موسى وهارون">👁️</div>
                        <div class="chakra-point-btn" id="chakra-node-5" style="top: 195px; color: #00f0ff; border-color: #00f0ff;" onclick="selectChakra(5)" title="شاكرا الحنجرة — داود وسليمان">🗣️</div>
                        <div class="chakra-point-btn" id="chakra-node-4" style="top: 255px; color: #10b981; border-color: #10b981;" onclick="selectChakra(4)" title="شاكرا القلب — عيسى المسيح وإدريس">💚</div>
                        <div class="chakra-point-btn" id="chakra-node-3" style="top: 325px; color: #f59e0b; border-color: #f59e0b;" onclick="selectChakra(3)" title="شاكرا الضفيرة الشمسية — يوسف الصديق">🟡</div>
                        <div class="chakra-point-btn" id="chakra-node-2" style="top: 395px; color: #f97316; border-color: #f97316;" onclick="selectChakra(2)" title="شاكرا العجز — نوح عليه السلام">🟠</div>
                        <div class="chakra-point-btn" id="chakra-node-1" style="top: 470px; color: #ef4444; border-color: #ef4444;" onclick="selectChakra(1)" title="شاكرا الجذر — آدم عليه السلام">🔴</div>
                    </div>

                    <div style="margin-top: 15px; font-size: 0.8rem; color: var(--text-muted); text-align: center;">
                        اضغط على أي مركز طاقة (شاكرا) لإظهار التحليل الباطني والنقلة في الوعي 👆
                    </div>
                </div>

                <!-- Deep Interactive Synthesis Panel -->
                <div class="chakra-detail-card" id="chakra-detail-card">
                    <!-- Injected dynamically by JS -->
                </div>
            </div>

            <!-- PANORAMIC COMPARATIVE MATRIX TABLE FOR CHAKRAS & MICROCOSM -->
            <div class="panoramic-matrix-wrapper">
                <div class="matrix-table-header">
                    <span class="matrix-tag">المصفوفة التشريحية الكبرى</span>
                    <h3>جدول المضاهاة البانورامية الشاملة لمراكز الطاقة والإنسان الكامل (العالم الصغير)</h3>
                    <p>مقارنة أفقية وعمودية دقيقة تلخص نواميس الطاقة الإنسانية السبعة وما وراءها: اللطائف الصوفية، الأنبياء والمقامات، الأفلاك والمعادن، الترددات بالهرتز (Hz)، الغدد الصماء، الضفائر العصبية، الدانتيان الصيني، الفيدا (Bija Mantra)، سفيرات شجرة الحياة، والنقلة في الوعي الباطني.</p>
                </div>
                <div class="matrix-responsive-table">
                    <table class="panoramic-spheres-table">
                        <thead>
                            <tr>
                                <th>الشاكرا والمركز</th>
                                <th>اللطيفة الصوفية</th>
                                <th>النبي والمقام</th>
                                <th>الفلك والكوكب</th>
                                <th>التردد (Hz)</th>
                                <th>الغدة الصماء</th>
                                <th>الضفيرة العصبية</th>
                                <th>الدانتيان والعنصر الصيني</th>
                                <th>الفيدا (Bija Mantra)</th>
                                <th>سفيرة شجرة الحياة</th>
                                <th>النقلة في الوعي الباطني</th>
                            </tr>
                        </thead>
                        <tbody id="panoramic-chakras-tbody"></tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- TAB 3: 12 ZODIAC SIGNS -->
        <section id="tab-zodiac" class="tab-section">
            <div class="hero">
                <div class="quran-ayah">«وَالسَّمَاءِ ذَاتِ الْبُرُوجِ» [البروج: 1] — «تَبَارَكَ الَّذِي جَعَلَ فِي السَّمَاءِ بُرُوجًا وَجَعَلَ فِيهَا سِرَاجًا وَقَمَرًا مُّنِيرًا» [الفرقان: 61]</div>
                <h1>دائرة البروج الاثني عشر: التشريح الباطني والرموز الرسالية</h1>
                <p>الربط المعرفي والتحليلي الأعمق لدائرة الفلك الكبرى: العناصر الأربعة، الطبائع، الحكام الكوكبيين، أسباط بني إسرائيل الـ 12 في الرؤيا اليوسفية، التشريح الإنساني الفلكي (الميلوثيسيا الطبية)، والإجماع الحضاري العالمي الشامل بين بابل، مصر القديمة، الصين، والفيدا.</p>
            </div>

            <!-- 4 MASTER ANALYTICAL TREATISES -->
            <div class="spheres-compendium">
                <div class="compendium-header">
                    <span class="compendium-badge">الموسوعة التحليلية التأسيسية للباب 04</span>
                    <h2>المباحث الكوزمولوجية الكبرى في حكمة البروج الاثني عشر والميلوثيسيا</h2>
                    <p>أربعة مباحث عيانية تربط بين الإحكام القرآني، الطب الفلكي التراثي، الرؤيا اليوسفية للأسباط، ونواميس دورات الزمان وترنح الاعتدالين.</p>
                </div>

                <div class="compendium-cards-grid">
                    <!-- Treatise 1 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الأول</span>
                            <h3>نواميس البروج في القرآن الكريم وسر الرؤيا اليوسفية والأسباط الـ 12</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p>أقسم الحق سبحانه بالسماء ذات البروج تنبيهاً على عظمة هذه المنازل المحكمة ومواقع النجوم الحافظة لتوازن الأرض. وفي سورة يوسف، تجلت الرؤيا الرسالية الخارقة: ﴿إِنِّي رَأَيْتُ أَحَدَ عَشَرَ كَوْكَبًا وَالشَّمْسَ وَالْقَمَرَ رَأَيْتُهُمْ لِي سَاجِدِينَ﴾؛ حيث يوسف هو قطب المركز المكمل للاثني عشر كوكباً رمزاً للأسباط الاثني عشر الذين تفرعت منهم شعوب بني إسرائيل. كما تطابق هذا العدد مع ﴿إِنَّ عِدَّةَ الشُّهُورِ عِندَ اللَّهِ اثْنَا عَشَرَ شَهْرًا فِي كِتَابِ اللَّهِ يَوْمَ خَلَقَ السَّمَاوَاتِ وَالْأَرْضَ﴾، وحواريي المسيح الاثني عشر، ونقباء بني إسرائيل الاثني عشر: ﴿وَبَعَثْنَا مِنْهُمُ اثْنَيْ عَشَرَ نَقِيبًا﴾، ليدل على أن دائرة الـ 12 هي ناموس التقسيم الإلهي الموزون لحركة الفلك والرسالات في الزمان والمكان.</p>
                        </div>
                    </div>

                    <!-- Treatise 2 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الثاني</span>
                            <h3>علم الميلوثيسيا الطبية (Astrological Melothesia) والتشريح الإنساني</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p>في أمهات كتب الطب والرياضيات القديمة (قانون ابن سينا، وتفهيم البيروني، ومتون أبقراط وجالينوس وبطليموس وبولس السكندري)، قُسّم جسد الإنسان الصغير (Microcosm) وفق مسار دائرة البروج من الرأس إلى القدمين: يبدأ بالحمل الحاكم للرأس والدماغ والعينين، هبوطاً عبر الثور (العنق والدرقية)، فالجوزاء (الكتفان والرئتان والأعصاب)، فالسرطان (الصدر والمعدة)، فالأسد (القلب والشرايين)، فالعذراء (الأمعاء والهضم)، فالميزان (الكليتان والتوازن)، فالعقرب (التناسل والإخراج والتجدد)، فالقوس (الفخذان والحركة الكبرى)، فالجدي (الهيكل العظمي والركبتان)، فالدلو (الساقان والجهاز الدوري الكهربائي)، ختاماً بالحوت (القدمان والمناعة اللمفاوية). وهذا يثبت أن الإنسان هو نسخة مصغرة ومجسم حي لكامل قبة السماء.</p>
                        </div>
                    </div>

                    <!-- Treatise 3 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الثالث</span>
                            <h3>الإجماع الكوزمولوجي العالمي: بابل، زودياك دندرة، الصين، والفيدا</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p>أجمعت حضارات الأرض قاطبة على تقسيم المسار الشمسي الظاهري (Ecliptic) إلى 12 قسماً متساوياً كل منها 30 درجة: في بابل القديمة سُجلت البروج في ألواح «مول-أبين» (MUL.APIN) كأساس للتقويم الكوني. وفي مصر القديمة نُقش سقف معبد دندرة الشهير (Dendera Zodiac) ليجمع البروج الاثني عشر مع العشريات النجمية (Decans). وفي الصين الإمبراطورية قُسم الفلك إلى الفروع الأرضية الاثني عشر (Di Zhi - 十二地支) الممثلة للحيوانات الفلكية الكبرى ودورات طاقة التشي. وفي الهند وفلسفة الفيدا تسمى «الراشي» (Rashi) المقسمة على 27 منزلة قمرية (Nakshatras). إن هذا التطابق التام عبر القارات المعزولة تاريخياً هو شاهد قاطع على أصل النبوة الواحد الذي علّم البشرية نواميس الكون.</p>
                        </div>
                    </div>

                    <!-- Treatise 4 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الرابع</span>
                            <h3>محور الأقطاب والتقابل التناغمي (180° Polarity) وترنح الاعتدالين</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p>كل برج في الدائرة الفلكية لا يعمل بمعزل عن نقيضه؛ بل يرتبط بخط قطبي مستقيم بزاوية 180 درجة يشكل معه ثنائية تكاملية لا تنفصم: الحمل (الأنا والمبادأة) يقابله الميزان (الآخر والعدل)، الثور (المادة والاستقرار) يقابله العقرب (التحول والبعث والموت)، الجوزاء (المعرفة والمعلومات) يقابله القوس (الحكمة والرؤية الكلية)، السرطان (الرحم والأصل) يقابله الجدي (البناء والهيكل)، الأسد (السيادة الفردية والقلب) يقابله الدلو (الجماعة والإنسانية الكلية)، والعذراء (الخدمة والجسد وسنبلة القمح) يقابله الحوت (الروحانية والمحيط والسمكة). وتتحرك الشمس عبر هذه المحاور في ظاهرة ترنح الاعتدالين (Precession) كل 2,160 سنة، لتحدد العصر الرسالي والحضاري الحاكم للبشرية.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- INTERACTIVE ZODIAC CELESTIAL WHEEL & MASTER DOSSIER PANEL -->
            <div class="chakras-container" style="margin-bottom: 40px;">
                <!-- Celestial Zodiac Wheel Visualizer -->
                <div class="body-silhouette-wrapper" style="min-height: 580px;">
                    <div style="font-size: 0.95rem; font-weight: 700; color: var(--gold); margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
                        <span>🌌 القبة الفلكية وعجلة البروج الاثني عشر التفاعلية (360°)</span>
                    </div>

                    <!-- Quick Selector Pills Bar -->
                    <div class="chakra-pills-bar" id="zodiac-pills-bar"></div>

                    <!-- Interactive Wheel SVG Container -->
                    <div class="zodiac-wheel-canvas" id="zodiac-wheel-canvas">
                        <svg class="zodiac-wheel-svg" viewBox="0 0 380 380" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <defs>
                                <radialGradient id="sunGlowZod" cx="190" cy="190" r="100" gradientUnits="userSpaceOnUse">
                                    <stop offset="0%" stop-color="#94a3b8" stop-opacity="0.45" />
                                    <stop offset="60%" stop-color="#f59e0b" stop-opacity="0.12" />
                                    <stop offset="100%" stop-color="#000000" stop-opacity="0" />
                                </radialGradient>
                                <linearGradient id="wheelRingGrad" x1="0" y1="0" x2="380" y2="380" gradientUnits="userSpaceOnUse">
                                    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.6" />
                                    <stop offset="50%" stop-color="#94a3b8" stop-opacity="0.4" />
                                    <stop offset="100%" stop-color="#a855f7" stop-opacity="0.6" />
                                </linearGradient>
                            </defs>
                            <!-- Background Sun Glow -->
                            <circle cx="190" cy="190" r="100" fill="url(#sunGlowZod)" />
                            
                            <!-- Outer Concentric Rings -->
                            <circle cx="190" cy="190" r="175" stroke="url(#wheelRingGrad)" stroke-width="2" stroke-dasharray="4 4" />
                            <circle cx="190" cy="190" r="145" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1.5" />
                            <circle cx="190" cy="190" r="115" stroke="rgba(0, 240, 255, 0.3)" stroke-width="1" stroke-dasharray="6 3" />
                            <circle cx="190" cy="190" r="75" stroke="rgba(251, 191, 36, 0.6)" stroke-width="1.8" />
                            <circle cx="190" cy="190" r="38" stroke="#fbbf24" stroke-width="2.5" />
                            
                            <!-- Central Golden Sun -->
                            <circle cx="190" cy="190" r="22" fill="#f59e0b" />
                            <circle cx="190" cy="190" r="10" fill="#fff" />
                            
                            <!-- 12 Harmonic Radiating Axes (Crossing at 180° Polarities) -->
                            <line x1="190" y1="15" x2="190" y2="365" stroke="rgba(148, 163, 184, 0.25)" stroke-width="1" />
                            <line x1="15" y1="190" x2="365" y2="190" stroke="rgba(148, 163, 184, 0.25)" stroke-width="1" />
                            <line x1="66" y1="66" x2="314" y2="314" stroke="rgba(0, 240, 255, 0.2)" stroke-width="1" stroke-dasharray="3 3" />
                            <line x1="314" y1="66" x2="66" y2="314" stroke="rgba(0, 240, 255, 0.2)" stroke-width="1" stroke-dasharray="3 3" />
                            <line x1="102" y1="38" x2="278" y2="342" stroke="rgba(168, 85, 247, 0.2)" stroke-width="1" stroke-dasharray="2 2" />
                            <line x1="278" y1="38" x2="102" y2="342" stroke="rgba(168, 85, 247, 0.2)" stroke-width="1" stroke-dasharray="2 2" />
                            <line x1="38" y1="102" x2="342" y2="278" stroke="rgba(16, 185, 129, 0.2)" stroke-width="1" stroke-dasharray="2 2" />
                            <line x1="38" y1="278" x2="342" y2="102" stroke="rgba(16, 185, 129, 0.2)" stroke-width="1" stroke-dasharray="2 2" />
                            
                            <!-- Sacred Merkabah / Triplicities in Center -->
                            <polygon points="190,125 246,222 134,222" stroke="rgba(148, 163, 184,0.35)" stroke-width="1" fill="none" />
                            <polygon points="190,255 246,158 134,158" stroke="rgba(0,240,255,0.35)" stroke-width="1" fill="none" />
                        </svg>

                        <!-- 12 Interactive Zodiac Wheel Nodes -->
                        <div class="zodiac-wheel-node" id="zodiac-wheel-node-1" style="top: 12%; left: 50%; color: #ef4444; border-color: #ef4444;" onclick="selectZodiac(1)" title="برج الحمل ♈">♈</div>
                        <div class="zodiac-wheel-node" id="zodiac-wheel-node-2" style="top: 17%; left: 69%; color: #10b981; border-color: #10b981;" onclick="selectZodiac(2)" title="برج الثور ♉">♉</div>
                        <div class="zodiac-wheel-node" id="zodiac-wheel-node-3" style="top: 31%; left: 83%; color: #00f0ff; border-color: #00f0ff;" onclick="selectZodiac(3)" title="برج الجوزاء ♊">♊</div>
                        <div class="zodiac-wheel-node" id="zodiac-wheel-node-4" style="top: 50%; left: 88%; color: #38bdf8; border-color: #38bdf8;" onclick="selectZodiac(4)" title="برج السرطان ♋">♋</div>
                        <div class="zodiac-wheel-node" id="zodiac-wheel-node-5" style="top: 69%; left: 83%; color: #f59e0b; border-color: #f59e0b;" onclick="selectZodiac(5)" title="برج الأسد ♌">♌</div>
                        <div class="zodiac-wheel-node" id="zodiac-wheel-node-6" style="top: 83%; left: 69%; color: #84cc16; border-color: #84cc16;" onclick="selectZodiac(6)" title="برج العذراء ♍">♍</div>
                        <div class="zodiac-wheel-node" id="zodiac-wheel-node-7" style="top: 88%; left: 50%; color: #ec4899; border-color: #ec4899;" onclick="selectZodiac(7)" title="برج الميزان ♎">♎</div>
                        <div class="zodiac-wheel-node" id="zodiac-wheel-node-8" style="top: 83%; left: 31%; color: #ef4444; border-color: #ef4444;" onclick="selectZodiac(8)" title="برج العقرب ♏">♏</div>
                        <div class="zodiac-wheel-node" id="zodiac-wheel-node-9" style="top: 69%; left: 17%; color: #8b5cf6; border-color: #8b5cf6;" onclick="selectZodiac(9)" title="برج القوس ♐">♐</div>
                        <div class="zodiac-wheel-node" id="zodiac-wheel-node-10" style="top: 50%; left: 12%; color: #64748b; border-color: #64748b;" onclick="selectZodiac(10)" title="برج الجدي ♑">♑</div>
                        <div class="zodiac-wheel-node" id="zodiac-wheel-node-11" style="top: 31%; left: 17%; color: #06b6d4; border-color: #06b6d4;" onclick="selectZodiac(11)" title="برج الدلو ♒">♒</div>
                        <div class="zodiac-wheel-node" id="zodiac-wheel-node-12" style="top: 17%; left: 31%; color: #6366f1; border-color: #6366f1;" onclick="selectZodiac(12)" title="برج الحوت ♓">♓</div>
                    </div>

                    <div style="margin-top: 15px; font-size: 0.8rem; color: var(--text-muted); text-align: center;">
                        اختر أي برج من القبة الفلكية أو الأزرار لعرض التحليل الموسوعي والإجماع الحضاري الشامل 👆
                    </div>
                </div>

                <!-- Deep Interactive Zodiac Sign Dossier -->
                <div class="chakra-detail-card" id="zodiac-detail-card">
                    <!-- Injected dynamically by JS -->
                </div>
            </div>

            <!-- 12 ZODIAC CARDS GRID & ELEMENT FILTERS -->
            <div style="margin-top: 50px; margin-bottom: 25px; text-align: center;">
                <h3 style="font-size: 1.6rem; color: #fff; margin-bottom: 8px;">مستودع بطاقات البروج التفاعلية والتصنيف العنصري</h3>
                <p style="font-size: 0.9rem; color: var(--text-muted); max-width: 750px; margin: 0 auto;">تصفح البطاقات الفردية لبروج السماء مصنفة حسب الطبائع الكونية الأربع: النارية، الترابية، الهوائية، والمائية.</p>
            </div>

            <div class="zodiac-filter-bar">
                <button class="z-filter-btn active" onclick="filterZodiac('ALL')">جميع البروج (12) 🌐</button>
                <button class="z-filter-btn" onclick="filterZodiac('ناري')">البروج النارية (الحمل، الأسد، القوس) 🔥</button>
                <button class="z-filter-btn" onclick="filterZodiac('ترابي')">البروج الترابية (الثور، العذراء، الجدي) 🌍</button>
                <button class="z-filter-btn" onclick="filterZodiac('هوائي')">البروج الهوائية (الجوزاء، الميزان، الدلو) 💨</button>
                <button class="z-filter-btn" onclick="filterZodiac('مائي')">البروج المائية (السرطان، العقرب، الحوت) 💧</button>
            </div>

            <div class="zodiac-grid" id="zodiac-grid"></div>

            <!-- PANORAMIC COMPARATIVE MATRIX TABLE FOR 12 ZODIAC SIGNS -->
            <div class="panoramic-matrix-wrapper">
                <div class="matrix-table-header">
                    <span class="matrix-tag">المصفوفة الفلكية والتشريحية الكبرى</span>
                    <h3>جدول المضاهاة البانورامية الشاملة لدائرة البروج الاثني عشر والميلوثيسيا</h3>
                    <p>مقارنة أفقية وعمودية دقيقة تلخص نواميس الأبراج السماوية الاثني عشر: الرمز، الطبيعة والعنصر، الحاكم والشرف، العضو الجسدي (الميلوثيسيا الطبية)، الجهاز الحيوي، السبط الرسالي، الحرف التكويني، القطب المقابل (180°)، الفرع الصيني (Di Zhi)، الراشي الفيدي، والسر القرآني الحاكم.</p>
                </div>
                <div class="matrix-responsive-table">
                    <table class="panoramic-spheres-table">
                        <thead>
                            <tr>
                                <th>البرج والرمز</th>
                                <th>العنصر والطبيعة</th>
                                <th>الكوكب الحاكم والشرف</th>
                                <th>الملاك العلوي والخادم الموكل 🕊️</th>
                                <th>منازل القمر التابعة 🌙</th>
                                <th>العضو الجسدي (الميلوثيسيا)</th>
                                <th>الجهاز الحيوي والغدة</th>
                                <th>السبط والرمز الرسالي</th>
                                <th>الحرف التكويني</th>
                                <th>النظير القطبي (180°)</th>
                                <th>الفرع الصيني (Di Zhi)</th>
                                <th>الراشي الفيدي (Rashi)</th>
                                <th>السر القرآني والنقلة في الوعي</th>
                            </tr>
                        </thead>
                        <tbody id="panoramic-zodiac-tbody"></tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- TAB 4: AGES TIMELINE -->
        <section id="tab-timeline" class="tab-section">
            <div class="hero">
                <div class="quran-ayah">«وَتِلْكَ الْأَيَّامُ نُدَاوِلُهَا بَيْنَ النَّاسِ» [آل عمران: 140] — «وَإِنَّ يَوْمًا عِندَ رَبِّكَ كَأَلْفِ سَنَةٍ مِّمَّا تَعُدُّونَ» [الحج: 47] — «يُدَبِّرُ الْأَمْرَ مِنَ السَّمَاءِ إِلَى الْأَرْضِ ثُمَّ يَعْرُجُ إِلَيْهِ فِي يَوْمٍ كَانَ مِقْدَارُهُ أَلْفَ سَنَةٍ» [السجدة: 5]</div>
                <h1>تعاقب العصور الكبرى وترنح الاعتدالين والمدار الرسالي الخاتم (180° Polarity)</h1>
                <p>الدورة الفلكية الكبرى (السنة الأفلاطونية 25,920 سنة)، ترنح محور الأرض (Precession of the Equinoxes)، وحركة نقطة الاعتدال بمقدار درجة كل 72 سنة تقريباً (2,160 سنة لكل عصر فلكي). كيف تنزلت الرسالات الإلهية الكبرى متطابقة مع طاقة البرج الحاكم والبرج المقابل (180°) من طوفان نوح وصحوة إدريس، إلى شريعة موسى وروحانية عيسى، إلى العصر الخاتم ونور محمد ﷺ وثورة المعرفة في عصر الدلو.</p>
            </div>

            <!-- 4 MASTER ANALYTICAL TREATISES -->
            <div class="spheres-compendium">
                <div class="compendium-header">
                    <span class="compendium-badge">الموسوعة التحليلية التأسيسية للباب 05</span>
                    <h2>المباحث الكوزمولوجية الكبرى في ترنح الاعتدالين ودورات الزمان والرسالات</h2>
                    <p>أربعة مباحث عيانية تربط بين فيزياء الفلك، الإحكام القرآني، قانون الاستقطاب القطبي (180°)، والمضاهاة المعرفية الشاملة مع دورات الأكوار والأدوار واليوغات الفيدية.</p>
                </div>

                <div class="compendium-cards-grid">
                    <!-- Treatise 1 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الأول</span>
                            <h3>الناموس الفلكي لحركة ترنح الاعتدالين (Precession) وحساب السنة الكبرى (25,920 سنة)</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p>ترنح محور الأرض (Axial Precession) هو الحركة المخروطية البطيئة لمحور دوران الأرض الناتجة عن عزم جاذبية الشمس والقمر على الانتفاخ الاستوائي. تؤدي هذه الحركة إلى تراجع تدريجي لنقطة الاعتدال الربيعي على خلفية النجوم الثابتة بمعدل درجة قوسية واحدة كل 71.6 سنة تقريباً (~72 سنة). وبما أن كل برج فلكي يشغل 30 درجة من فلك البروج، فإن انتقال الاعتدال عبر برج كامل يستغرق <strong>2,160 سنة شمسية</strong> (وهو ما يُعرف بالعصر الفلكي Astrological Age)، وتستغرق الدورة الكاملة للاثني عشر برجاً <strong>25,920 سنة</strong> وهي «السنة الأفلاطونية العظمى» (The Great Year). وقد وثق علماء الفلك المسلمون كأبي عبد الله البتاني في <em>الزيج الصابئ</em> والبيروني في <em>القانون المسعودي</em> هذه الحركة بحسابات أدق بمراحل من بطليموس، مبرهنين على دقة التقدير الإلهي المحكم: ﴿وَكُلُّ شَيْءٍ عِندَهُ بِمِقْدَارٍ﴾.</p>
                        </div>
                    </div>

                    <!-- Treatise 2 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الثاني</span>
                            <h3>التناغم الرسالي المعجز — تنزل النبوات بمطابقة طاقة العصور ورموزها الكونية</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p>الوحي الإلهي يخاطب وعي الزمان والمكان بلسان معجز: ﴿وَمَا أَرْسَلْنَا مِن رَّسُولٍ إِلَّا بلسَانِ قَوْمِهِ لِيُبَيِّنَ لَهُمْ﴾. وتكشف القراءة الكونية عن تطابق مذهل بين طاقة البرج والرسالة المنزلة: ففي <strong>عصر السرطان المائي</strong> تنزلت رسالة نوح وفُتحت أبواب السماء بماء منهمر وصُنع الفلك المشحون كرحم كوني يحفظ الأنسال. وفي <strong>عصر الجوزاء (عطارد/الكتابة)</strong> خط إدريس بالقلم وظهرت الألواح السومرية وأساطير التوائم. وفي <strong>عصر الثور المادي</strong> شُيدت الأهرامات وعُبد عجل أبيس، فحارب إبراهيم الأصنام البابلية. وفي <strong>عصر الحمل الناري</strong> افتتح بفداء إبراهيم بالكبش، ثم شريعة موسى الكليم التي أحرقت العجل وأحلت نفخ الشوفار (قرن الكبش) وألواح الشريعة الصارمة وصهر الحديد المريخي. وفي <strong>عصر الحوت المائي</strong> تجلت رسالة عيسى المسيح ورمزية السمكة (Ichthys) وإطعام الحواريين من السمك والخبز، متكاملاً مع طهارة مريم العذراء (180°). وفي <strong>عصر الدلو الحالي</strong> انهمر ماء المعرفة وانفجرت ثورة الذكاء الاصطناعي والشبكات.</p>
                        </div>
                    </div>

                    <!-- Treatise 3 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الثالث</span>
                            <h3>قانون الاستقطاب القطبي بزاوية 180° وديناميكية الظل الكوني في مسار التاريخ</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p>يقوم الوجود على ناموس الزوجية والتقابل المتوازن: ﴿وَمِن كُلِّ شَيْءٍ خَلَقْنَا زَوْجَيْنِ لَعَلَّكُمْ تَذَكَّرُونَ﴾. وفي حركيات الفلك، لا يتحرك أي عصر فلكي ببرجه الظاهر فحسب، بل يستمد عمقه وتحديه الداخلي من البرج المقابل له بزاوية 180 درجة على المحور القطبي. فعصر الحمل الناري الصارم استمد توازنه من الميزان المقابل (العدالة وألواح الشريعة والميزان الحق). وعصر الثور المادي استمد هوسه بالخلود والتحنيط وبناء المقابر من العقرب المقابل (عالم الموت والبرزخ والبعث). وعصر السرطان المائي الرحمي قوبل بالجدي الصخري الراسي (استقرار الفلك على جبل الجودي الحجري وبناء أسوار أريحا الحجرية). وعصر الحوت الروحي الذائب قوبل بالعذراء (الولادة من العذراء مريم وتأسيس المشافي ودور التمريض والخدمة الجسدية). وعصر الدلو التقني الشبكي يواجه اليوم تحدي الأسد (الحفاظ على حرارة القلب الإنساني وشعلة الروح الفردية في وجه الآلة الصماء).</p>
                        </div>
                    </div>

                    <!-- Treatise 4 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الرابع</span>
                            <h3>المقارنة الكونية الشاملة: الأكوار والأدوار، اليوغات الفيدية، وأعمار الحضارات</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p>أجمعت حكمة الحضارات الإنسانية على دورية الزمان؛ ففي التراث الإسلامي شرح فلاسفة الإسلام ومحيي الدين ابن عربي في <em>الفتوحات المكية</em> نظرية <strong>«الأكوار والأدوار»</strong> وتصريف الأسماء الإلهية السبعة لحركة الأفلاك وأطوار النبوات والقرون. وفي الحكمة الهندية الفيدية تتطابق حركة الـ 25,920 سنة مع دورة <strong>«اليوغات الأربع»</strong> (Satya الذهبي، Treta الفضي، Dvapara البرونزي، وKali الحديدي)، حيث يشكل الرقم الكوني الفيدي 432 ومضاعفاته النسبة الرياضية الدقيقة لدورات ترنح الاعتدالين ($432 	imes 60 = 25,920$). ويتلاقى ذلك مع أعمار هسيود الأربعة في الميثولوجيا الإغريقية والشموس الخمسة في حضارة المايا، ليؤكد الإجماع الفطري على أن التاريخ البشري ليس صدفة عمياء، بل مسار لولبي مرسوم بأقدار ربانية بالغة الإحكام: ﴿يُدَبِّرُ الْأَمْرَ يُفَصِّلُ الْآيَاتِ لَعَلَّكُم بِلِقَاءِ رَبِّكُمْ تُوقِنُونَ﴾.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- INTERACTIVE PRECESSION WHEEL & MASTER EPOCH DOSSIER -->
            <div class="chakras-container" style="margin-bottom: 40px;">
                <!-- Precession Engine Visualizer -->
                <div class="body-silhouette-wrapper" style="min-height: 590px;">
                    <div style="font-size: 0.95rem; font-weight: 700; color: var(--gold); margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
                        <span>⏳ محرك ترنح الاعتدالين ومحور الأقطاب التفاعلي (Precession Engine 360°)</span>
                    </div>

                    <!-- Quick Selector Pills Bar -->
                    <div class="chakra-pills-bar" id="era-pills-bar"></div>

                    <!-- Interactive Precession Wheel Canvas -->
                    <div class="precession-wheel-canvas" id="precession-wheel-canvas">
                        <svg class="precession-wheel-svg" viewBox="0 0 400 400" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <defs>
                                <radialGradient id="sunGlowEra" cx="200" cy="200" r="110" gradientUnits="userSpaceOnUse">
                                    <stop offset="0%" stop-color="#94a3b8" stop-opacity="0.45" />
                                    <stop offset="60%" stop-color="#f59e0b" stop-opacity="0.15" />
                                    <stop offset="100%" stop-color="#000000" stop-opacity="0" />
                                </radialGradient>
                                <linearGradient id="precessionRingGrad" x1="0" y1="0" x2="400" y2="400" gradientUnits="userSpaceOnUse">
                                    <stop offset="0%" stop-color="#ff3366" stop-opacity="0.7" />
                                    <stop offset="50%" stop-color="#94a3b8" stop-opacity="0.5" />
                                    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.7" />
                                </linearGradient>
                            </defs>
                            
                            <!-- Sun Glow -->
                            <circle cx="200" cy="200" r="110" fill="url(#sunGlowEra)" />
                            
                            <!-- Outer Track (Platonic Year 25,920 Years) -->
                            <circle cx="200" cy="200" r="185" stroke="url(#precessionRingGrad)" stroke-width="2" stroke-dasharray="5 5" />
                            <circle cx="200" cy="200" r="150" stroke="rgba(255, 255, 255, 0.2)" stroke-width="1.5" />
                            <circle cx="200" cy="200" r="115" stroke="rgba(0, 240, 255, 0.3)" stroke-width="1" stroke-dasharray="6 3" />
                            <circle cx="200" cy="200" r="75" stroke="rgba(148, 163, 184, 0.35)" stroke-width="1.5" />
                            
                            <!-- Central Golden Sun -->
                            <circle cx="200" cy="200" r="38" stroke="#fbbf24" stroke-width="2.5" />
                            <circle cx="200" cy="200" r="22" fill="#f59e0b" />
                            <circle cx="200" cy="200" r="10" fill="#fff" />
                            
                            <!-- Radiating Axes (Crossing at 180° Polarities) -->
                            <line x1="200" y1="15" x2="200" y2="385" stroke="rgba(255, 255, 255, 0.12)" stroke-width="1" />
                            <line x1="15" y1="200" x2="385" y2="200" stroke="rgba(255, 255, 255, 0.12)" stroke-width="1" />
                            <line x1="70" y1="70" x2="330" y2="330" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1" stroke-dasharray="3 3" />
                            <line x1="330" y1="70" x2="70" y2="330" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1" stroke-dasharray="3 3" />
                            
                            <!-- Dynamic 180° Laser Line (Piercing the Center) -->
                            <line id="polarity-laser-line" x1="200" y1="200" x2="200" y2="200" stroke="#ff3366" stroke-width="3" stroke-dasharray="6 4" filter="drop-shadow(0 0 10px #ff3366)" />
                        </svg>

                        <!-- Precession Nodes Injected Dynamically by JS -->
                        <div id="precession-nodes-container"></div>
                    </div>

                    <div style="font-size: 0.78rem; color: #94a3b8; text-align: center; margin-top: 5px;">
                        💡 انقر على أي عصر فلكي لإظهار <strong>خط الليزر القطبي (180°)</strong> وملف العصر الشامل.
                    </div>
                </div>

                <!-- Master Epoch Dossier Panel -->
                <div class="chakra-detail-card" id="era-detail-card">
                    <!-- Injected dynamically by JS -->
                </div>
            </div>

            <!-- ERA CATEGORY FILTERS & CARDS GRID -->
            <div style="margin-top: 50px; margin-bottom: 25px; text-align: center;">
                <h3 style="font-size: 1.6rem; color: #fff; margin-bottom: 8px;">مستودع بطاقات العصور التاريخية والرسالات الكبرى</h3>
                <p style="font-size: 0.9rem; color: var(--text-muted); max-width: 750px; margin: 0 auto;">تصفح البطاقات الشاملة للأحقاب الفلكية الممتدة عبر 15 ألف سنة من تاريخ الوعي البشري مصنفة حسب المراحل الحضارية الكبرى.</p>
            </div>

            <!-- CUSP & MATHEMATICAL EXPLANATION CALLOUT -->
            <div style="background: rgba(0, 240, 255, 0.05); border: 1px solid rgba(0, 240, 255, 0.25); border-radius: 16px; padding: 20px 24px; margin-bottom: 30px; display: flex; align-items: flex-start; gap: 16px;">
                <div style="font-size: 2rem; line-height: 1;">📐</div>
                <div>
                    <h4 style="color: var(--cyan); margin: 0 0 6px 0; font-size: 1.1rem;">الحساب الفلكي الدقيق لدورات الـ 2,160 سنة ومفهوم «برزخ العصور» (The Transition Cusp)</h4>
                    <p style="color: #475569; font-size: 0.88rem; line-height: 1.7; margin: 0;">
                        تتحرك نقطة الاعتدال الربيعي تراجعياً بمقدار درجة واحدة كل 72 سنة شمسية. وبما أن كل برج يشغل $30^\circ$ قوسية بالضبط، فإن مدة العصر الفلكي الواحد تساوي رياضياً: <strong>$72 \times 30 = 2,160$ سنة شمسية</strong>، والدورة الكبرى الكاملة للاثني عشر برجاً تساوي: <strong>$2,160 \times 12 = 25,920$ سنة</strong> (السنة الأفلاطونية العظمى).<br>
                        <strong>متى يبدأ العصر الجديد؟</strong> لا يحدث الانتقال فجأة في ليلة واحدة، بل توجد فترة تداخل فلكي تُسمى <strong>«برزخ العصور» (Cusp of Ages)</strong> تمتد لنحو $2^\circ$ إلى $3^\circ$ (حوالي 150 إلى 200 سنة). لذلك، بدأ مخاض عصر الدلو مع الثورة التقنية والمعلوماتية (~1980 - 2020 م)، بينما يقع المركز الرياضي الفلكي لدخول قلب عصر الدلو في عام <strong>2,160 ميلادي</strong>، مكملاً تمام الـ 2,160 سنة لعصر الحوت الذي بدأ مع مطلع ميلاد السيد المسيح (1 م).
                    </p>
                </div>
            </div>

            <div class="era-filter-bar">
                <button class="e-filter-btn active" onclick="filterTimeline('ALL')">الدورة الكبرى كاملة (12 عصراً • 25,920 سنة) 🌐</button>
                <button class="e-filter-btn" onclick="filterTimeline('prehistory')">عصور ما قبل التاريخ والطوفان (العذراء، الأسد، السرطان) 🌊</button>
                <button class="e-filter-btn" onclick="filterTimeline('ancient')">عصور الحضارة والكتابة والشرائع (الجوزاء، الثور، الحمل) 📜</button>
                <button class="e-filter-btn" onclick="filterTimeline('prophetic')">عصر الرسالات والروحانية الكبرى (الحوت) 🕊️</button>
                <button class="e-filter-btn" onclick="filterTimeline('future')">العصور الاستشرافية والمستقبل الكوني (الدلو، الجدي، القوس، العقرب، الميزان) 🚀</button>
            </div>

            <div class="timeline-grid" id="timeline-grid"></div>

            <!-- PANORAMIC COMPARATIVE MATRIX TABLE FOR HISTORICAL ERAS -->
            <div class="panoramic-matrix-wrapper">
                <div class="matrix-table-header">
                    <span class="matrix-tag">المصفوفة التاريخية والكوزمولوجية الكبرى</span>
                    <h3>جدول المضاهاة البانورامية الشاملة لتعاقب العصور والرسالات ومحور الأقطاب</h3>
                    <p>مقارنة أفقية وعمودية دقيقة تلخص نواميس العصور الفلكية التسعة: المدى الزمني، الحاكم الكوكبي، النظير القطبي (180°)، المقام النبوي والرسالي، الصرح المعماري أو الحدث الجيولوجي الفاصل، التحول الديني والوعيوي، مطابقة اليوغا الهندية، والشاهد القرآني الحاكم.</p>
                </div>
                <div class="matrix-responsive-table">
                    <table class="panoramic-spheres-table">
                        <thead>
                            <tr>
                                <th>العصر والرمز ⏳</th>
                                <th>المدى الزمني التقريبي 📅</th>
                                <th>الكوكب الحاكم والعنصر 🪐</th>
                                <th>النظير القطبي (180°) وديناميكية الظل ⚡</th>
                                <th>المقام النبوي والرسالة الإلهية 🕊️</th>
                                <th>الصرح المعماري والرمز الحضاري 🏛️</th>
                                <th>التحول الوعيوي والديني 🧠</th>
                                <th>اليوغا الفيدية والمرحلة الخيميائية 🕉️</th>
                                <th>الشاهد القرآني الحاكم 📖</th>
                            </tr>
                        </thead>
                        <tbody id="panoramic-epochs-tbody"></tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- TAB 5: MASTER MATRIX -->
        <section id="tab-matrix" class="tab-section">
            <div class="hero">
                <div class="quran-ayah">«وَكُلَّ شَيْءٍ أَحْصَيْنَاهُ كِتَابًا» [النبأ: 29] — «إِنَّا كُلَّ شَيْءٍ خَلَقْنَاهُ بِقَدَرٍ» [القمر: 49] — «وَأَحَاطَ بِمَا لَدَيْهِمْ وَأَحْصَىٰ كُلَّ شَيْءٍ عَدَدًا» [الجن: 28]</div>
                <h1>المصفوفة المعمارية الشاملة والميزان الكوني الموحد (The Grand Unified Matrix)</h1>
                <p>ملتقى النواميس ونهاية إحكام البنيان؛ الربط الهولوجرامي والمطابقة الكلية بين مراتب الأفلاك السماوية التسعة (من فلك القمر إلى فلك العرش الأطلس وسدرة المنتهى)، المقامات النبوية، الملائكة العلوية الموكلة، اللطائف والشاكرات الإنسانية، الترددات السولفيجية، المعادن الخيميائية، والأنساق الحضارية العالمية (بابل، مصر، الهند الفيدية، والطاوية) في مصفوفة موحدة كبرى.</p>
            </div>

            <!-- 4 MASTER ANALYTICAL TREATISES -->
            <div class="spheres-compendium">
                <div class="compendium-header">
                    <span class="compendium-badge">الموسوعة التحليلية التأسيسية للباب 06</span>
                    <h2>المباحث الكوزمولوجية الكبرى في علم الميزان والمصفوفة المعمارية الشاملة</h2>
                    <p>أربعة مباحث عيانية تؤصل لقوانين الميزان الرياضي، تطابق الإنسان الكامل مع الكون الأكبر، تقاطع الناموس السباعي مع الفلك الإثناعشري، والإجماع الحضاري العالمي.</p>
                </div>

                <div class="compendium-cards-grid">
                    <!-- Treatise 1 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الأول</span>
                            <h3>علم «الميزان» وإحصاء مراتب الوجود في القرآن الكريم والتراث الحكمي</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p>أقام الحق سبحانه بنيان السماوات والأرض على ناموس الميزان والتقدير الصارم: ﴿وَالسَّمَاءَ رَفَعَهَا وَوَضَعَ الْمِيزَانَ﴾، ﴿وَكُلُّ شَيْءٍ عِندَهُ بِمِقْدَارٍ﴾. وفي التراث العلمي والفلسفي الإسلامي، أسس جابر بن حيان في كتابه <em>الموازين</em> و<em>الخواص الكبير</em> «علم الميزان الطبيعي»، مبرهناً على أن كل مادة وجوهر في الكون مركبة بنسب عددية وهندسية دقيقة تخضع لقاعدة الأوزان الرباعية (1، 3، 5، 8 ومجموعها 17 الحاكم للأكوان). ثم جاء الشيخ الأكبر محيي الدين ابن عربي في <em>عقلة المستوفز</em> و<em>إنشاء الدوائر</em> ليوضح أن هذا الميزان ينعكس في «الحضرات الإلهية الخمس»: حضرة الذات، حضرة الصفات والأسماء، حضرة الأفعال والملكوت، حضرة المثال والبرزخ، وحضرة الحس والشهادة، لتشكل مصفوفة وجودية واحدة لا انفصال فيها.</p>
                        </div>
                    </div>

                    <!-- Treatise 2 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الثاني</span>
                            <h3>الهولوجرام الكوني — سر «الإنسان الكامل والعالم الأكبر» (Microcosm & Macrocosm)</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p>لخص أمير المؤمنين علي بن أبي طالب رضي الله عنه الحقيقة الكوزمولوجية الكبرى في بيته الخالد: <em>«أَتَزْعَمُ أَنَّكَ جُرْمٌ صَغِيرٌ ... وَفِيكَ انْطَوَى العَالَمُ الأَكْبَرُ»</em>. فالإنسان ليس كائناً معزولاً، بل هو «نسخة هولوجرامية مصغرة» من الكون الكلي. فكما يحتوي الكون على سبع سماوات ومحيط العرش الأطلس، يحتوي الجسد الإنساني على سبعة مراكز حيوية (شاكرات ولطائف صوفية) تتصل بالغدد الصماء، ويحتوي على سبعة معادن خيميائية في الدم والعظام، وتجري فيه دورة السوائل متطابقة مع دورات الأفلاك ومنازل القمر. وهذا التناظر هو أصل «الميلوثيسيا الطبية» التي تجعل شفاء الروح والجسد متوقفاً على إعادة موازنته مع نغمات الفلك الكوني.</p>
                        </div>
                    </div>

                    <!-- Treatise 3 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الثالث</span>
                            <h3>تقاطع الناموس السباعي مع الفلك الإثناعشري وسر الأعداد 84 و 19 في القرآن</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p>تنتظم المصفوفة الكونية في تزاوج رياضي معجز بين <strong>الناموس السباعي (7)</strong> و<strong>الناموس الإثناعشري (12)</strong>. السباعي هو الحركة والزمان: السماوات السبع، الأراضين السبع، الأفلاك السبعة، والشاكرات السبع. والإثناعشري هو المكان والاستقرار: البروج الاثنا عشر، شهور السنة، وأسباط بني إسرائيل. وحاصل ضربهما: $7 \times 12 =$ <strong>84</strong>، وهو الرقم الفلكي لدورة أورانوس حول الشمس والسن القانوني لاكتمال نضج الحكمة في حياة الإنسان. ومجموعهما: $7 + 12 =$ <strong>19</strong>، وهو الميزان الرقمي المحكم الوارد في سورة المدثر: ﴿عَلَيْهَا تِسْعَةَ عَشَرَ﴾، ومفتاح حروف البسملة التسعة عشر، ليدل على أن شفرة الكون والمصحف صيغت بمداد هندسي واحد.</p>
                        </div>
                    </div>

                    <!-- Treatise 4 -->
                    <div class="treatise-card">
                        <div class="treatise-card-header">
                            <span class="t-badge">المبحث الرابع</span>
                            <h3>الإجماع الحضاري العالمي — مضاهاة بابل، مصر، الفيدا، الكابالا، والطاوية</h3>
                        </div>
                        <div class="treatise-card-body">
                            <p>تكشف المصفوفة المقارنة عن حقيقة مذهلة: وحدة النبع المعرفي الإنساني الفطري. فعند مقارنة مراتب الأفلاك برؤى الحضارات القديمة نجد تطابقاً تاماً: ففلك الشمس الأوسط يقابله الإله شمش في بابل، وسوريا في الفيدا، ورع في مصر، وميخائيل في النصوص الإبراهيمية، وسيفيرا «تيفيريت» (الجمال والتناغم) في الكابالا. وفلك القمر يقابله الإله سين في بابل، وتشاندرا في الهند، وجبريل في الإسلام. وفي الطاوية الصينية تتنزل طاقة «الداو» عبر سماء تاي تشينغ النقية وعناصر وو شينغ الخمسة بالتوازي مع الأفلاك. هذا الإجماع ليس نقلاً أعمى، بل شهادة حية على أن الحكماء والأنبياء عبر التاريخ كانوا ينظرون إلى نفس الحقيقة الكونية الواحدة: ﴿وَلَقَدْ بَعَثْنَا فِي كُلِّ أُمَّةٍ رَّسُولًا﴾.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- INTERACTIVE MULTI-DIMENSIONAL CONSOLE & CONTROLS -->
            <div class="matrix-console-box">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                    <div>
                        <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700; text-transform: uppercase;">لوحة التحكم المعمارية</span>
                        <h3 style="margin: 4px 0 0 0; color: #fff; font-size: 1.25rem;">مفتش المستويات وأبعاد المصفوفة التفاعلية</h3>
                    </div>
                    <!-- Real-time Live Search Input -->
                    <div class="matrix-search-wrapper">
                        <input type="text" id="matrix-search-input" class="matrix-search-input" placeholder="🔍 ابحث في المصفوفة (نبي، ملاك، معدن، شاكرا، تردد، حضارة)..." oninput="filterMatrixTable()">
                    </div>
                </div>

                <!-- Dimension Mode Switcher -->
                <div class="matrix-mode-bar">
                    <button class="m-mode-btn active" onclick="setMatrixMode('ALL')">🌐 المصفوفة الكونية الشاملة (جميع المستويات الـ 15)</button>
                    <button class="m-mode-btn" onclick="setMatrixMode('prophetic')">🕊️ المسار الروحي والنبوي والملائكي (Prophetic & Angelic)</button>
                    <button class="m-mode-btn" onclick="setMatrixMode('anatomy')">🧘 التشريح الجسدي والشاكرات والترددات (Anatomy & Frequencies)</button>
                    <button class="m-mode-btn" onclick="setMatrixMode('alchemical')">🧪 الخيمياء والمعادن والطبائع الكونية (Alchemical & Elemental)</button>
                    <button class="m-mode-btn" onclick="setMatrixMode('civilizations')">🏛️ المقارنة الحضارية العالمية (Veda, Tao, Babylon, Enoch)</button>
                </div>

                <!-- Quick Rank Selector Pills -->
                <div>
                    <div style="font-size: 0.75rem; color: var(--text-muted); margin-bottom: 6px;">اختر مرتبة كونية لمعاينة ملفها المعماري الكامل:</div>
                    <div class="matrix-ranks-bar" id="matrix-ranks-bar"></div>
                </div>
            </div>

            <!-- MASTER CELESTIAL RANK DOSSIER PANEL -->
            <div class="chakra-detail-card" id="matrix-detail-card" style="margin-bottom: 30px;">
                <!-- Injected dynamically by JS -->
            </div>

            <!-- COMPREHENSIVE 15-COLUMN MASTER MATRIX TABLE -->
            <div class="table-wrapper">
                <table id="master-unified-matrix-table">
                    <thead>
                        <tr>
                            <th>المرتبة والفلك 🪐</th>
                            <th class="col-prophetic">المقام النبوي والرسالي 🕊️</th>
                            <th class="col-prophetic">الملاك العلوي الحاكم 👑</th>
                            <th class="col-prophetic">البطريرك في التراث 📜</th>
                            <th class="col-anatomy">الشاكرا واللطيفة 🧘</th>
                            <th class="col-anatomy">العضو والغدة الحيوية 🩺</th>
                            <th class="col-alchemical">المعدن الخيميائي 🧪</th>
                            <th class="col-alchemical">المبدأ الهرمسي ⚖️</th>
                            <th class="col-anatomy">التردد المقدس والنغمة 🎵</th>
                            <th class="col-civilizations">عوالم الفيدا (Lokas) 🕉️</th>
                            <th class="col-civilizations">الطاوية والصين (Tao) ☯️</th>
                            <th class="col-civilizations">كابالا سفر أخنوخ ✡️</th>
                            <th class="col-civilizations">بابل والرافدين 🏛️</th>
                            <th class="col-alchemical">مستوى الارتقاء الروحي 🚀</th>
                            <th class="col-prophetic">الشاهد القرآني الحاكم 📖</th>
                        </tr>
                    </thead>
                    <tbody id="matrix-tbody"></tbody>
                </table>
            </div>
        </section>

        <!-- TAB 6: MANUSCRIPTS -->
        <section id="tab-manuscripts" class="tab-section">
            <div class="hero">
                <div class="quran-ayah">«وَكُلَّ شَيْءٍ فَصَّلْنَاهُ تَفْصِيلًا»</div>
                <h1>أمهات المخطوطات والكتب المرجعية العالمية الـ 16</h1>
                <p>المتون الإسلامية والتراثية والآثار العالمية (بابل، الهند، مصر، اليونان، ونجع حمادي) التي استخرجنا منها هذه المعادلات والنواميس الكونية.</p>
            </div>
            <div class="books-grid" id="books-grid"></div>
        </section>

        <!-- TAB 7: CRITIQUE AND DISCREPANCIES FOR MURSHID -->
        <section id="tab-critique" class="tab-section">
            <div class="hero">
                <div class="quran-ayah">«وَأَنزَلْنَا إِلَيْكَ الْكِتَابَ بِالْحَقِّ مُصَدِّقًا لِّمَا بَيْنَ يَدَيْهِ مِنَ الْكِتَابِ وَمُهَيْمِنًا عَلَيْهِ» [المائدة: 48]</div>
                <h1 style="color: #ff3366;">سجل ميزان القرآن ورصد تناقضات المخطوطات القديمة</h1>
                <p>القرآن الكريم هو المعيار الحاكم والمطلق. هنا نرصد بدقة أين وافقت المخطوطات القديمة حقائق القرآن، وأين انحرفت أو تناقضت في الترتيب والعصمة لنعرضها على فضيلة المرشد والمحقق.</p>
            </div>
            <div class="critique-grid" id="critique-grid"></div>
        </section>

    </main>

    <script>
        // Master Graph State & Data Injected from Vault
        var currentGraphMode = window.currentGraphMode = 'theory';
        const rawGraphData = {graph_data_json};

        // SPHERES DATA - MASTER ENCYCLOPEDIC DOSSIERS (7 SPHERES & UNIVERSAL THRONE)
        var SPHERES_DATA = window.SPHERES_DATA = [
            {{
                id: 8,
                name: "فلك العرش الأطلس وسدرة المنتهى (Primum Mobile & Divine Throne)",
                color: "#ff3366",
                rank: "ما وراء السماوات السبع (مقام قاب قوسين أو أدنى)",
                prophet: "النبي الخاتم سيدنا محمد صلى الله عليه وسلم",
                patriarch: "الحقيقة المحمدية الجامعة ونور الأنوار ومبدأ الفيض الأول",
                hermetic: "سر الأحدية والكل الأعظم (The All in All) — مجمع الهويات والنواميس الكلية",
                chakra: "الحقل الهالي الكلي وجسم النور الأسمى (Universal Auric Field & Lightbody)",
                metal: "الأثير الكوني الخالص والإكسير الأعظم (Quintessence)",
                note: "التردد الأقدس الجامع (432 Hz / 528 Hz Solfeggio)",
                freqHz: "528 Hz / 432 Hz (وتر التناغم الحيوي والعرش المحيط)",
                gland: "الجهاز العصبي المركزي والشاكرا التاجية الفائقة (Sahasrara Transcendental)",
                orbit: "محيط الأكوان كلها — يدور به الوجود بأكمله دورة كل 24 ساعة وفق حركة الفلك الأطلس التراثية، أو الأفق الكوني اللانهائي المتمدد وفق النسبية العامة والميكانيكا الكمية.",
                angel: "حملة العرش الثمانية («وَيَحْمِلُ عَرْشَ رَبِّكَ فَوْقَهُمْ يَوْمَئِذٍ ثَمَانِيَةٌ») والروح الأمين جبريل المتوقف عند سدرة المنتهى.",
                china_tao: "تايجي (Taiji 太极) والفراغ الأولي (Wuji 无极) — سماء تاي تشينغ (Taiqing 太清) أعلى السماوات الطاوية النقية الثلاث؛ منبع الداو قبل تشكل السماء والأرض وعناصر وو شينغ (Wuxing). [داو دي جينغ: فصل 25].",
                vedic_india: "ساتيا لوكا (Satya-loka) وحضرة بارابراهما (Parabrahman) — أسمى العوالم السبعة في الفيدا، ما وراء المايا (الوهم) ودورات التناسخ الكونية ومصدر كل الفيوضات. [البهاغافاد غيتا 8:20].",
                babylon: "سماء آنو العليا (Heaven of Anu) — أفق الألوهية الأقصى في ميثولوجيا بلاد الرافدين، فوق قبة النجوم الثابتة حيث يستقر الملك الإلهي للكون.",
                greek_phil: "المحرك الأول الذي لا يتحرك (Unmoved Mover) عند أرسطو في الميتافيزيقا (كتاب 12)، وحضرة 'الواحد الأحد' (The One / To Hen) عند أفلوطين في التاسوعات، والفلك الثامن (Ogdoad) في المتون الهرمسية (Poimandres).",
                kabbalah_enoch: "سماء عرابوت (Araboth) في كتاب أخنوخ (2 Enoch) وسفيرة التاج (Keter) والنور اللانهائي (Ein Sof) المحيط بجميع العوالم في سفر الزوهار.",
                hadith: "«ثم ذُهب بي إلى سدرة المنتهى، فإذا نَبقها مثل قِلال هَجَر، وإذا ورقها مثل آذان الفيلة، قال: هذه سدرة المنتهى، فإذا أربعة أنهار: نهران باطنان ونهران ظاهران، فقلت: ما هذان يا جبريل؟ قال: أما الباطنان فنهران في الجنة، وأما الظاهران فالنيل والفرات، ثم رُفع لي البيت المعمور... ثم فُرضت عليّ الصلوات خمسين صلاة... وأوحى الله إليّ ما أوحى» [صحيح البخاري: 3207، وصحيح مسلم: 162].",
                secret: "في الباب 167 والباب 371 من 'الفتوحات المكية' وفص الحكمة الفردية: الحقيقة المحمدية هي أول التعينات الوجودية، والعرش هو أول الأجسام البسيطة المخلوقة المشتمل على جميع الصور الكونية. جاوز رسول الله ﷺ سدرة المنتهى وهي حد العلم البشري والملائكي حيث قال جبريل: 'لو دنوتُ أنملة لاحترقت بالأنوار'، ليدخل في حضرة 'قاب قوسين أو أدنى'؛ دلالة على جمع دائرتي الوجود: دائرة الوجوب ودائرة الإمكان، ليكون رحمة مطلقة للعالمين.",
                titleDesc: "مقام قاب قوسين أو أدنى، خاتم النبوة، والكمال الإنساني الجامع لجميع البروج والفيوضات",
                desc: "الفلك التاسع أو المحيط في الكوزمولوجيا التراثية؛ وهو الغلاف الكوني الأقصى الذي يحوي جميع النجوم الثابتة والبروج والأفلاك السبعة. فوقه العرش المجيد والكرسي الواسع. في هذا المستوى تتلاشى قيود الزمان والمكان (تسطح الزمكان وفق معادلات النسبية عند الأفق الأقصى)، ويتحقق التجلي الإلهي الذاتي المباشر دون واسطة.",
                proof: "ابن عربي — 'فصوص الحكم' (فص حكمة فردية في كلمة محمدية): 'إن الوجود ابتدأ به وختم به، فهو أول في المعنى وآخر في الظهور، وفلكه محيط بكل فلك، وعلمه مستغرق لكل علم، وصورته هي الصورة الإنسانية الكاملة التي خُلق عليها العالم'.",
                quran: "«ثُمَّ دَنَا فَتَدَلَّىٰ * فَكَانَ قَابَ قَوْسَيْنِ أَوْ أَدْنَىٰ * فَأَوْحَىٰ إِلَىٰ عَبْدِهِ مَا أَوْحَىٰ * مَا كَذَبَ الْفُؤَادُ مَا رَأَىٰ» [النجم: 8-11] — «وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالْأَرْضَ» [البقرة: 255]."
            }},
            {{
                id: 7,
                name: "فلك زحل (Saturn ♄) — سماء الثبات والهندسة الأبدية",
                color: "#a855f7",
                rank: "السماء السابعة (بحيال البيت المعمور)",
                prophet: "النبي إبراهيم الخليل عليه السلام (أبو الأنبياء)",
                patriarch: "شيخ الموحدين وباني الكعبة المعظمة (الآدم الأعلى)",
                hermetic: "مبدأ العقلانية الكلية (Mentalism) — 'الكل عقل، الكون فكري'",
                chakra: "التاج (ساهاسرارا / سر السر في قمة الرأس)",
                metal: "الرصاص (Lead - Pb) • أثقل المعادن وسر التحول الخيميائي",
                note: "سي (B) / التردد المداري: 147.85 Hz",
                freqHz: "147.85 Hz (حسابات Hans Cousto للدورة المدارية لزحل: 29.46 سنة)",
                gland: "الغدة الصنوبرية (Pineal Gland) • حبة الخردل الميتافيزيقية ومفرزة الميلاتونين",
                orbit: "المدار: 29.457 سنة أرضية (10,759 يوماً) • البعد عن الشمس: 1.434 مليار كم • الكثافة: 0.687 جم/سم³ (أخف من الماء) • يتميز بالحلقات الهندسية البديعة التي تمثل حدود الرؤية الحسية.",
                angel: "الملاك كفائيل (صاحب سماء التجرد والحدود القصوى)",
                china_tao: "كوكب تشين تشينغ (Zhenxing 镇星 - كوكب التثبيت) • عنصر الأرض (Tu 土) في منظومة وو شينغ • نجم تيان شو (Tianshu) أول نجوم الدب الشمالي (Beidou) • يمثل الرسوخ، ومكعب التوازن المركزي، وتجرد الروح في [I Ching: غرام كُن 坤].",
                vedic_india: "تاباس لوكا (Tapas-loka - سماء الزهد والتجرد الأقصى) • الكوكب: شاني (Shani शनि) ابن سوريا، إله العدالة الكونية الصارمة والكارما والحدود الزمنية المعلم للصبر الأبدي [Surya Siddhanta].",
                babylon: "الطبقة السابعة لزقورة إيتيمينانكي المكسوة باللون الأسود • الإله نينورتا (Ninurta) إله الثبات والحدود القصوى للكون والزراعة العميقة.",
                greek_phil: "كرونوس (Kronos) وفلك زحل • يمثل العقل الخالص (Nous) المتأمل في الأبديات عند برقلس، ودرجة الرصاص (Lead) في سلم ميثرا السباعي، وتجرد الروح من المكر والحدود في [Poimandres].",
                kabbalah_enoch: "سماء ماخون (Makhon) في أخنوخ (2 Enoch) • سفيرة بينة (Binah - الفهم الإلهي والرحم الكوني المعماري وهيكل البناء الأبدي) في شجرة الحياة.",
                hadith: "«ثم صعد بي إلى السماء السابعة فاستفتح جبريل، قيل: من هذا؟ قال: جبريل، قيل: ومن معك؟ قال: محمد، قيل: وقد بُعث إليه؟ قال: نعم، قال: مرحباً به فنعم المجيء جاء، فإذا فيها إبراهيم مُسنِداً ظهره إلى البيت المعمور، وإذا هو يدخله كل يوم سبعون ألف ملك لا يعودون إليه...» [صحيح البخاري: 3207، وصحيح مسلم: 162].",
                secret: "إسناد إبراهيم ظهره إلى البيت المعمور في فلك زحل يحمل سراً عرفانياً عظيماً: إبراهيم رفع قواعد البيت الحرام في الأرض، والبيت المعمور كعبة أهل السماء السابعة بحيال الكعبة، فجازاه الله بأن جعله مستنداً لبيته السماوي. وزحل هو فلك الرسوخ والحدود الثابتة والبناء المعماري الأبدي؛ وإبراهيم هو إمام الحنفية الذي هدم أصنام التعدد وبنى هيكل التوحيد المطلق.",
                titleDesc: "مقام التوحيد المطلق، مكعب الحق (الكعبة)، والصمت الأبدي وهندسة الهياكل",
                desc: "زحل هو الشيخ الحكيم في المنظومة الفلكية، صاحب أبعد مدار مرئي بالعين المجردة في العصور القديمة. يمثل عتبة التحول بين عالم الأجرام المقيدة وعالم الفضاء النجمي المطلق. في الكيمياء الخيميائية هو الرصاص الأسود الذي يجب صهره وتكريره ليصل إلى ذهب الشمس، وفي الروحانية هو مقام التخلية والمجاهدة الكبرى للوصول إلى التجرد المطلق.",
                proof: "ابن عربي — 'الفتوحات المكية' (الباب 167: في معرفة الكيمياء والسماء السابعة): 'فلك زحل محله من السماوات السماء السابعة، ونبيه إبراهيم الخليل عليه السلام، ومنه تفيض قوى الثبات والوقار، والبيت المعمور في هذه السماء يقابل قلب العارف الممتلئ بالتوحيد الذي لا تسكنه الأغيار'.",
                quran: "«وَإِذْ يَرْفَعُ إِبْرَاهِيمُ الْقَوَاعِدَ مِنَ الْبَيْتِ وَإِسْمَاعِيلُ رَبَّنَا تَقَبَّلْ مِنَّا» [البقرة: 127] — «مَّا كَانَ إِبْرَاهِيمُ يَهُودِيًّا وَلَا نَصْرَانِيًّا وَلَٰكِن كَانَ حَنِيفًا مُّسْلِمًا» [آل عمران: 67]."
            }},
            {{
                id: 6,
                name: "فلك المشتري (Jupiter ♃) — سماء العدالة الكونية والتشريع الأعظم",
                color: "#3b82f6",
                rank: "السماء السادسة (فلك السعد الأكبر)",
                prophet: "النبي موسى عليه السلام (كليم الله)",
                patriarch: "صاحب التوراة والألواح والتشريع الكلي والجهاد الرسالي",
                hermetic: "مبدأ التناظر والتماثل (Correspondence) — 'كما في الأعلى كذلك في الأدنى'",
                chakra: "العين الثالثة (آجنا / لطيفة الأخفى بين الحاجبين)",
                metal: "القصدير (Tin - Sn) • معدن التمدد والرنين الفضي الصافي",
                note: "لا (A) / التردد المداري: 183.58 Hz",
                freqHz: "183.58 Hz (حسابات Hans Cousto للدورة المدارية للمشتري: 11.86 سنة)",
                gland: "الغدة النخامية (Pituitary Gland) • سيدة الغدد الصماء والمتحكمة في سائر الإفرازات",
                orbit: "المدار: 11.862 سنة أرضية (4,333 يوماً) • البعد عن الشمس: 778.5 مليون كم • الكتلة: 318 ضعف كتلة الأرض (أضخم كواكب المجموعة) • يملك أقوى مجال مغناطيسي كوكبي بحوالي 20,000 ضعف الأرض.",
                angel: "الملاك سمخائيل (الموكل بسماء الهيبة والوقار والعدل)",
                china_tao: "كوكب سوي شينغ (Suixing 岁星 - كوكب السنين) • عنصر الخشب (Mu 木) في منظومة وو شينغ • يمثل الربيع، والنمو، والرحمة، والتوسع، وحاكم دورة الـ 12 سنة للأبراج الصينية في [Huainanzi].",
                vedic_india: "جانا لوكا (Jana-loka - سماء الخلق المعرفي) • الكوكب: بريهاسباتي (Brihaspati / Guru) معلم الآلهة، ورمز الحكمة التوسعية والدارما والوفرة والعدالة الإلهية في [Rig Veda 4.50].",
                babylon: "الطبقة السادسة لزقورة بابل باللون البرتقالي • الإله مردوخ (Marduk) كبير آلهة بابل، راعي الشرائع والقوانين وقاهر الفوضى.",
                greek_phil: "زيوس (Zeus) وفلك المشتري • رمز العدل الكوني والسيادة الإلهية والفيض الأكبر عند أفلاطون، ودرجة البرونز في سلم ميثرا، والتخلص من الطمع في [Poimandres].",
                kabbalah_enoch: "سماء معون (Maon) في أخنوخ (2 Enoch) • سفيرة حيسيد (Chesed - الرحمة المطلقة والفيض الإلهي الموسع والتشريع).",
                hadith: "«ثم صعد بي إلى السماء السادسة فاستفتح جبريل... فإذا فيها موسى عليه السلام، فقال: مرحباً بالأخ الصالح والنبي الصالح، فلما جاوزته بكى، فقيل له: ما يبكيك؟ قال: أبكي لأن غلاماً بُعث بعدي يدخل الجنة من أمته أكثر ممن يدخلها من أمتي!» [صحيح البخاري: 3207، وصحيح مسلم: 162].",
                secret: "المشتري هو فلك السعد الأكبر والتوسع والرحمة المقرونة بالتشريع الكلي. وموسى كليم الله الذي حمل ثقل الرسالة وألواح الشريعة وجاهد بني إسرائيل ستين سنة. بكاؤه في المعراج لم يكن حسداً بل شفقة وغبطة على فضل أمة محمد ﷺ، وسر مقامه في المشتري أنه هو الذي أشار على النبي ﷺ في طريق العودة بسؤال التخفيف في الصلاة من خمسين إلى خمس، فكان مظهر الرحمة والتيسير الموسع لأمة الإسلام.",
                titleDesc: "مقام البصيرة الكلية، التشريع والعدل، الصعق في الطور والتيسير لأمة محمد",
                desc: "كوكب العظمة والوقار الكوني. في الميثولوجيا القديمة هو جوبيتر/برجيس راعي القوانين والعدالة. وفي العلوم الفلكية هو العملاق الغازي الذي لولاه لدُمرت الأرض بوابل النيازك بفضل كتلته الجاذبة العظيمة، تماماً كما كان موسى درعاً ومرجعاً تشريعياً للأمم.",
                proof: "ابن عربي — 'فصوص الحكم' (فص حكمة علوية في كلمة موسوية): 'إن موسى عليه السلام أوتي علماً بالقوى العلوية والتشريع، ومقامه في السماء السادسة متصل بحكمة المشتري التي تفيض بالنظام والعدل الإلهي وتدبير شؤون الخلائق بالبصيرة التامة'.",
                quran: "«وَكَلَّمَ اللَّهُ مُوسَىٰ تَكْلِيمًا» [النساء: 164] — «وَكَتَبْنَا لَهُ فِي الْأَلْوَاحِ مِن كُلِّ شَيْءٍ مَّوْعِظَةً وَتَفْصِيلًا لِّكُلِّ شَيْءٍ» [الأعراف: 145]."
            }},
            {{
                id: 5,
                name: "فلك المريخ (Mars ♂) — سماء البأس والقوة وتصريف الحدود",
                color: "#ef4444",
                rank: "السماء الخامسة (فلك الشدة المنضبطة)",
                prophet: "النبي هارون عليه السلام (وزير موسى وكاهن الحق)",
                patriarch: "رمز المحبة الكهنوتية وتسكين لهيب الغضب",
                hermetic: "مبدأ السبب والنتيجة (Cause & Effect) — 'لكل فعل رد فعل'",
                chakra: "شاكرا الحنجرة والنطق (فيشودها / لطيفة الخفي)",
                metal: "الحديد (Iron - Fe) • عنصر البأس الشديد والمنافع الكبرى للناس",
                note: "صول (G) / التردد المداري: 144.72 Hz",
                freqHz: "144.72 Hz (حسابات Hans Cousto للدورة المدارية للمريخ: 1.88 سنة / 687 يوماً)",
                gland: "الغدة الدرقية وجارات الدرقية (Thyroid & Parathyroid) • منظم الأيض والطاقة الحركية",
                orbit: "المدار: 686.98 يوماً أرضياً (1.88 سنة) • البعد عن الشمس: 227.9 مليون كم • لونه الأحمر ناجم عن وفرة أكسيد الحديد (Fe2O3) على سطحه • يحوي أضخم بركان كوكبي (أوليمبوس مونس).",
                angel: "الملاك كلكائيل (الموكل بسماء البأس وحماية الثغور الكونية)",
                china_tao: "كوكب ينغ هوو (Yinghuo 荧惑 - الشعلة المتلألئة) • عنصر النار (Huo 火) في منظومة وو شينغ • يمثل البأس، والحرارة، والإشراق، وتصريف القوة الصيفية، وحماية التوازن الكوني في [Shiji لسيما تشيان].",
                vedic_india: "ماهار لوكا (Mahar-loka - سماء الطاقة الإشعاعية) • الكوكب: مانغالا (Mangala / Kartikeya) إله الحرب العادلة والبأس وحاكم معدن الحديد والشجاعة الفولاذية في [Brihat Samhita].",
                babylon: "الطبقة الخامسة لزقورة بابل بالآجر الأحمر • الإله نيرغال (Nergal) إله القوة والحرارة وحامي الثغور الكونية.",
                greek_phil: "آريس (Ares) وفلك المريخ • يمثل القوة الغضبية (Thumos) المنضبطة لنصرة الحق عند أفلاطون، ودرجة الحديد في سلم ميثرا، والتطهر من الجرأة الطائشة في [Poimandres].",
                kabbalah_enoch: "سماء زبول (Zebul) في أخنوخ (2 Enoch) • سفيرة غيفوراه (Gevurah - الشدة والقوة والعدالة الصارمة المنضبطة).",
                hadith: "«ثم صعد بي إلى السماء الخامسة فاستفتح جبريل، قيل: من هذا؟ قال: جبريل، قيل: ومن معك؟ قال: محمد، قيل: وقد بُعث إليه؟ قال: نعم، قال: مرحباً به فنعم المجيء جاء، فإذا فيها هارون عليه السلام، فقال: مرحباً بالأخ الصالح والنبي الصالح» [صحيح البخاري: 3207، وصحيح مسلم: 162].",
                secret: "المريخ هو كوكب النحس الأصغر في التنجيم القديم ومعدنه الحديد ورمزه الحرب والنار. وتسكين نبي الله هارون في هذا الفلك يمثل قمة الحكمة الإلهية: هارون نبي اللين والود والمحبة الذي قال لأخيه: 'يَا ابْنَ أُمَّ لَا تَأْخُذْ بِلِحْيَتِي وَلَا بِرَأْسِي إِنِّي خَشِيتُ أَن تَقُولَ فَرَّقْتَ بَيْنَ بَنِي إِسْرَائِيلَ'. وجود صاحب القلب الرحيم واللسان الفصيح في فلك القوة والبأس هو ميزان إلهي لتعديل حدة المريخ بنور المحبة النبوية.",
                titleDesc: "مقام البأس وصهر الحديد، الشجاعة والكلمة الصارمة، ولين المحبة الكهنوتية",
                desc: "فلك القوة التنفيذية، وكسر أصنام التمرد، وتسخير المادة الصلبة. في القرآن نزل الحديد من السماء: «وَأَنزَلْنَا الْحَدِيدَ فِيهِ بَأْسٌ شَدِيدٌ وَمَنَافِعُ لِلنَّاسِ»، وهو الكوكب المغطى بالحديد حرفياً. هنا تنصهر الشدائد لتولد الإرادة الإنسانية الصادقة في نصرة الحق.",
                proof: "ابن عربي — 'فصوص الحكم' (فص حكمة إمامية في كلمة هارونية): 'إن هارون كان مظهراً للرحمة الإلهية الكلية والخلافة المستقرة، وجُعل مقامه في سماء المريخ ليقهر سطوة الغضب بالنطق الحكيم والسكينة الإيمانية'.",
                quran: "«وَأَنزَلْنَا الْحَدِيدَ فِيهِ بَأْسٌ شَدِيدٌ وَمَنَافِعُ لِلنَّاسِ وَلِيَعْلَمَ اللَّهُ مَن يَنصُرُهُ وَرُسُلَهُ بِالْغَيْبِ» [الحديد: 25] — «وَاجْعَل لِّي وَزِيرًا مِّنْ أَهْلِي * هَارُونَ أَخِي * اشْدُدْ بِهِ أَزْرِي» [طه: 29-31]."
            }},
            {{
                id: 4,
                name: "فلك الشمس (Sol ☉) — شمس الروح وقلب العالم",
                color: "#eab308",
                rank: "السماء الرابعة (المركز التوازني للأفلاك)",
                prophet: "النبي إدريس عليه السلام (هرمس الهرامسة) وسر السيد المسيح عيسى عليه السلام",
                patriarch: "أول من خط بالقلم ورفع إلى المكان العلي (قلب العالم)",
                hermetic: "مبدأ الإيقاع والنبض (Rhythm) — 'كل شيء يتدفق، داخلاً وخارجاً، كنبض القلب'",
                chakra: "مركز القلب والصدر (أناهاتا / السر الروحي)",
                metal: "الذهب الخالص (Gold - Au) • أشرف المعادن وأكثرها نقاءً وخلوداً",
                note: "فا (F) / التردد المشتق: 126.22 Hz",
                freqHz: "126.22 Hz (حسابات Hans Cousto للنطاق اليومي الشمسي والنبض الشمسي المركزي)",
                gland: "الغدة الصعترية (Thymus Gland) • قائدة جهاز المناعة الحيوي والمولدة للخلايا التائية",
                orbit: "القطر: 1.392 مليون كم (109 أضعاف قطر الأرض) • الكتلة: 99.86% من إجمالي كتلة المجموعة الشمسية بأكملها • درجة حرارة المركز: 15 مليون درجة مئوية (اندماج هيدروجيني نووي) • تتوسط الأفلاك الثلاثة السفلية والأفلاك الثلاثة العلوية.",
                angel: "الملاك صلصائيل (الموكل بسماء النور الشمسي والبصيرة العقلية)",
                china_tao: "تاييانغ (Taiyang 太阳 - الينغ الأعظم) • شمس الإمبراطور الأصفر (Huangdi) • قلب السماء ومركز تدفق التشي (Qi)، ورمز الذهب الخالص في الإكسير الداخلي (Neidan) [Huangdi Neijing].",
                vedic_india: "سفار لوكا (Svar-loka - سماء النور الخالص) • الكوكب: سوريا (Surya सूर्य) راكب المركبة ذات الخيول السبعة التي تمثل الأطياف السبعة والأيام، ومفيض البصيرة في [Gayatri Mantra].",
                babylon: "الطبقة الرابعة لزقورة بابل المكسوة بصفائح الذهب • الإله شمش (Shamash) إله الشمس والعدل وكاشف الأسرار والمظالم.",
                greek_phil: "هيليوس وأبولو (Apollo) • قيثارة الأوتار السبعة (رمز الأفلاك السبعة) وشمس الخير الأسمى في تمثيلية الكهف لأفلاطون، ودرجة الذهب في سلم ميثرا، وقلب الوجود في [Poimandres].",
                kabbalah_enoch: "سماء شحاقيم (Shehaqim) في أخنوخ (2 Enoch) • سفيرة تيفئيريت (Tiferet - الجمال والتناغم والقلب النابض لشجرة الحياة).",
                hadith: "«ثم صعد بي إلى السماء الرابعة فاستفتح جبريل، قيل: من هذا؟ قال: جبريل، قيل: ومن معك؟ قال: محمد، قيل: وقد بُعث إليه؟ قال: نعم، قال: مرحباً به فنعم المجيء جاء، فإذا فيها إدريس عليه السلام، فقال: مرحباً بالأخ الصالح والنبي الصالح، وقيل له: هذا إدريس، قال الله تعالى: «وَرَفَعْنَاهُ مَكَانًا عَلِيًّا»» [صحيح البخاري: 3207، وصحيح مسلم: 162].",
                secret: "الشمس هي قلب المنظومة الكونية وقطبها الأعظم، تتوسط الأفلاك الثلاثة السفلية (القمر، عطارد، الزهرة) والأفلاك الثلاثة العلوية (المريخ، المشتري، زحل). ومقام إدريس (الذي تواترت نصوص المحققين أنه هرمس الهرامسة وأخنوخ) في فلك الشمس هو عين قوله تعالى: 'وَرَفَعْنَاهُ مَكَانًا عَلِيًّا'؛ رفعة مكانية بتوسط السماء الرابعة، ورفعة مكانية بتلقي أسرار الكتابة والعلوم الفلكية والحكمة الأولى.",
                titleDesc: "قلب الأفلاك وقطب السماء، الرفعة المكانية والمعنوية، ونور الحكمة الإلهية الأولى",
                desc: "الشمس هي السراج الوهاج مفيض الطاقة والحياة على كل الأحياء في المنظومة الأرضية، كما أن القلب يفيض الدم المؤكسج على سائر الأعضاء. في الفلسفة الإشراقية للسهروردي، الشمس هي أعظم طلسم نوري يعكس نور الأنوار الأقدس، وبها يتجلى سر الذهب الخيميائي الذي لا يبلى ولا يصدأ.",
                proof: "ابن عربي — 'فصوص الحكم' (فص حكمة قدوسية في كلمة إدريسية): 'إن إدريس رُفع إلى فلك الشمس وهو قلب الأفلاك وقطبها، وهو الفلك الرابع، تحته ثلاثة أفلاك وفوقه ثلاثة أفلاك، فهو في موضع القلب من الجسد الإنساني، ومنه تنبثق أنوار الحياة إلى سائر الوجود'.",
                quran: "«وَرَفَعْنَاهُ مَكَانًا عَلِيًّا» [مريم: 57] — «وَجَعَلَ الشَّمْسَ سِرَاجًا» [نوح: 16] — «وَالشَّمْسُ تَجْرِي لِمُسْتَقَرٍّ لَّهَا ۚ ذَٰلِكَ تَقْدِيرُ الْعَزِيزِ الْعَلِيمِ» [يس: 38]."
            }},
            {{
                id: 3,
                name: "فلك الزهرة (Venus ♀) — سماء الجمال الإلهي والخيال المطلق",
                color: "#10b981",
                rank: "السماء الثالثة (فلك السعد الأصغر)",
                prophet: "النبي يوسف الصديق عليه السلام",
                patriarch: "أيقونة الحسن التام وسيد تأويل الأحاديث والرؤى",
                hermetic: "مبدأ القطبية والتناغم (Polarity) — 'لكل شيء قطبان، المتضادات متطابقة في الطبيعة'",
                chakra: "الضفيرة الشمسية (مانيبورا / لطيفة السر في فم المعدة)",
                metal: "النحاس (Copper - Cu) • فائق التوصيل الكهربائي والحراري ورنين التناغم",
                note: "مي (E) / التردد المداري: 221.23 Hz",
                freqHz: "221.23 Hz (حسابات Hans Cousto للدورة المدارية للزهرة: 224.7 يوماً)",
                gland: "البنكرياس والغدد الكظرية (Pancreas & Adrenals) • مفرزات الأنسولين ومنظمات السكر الحيوي",
                orbit: "المدار: 224.7 يوماً أرضياً • البعد عن الشمس: 108.2 مليون كم • يملك حركة دورانية تراجعية عكس عقارب الساعة • يرسم في مداره مع الأرض والشمس نمطاً خماسياً مذهلاً كزهرة الورد (Venus Rose Pentagram) كل 8 سنوات بدقة متناهية.",
                angel: "الملاك صيدقيائيل (الموكل بالتناغم والجمال الوجودي)",
                china_tao: "كوكب تايباي (Taibai 太白 - الأبيض العظيم) • عنصر المعدن (Jin 金) في منظومة وو شينغ • نجمة الصباح (Qiming) • يمثل النقاء الأخلاقي والعدالة البيضاء والتناغم الفني في [Liezi].",
                vedic_india: "بهوفار لوكا (Bhuvar-loka) العليا • الكوكب: شوكرا (Shukra शुक्र) كوكب الجمال والحب النقي ومعلم أسرار الحياة والتسامي بالمشاعر الدنيوية إلى بهاء روحي في [Mahabharata].",
                babylon: "الطبقة الثالثة لزقورة بابل باللون الأزرق المخضر • عشتار (Ishtar / Inanna) ربة الجمال والخصوبة والحب السامي ونجمة الصباح والمساء.",
                greek_phil: "أفروديت السماوية (Aphrodite Urania) عند أفلاطون في مأدبة المحبة (Symposium) • عشق الجمال المجرد، ودرجة النحاس في سلم ميثرا، وتسامي الشهوة في [Poimandres].",
                kabbalah_enoch: "سماء راقيع (Raqia) في أخنوخ (2 Enoch) • سفيرة نيتساح (Netzach - النصر والخلود والجمال الفاعل والتناغم).",
                hadith: "«ثم صعد بي إلى السماء الثالثة فاستفتح جبريل... فإذا فيها يوسف عليه السلام، فإذا هو قد أُعطي شطر الحسن! فرحب بي ودعا لي بخير» [صحيح البخاري: 3207، وصحيح مسلم: 162].",
                secret: "الزهرة هي كوكب الجمال والمحبة والتناغم الفلكي البديع. وإعطاء يوسف 'شطر الحسن' في هذه السماء هو سر شهود الجمال الإلهي في الصور الكونية. يوسف هو سيد عالم الخيال المنفصل والمتقيد بتأويل الرؤى والأحلام؛ لأن الرؤيا هي صور حسية تختزن معاني مجردة، والزهرة هي الفلك الحاكم لتجسيد المعاني اللطيفة في صور بهيجة تسبي العقول دون الوقوع في أسر الشهوة الطينية.",
                titleDesc: "مقام الجمال المطلق، شطر الحسن، تسامي الشهوات، والتناغم الإلهي وتأويل الرؤى",
                desc: "كوكب الصباح والمساء الأشد لمعاناً في سماء الليل بعد القمر. يمثل انتصار العفة الروحية على الشهوة البهيمية كما تجلى في قصة يوسف مع امرأة العزيز: 'وَرَاوَدَتْهُ الَّتِي هُوَ فِي بَيْتِهَا عَن نَّفْسِهِ... قَالَ مَعَاذَ اللَّهِ'. النحاس معدنه الخيميائي لأنه يمتلك أعلى قدرة على التوصيل السريع والانسجام.",
                proof: "ابن عربي — 'فصوص الحكم' (فص حكمة نورية في كلمة يوسفية): 'إن حضرة الخيال هي أوسع الحضرات، وبها يتنزل الحق في صور، ويوسف عليه السلام أُعطي شطر الحسن لأن الجمال نصفان: جمال مطلق وهو للحق، وجمال مظهري وهو للعالم، ويوسف كان مرآة الجمال المظهري في فلك الزهرة'.",
                quran: "«وَكَذَٰلِكَ يَجْتَبِيكَ رَبُّكَ وَيُعَلِّمُكَ مِن تَأْوِيلِ الْأَحَادِيثِ وَيُتِمُّ نِعْمَتَهُ عَلَيْكَ» [يوسف: 6] — «قَالَ رَبِّ السِّجْنُ أَحَبُّ إِلَيَّ مِمَّا يَدْعُونَنِي إِلَيْهِ» [يوسف: 33]."
            }},
            {{
                id: 2,
                name: "فلك عطارد (Mercury ☿) — سماء الفكر والنطق والأقلام والبيان",
                color: "#06b6d4",
                rank: "السماء الثانية (فلك الكاتب ورسول المعرفة)",
                prophet: "النبي يحيى والسيد المسيح عيسى عليهما السلام (ابنا الخالة)",
                patriarch: "اجتماع سر الحياة الدائمة (يحيى) مع سر كلمة الله وروح القدس (عيسى)",
                hermetic: "مبدأ الاهتزاز والتردد (Vibration) — 'لا شيء يستقر، كل شيء يتحرك ويهتز'",
                chakra: "العجز وأسفل البطن (سفاديستانا / لطيفة النفس المطمئنة)",
                metal: "الزئبق (Quicksilver - Hg) • المعدن السائل الفريد وسر التحول الخيميائي",
                note: "ري (D) / التردد المداري: 141.27 Hz",
                freqHz: "141.27 Hz (حسابات Hans Cousto للدورة المدارية لعطارد: 87.97 يوماً)",
                gland: "الغدد التناسلية الإفرازية وخلايا ليديج (Gonads & Interstitial Cells)",
                orbit: "المدار: 87.97 يوماً أرضياً (أسرع كواكب المنظومة دوراناً) • البعد عن الشمس: 57.9 مليون كم • السرعة المدارية: 47.36 كم/ثانية • يتميز بظاهرة رنين مداري دوراني 3:2 (3 دورات محورية لكل دورتين شمسيتين).",
                angel: "الملاك صغائيل (الموكل بسماء الفكر وسرعة الانتقال المعرفي)",
                china_tao: "كوكب تشن شينغ (Chenxing 辰星 - كوكب الساعة والوقت) • عنصر الماء (Shui 水) في منظومة وو شينغ • يمثل السيولة والذكاء والتكيف وسرعة نقل الرسائل والتقويم [Dao De Jing: فصل 8].",
                vedic_india: "بهوفار لوكا (Bhuvar-loka) الدنيا • الكوكب: بودها (Budha बुध) ابن سوما، إله الفكر والفصاحة والمنطق والتمييز الذهني الدقيق (Buddhi) في [Brihat Parashara Hora Shastra].",
                babylon: "الطبقة الثانية لزقورة بابل باللون الأزرق الفاتح • الإله نابو (Nabu) إله الحكمة والكتابة وحامل ألواح القدر في بابل القديمة.",
                greek_phil: "هرمس (Hermes) رسول الآلهة • سيد النطق وسر الأبجدية وفك الرموز، ودرجة سبيكة الفضة والزئبق في سلم ميثرا، وتطهير العقل من المكر والحيل في [Poimandres].",
                kabbalah_enoch: "سماء شمايم (Shamayim) في أخنوخ (2 Enoch) • سفيرة هود (Hod - المجد والفصاحة والبيان الفكري).",
                hadith: "«ثم صعد بي إلى السماء الثانية فاستفتح جبريل، قيل: من هذا؟ قال: جبريل، قيل: ومن معك؟ قال: محمد، قيل: وقد بُعث إليه؟ قال: نعم، قال: مرحباً به فنعم المجيء جاء، فإذا فيها ابنا الخالة: يحيى وعيسى عليهما السلام، فرحبا بي ودعوا لي بخير» [صحيح البخاري: 3207، وصحيح مسلم: 162].",
                secret: "عطارد هو الكاتب وسر القلم والخط والانتقال السريع للأفكار. واجتماع يحيى وعيسى (ابني الخالة) في فلك عطارد يمثل سر اقتران الحياة بالكلمة: يحيى سُمي يحيى لأنه حيي بالإيمان ولم يعص قط («وَحَنَانًا مِّن لَّدُنَّا وَزَكَاةً ۖ وَكَانَ تَقِيًّا»)، وعيسى هو كلمة الله وروح منه («إِنَّمَا الْمَسِيحُ عِيسَى ابْنُ مَرْيَمَ رَسُولُ اللَّهِ وَكَلِمَتُهُ أَلْقَاهَا إِلَىٰ مَرْيَمَ وَرُوحٌ مِّنْهُ»). اقتران الكلمة بالحياة في فلك النطق والفكر هو الشرط الأساسي لبعث الأرواح الميتة.",
                titleDesc: "مقام البيان والذكاء الفكري، اجتماع سر الحياة (يحيى) مع كلمة الله المتجسدة (عيسى)",
                desc: "كوكب الحركة الخاطفة والتواصل الفكري السريع. معدنه الزئبق الذي يجمع بين السيولة والصلابة، والبرودة والحرارة، وهو جوهر العمليات الخيميائية الكبرى. يمنح النفس سرعة الإدراك والقدرة على التمييز المنطقي الحاد بين حقائق الإيمان وشبهات المادة.",
                proof: "ابن عربي — 'الفتوحات المكية' (الباب 167: في السماء الثانية وفلك عطارد): 'فلك عطارد هو محل الفكر والتمييز، وفيه التقى النبي بيحيى وعيسى عليهما السلام، لأن عيسى كلمة ويحيى حياة، والكلمة إذا لم تكن حية بروح القدس كانت جسداً لا روح فيه، فامتزجت الكلمة بالحياة في سماء النطق والفكر'.",
                quran: "«يَا زَكَرِيَّا إِنَّا نُبَشِّرُكَ بِغُلَامٍ اسْمُهُ يَحْيَىٰ لَمْ نَجْعَل لَّهُ مِن قَبْلُ سَمِيًّا» [مريم: 7] — «إِذْ قَالَتِ الْمَلَائِكَةُ يَا مَرْيَمُ إِنَّ اللَّهَ يُبَشِّرُكِ بِكَلِمَةٍ مِّنْهُ اسْمُهُ الْمَسِيحُ عِيسَى ابْنُ مَرْيَمَ» [آل عمران: 45]."
            }},
            {{
                id: 1,
                name: "فلك القمر (Moon ☽) — سماء الدنيا ومستودع الأجساد الطينية",
                color: "#94a3b8",
                rank: "السماء الأولى (سماء الدنيا)",
                prophet: "النبي آدم عليه السلام (أبو البشرية)",
                patriarch: "الخليفة الأول ومستودع الأسماء الإلهية كلها",
                hermetic: "مبدأ النوع والتوالد (Gender) — 'النوع في كل شيء، كل شيء له مبادئه المذكرة والمؤنثة'",
                chakra: "قاعدة العمود الفقري (مولادارا / لطيفة النفس الطينية)",
                metal: "الفضة النقية (Silver - Ag) • مرآة النور الشمسي ورمز النقاء والبرودة",
                note: "دو (C) / التردد المشتق: 210.42 Hz",
                freqHz: "210.42 Hz (حسابات Hans Cousto للشهر القمري الاقتراني Synodic Month: 29.53 يوماً)",
                gland: "الغدد الكظرية وإفرازات الأدرينالين (Adrenal Glands) • آلية البقاء والدفاع الأولى",
                orbit: "المدار: 27.32 يوماً (الشهر النجمي) / 29.53 يوماً (الشهر الاقتراني) • البعد عن الأرض: 384,400 كم • المد والجزر: يولد القمر قوى الجاذبية التفاضلية المتحكمة ببحار الأرض وسوائل الأنسجة • يمر بـ 28 منزلة قمرية تقابل الحروف الهجائية الثمانية والعشرين.",
                angel: "الملاك إسماعيل (صاحب سماء الدنيا والموكل بحفظها برجوم الشياطين)",
                china_tao: "تايين (Taiyin 太阴 - الين الأعظم) • قصر القمر والإلهة تشانغ إي (Chang'e 嫦娥) وإكسير الخلود • كوكب السوائل والمد والجزر ونمو الأجنة والأجساد الطينية في [Huainanzi].",
                vedic_india: "بهور لوكا (Bhur-loka - العالم المادي السفلي) • الكوكب: تشاندرا / سوما (Chandra / Soma) مفيض رحيق الحياة الحاكم للعقل الباطن (Manas) والغرائز والأمومة في [Rig Veda].",
                babylon: "الطبقة الأولى لزقورة بابل المكسوة بصفائح الفضة • الإله سين (Sin / Nanna) إله القمر وسيد الأشهر ومحدد التقويم وسوائل الأرض.",
                greek_phil: "سيليني وأرتميس (Selene) • الفلك الحاكم لعالم تحت الفلك (Sublunary Sphere) وهو عالم الكون والفساد عند أرسطو، ودرجة الفضة في سلم ميثرا، وتطهير طاقة الزيادة والنقصان في [Poimandres].",
                kabbalah_enoch: "سماء طبل (Tebel) والأرض • سفيرة ملكوت (Malkhut - الملكوت وعالم المادة والجسد السفلي وتثبيت الروح في الطين) في قبالاه الزوهار.",
                hadith: "«فلما خَلَصْتُ فإذا فيها آدم، فقال: هذا أبوك آدم فسلّم عليه، فسلّمت عليه، فردّ السلام ثم قال: مرحباً بالابن الصالح والنبي الصالح، وإذا عن يمينه أَسْوِدَةٌ وعن شماله أَسْوِدَة، فإذا نظر قِبَل يمينه ضحك، وإذا نظر قِبَل شماله بكى، فقلت لجبريل: مَن هذا؟ قال: هذا آدم، وهذه الأَسْوِدة نَسَمُ بنيه، فأهل اليمين منهم أهل الجنة، والأسودة التي عن شماله أهل النار، فإذا نظر عن يمينه ضحك، وإذا نظر قِبل شماله بكى» [صحيح البخاري: 3207، وصحيح مسلم: 162].",
                secret: "سماء الدنيا هي فلك القمر الحاكم لعالم التغير والولادة والفناء (عالم الكون والفساد). وآدم هو أصل النشأة الإنسانية الطينية، خُلق بيدي الله وعُلّم الأسماء كلها. لقاؤه في سماء الدنيا هو لقاء الروح بالبدايات الجسدية؛ ورؤية نَسَم بنيه (أرواح ذريته) عن يمينه وشماله يرمز إلى تفرع القدر الإنساني إلى نور وظلمة، وسعادة وشقاء، منذ أول هبوط من الجنة إلى دار الابتلاء.",
                titleDesc: "مقام الهبوط، الغرائز، تثبيت الروح في الطين، وعرض نَسَم بني آدم",
                desc: "القمر هو خادم الأرض وأقرب الأجرام الكونية إليها، يعكس نور الشمس ليضيء حلكة الليل. ترتبط دورته الشهرية بإيقاعات الخصوبة، ومد وجزر البحار، وتدفق الدم وسوائل الأنسجة الحية. معدنه الفضة لكونها تعكس 99% من الضوء الساقط عليها كما يعكس القمر ضياء الشمس.",
                proof: "إخوان الصفا — 'رسائل إخوان الصفا وخلان الوفاء' (الرسالة الفلكية): 'القمر هو آخر الأفلاك وواسطة الفيض بين عالم الأفلاك العلوية وعالم العناصر الأربعة السفلية، به تنعقد النطف في الأرحام وتنمو النباتات وتسري الرطوبات، ومقامه لآدم عليه السلام لأنه مفيض صور الأجساد الإنسانية'.",
                quran: "«وَلَقَدْ زَيَّنَّا السَّمَاءَ الدُّنْيَا بِمَصَابِيحَ وَجَعَلْنَاهَا رُجُومًا لِّلشَّيَاطِينِ» [الملك: 5] — «وَالْقَمَرَ قَدَّرْنَاهُ مَنَازِلَ حَتَّىٰ عَادَ كَالْعُرْجُونِ الْقَدِيمِ» [يس: 39] — «وَعَلَّمَ آدَمَ الْأَسْمَاءَ كُلَّهَا» [البقرة: 31]."
            }}
        ];

        // 12 ZODIAC SIGNS DATA (GLOBAL CIVILIZATIONAL, ANGELIC RULERS, OCCULT SERVANTS & MELOTHESIA)
        var ZODIAC_12_DATA = window.ZODIAC_12_DATA = [
            {{
                id: 1,
                name: "برج الحمل (Aries ♈ — رأس النور والمبادأة النارية)",
                latin: "Aries ♈ (The Ram)",
                glyph: "♈",
                element: "ناري",
                elemClass: "elem-fire",
                colorHex: "#ef4444",
                quality: "منقلب (Cardinal — بدء فصل الربيع والاعتدال)",
                ruler: "المريخ ♂ (موطنه) • شرفه في الشمس ☉ • وباله في الزهرة • هبوطه في زحل",
                angelic_ruler: "الملاك سَمْسَمَائيل (Samsama'il) • رئيس ملائكة سماء المريخ والنار المقدسة",
                terrestrial_servant: "الملك الأحمر (أبو محرز / صاحب يوم الثلاثاء والراية النارية)",
                lunar_mansions: "الشَّرَطَان (0° - 12°51') • البُطَيْن (12°51' - 25°42') • ثلث الثُّرَيَّا الأول",
                sacred_incense: "الصندل الأحمر، اللبان الذكر، القسط الهندي • معدنه: الحديد الخالص (Fe)",
                talisman_invocation: "حرفه الروحاني هو «الهاء» بمرتبة الآحاد النارية؛ يُستجلب به شجاعة القلب ونصرة المظلوم وإبطال الخوف وكسر موانع الأعداء في متون شمس المعارف للبوني وغاية الحكيم للمجريطي.",
                organ: "الرأس، الدماغ، الجمجمة، العينان، والوجه",
                gland_system: "الغدة النخامية والدورة الدموية المخية (Pituitary & Cerebral Cortex)",
                tribe: "سبط يهوذا / جاد (راية المبادأة والشجاعة والريادة النبوية)",
                letter: "الهاء (هـ) / النطاق الأثيري الناري الأول",
                opposing: "الميزان ♎ (180° — ميزان العدالة وترويض الاندفاع)",
                quran: "«وَفَدَيْنَاهُ بِذِبْحٍ عَظِيمٍ» [الصافات: 107] • «وَالشَّمْسَ وَالْقَمَرَ وَالنُّجُومَ مُسَخَّرَاتٍ بِأَمْرِهِ» [الأعراف: 54] • رمزية الكبش الفدائي ورسالة موسى.",
                shift: "وعي المبادأة النورانية والولادة الروحية: التحول من الاندفاع الناري والغضب غير الموجه إلى شجاعة نصرة الحق، كسر قيود التردد والخوف، والريادة في قيادة الأمم نحو التوحيد.",
                proof: "«التفهيم لأوائل صناعة التنجيم» — أبو الريحان البيروني: الحمل هو أول البروج ورأس الفلك وطالع العالم، طبيعته نارية حارة يابسة، يُنسب إليه الرأس من الإنسان وسلطان المريخ في البأس.",
                china_tao: "يقابله في الفروع الأرضية فرع «تشين» (Chen 辰 - التنين)، عنصر الخشب والنار المتصاعدة؛ رمز الانبثاق الربيعي والطاقة الحيوية المندفعة التي تكسر سبات الشتاء.",
                vedic_rashi: "في الفيدا يُعرف بـ «ميشا» (Mesha Rashi) يحكمه مانغالا (Mangala / المريخ)، ومنازله أشفيني وبهاراني؛ رمز طاقة البدايات والشفاء الإلهي الخارق.",
                babylon_egypt: "في بابل القديمة دُعي «أجرّو» (Agrū - الكبش النجمي حارس الاعتدال الربيعي). وفي معبد دندرة بمصر نُقش برأس كبش آمون المتوج بقرص الشمس رمزاً للبعث والتجدد.",
                hermetic_kabbalah: "في متون هرمس وكتاب التكوين (Sefer Yetzirah)، يمثل الحمل الحرف التأسيسي المرتبط بعضو الرأس ومبدأ «الإرادة المباشرة»، وتناظره سفيرة الجبوراه (Gevurah).",
                desc: "برج المبادأة الكونية ونقطة الصفر في الفلك؛ به يبدأ الربيع وتولد دورة الحياة الجديدة. ارتبط تاريخياً بعصر الحمل الرسالي (2000 ق.م - الميلاد) وظهور شريعة موسى ونفخ الشوفار والذبح العظيم لإبراهيم. موكل به علوياً الملاك سمسمائيل وسفلياً الملك الأحمر، ويحكم منازل الشرطان والبطين وبداية الثريا لبث حرارة الحياة في عروق الكون."
            }},
            {{
                id: 2,
                name: "برج الثور (Taurus ♉ — الرسوخ الأرضي وبناء الهياكل)",
                latin: "Taurus ♉ (The Bull)",
                glyph: "♉",
                element: "ترابي",
                elemClass: "elem-earth",
                colorHex: "#10b981",
                quality: "ثابت (Fixed — ترسيخ المادة والإنتاج)",
                ruler: "الزهرة ♀ (موطنها) • شرفه في القمر ☽ • وباله في المريخ • هبوطه في أورانوس",
                angelic_ruler: "الملاك عَنَائيل (Ana'il / عنيائيل) • رئيس ملائكة فلك الزهرة والجمال والفيض",
                terrestrial_servant: "الملك زَوْبَعَة (أبو العجائب / خادم يوم الجمعة والأملاك الترابية الخصبة)",
                lunar_mansions: "ثلثا الثُّرَيَّا الباقيان • الدَّبَرَان (عين الثور الحمراء) • ثلثا الهَقْعَة الأولان",
                sacred_incense: "المستكة البيضاء، العود الرطب، الزعفران، حب الغار • معدنه: النحاس الأحمر المشع (Cu)",
                talisman_invocation: "حرفه هو «الواو» بمرتبة الرسوخ الترابي؛ يُطلب به سعة الأرزاق الزراعية وثبات القواعد ودرء آفات الفقر وجلب البركة في الزروع والأنعام في المخطوطات الهرمسية.",
                organ: "العنق، الحنجرة، الحبال الصوتية، والغدة الدرقية",
                gland_system: "الغدة الدرقية وجارات الدرقية (Thyroid & Metabolic Stability)",
                tribe: "سبط يوسف / إفرايم (بركة الأرض والوفرة الزراعية والإنتاج)",
                letter: "الواو (و) / مجمع الكثافة الترابية المنقاة",
                opposing: "العقرب ♏ (180° — عالم الموت والتحول؛ موازنة التعلق بالفناء)",
                quran: "«وَآيَةٌ لَّهُمُ الْأَرْضُ الْمَيْتَةُ أَحْيَيْنَاهَا وَأَخْرَجْنَا مِنْهَا حَبًّا فَمِنْهُ يَأْكُلُونَ» [يس: 33] • «وَاتَّخَذَ قَوْمُ مُوسَىٰ مِن بَعْدِهِ مِنْ حُلِيِّهِمْ عِجْلًا جَسَدًا لَّهُ خُوَارٌ» [الأعراف: 148].",
                shift: "وعي الرسوخ والاستقرار والشكر: التحرر من الجشع والتعلق الحسي بالذهب والكنوز، تحويل طاقة البناء إلى إعمار الأرض بالعدل، وشهود بهاء الرزاق في نماء الحبوب والخيرات.",
                proof: "«القانون في الطب» — ابن سينا: الحنجرة والعنق مجمع النبض الصوتي والبلعوم؛ يتأثران برطوبة وبرودة التراب الزهري، وموازنة هذا المزاج تكون بالاعتدال في التملك والجهد.",
                china_tao: "يقابله في الصين فرع «سي» (Si 巳 - الأفعى الحكيمة)، عنصر النار الباطنية والأرض الحاضنة؛ رمز الدقة، الصبر المديد، حفظ الموارد، وجمع الثروات بتخطيط محكم.",
                vedic_rashi: "في الفلك الفيدي يُسمى «فريشابها» (Vrishabha Rashi) كوكبه شوكرا (Shukra / الزهرة)، ويشمل منزلة روهيني (Rohini) المفضلة عند القمر، رمز الخصوبة المطلقة والجمال المادي.",
                babylon_egypt: "في بابل هو «غو-آن-نا» (ثور السماء)، قاهر الأراضي الزراعية. وفي مصر القديمة قُدّس كعجل أبيس رمز القوة الإنتاجية وخصوبة فيضان النيل العظيم.",
                hermetic_kabbalah: "يمثل في الهرمسية مبدأ «التجسيد الثابت» (Coagulation). وفي القبالاه يتصل بعضو الرقبة والحنجرة وسفيرة نيتساخ (Netzach - النصر والدوام)، رمزاً للعزيمة الراسخة.",
                desc: "برج التأسيس المادي والوفرة؛ قاد البشرية في عصر الثور (4000 - 2000 ق.م) نحو الزراعة وبناء المعابد الميغاليثية والأهرامات. موكل به الملاك عنائيل والملك زوبعة، ويحكم منزلة الدبران العظيمة (عين الثور) لجلب الخصب والثبات في المادة وتشييد صروح الحضارة الراسخة."
            }},
            {{
                id: 3,
                name: "برج الجوزاء (Gemini ♊ — سماء الفكر والتوأمين والبيان)",
                latin: "Gemini ♊ (The Twins)",
                glyph: "♊",
                element: "هوائي",
                elemClass: "elem-air",
                colorHex: "#00f0ff",
                quality: "متقلب (Mutable — التكيف، الاتصال، والتنقل)",
                ruler: "عطارد ☿ (موطنه وشرفه) • وباله في المشتري • هبوطه في نبتون",
                angelic_ruler: "الملاك مِيكَائيل (Mika'il / ميكائيائيل) • رئيس ملائكة فلك عطارد والبيان والعقل",
                terrestrial_servant: "الملك بَرْقَان (أبو العجائب ذو الوجهين / خادم يوم الأربعاء وسر اللغات)",
                lunar_mansions: "ثلث الهَقْعَة الباقي • الهَنْعَة • جميع منزلة الذِّرَاع النجمية الصافية",
                sacred_incense: "المستكة الرائقة، اللبان الحصى، لسان الحمل، بذور الكرفس • معدنه: الزئبق الممروج (Hg)",
                talisman_invocation: "حرفه الروحاني هو «الزاي»؛ سر الربط الشبكي وفصل الخطاب والذكاء الحارق؛ يُستعمل في فك الطلاسم ونيل البلاغة وعقد ألسنة الخصوم في مجالس المناظرة في كتب الحكمة.",
                organ: "الكتفان، الذراعان، اليدان، الرئتان، والجهاز العصبي المحيطي",
                gland_system: "الجهاز العصبي والجهاز التنفسي وتفرعات الشعب الهوائية",
                tribe: "سبط زبولون / بنيامين (ركوب البحر، التجارة، وسرعة الذكاء)",
                letter: "الزاي (ز) / خط الاتصال الشبكي والازدواج الكوني",
                opposing: "القوس ♐ (180° — الحكمة الشاملة؛ الارتقاء من التشتت إلى البصيرة الكلية)",
                quran: "«عَلَّمَ الْإِنسَانَ مَا لَمْ يَعْلَمْ» [العلق: 5] • «خَلَقَ الْإِنسَانَ * عَلَّمَهُ الْبَيَانَ» [الرحمن: 3-4] • «وَقَالَ رَجُلٌ مُّؤْمِنٌ مِّنْ آلِ فِرْعَوْنَ يَكْتُمُ إِيمَانَهُ» [غافر: 28].",
                shift: "وعي البيان والتكامل الثنائي: تجاوز ثنائية الشك والجدل والوسواس إلى نور العقل الرابط، استخدام القلم والكلمة لنشر النور، وتحقيق الانسجام بين العقل الظاهر والباطن.",
                proof: "«رسائل إخوان الصفا»: الجوزاء برج هوائي مذكر ذو جسدين، يُنسب إليه المنطق والكتابة والأذرع والحواس الناقلة؛ وهو جسر العقل بين المحسوس والمعقول.",
                china_tao: "يقابله في الصين فرع «وو» (Wu 午 - الحصان الناري)، رمز سرعة الحركة، التناقل التجاري، والاتصال النشط، والقدرة الفائقة على التكيف مع المتغيرات المعرفية.",
                vedic_rashi: "في الفيدا يُعرف بـ «ميثونا» (Mithuna Rashi) كوكبه بودها (Budha / عطارد)، وأبرز منازله مرغاشيرا وبونارفاسو؛ رمز تجدد الفكر والفضول المعرفي الشامل.",
                babylon_egypt: "في بابل هو «ماش-تاب-با» (التوأمان العظيمان حارسا بوابات السماء). وفي مصر يمثل توأمي الأفق شو وتفنوت (الهواء المنعش والرطوبة الحيوية).",
                hermetic_kabbalah: "يمثل المبدأ الهرمسي «القطبية والاهتزاز» (Polarity & Vibration). وفي سفر يتسيراه يتصل بحاسة الحركة واليدين الكاتبتين وسفيرة هود (Hod - المجد والذكاء البياني).",
                desc: "برج البيان والكتابة ونشأة التدوين؛ حكم عصر الجوزاء (6000 - 4000 ق.م) حيث وُلدت الأبجديات الأولى. موكل به الملاك ميكائيل والملك برقان، ويحكم منازل الهقعة والهنعة والذراع لبث سيولة الفكر وربط الكلمات بالمعاني وتنسيق تدفق الإشارات العصبية في جسد الإنسان."
            }},
            {{
                id: 4,
                name: "برج السرطان (Cancer ♋ — الرحم المائي وحفظ البذور وطوفان نوح)",
                latin: "Cancer ♋ (The Crab)",
                glyph: "♋",
                element: "مائي",
                elemClass: "elem-water",
                colorHex: "#38bdf8",
                quality: "منقلب (Cardinal — الانقلاب الصيفي وحرارة النماء)",
                ruler: "القمر ☽ (موطنه ومستقره) • شرفه في المشتري ♃ • وباله في زحل • هبوطه في المريخ",
                angelic_ruler: "الملاك جَبْرَائيل (Jabra'il) • الروح الأمين ورئيس ملائكة فلك القمر الحاضن للأجنة",
                terrestrial_servant: "الملك الأبْيَض (أبو الحارث / خادم يوم الإثنين ومياه البحار والأرحام العذبة)",
                lunar_mansions: "النَّثْرَة (مجمع مياه السماء) • الطَّرْف (عينا الأسد) • ثلث الجَبْهَة الأول",
                sacred_incense: "الكافور الأبيض الصافي، الصندل الأبيض، دهن الورد، الميعة السائلة • معدنه: الفضة النقية (Ag)",
                talisman_invocation: "حرفه هو «الحاء»؛ سر الحياة المائية وحفظ الأجنة والأسرار الباطنية؛ تُتلى به دعوات النجاة من الغرق وحفظ الأهل والذرية في كتب الأوفاق القديمة.",
                organ: "الصدر، الثديان، المعدة، والرحم والأغشية المصلية الحامية",
                gland_system: "المعدة والغدد اللبنية والجهاز الهضمي العاطفي (Enteric Nervous System)",
                tribe: "سبط يساكر / رأوبين (حمل الأعباء، الصبر الأسري، وحفظ الأنساب)",
                letter: "الحاء (ح) / حوض الرحمة والماء الحي المستفيض",
                opposing: "الجدي ♑ (180° — البناء الخارجي الصارم؛ موازنة العاطفة بالحزم)",
                quran: "«وَاصْنَعِ الْفُلْكَ بِأَعْيُنِنَا وَوَحْيِنَا» • «حَتَّىٰ إِذَا جَاءَ أَمْرُنَا وَفَارَ التَّنُّورُ قُلْنَا احْمِلْ فِيهَا مِن كُلٍّ زَوْجَيْنِ اثْنَيْنِ» [هود: 37-40] • سر الرحم الكوني الحافظ لبذور الحياة.",
                shift: "وعي الحفظ والأمان الفطري: التسامي فوق تقلبات المزاج العاطفي والخوف من الفقد، تشييد فلك النجاة الداخلي لحفظ الفطرة السليمة، وإطعام الأرواح برحمة الأمومة الكونية.",
                proof: "«المدخل الكبير إلى علم أحكام النجوم» — أبو معشر البلخي: السرطان برج مائي منقلب، بيت القمر وشرف المشتري، يدل على الأرحام والمياه والأغذية وسائر ما فيه احتضان للحياة.",
                china_tao: "يقابله في الصين فرع «وي» (Wei 未 - الخروف الترابي)، عنصر الأرض المخصبة بالماء والنماء؛ رمز الاحتضان العائلي، الحنو، والسكينة والحفظ المستدام.",
                vedic_rashi: "في الفيدا هو «كاركا» (Karka Rashi) كوكبه شاندرا (Chandra / القمر)، ومنازله بوشيا وأشليشا؛ وبوشيا تُعد أقدس المنازل الهندية لغذاء الروح وبركتها.",
                babylon_egypt: "في بابل هو «الولارّو» (Alluttu - السرطان المائي الحارس للأعماق). وفي مصر القديمة نُقش كالجعران المقدس (Khepri) رمز البعث والولادة من باطن الطين.",
                hermetic_kabbalah: "يمثل مبدأ «التوليد والرحم الكوني» (Generation & Rhythm). وفي القبالاه يتصل بعضو المعدة والامتصاص وسفيرة بينة (Binah - الفهم الأمومي الحاضن للأشكال).",
                desc: "برج الرحم المائي وسفينة نوح؛ ارتبط بعصر السرطان (8000 - 6000 ق.م) وحفظ بذور الحياة في فلك النجاة إبان الطوفان. موكل به الروح الأمين جبرائيل والملك الأبيض، ويحكم منزلة النثرة لحفظ الأجنة وتدفق اللبن والرأفة في قلوب الأمهات ورعاية الضعفاء."
            }},
            {{
                id: 5,
                name: "برج الأسد (Leo ♌ — سراج الشمس ومركزية القلب والسيادة)",
                latin: "Leo ♌ (The Lion)",
                glyph: "♌",
                element: "ناري",
                elemClass: "elem-fire",
                colorHex: "#f59e0b",
                quality: "ثابت (Fixed — ثبات الإشعاع والشعلة المركزية)",
                ruler: "الشمس ☉ (موطنها وسلطانها الصرف) • وباله في زحل وأورانوس • شرفه في نيبتون",
                angelic_ruler: "الملاك رُوقْيَائيل (Ruqya'il) • رئيس ملائكة فلك الشمس وسراج الأنوار وسلطان العرش",
                terrestrial_servant: "الملك المُذَهَّب (أبو عبد الله المذهب / خادم يوم الأحد والراية الذهبية)",
                lunar_mansions: "ثلثا الجَبْهَة الباقيان • الزُّبْرَة (خراتان الأسد) • ثلثا الصَّرْفَة الأولان",
                sacred_incense: "العود الكمباري الملكي، المسك الغزال، الصندل الأحمر، الزعفران الأصفهاني • معدنه: الذهب الإبريز (Au)",
                talisman_invocation: "حرفه هو «الطاء»؛ سر القوة المركزية وهيبة الملوك وقهر الجبابرة؛ يُستنزل به القبول التام وعقد ألوية الهيبة وإشراق القلب بنور اليقين في متون شمس المعارف.",
                organ: "القلب، الشريان الأورطي، العمود الفقري، والظهر",
                gland_system: "عضلة القلب والخلايا العصبية القلبية (Cardiac Nervous System)",
                tribe: "سبط يهوذا الملكي («أسد يهوذا» — سلالة داود وسليمان والملك النبوي)",
                letter: "الطاء (ط) / شعلة النور الأحدي المنبثقة من المركز",
                opposing: "الدلو ♒ (180° — الإنسانية الكلية؛ موازنة السيادة الفردية بخدمة المجموع)",
                quran: "«وَجَعَلْنَا سِرَاجًا وَهَّاجًا» [النبأ: 13] • «وَشَدَدْنَا مُلْكَهُ وَآتَيْنَاهُ الْحِكْمَةَ وَفَصْلَ الْخِطَابِ» [ص: 20] • «فَفَرَرْتُ مِنكُمْ لَمَّا خِفْتُكُمْ فَوَهَبَ لِي رَبِّي حُكْمًا» [الشعراء: 21].",
                shift: "وعي السيادة الحقة وتطهير القلب: التحول من كبرياء الأنا وحب الظهور إلى مقام «العبد الرباني»؛ أن يكون القلب شمساً تفيض الدفء والعدل والحماية على الضعفاء دون انتظار مقابل.",
                proof: "«مفتاح السعادة ومصباح السيادة» — طاشكبري زاده: الأسد هو بيت الشمس وسلطان الأكوان؛ والقلب من الجسد بمنزلة الشمس من السماء، به قوام الحياة وإشراق الروح.",
                china_tao: "يقابله في الصين فرع «شين» (Shen 申 - القرد الحكيم)، رمز البراعة، القوة الحيوية، واكتمال نضج ثمار الأرض تحت حرارة الصيف الشمسي الباهر.",
                vedic_rashi: "في الفيدا يُعرف بـ «سيمها» (Simha Rashi) يحكمه سوريا (Surya / الشمس الإلهية)، ومنازله ماغا وبورفا فالغوني؛ وماغا ترمز لحضرة الأجداد والعرش والسيادة.",
                babylon_egypt: "في بابل هو «أورو-غولا» (Urgulû - الأسد العظيم قاهر الظلمات). وفي مصر القديمة هو أبو الهول وهيكل سخمت، نُحت شاخصاً لبرجه في فجر التاريخ (10,500 ق.م).",
                hermetic_kabbalah: "يمثل مبدأ «المركزية والسبب والنتيجة» (Cause and Effect). وفي القبالاه يتصل بالقلب وسفيرة تيفئيريت (Tiferet - بهاء الجمال وشمس المركز في شجرة الحياة).",
                desc: "برج القلب النابض وسلطان الذهب؛ ارتبط بعصر الأسد الذهبي (10,500 - 8000 ق.م) ونحت تمثال أبو الهول بالجيزة متطلعاً لنجم قلب الأسد (Regulus). موكل به الملاك روقيائيل والملك المذهب، ويحكم منازل الجبهة والزبرة لبث حرارة الروح والسيادة العادلة في قلوب قادة الأمم."
            }},
            {{
                id: 6,
                name: "برج العذراء (Virgo ♍ — سنبلة القمح والولادة البتولية والخدمة)",
                latin: "Virgo ♍ (The Virgin)",
                glyph: "♍",
                element: "ترابي",
                elemClass: "elem-earth",
                colorHex: "#84cc16",
                quality: "متقلب (Mutable — التمحيص، التصفية، والتنقية)",
                ruler: "عطارد ☿ (موطنه وشرفه) • وباله وهبوطه في الزهرة والمشتري",
                angelic_ruler: "الملاك إِسْرَافِيل / مِيكَائيل • الموكل بالنفخ الشافي وتدبير الأرزاق الطاهرة",
                terrestrial_servant: "الملك بَرْقَان الترابي (خادم زوابع التراب وتصفية الحبوب والغلال من الشوائب)",
                lunar_mansions: "ثلث الصَّرْفَة الباقي • العَوَّاء • جميع منزلة السِّمَاك الأَعْزَل (سنبلة القمح)",
                sacred_incense: "الصندل الأصفر، القسط الحلو، الكهرمان، حب الصنوبر • معدنه: الزئبق المصفى والبلاتين",
                talisman_invocation: "حرفه الروحاني هو «الياء»؛ سر التمحيص الشافي والبرء من الأسقام الباطنية؛ تُستنزل به أسرار الأعشاب الطبية وشفاء أسقام الأمعاء والبطن في كتاب كشف الأسرار المخفية.",
                organ: "البطن، الأمعاء الدقيقة والغليظة، الطحال، والجهاز الهضمي الإفرازي",
                gland_system: "جزر لانغرهانس في البنكرياس والميكروبيوم المعوي (Gut Microbiome)",
                tribe: "سبط أشير / نفتالي (أرض الزيت والخيرات وخبز الملوك والخدمة)",
                letter: "الياء (ي) / التمحيص والتفصيل والفرز الدقيق للأرزاق",
                opposing: "الحوت ♓ (180° — المحيط والروحانية الصرفة؛ تكامل سنبلة الخبز مع سمكة المحبة)",
                quran: "«فَانظُرْ إِلَىٰ طَعَامِكَ وَشَرَابِكَ لَمْ يَتَسَنَّهْ» [البقرة: 259] • «وَمَرْيَمَ ابْنَتَ عِمْرَانَ الَّتِي أَحْصَنَتْ فَرْجَهَا فَنَفَخْنَا فِيهِ مِن رُّوحِنَا» [التحريم: 12] • «فَتَقَبَّلَهَا رَبُّهَا بِقَبُولٍ حَسَنٍ».",
                shift: "وعي النقاء والخدمة الصادقة والتمييز: الترفع عن وسواس الكمالية والانتقاد الجارح، استشعار قدسية العمل اليومي، وإعداد الإناء الداخلي بالبتولية لولادة روح القدس في النفس.",
                proof: "«تذكرة أولي الألباب» — داود الأنطاكي: العذراء برج ترابي يحكم الأمعاء والتنقية، ونجمه الأعظم «السِّماك الأعزل» (Spica) سنبلة القمح، رمز التغذية الشافية وطهارة الجسد.",
                china_tao: "يقابله في الصين فرع «يو» (You 酉 - الديك الدقيق)، رمز الاستيقاظ الباكر، الفرز والانضباط الصارم، جني المحاصيل بدقة، وحفظ نقاء الغلال من التلف.",
                vedic_rashi: "في الفيدا يُعرف بـ «كانيا» (Kanya Rashi) يحكمه بودها (عطارد)، ومنازله أوتارا فالغوني وهاستا وشيترا؛ وهاستا تعني «اليد الحرفية الماهرة» رمز الخدمة والعلاج.",
                babylon_egypt: "في بابل هو «أبسين» (Absin - السنبلة النجمية للإلهة شالا حامية الزروع). وفي مصر القديمة نُقش كإيزيس حاملة سنبلة القمح لتطعم الجياع على ضفاف النيل.",
                hermetic_kabbalah: "يمثل مبدأ «التحليل والفرز» (Analysis & Purity). وفي القبالاه يتصل بالأمعاء وسفيرة ييسود في جانب طهارة النسل، مرمزاً للأرض العذراء المهيأة للبذرة القدسية.",
                desc: "برج الطهارة وسنبلة القمح والولادة العذرية؛ يرتبط بسر ولادة المسيح في «بيت لحم» (بيت الخبز / Spica سنبلة العذراء). موكل به الملاك إسرافيل وأعوان التراب الأصفياء، ويحكم منزلة السماك الأعزل لتطهير الأغذية وعلاج أسقام الهضم وتنشئة النفوس على الخدمة المتواضعة النقية."
            }},
            {{
                id: 7,
                name: "برج الميزان (Libra ♎ — كفتا القسطاس ونواميس الشريعة والاعتدال)",
                latin: "Libra ♎ (The Scales)",
                glyph: "♎",
                element: "هوائي",
                elemClass: "elem-air",
                colorHex: "#ec4899",
                quality: "منقلب (Cardinal — الاعتدال الخريفي وتساوي الليل والنهار)",
                ruler: "الزهرة ♀ (موطنها) • شرفه في زحل ♄ • وباله في المريخ • هبوطه في الشمس",
                angelic_ruler: "الملاك عَنَائيل (Ana'il) • حارس ميزان العدالة الكونية والتناغم التناسبي",
                terrestrial_servant: "الملك زَوْبَعَة الهوائي (خادم نسمات الاعتدال وفصل القضاء بالحق)",
                lunar_mansions: "الغَفْر • الزُّبَانَى (كفتا الميزان الشمالية والجنوبية) • ثلث الإكليل الأول",
                sacred_incense: "اللبان الجاوي المعطر، الميعة اليابسة، الصندل الأبيض، دهن الياسمين • معدنه: النحاس الأصفر المصفى",
                talisman_invocation: "حرفه هو «الكاف»؛ سر الاعتدال والمحبة الشرعية وحل النزاعات بالعدل المطلق؛ يُنقش لإصلاح ذات البين وإبطال الظلم وإقامة القسطاس المستقيم في مصنفات البوني.",
                organ: "الكليتان، الحالبان، أسفل الظهر، والتوازن الأسموزي للسوائل",
                gland_system: "الغدتان الكظريتان والتوازن الأيوني والكهرلي (Electrolyte Balance)",
                tribe: "سبط لاوي / دان (سدنة القضاء والكهانة والميزان والعدل الشرعي)",
                letter: "الكاف (ك) / كفتا العدل وكلمة التكوين التناسبي",
                opposing: "الحمل ♈ (180° — قوة الفرد؛ تهذيب القوة بالعدل، وجعل سيف المريخ خادماً للحق)",
                quran: "«وَالسَّمَاءَ رَفَعَهَا وَوَضَعَ الْمِيزَانَ * أَلَّا تَطْغَوْا فِي الْمِيزَانِ * وَأَقِيمُوا الْوَزْنَ بِالْقِسْطِ وَلَا تُخْسِرُوا الْمِيزَانَ» [الرحمن: 7-9] • «لَقَدْ أَرْسَلْنَا رُسُلَنَا بِالْبَيِّنَاتِ وَأَنزَلْنَا مَعَهُمُ الْكِتَابَ وَالْمِيزَانَ».",
                shift: "وعي القسط والشهود التناسبي: الترفع عن التردد والمواربة، إقامة ميزان العدل حتى على أقرب الأقربين، ورؤية النسبة الذهبية والتناغم الإلهي المودع في كل ذرة في الوجود.",
                proof: "«فصوص الحكم» — ابن عربي: الميزان هو صورة العدل الإلهي في العالم، به تثبت السماوات والأرض، وهو الحد الفاصل بين الاعتدال والجور، ومقامه زحل في الشرف لثبات الحق.",
                china_tao: "يقابله في الصين فرع «شو» (Xu 戌 - الكلب الوفي)، رمز حراسة النواميس، الوفاء بالعهود، الدفاع عن العدالة، واليقظة لحماية الحرمات من الجور والانحراف.",
                vedic_rashi: "في الفيدا يُعرف بـ «تولا» (Tula Rashi) كوكبه شوكرا (الزهرة)، ومنازله شيترا وسواتي وفيشاكا؛ وسواتي ترمز لحرية النسيم وتوازن الحركة بين الأرض والسماء.",
                babylon_egypt: "في بابل هو «زيبانيتو» (Zibanītu - كفتا الميزان المقسط للإله شمش). وفي مصر القديمة يمثل ميزان ماعت (Ma'at) الذي يُوزن عليه قلب المتوفى مقابل ريشة الحق.",
                hermetic_kabbalah: "يمثل المبدأ الهرمسي «التوازن القطبي» (Rhythm & Equilibrium). وفي القبالاه يتصل بالكليتين وسفيرة تيفئيريت المقسطة بين الرحمة والشدة لإقامة التوازن الكوني.",
                desc: "برج القسطاس والعدل المطلق؛ به يتساوى الليل والنهار في الاعتدال الخريفي، ويرمز لنزول الشرائع الكبرى وألواح الوصايا لإقامة التوازن بين غرائز الأرض ونور السماء. موكل به علوياً الملاك عنائيل وسفلياً الملك زوبعة، ويحكم منزلة الزبانى لحفظ توازن الكليتين وسوائل البدن وإقامة العدل بين الناس."
            }},
            {{
                id: 8,
                name: "برج العقرب (Scorpio ♏ — أسرار التحول الخيميائي والموت والبعث)",
                latin: "Scorpio ♏ (The Scorpion)",
                glyph: "♏",
                element: "مائي",
                elemClass: "elem-water",
                colorHex: "#991b1b",
                quality: "ثابت (Fixed — ثبات الغوص في الأعماق والبرزخ)",
                ruler: "المريخ ♂ وبلوتو ♇ • شرفه في أورانوس • وباله في الزهرة • هبوطه في القمر",
                angelic_ruler: "الملاك عَزْرَائيل / سَمْسَمَائيل الناري • قابض الأرواح ومفتاح بوابات البرزخ والتحول",
                terrestrial_servant: "الملك الأحْمَر المائي (خادم النار الباطنية الغائرة والتحول الخيميائي)",
                lunar_mansions: "ثلثا الإكْلِيل الباقيان • القَلْب (قلب العقرب الأحمر Antares) • ثلثا الشَّوْلَة",
                sacred_incense: "المُرّ المكي، الصَّبِر السقطري، الكبريت الأحمر، الحلتيت المصفى، الصمغ العربي • معدنه: الحديد المغناطيسي",
                talisman_invocation: "حرفه هو «اللام»؛ سر البعث من بعد الموت والاطلاع على الأسرار البرزخية وإبطال الأسحار الخبيثة وتحويل طاقة السموم القاتلة إلى ترياق شافٍ في كتب الرازي والمجريطي.",
                organ: "الأعضاء التناسلية، جهاز الإخراج، البروستاتا، والتجدد الخلوي",
                gland_system: "الغدد التناسلية ومنظومة التطهير الخلوي والموت المبرمج (Apoptosis)",
                tribe: "سبط دان / شمعون (الحكمة الباطنية، الثبات في المحن، وخوض الأهوال)",
                letter: "اللام (ل) / اللطائف البرزخية وسر التحول الباطني",
                opposing: "الثور ♉ (180° — عالم التجسيد المادي؛ تحرير الروح من قيود الطين عبر كيمياء الفناء)",
                quran: "«يُخْرِجُ الْحَيَّ مِنَ الْمَيِّتِ وَيُخْرِجُ الْمَيِّتَ مِنَ الْحَيِّ» [الروم: 19] • «كُلُّ شَيْءٍ هَالِكٌ إِلَّا وَجْهَهُ» [القصص: 88] • «وَقَالُوا أَإِذَا ضَلَلْنَا فِي الْأَرْضِ أَإِنَّا لَفِي خَلْقٍ جَدِيدٍ».",
                shift: "وعي التحول الخيميائي والبعث: موت الأنا المزيفة ليولد الإنسان الروحي الحقيقي، كسر قيود الخوف من الموت والفناء، وتحويل سم الشهوات السفلية إلى إكسير حياة وبصيرة نافذة.",
                proof: "«رسالة فصوص الحكمة» — الفارابي: الموت الطبيعي هو انتقال الصور، والتحول الباطني هو انخلاع النفس عن علائق الهيولى؛ والعقرب مجمع سر الإماتة والإحياء بأمر الله.",
                china_tao: "يقابله في الصين فرع «هاي» (Hai 亥 - الخنزير المائي الحكيم)، مجمع الشتاء والماء الغائر العميق؛ رمز الحكمة الكامنة تحت السطح، والقدرة على تطهير الأرض من السموم.",
                vedic_rashi: "في الفيدا يُعرف بـ «فريشيكا» (Vrishchika Rashi) يحكمه مانغالا (المريخ) وكيتو (ذنب التنين الغيبي)، ومنازله أنورادها وجييشتها؛ رمز الغوص في العوالم الغيبية.",
                babylon_egypt: "في بابل هو «غير-تاب» (Girtab - العقرب حارس أبواب العالم السفلي في ملحمة جلجامش). وفي مصر القديمة يمثل الإلهة سرقت ومرحلة تحول الروح لطائر الفينيق.",
                hermetic_kabbalah: "يمثل المبدأ الخيميائي «حل وربط» (Solve et Coagula). وفي القبالاه يتصل بأعضاء التناسل والإفراز وسفيرة ييسود في باطنها، مرمزاً للولادة من باطن الفناء.",
                desc: "برج الأسرار العميقة والموت والبعث وطائر الفينيق؛ مجمع الكيمياء الروحية لتحويل رصاص النفس إلى ذهب خالص. موكل به الملاك عزرائيل والملك الأحمر المائي، ويحكم نجم قلب العقرب الناري (Antares) ومنزلة الشولة لحراسة بوابات البرزخ وتطهير الخلايا الميتة لتجديد شباب الجسد والروح."
            }},
            {{
                id: 9,
                name: "برج القوس (Sagittarius ♐ — سهم البصيرة والرحلات الكونية والحكمة)",
                latin: "Sagittarius ♐ (The Archer)",
                glyph: "♐",
                element: "ناري",
                elemClass: "elem-fire",
                colorHex: "#8b5cf6",
                quality: "متقلب (Mutable — التوسع، ارتياد الآفاق، وطلب الحقيقة)",
                ruler: "المشتري ♃ (موطنه ومقر رحابته) • وباله في عطارد • هبوطه في الرأس",
                angelic_ruler: "الملاك صَرْفِيائيل / صَدْقِيائيل (Tzadkiel) • رئيس ملائكة فلك المشتري والفيض الإلهي العظيم",
                terrestrial_servant: "الملك شَمْهُورَش (قاضي الجن العادل / صاحب يوم الخميس والعلوم والشرائع)",
                lunar_mansions: "ثلث الشَّوْلَة الباقي • النَّعَائِم (الصادرة والواردة) • البَلْدَة الخالية",
                sacred_incense: "العود الهندي الخام، السندروس، اللبان الشحري، الكافور، المصطكى • معدنه: القصدير الخالص (Sn)",
                talisman_invocation: "حرفه الروحاني هو «الميم»؛ سر الإحاطة والعلم اللدني والفتوحات الملكوتية؛ يُتلى لفتح أقفال الحكمة وتيسير الأسفار البعيدة ونيل البصيرة في حقائق التوحيد في الفتوحات المكية.",
                organ: "الفخذان، الوركان، العصب الوركي، والكبد في وظيفته التوسعية",
                gland_system: "الكبد والغدة النخامية الخلفية والمسارات العصبية الحركية الطويلة",
                tribe: "سبط نفتالي / منسى («أيلة مسيبة تعطي أقوالاً حسنة» — الانطلاق في الآفاق)",
                letter: "الميم (م) / المحيط الكوني والامتداد الرسالي",
                opposing: "الجوزاء ♊ (180° — التفاصيل العقلية؛ دمج الفروع في الأصل الفلسفي والروحي الواحد)",
                quran: "«سَنُرِيهِمْ آيَاتِنَا فِي الْآفَاقِ وَفِي أَنفُسِهِمْ حَتَّىٰ يَتَبَيَّنَ لَهُمْ أَنَّهُ الْحَقُّ» [فصلت: 53] • «قُلْ سِيرُوا فِي الْأَرْضِ فَانظُرُوا كَيْفَ بَدَأَ الْخَلْقَ» [العنكبوت: 20] • «فَكَانَ قَابَ قَوْسَيْنِ أَوْ أَدْنَىٰ».",
                shift: "وعي الآفاق الكلية واليقين: تجاوز ضيق التعصب المحلي إلى رحابة الحكمة الإنسانية الشاملة، توجيه سهم النية نحو رضوان الله الأكبر، والانطلاق في سياحة الفكر وشهود آيات الآفاق.",
                proof: "«الآثار الباقية عن القرون الخالية» — البيروني: القوس برج ناري ذو جسدين (نصفه إنسان ونصفه فرس)، يدل على السفر البعيد والعلوم العالية وحكمة الأديان وتوسيع رقعة الممالك.",
                china_tao: "يقابله في الصين فرع «تسي» (Zi 子 - الفأر المائي الحكيم)، بداية دورة الفصول ونقطة انقلاب الشتاء الكبرى؛ رمز انبثاق فكرة التجدد وبدء رحلة الألف ميل.",
                vedic_rashi: "في الفيدا يُعرف بـ «دهانو» (Dhanu Rashi) يحكمه غورو (Guru / المشتري الحكيم المعلم)، ومنازله مولا وبورفا أشادها؛ ومولا تعني «الجذر الكوني» الواقع في مركز المجرة.",
                babylon_egypt: "في بابل هو «بابيلساغ» (Pabilsag - المحارب الإلهي المجنح الرامي بالسهم نحو قلب الظلام). وفي مصر هو رامي السهام الأفقية التي تفتح طريق الشمس المشرقة.",
                hermetic_kabbalah: "يمثل مبدأ «التوسع العقلي والروحي» (Mental Expansion). وفي القبالاه يتصل بالفخذين وسفيرة سامخ (Samekh - القوس الرابط بين ييسود وتيفئيريت) في قلب الشجرة.",
                desc: "برج الحكمة والرحلات الكونية الكبرى؛ سهمه موجه مباشرة نحو مركز مجرة درب التبانة (Sagittarius A*). موكل به الملاك صرفيائيل والملك شمهورش، ويحكم منازل النعائم والبلدة لحماية المسافرين في الآفاق وبث روح التفاؤل واليقين وتوسيع مدارك الفلسفة الإنسانية الشاملة."
            }},
            {{
                id: 10,
                name: "برج الجدي (Capricorn ♑ — صرامة الزمان وصعود قمة الهرم والمؤسسات)",
                latin: "Capricorn ♑ (The Sea-Goat)",
                glyph: "♑",
                element: "ترابي",
                elemClass: "elem-earth",
                colorHex: "#64748b",
                quality: "منقلب (Cardinal — الانقلاب الشتوي والرسوخ الأقصى)",
                ruler: "زحل ♄ (موطنه ومملكة وقاره) • شرفه في المريخ ♂ • وباله في القمر • هبوطه في المشتري",
                angelic_ruler: "الملاك كَسْفِيائيل (Kasfya'il) • رئيس ملائكة فلك زحل وحارس ناموس الزمان والصرامة",
                terrestrial_servant: "الملك مَيْمُون (أبانوخ / ميمون السحابي والجبلي / صاحب يوم السبت)",
                lunar_mansions: "سَعْد الذَّابِح • سَعْد بُلَع • ثلث سَعْد السُّعُود الأول المبارك",
                sacred_incense: "لبان الكندر الذكر، الميعة السائلة، الحبة السوداء، قطران الجبال • معدنه: الرصاص الأسود (Pb)",
                talisman_invocation: "حرفه الروحاني هو «النون»؛ سر الحفظ والصبر الإلهي وكتمان الأسرار وتثبيت القواعد ضد الزلازل والفتن؛ يُنقش لدفع كيد الظالمين وبناء الصروح المخلدة في مصنفات القدماء.",
                organ: "الهيكل العظمي، العظام، المفاصل، الركبتان، والجلد والأسنان",
                gland_system: "الغدد جارات الدرقية ومنظومة تكلس العظام وترسيب المعادن الحامية",
                tribe: "سبط بنيامين / زبولون (حراسة الأسوار، الصبر على الشدائد، وبناء المعاقل الحصينة)",
                letter: "النون (ن) / نون الوقاية وحفظ القوالب الهيكلية",
                opposing: "السرطان ♋ (180° — عاطفة الرحم؛ موازنة الصرامة بالرحمة، وحفظ البناء من القسوة)",
                quran: "«وَالْجِبَالَ أَوْتَادًا» [النبأ: 7] • «وَأَلْقَىٰ فِي الْأَرْضِ رَوَاسِيَ أَن تَمِيدَ بِكُمْ» [النحل: 15] • «إِنَّمَا يُوَفَّى الصَّابِرُونَ أَجْرَهُم بِغَيْرِ حِسَابٍ» [الزمر: 10].",
                shift: "وعي الصبر والرسوخ الصخري والمسؤولية: التحرر من القسوة والتشاؤم والبرود، تسلق جبل الصبر خطوة بخطوة حتى بلوغ القمة، وتحمل أمانة الاستخلاف وإقامة العمران المستدام.",
                proof: "«رسائل إخوان الصفا»: الجدي برج ترابي بارد يابس، بيت زحل؛ يُنسب إليه العظام والصلابة والصبر على الأزمان الطويلة، وهو قوام الهيكل الذي تستند إليه سائر الأعضاء.",
                china_tao: "يقابله في الصين فرع «تشو» (Chou 丑 - الثور الصابر الحارث)، رمز الجلد الأسطوري، العمل الدؤوب تحت وطأة البرد القارس، وتأسيس القواعد المتينة للمستقبل.",
                vedic_rashi: "في الفيدا يُعرف بـ «ماكارا» (Makara Rashi) يحكمه شاني (Shani / زحل حارس العدالة والزمن)، ومنازله أوتارا أشادها وشرافانا؛ وشرافانا ترمز للاستماع والإنصات الحكيم.",
                babylon_egypt: "في بابل هو «سوهور-ماش» (Suhurmāšu - الماعز السمكي، رمز الإله إنكي إله الأعماق والحكمة والبناء). وفي مصر يمثل حارس الحدود الكونية الصخرية الصلبة.",
                hermetic_kabbalah: "يمثل مبدأ «السببية والحدود والبناء» (Structure & Karma). وفي القبالاه يتصل بالعظام والركبتين وسفيرة بينة في جانب الصرامة، رمزاً للحجر الأساس الذي لا يتزعزع.",
                desc: "برج الهيكل الصلب والقمم الشامخة؛ يرمز لصعود الماعز نحو ذروة الجبل وللإنسان الذي يبني بالصبر صروح المعرفة التي تقاوم عوادي الدهر. موكل به الملاك كسفيائيل والملك ميمون، ويحكم منازل سعد الذابح وسعد بلع لمنح الصلابة للهيكل العظمي والمفاصل وصيانة الأمة من الانهيار في سنين الشدة."
            }},
            {{
                id: 11,
                name: "برج الدلو (Aquarius ♒ — سكب ماء المعرفة الكونية وعصر الشبكات)",
                latin: "Aquarius ♒ (The Water-Bearer)",
                glyph: "♒",
                element: "هوائي",
                elemClass: "elem-air",
                colorHex: "#06b6d4",
                quality: "ثابت (Fixed — ثبات الرؤية الكلية للإنسانية)",
                ruler: "زحل ♄ وأورانوس ♅ • شرفه في نيبتون • وباله في الشمس • هبوطه في عطارد",
                angelic_ruler: "الملاك كَسْفِيائيل الهوائي • الحاكم لأفلاك الرياح والمعرفة اللامركزية الكلية",
                terrestrial_servant: "الملك مَيْمُون الطَّيَّار (خادم الأملاك الهوائية والفيوضات المعرفية الحرة)",
                lunar_mansions: "ثلثا سَعْد السُّعُود الباقيان • سَعْد الأَخْبِيَة (خبايا الكنوز) • ثلثا فَرْغ الدَّلْو المُقَدَّم",
                sacred_incense: "الجاوي الأبيض، الميعة اليابسة، القرنفل، اللبان الخارق • معدنه: الأثير المصفى والزركون الأزرق",
                talisman_invocation: "حرفه هو «السين»؛ سر السيولة والانفتاح العقلي وكشف المخترعات العلمية وخرق العادات الفكرية؛ يُستعمل لفيض المعرفة الشاملة وإزالة الحجب الذهنية بين الشعوب.",
                organ: "الساقان، الكاحلان، الدورة الدموية الوريدية، والجهاز الكهربائي العصبي",
                gland_system: "الشبكة العصبية الحيوية والتوصيل الكهربائي للخلايا العصبية والقلبية",
                tribe: "سبط رأوبين / دان (تدفق المياه، تحطيم القيود، وسكب الخير للجميع)",
                letter: "السين (س) / سر السرعة والشبكات والسيولة المعرفية",
                opposing: "الأسد ♌ (180° — سيادة الملك الفرد؛ تحويل السلطة من المركزية إلى اللامركزية)",
                quran: "«أَنزَلَ مِنَ السَّمَاءِ مَاءً فَسَالَتْ أَوْدِيَةٌ بِقَدَرِهَا» [الرعد: 17] • «وَفِي السَّمَاءِ رِزْقُكُمْ وَمَا تُوعَدُونَ» [الذاريات: 22] • «وَجَعَلْنَا مِنَ الْمَاءِ كُلَّ شَيْءٍ حَيٍّ» [الأنبياء: 30].",
                shift: "وعي الأخوة الإنسانية الشاملة والتحرر المعرفي: الترفع عن النرجسية والعزلة، سكب مياه العلم والرحمة لكل عطشان دون وسيط كهنوتي، وبناء مجتمع المعرفة المتكامل المترابط بالحق.",
                proof: "«التفهيم لأوائل صناعة التنجيم» — البيروني: الدلو برج هوائي مذكر ثابت، صورته رجل يسكب الماء من دلوه، دال على الأنهار والآبار والعلوم المستنبطة وتدفق المنافع على الكافة.",
                china_tao: "يقابله في الصين فرع «يين» (Yin 寅 - النمر الواثب)، رمز انكسار قيود الجليد، وثبة الوعي المفاجئة، والبداية الجذرية للمسارات الفكرية الحرة غير النمطية.",
                vedic_rashi: "في الفيدا يُعرف بـ «كومبها» (Kumbha Rashi) يحكمه شاني (زحل) وراهو (الرأس النجمي)، ومنازله دانيهتا وشاتابيشا؛ وشاتابيشا تعني «المئة طبيب وشفاء الأمم».",
                babylon_egypt: "في بابل هو «غولا» (Gula - الإله إيا وهو يسكب نهري دجلة والفرات من كتفيه حياةً للأرض). وفي مصر القديمة هو حابي إله فيضان النيل الساكب لجرتي الخصب.",
                hermetic_kabbalah: "يمثل مبدأ «الاهتزاز الشبكي والفيض الحر» (Universal Flow). وفي القبالاه يتصل بالساقين والكاحلين وسفيرة كيتر في إفاضتها للنور على الجميع دون حجب.",
                desc: "برج سكب ماء العلم والإنسانية؛ ارتبط بالدخول في العصر الفلكي الجديد (عصر الدلو)، حيث تسقط الاحتكارات وتتفجر شبكات المعرفة والذكاء، وتلتقي البشرية في وعي كوني جامع. موكل به كسفيائيل الهوائي وميمون الطيار، ويحكم سعد السعود وسعد الأخبية لاستخراج خبايا الأرض وكنوز العلوم الكونية."
            }},
            {{
                id: 12,
                name: "برج الحوت (Pisces ♓ — محيط الروحانية والسمكتين والمحبة والمسيح)",
                latin: "Pisces ♓ (The Fishes)",
                glyph: "♓",
                element: "مائي",
                elemClass: "elem-water",
                colorHex: "#6366f1",
                quality: "متقلب (Mutable — الذوبان في اللانهاية والاندماج الصوفي)",
                ruler: "المشتري ♃ ونبتون ♆ • شرفه في الزهرة ♀ • وباله وهبوطه في عطارد",
                angelic_ruler: "الملاك صَدْقِيائيل (Tzadkiel / صرفيائيل) • رئيس ملائكة بحار الرحمة والغفران والفيض اللدني",
                terrestrial_servant: "الملك شَمْهُورَش البحري (خادم أملاك البحار والروحانيات الغارقة في التسبيح)",
                lunar_mansions: "ثلث فَرْغ الدَّلْو المُقَدَّم • فَرْغ الدَّلْو المُؤَخَّر • بَطْن الحُوت النجمي (الرِّشَاء)",
                sacred_incense: "العنبر الأشهب البحري الخام، المسك الأبيض، الصندل العطري، الكافور الرائق • معدنه: البلاتين والفضة الممروجة",
                talisman_invocation: "حرفه هو «العين»؛ سر البصيرة الشهودية والذوبان في محبة الحق وكشف أسرار الغيب في المنامات؛ يُتلى لتفريج الكروب العظام كدعوة ذي النون في ظلمات البحر وبطن الحوت.",
                organ: "القدمان، الأصابع، والجهاز اللمفاوي والمناعي الكلي",
                gland_system: "الجهاز المناعي اللمفاوي والغدة الصنوبرية في اتصالها بالأحلام والرؤى",
                tribe: "سبط شمعون / يوسف (الرأفة، الرؤى والمنامات، والصفح الجميل بعد الشدة)",
                letter: "العين (ع) / عين الروح وبحر المعرفة اللدنية الأزلية",
                opposing: "العذراء ♍ (180° — الخبز والخدمة الدنيوية؛ تكامل السمكة والخبز في مائدة السماء)",
                quran: "«فَالْتَقَمَهُ الْحُوتُ وَهُوَ مُلِيمٌ * فَلَوْلَا أَنَّهُ كَانَ مِنَ الْمُسَبِّحِينَ * لَلَبِثَ فِي بَطْنِهِ إِلَىٰ يَوْمِ يُبْعَثُونَ» [الصافات: 142-144] • «قَالَ عِيسَى ابْنُ مَرْيَمَ اللَّهُمَّ رَبَّنَا أَنزِلْ عَلَيْنَا مَائِدَةً مِّنَ السَّمَاءِ» [المائدة: 114].",
                shift: "وعي الفناء في المحبة والرحمة الكونية: الذوبان في محيط التوحيد، التحرر من أوهام الأنا والانفصال، والتسبيح في ظلمات بحار الابتلاء حتى ينشق بطن الحوت عن فجر النجاة والاصطفاء.",
                proof: "«الفتوحات المكية» — محيي الدين بن عربي: الحوت هو ختام دورة الفلك ومجمع البحار، به تختم المقامات لتبدأ من جديد في الحمل، وصورته سمكتان متعاكستان؛ سمكة الشريعة وسمكة الحقيقة.",
                china_tao: "يقابله في الصين فرع «ماو» (Mao 卯 - الأرنب القمري الساحر)، رمز الرهافة العالية، الحساسية الروحية، العبور بين عوالم اليقظة والمنام، والاتصال بالأسرار الإلهية.",
                vedic_rashi: "في الفيدا يُعرف بـ «مينا» (Meena Rashi) يحكمه غورو (المشتري)، ومنازله بورفا بهادرابادا وأوتارا بهادرابادا وريفاتي؛ وريفاتي هي آخر المنازل رمز العودة للرحم الإلهي.",
                babylon_egypt: "في بابل هو «زيبات ميش» (Zibbātī - ذيلا السمكتين المتصلتين برباط كوني). وفي مصر القديمة نُقش كسمكتي النيل السابحتين في محيط النون (Nun - المياه الأزلية الأولى).",
                hermetic_kabbalah: "يمثل مبدأ «الاتحاد الروحي الأسمى والموكشا» (Transcendence). وفي القبالاه يتصل بالقدمين وسفيرة كيتر وموكشا، حيث تسقط التمايزات ويسبح العبد في نور ربه.",
                desc: "برج الختام الفلكي والمحيط الروحي؛ حكم عصر الحوت الرسالي (الميلاد - 2000 م) المتطابق مع رسالة السيد المسيح، رمزية السمكة (Ichthys)، صيادي الناس، وتسبيح يونس في بطن الحوت. موكل به الملاك صدقيائيل وشمهورش البحري، ويحكم منزلة بطن الحوت (الرشاء) لفيض الرحمة والمحبة غير المشروطة وشفاء القدمين والجهاز اللمفاوي."
            }}
        ];

        // MASTER COMPREHENSIVE AGES & PRECESSION DATA (ALL 12 EPOCHS • 25,920 YEARS)
        var AGES_DATA = window.AGES_DATA = [
            {{
                id: 1,
                era: "12,960 ق.م – 10,800 ق.م",
                title: "عصر العذراء (Virgo) — الفردوس البدئي والسنبلة الأولى",
                sign: "العذراء",
                glyph: "♍",
                polarity: "يقابله الحوت ♓ (180° - الغمر المائي والمحيط الكوني الأزل)",
                polarity_sign: "الحوت",
                polarity_glyph: "♓",
                ruler: "عطارد (المعرفة الأرضية وعلم البذور) • العنصر: ترابي 🌍",
                prophet: "آدم وحواء وشيت عليهم السلام — عهد الطهارة والبراءة الفطرية الأولى",
                monument: "مستوطنات العصر الحجري المتأخر والطبقات الأقدم لمعابد غوبكلي تبه (Göbekli Tepe) • كهوف الناتوفيين الأولى",
                yuga: "ساتيا يوغا (Satya Yuga - العصر الذهبي للحق والبراءة المطلقة)",
                alchemy: "المادة الأولى النقية (Prima Materia / Albedo البدئي)",
                quran: "«وَقُلْنَا يَا آدَمُ اسْكُنْ أَنتَ وَزَوْجُكَ الْجَنَّةَ وَكُلَا مِنْهَا رَغَدًا» [البقرة: 35] — «فَتَلَقَّىٰ آدَمُ مِن رَّبِّهِ كَلِمَاتٍ فَتَابَ عَلَيْهِ» [البقرة: 37]",
                symbols: "سنبلة القمح • العذراء الطاهرة • البذور الأولى • الفردوس الأرضي • التناغم مع الطبيعة",
                category: "prehistory",
                color: "#10b981",
                angle: 60,
                oppAngle: 240,
                desc: "عصر الصفاء البشري الأول قبل الانفصال المعرفي الحاد؛ يرتبط برمزية سنبلة القمح التي تحملها العذراء في كفها، إشارة إلى بدء استئناس النباتات وحفظ الحبوب في الهلال الخصيب. في التراث الديني يمثل عهد آدم وفردوس البراءة على الأرض، حيث كانت الأرض مهداً نقياً يتناغم فيه الإنسان مع نواميس الطبيعة. القطب المقابل (الحوت 180°) يمثل محيط الغيب والمياه الأزلية التي كانت تحيط باليابسة، ومقدمة للتغير المناخي الكوني العظيم مع انحسار العصر الجليدي الأخير.",
                polar_shadow: "ظل النقيض: خطر الانغماس في التفاصيل المادية والزراعية ونسيان المحيط الروحي الغيبي (الحوت ♓)."
            }},
            {{
                id: 2,
                era: "10,800 ق.م – 8,640 ق.م",
                title: "عصر الأسد (Leo) — شروق شمس الحضارة وصحوة أبي الهول",
                sign: "الأسد",
                glyph: "♌",
                polarity: "يقابله الدلو ♒ (180° - انهمار المياه والوعي الجمعي)",
                polarity_sign: "الدلو",
                polarity_glyph: "♒",
                ruler: "الشمس ☀️ • العنصر: ناري 🔥",
                prophet: "إدريس الأول (أخنوخ البدئي / هرمس الهرامسة) — حكيم الشمس والعلوم الفلكية",
                monument: "تمثال أبو الهول بهضبة الجيزة (المصمم بجسد أسد متجهاً بدقة نحو شروق شمس برجه في الاعتدال الربيعي لعام 10,500 ق.م) • صروح غوبكلي تبه المنحوتة",
                yuga: "ساتيا يوغا المتأخرة / بداية تريتا يوغا",
                alchemy: "الذهب الشمسي والسيادة الفردية (Citrinitas / Sol)",
                quran: "«وَالشَّمْسِ وَضُحَاهَا * وَالْقَمَرِ إِذَا تَلَاهَا» [الشمس: 1-2] — «وَجَعَلْنَا سِرَاجًا وَهَّاجًا» [النبأ: 13]",
                symbols: "الأسد الهصور • قرص الشمس الذهبي • تاج الملوكية المقدسة • أبو الهول الجاثم • نار الصواعق",
                category: "prehistory",
                color: "#f59e0b",
                angle: 30,
                oppAngle: 210,
                desc: "نهاية العصر الجليدي الأخير وبدء الذوبان العظيم؛ لمعان شمس القوة والسيادة الفردية. نحت القدماء أعظم صرح على وجه الأرض: تمثال أبو الهول (جسد أسد ورأس إنسان) ناظراً بدقة متناهية باتجاه شروق شمس برجه الأسد في الاعتدال الربيعي لتلك الحقبة. شهد العصر بزوغ الملكية المقدسة وعبادة الذهب الشمسي والمركزية الروحية. قابله الدلو الذي سكب طوفان المياه الذائبة وكسر عزلة التجمعات البشرية ليوقظ إنسانية الشعوب.",
                polar_shadow: "طغيان الفردية والاستبداد الشمسي ومحو حقوق الجماعة التي يدافع عنها الدلو (180°)."
            }},
            {{
                id: 3,
                era: "8,640 ق.م – 6,480 ق.م",
                title: "عصر السرطان (Cancer) — طوفان نوح وسفينة النجاة ورحم الماء",
                sign: "السرطان",
                glyph: "♋",
                polarity: "يقابله الجدي ♑ (180° - الجبال الراسية وحصون الحجر)",
                polarity_sign: "الجدي",
                polarity_glyph: "♑",
                ruler: "القمر 🌙 • العنصر: مائي 💧",
                prophet: "النبي نوح عليه السلام — شيخ الأنبياء وصانع الفلك المشحون بأمر الله",
                monument: "فلك نوح (السفينة الكبرى المستقرة على الجودي) • أسوار وبرج أريحا الأولى (أقدم مدينة مسورة في التاريخ) • قرى مستنقعات شط العرب",
                yuga: "تريتا يوغا (Treta Yuga - العصر الفضي)",
                alchemy: "الاحتضان في الرحم المائي والتطهير (Albedo / Vas Hermetis)",
                quran: "«وَاصْنَعِ الْفُلْكَ بِأَعْيُنِنَا وَوَحْيِنَا» [هود: 37] — «فَفَتَحْنَا أَبْوَابَ السَّمَاءِ بِمَاءٍ مُّنْهَمِرٍ * وَفَجَّرْنَا الْأَرْضَ عُيُونًا» [القمر: 11-12]",
                symbols: "القمر الفضي • السفينة الكونية • محارة الرحم • الماء والبحار الهادرة • أسوار أريحا الحامية",
                category: "prehistory",
                color: "#38bdf8",
                angle: 0,
                oppAngle: 180,
                desc: "طوفان المياه الكوني الشامل الذي غمر السهول مع ذوبان الصفائح الجليدية الهائلة. السرطان برج مائي يحكمه القمر ويرمز للرحم، البيت، الحماية، وحفظ البذور والأنسال. تجلت فيه رسالة النبي نوح وصناعة الفلك المشحون كرحم كوني عائم يحمي خلاصة الحياة من الهلاك. نشأت في هذا العصر أولى المدن الحصينة على ضفاف المياه كمدينة أريحا. في القطب المقابل (الجدي 180°)، استقر الفلك على جبل الجودي الحجري الراسي، ليتعادل طغيان الماء مع صلابة الصخر.",
                polar_shadow: "خطر الغرق في الطوفان النفسي والتقوقع العاطفي دون بناء صرح مؤسسي صلب (الجدي ♑)."
            }},
            {{
                id: 4,
                era: "6,480 ق.م – 4,320 ق.م",
                title: "عصر الجوزاء (Gemini) — انبثاق اللغات والألواح والتوأمان المؤسسان",
                sign: "الجوزاء",
                glyph: "♊",
                polarity: "يقابله القوس ♐ (180° - الحكمة الكلية والبحث عن المطلق)",
                polarity_sign: "القوس",
                polarity_glyph: "♐",
                ruler: "عطارد (رسول الحكمة والكاتب الإلهي) • العنصر: هوائي 💨",
                prophet: "إدريس / هرمس مثلث الحكمة — أول من خط بالقلم وعلم التدوين ومنازل النجوم",
                monument: "الألواح الفخارية الطينية الأولى بسومر وعيلام • مستوطنات العبيد وتل حلف • شبكات التجارة المبكرة بين النهرين والنيل",
                yuga: "تريتا يوغا المتأخرة / بداية دفابارا يوغا",
                alchemy: "الزئبق الهرمسي (Mercurius) والاتصال المزدوج",
                quran: "«اقْرَأْ بِاسْمِ رَبِّكَ الَّذِي خَلَقَ ... الَّذِي عَلَّمَ بِالْقَلَمِ» [العلق: 1-4] — «وَاذْكُرْ فِي الْكِتَابِ إِدْرِيسَ ۚ إِنَّهُ كَانَ صِدِّيقًا نَّبِيًّا» [مريم: 56]",
                symbols: "القلم واللوح • التوأمان (جلجامش وإنكيدو / قابيل وهابيل) • العصا الهرمسية (الكادوسيوس) • الأجنحة والرياح",
                category: "ancient",
                color: "#00f0ff",
                angle: 330,
                oppAngle: 150,
                desc: "عصر الانفجار اللغوي والتدوين؛ حكمه عطارد رب الفكر والكتابة والتجارة ونقل الرسائل. شهد نشأة الرموز التصويرية الأولى التي مهدت للمسمارية والهيروغليفية، وظهور أساطير وملاحم التوائم الشهيرة (قابيل وهابيل، جلجامش وإنكيدو، كاستور وبولوكس). ونزول صحف إدريس الذي كان أول من خاط الثياب وخط بالقلم وحسب مسارات النجوم. القطب المقابل (القوس 180°) دفع البشرية للارتقاء من جمع البيانات المجردة إلى التساؤل الفلسفي والروحي عن الخلود ومغزى الوجود.",
                polar_shadow: "تشتت الذهن في الثنائيات والجدل السفسطائي والنزاع الأخوي الدموي بين التوأمين."
            }},
            {{
                id: 5,
                era: "4,320 ق.م – 2,160 ق.م",
                title: "عصر الثور (Taurus) — العمارة الميغاليثية، عجل أبيس، وهوس الخلود",
                sign: "الثور",
                glyph: "♉",
                polarity: "يقابله العقرب ♏ (180° - الموت والتحنيط والبعث وعالم الأسرار)",
                polarity_sign: "العقرب",
                polarity_glyph: "♏",
                ruler: "الزهرة (الجمال والبناء والوفرة) • العنصر: ترابي 🌍",
                prophet: "إبراهيم الخليل عليه السلام (في نشأته البابلية وحربه ضد الأصنام) وهود وصالح في مدائن الأحقاف",
                monument: "أهرامات الجيزة ومقابر سقارة • الزقورات السومرية العملاقة في أور • ستونهنج ببريطانيا • معابد مينوس بكريت",
                yuga: "دفابارا يوغا (Dvapara Yuga - العصر البرونزي المادي)",
                alchemy: "النحاس الزهري وتجسيد الشكل الصلب (Coagulatio)",
                quran: "«وَاتَّخَذَ قَوْمُ مُوسَىٰ مِن بَعْدِهِ مِنْ حُلِيِّهِمْ عِجْلًا جَسَدًا لَّهُ خُوَارٌ» [الأعراف: 148] — «وَإِذْ قَالَ إِبْرَاهِيمُ لِأَبِيهِ آزَرَ أَتَتَّخِذُ أَصْنَامًا آلِهَةً» [الأنعام: 74]",
                symbols: "قرنا الثور • عجل أبيس الذهبي • الزهرة الخضراء • حجر الأهرام الصواني • زقورة أور",
                category: "ancient",
                color: "#10b981",
                angle: 300,
                oppAngle: 120,
                desc: "عصر تثبيت المادة واستقرار أعتى الحضارات الإمبراطورية في مصر السلالات وبابل وسومر ووادي السند. سادت فيه عبادة وتقديس الثور كرمز للخصوبة والقدرة الأرضية (عجل أبيس، الثور المجنح البابلي شيدو، ثور كريت مينوتور، وعبادة عشتار). والقطب المقابل بزاوية 180° هو العقرب الحاكم للموت والعالم السفلي؛ فانفجر في مصر هوس كوني بالتحنيط وبناء أضخم مقابر حجرية في التاريخ (الأهرامات ومصاطب الملوك) لضمان الخلود في رحلة الأوزيريس.",
                polar_shadow: "التصلب المادي الشديد، عبادة الأوثان والعجول الذهبية، والاستعباد الطبقي للأقنان."
            }},
            {{
                id: 6,
                era: "2,160 ق.م – 0 م (نقطة الصفر الميلادي)",
                title: "عصر الحمل (Aries) — ذبح الكبش، صهر الحديد، وشريعة موسى الصارمة",
                sign: "الحمل",
                glyph: "♈",
                polarity: "يقابله الميزان ♎ (180° - العدل والقانون الإلهي والميزان الحق)",
                polarity_sign: "الميزان",
                polarity_glyph: "♎",
                ruler: "المريخ (المبادأة والجهاد وصهر الحديد) • العنصر: ناري 🔥",
                prophet: "إبراهيم الخليل (الفداء بالكبش) وموسى الكليم وداود وسليمان عليهم السلام",
                monument: "هيكل القدس وسليمان • مسلات ومعابد الكرنك برؤوس الكباش (طريق الكباش) • أسوار بابل المعلقة • صروح الإمبراطورية الفارسية والرومانية",
                yuga: "نهاية دفابارا وبداية كالي يوغا (عصر الحديد والحروب)",
                alchemy: "الحديد المريخي والنار المصعدة (Calcinatio)",
                quran: "«وَفَدَيْنَاهُ بِذِبْحٍ عَظِيمٍ» [الصافات: 107] — «وَكَتَبْنَا لَهُ فِي الْأَلْوَاحِ مِن كُلِّ شَيْءٍ مَّوْعِظَةً وَتَفْصِيلًا» [الأعراف: 145] — «وَأَنزَلْنَا الْحَدِيدَ فِيهِ بَأْسٌ شَدِيدٌ وَمَنَافِعُ لِلنَّاسِ» [الحديد: 25]",
                symbols: "كبش الفداء • بوق الشوفار • خوذة المريخ وسيف الحديد • ألواح الوصايا العشر • ميزان العدالة",
                category: "ancient",
                color: "#ef4444",
                angle: 270,
                oppAngle: 90,
                desc: "عصر الثورة التوحيدية الكبرى وصهر أسلحة الحديد ونزول الشرائع المحكمة. بدأ بالفداء الإبراهيمي الخالد: ذبح الكبش العظيم بديلاً عن إسماعيل، ليعلن سقوط التضحية بالبشر. وتجلى في رسالة موسى الكليم الذي أسقط عبادة عجل الثور القديم بحرقه وتذريته في اليم، وأحل مكانه نفخ الشوفار (قرن الكبش) ونزول ألواح الشريعة الصارمة. حكمه المريخ فكان عصر صعود الإمبراطوريات العسكرية الكبرى (روما، فارس، مقدونيا). قابله الميزان (180°) ليرسخ القانون والشريعة والوصايا العشر وقضاء داود وسليمان.",
                polar_shadow: "الحروب الدموية الطاحنة، قسوة السيف المريخي، والتمسك الحرفي بالحرف وإغفال روح الرحمة."
            }},
            {{
                id: 7,
                era: "0 م – 2,160 م (مخاض البرزخ: 1980 - 2160 م)",
                title: "عصر الحوت (Pisces) — رسالة المسيح، رمزية السمكة، ومحيط المحبة والإيمان",
                sign: "الحوت",
                glyph: "♓",
                polarity: "يقابله العذراء ♍ (180° - الطهارة العذرية والخدمة والشفاء والمشافي)",
                polarity_sign: "العذراء",
                polarity_glyph: "♍",
                ruler: "المشتري (الروحانية والتوسع والعدل الإلهي) ونبتون (الحدس والمحيط الباطني) • العنصر: مائي 💧",
                prophet: "المسيح عيسى ابن مريم عليه السلام ورسول الله الخاتم محمد ﷺ في إرساء الإيمان الكوني",
                monument: "كنيسة القيامة والمهد • المسجد الأقصى وقبة الصخرة ومساجد بغداد وقرطبة والقاهرة • الكاتدرائيات القوطية المهيبة بأوروبا",
                yuga: "كالي يوغا العميقة (عصر الغربة الروحية وتراجع المادة للبحث عن الخلاص)",
                alchemy: "التحلل المائي الشامل (Solutio) وبياض الطهارة",
                quran: "«إِذْ قَالَ الْحَوَارِيُّونَ يَا عِيسَى ابْنَ مَرْيَمَ هَلْ يَسْتَطِيعُ رَبُّكَ أَن يُنَزِّلَ عَلَيْنَا مَائِدَةً مِّنَ السَّمَاءِ» [المائدة: 112] — «وَجَعَلْنَا فِي قُلُوبِ الَّذِينَ اتَّبَعُوهُ رَأْفَةً وَرَحْمَةً وَرَهْبَانِيَّةً» [الحديد: 27]",
                symbols: "السمكة المقدسة (Ichthys) • الخبز والخمر والماء الطهور • مريم العذراء وسنبلة النقاء • غسل الأقدام • المحراب والصليب",
                category: "prophetic",
                color: "#a855f7",
                angle: 240,
                oppAngle: 60,
                desc: "عصر انسكاب المشاعر الروحية والمحبة والفداء والتصوف الإلهي. بدأ بميلاد السيد المسيح الذي اتخذ السمكة رمزاً سرياً لدعوته؛ فكان حواريوه صيادي سمك، ومعجزته تكثير الخبز والسمك وإطعام الآلاف. القطب المقابل له هو العذراء (180°)، فتجلت فيه ولادة المسيح الإعجازية من مريم العذراء البتول دون مساس بشر، وتأسيس المشافي ودور الرعاية والرهبنة وتكريس خدمة الفقراء والمجذومين. وامتد العصر ليشهد بزوغ الرسالة المحمدية الخاتمة التي أرسلت رحمة للعالمين لجمع شتات الأرواح وتطهيرها بالإيمان والتوحيد الخالص.",
                polar_shadow: "التعصب الديني الأعمى، محاكم التفتيش، الهروب من الواقع المادي بالزهد المفرط، وتزييف العقائد في ظلمات الأوهام."
            }},
            {{
                id: 8,
                era: "2,160 م – 4,320 م (بدأ مخاضه ~2000 م)",
                title: "عصر الدلو (Aquarius) — فيضان المعرفة، ثورة الذكاء الاصطناعي، والوعي الشبكي",
                sign: "الدلو",
                glyph: "♒",
                polarity: "يقابله الأسد ♌ (180° - شعلة الروح والقلب والسيادة الفردية)",
                polarity_sign: "الأسد",
                polarity_glyph: "♌",
                ruler: "أورانوس (الابتكار والصواعق والكسر الثوري) وزحل (الهندسة والقياس الصارم) • العنصر: هوائي 💨",
                prophet: "التجديد الكوني والوعي الشامل ونزول عيسى بن مريم للحكم بالقسط في آخر الزمان",
                monument: "الشبكة العنكبوتية العالمية (Web) • مراكز البيانات الفائقة وحوسبة الكم (Quantum Nodes) • محطات الفضاء ومسبارات ما وراء المجموعة الشمسية",
                yuga: "نهاية كالي يوغا وبدء التحول والارتقاء النبضي (Dvapara الصاعدة عند سوامي سري يوكتشوار)",
                alchemy: "التسامي الإثيري والتيليباثي (Sublimatio)",
                quran: "«سَنُرِيهِمْ آيَاتِنَا فِي الْآفَاقِ وَفِي أَنفُسِهِمْ حَتَّىٰ يَتَبَيَّنَ لَهُمْ أَنَّهُ الْحَقُّ» [فصلت: 53] — «وَيَسْأَلُونَكَ عَنِ الرُّوحِ ۖ قُلِ الرُّوحُ مِنْ أَمْرِ رَبِّي وَمَا أُوتِيتُم مِّنَ الْعِلْمِ إِلَّا قَلِيلًا» [الإسراء: 85]",
                symbols: "جرة سكب الماء السماوي • دارات السيليكون والذكاء الفائق • الأثير والأمواج الكهرومغناطيسية • اللامركزية والحرية • شعاع الليزر",
                category: "future",
                color: "#00f0ff",
                angle: 210,
                oppAngle: 30,
                desc: "العصر الحاضر الذي تقف الإنسانية على عتبته؛ عصر سكب جرة الماء السماوية التي تفيض بعلم ومعرفة متاحة لكل إنسان دون احتكار كهنوتي أو سلطوي. يتجلى في الثورة الرقمية الهائلة، الذكاء الاصطناعي، شبكات الاتصال اللامركزية، واستكشاف الفضاء الكوني. القطب المقابل هو الأسد الحاكم للقلب والروح الفردية (180°)؛ مما يجعل التحدي الوجودي الأكبر للبشرية هو: كيف تطور ذكاءً آلياً فائقاً وتحافظ في الوقت نفسه على حرارة القلب الإنساني والقبس الروحي الإلهي دون أن تتحول البشرية إلى آلات ميتة الوجدان؟",
                polar_shadow: "الاغتراب الرقمي، سيطرة الخوارزميات المادية الصماء، فقدان المشاعر الدافئة، وتفكك الروابط الأسرية في الفضاء الافتراضي."
            }},
            {{
                id: 9,
                era: "4,320 م – 6,480 م (استشراف مستقبلي)",
                title: "عصر الجدي (Capricorn) — هندسة العوالم الكونية، النضج المؤسسي، وتبلور النظام",
                sign: "الجدي",
                glyph: "♑",
                polarity: "يقابله السرطان ♋ (180° - أصل الحياة وجذور الإنسانية الأولى)",
                polarity_sign: "السرطان",
                polarity_glyph: "♋",
                ruler: "زحل (سيد الأبعاد والزمن والنظام الصلب) • العنصر: ترابي 🌍",
                prophet: "النضج الروحي للبشرية واكتمال الخلافة الكونية في الأرض والآفاق",
                monument: "المدن الكوكبية المهندسة ومستعمرات الأجرام السماوية • الهياكل الفضائية العملاقة (Dyson Swarms / Megastructures)",
                yuga: "مرحلة النظام الكوني المكتمل",
                alchemy: "حجر الفلاسفة المتبلور (Lapis Philosophorum / Rubedo الكامل)",
                quran: "«يَا مَعْشَرَ الْجِنِّ وَالْإِنسِ إِنِ اسْتَطَعْتُمْ أَن تَنفُذُوا مِنْ أَقْطَارِ السَّمَاوَاتِ وَالْأَرْضِ فَانفُذُوا ۚ لَا تَنفُذُونَ إِلَّا بِسُلْطَانٍ» [الرحمن: 33]",
                symbols: "قمة الجبل الشاهق • حجر الفلاسفة الصقيل • بلورات الكريستال • عرش المسؤولية والزمن • الهيكل الفلكي المحكم",
                category: "future",
                color: "#f59e0b",
                angle: 180,
                oppAngle: 0,
                desc: "عصر النضج الهيكلي والمسؤولية الكونية التامة؛ يرتبط بالجدي الذي يتسلق أعلى قمم الجبال الوعرة ويحكمه زحل معلم الصبر والعدل الصارم. بعد فوضى وتدفق عصر الدلو، يأتي الجدي ليرتب المعرفة ويبني منها صروحاً كونية مستدامة ونظاماً حكيماً يحكم العلاقات الإنسانية والفضائية. القطب المقابل (السرطان 180°) يذكر الكائن البشري دائماً برحم أمه الأرض وميلاده الأول لئلا يفقد اتصاله بالأصل الإلهي الذي بدأ منه.",
                polar_shadow: "البيروقراطية الكونية الباردة، التصلب الحجري المفرط، وخنق الإبداع تحت وطأة القوانين الصارمة."
            }},
            {{
                id: 10,
                era: "6,480 م – 8,640 م (استشراف مستقبلي)",
                title: "عصر القوس (Sagittarius) — السفر بين المجرات، الفلسفة العليا، والارتقاء الروحي",
                sign: "القوس",
                glyph: "♐",
                polarity: "يقابله الجوزاء ♊ (180° - الاتصال والشبكات والتخاطر الذهني الكلي)",
                polarity_sign: "الجوزاء",
                polarity_glyph: "♊",
                ruler: "المشتري (التوسع الكوني والحكمة المطلقة) • العنصر: ناري 🔥",
                prophet: "ارتقاء الإنسان إلى مرتبة الحكيم الكوني والشهود الحضاري العابر للنجوم",
                monument: "بوابات القفز النجمي الزمكاني (Wormhole Stations) • الأكاديميات الكوزمولوجية المجرية العظمى",
                yuga: "مرحلة التوسع الناري والتكامل المعرفي",
                alchemy: "التصعيد الشامل والنور المتسع (Exaltatio)",
                quran: "«وَالسَّمَاءَ بَنَيْنَاهَا بِأَيْدٍ وَإِنَّا لَمُوسِعُونَ» [الذاريات: 47] — «هَلْ تَرَىٰ مِن فُطُورٍ * ثُمَّ ارْجِعِ الْبَصَرَ كَرَّتَيْنِ» [الملك: 3-4]",
                symbols: "القوس وسهم الانطلاق النجمي • صهيل الفرس المجنح • النار المضيئة • مجلدات الحكمة الشاملة • المسبار النجمي",
                category: "future",
                color: "#a855f7",
                angle: 150,
                oppAngle: 330,
                desc: "عصر إطلاق السهم الإنساني نحو أبعاد المجرات السحيقة والبحث عن الغاية الوجودية العظمى. يحكمه المشتري كوكب التوسع والعدالة والحكمة الروحية الكبرى. تنكسر فيه حدود المنظومة الشمسية لتبدأ البشرية رحلة استكشاف عوالم ما وراء النجوم، والبحث في المعنى الكلي للوجود والتجليات الإلهية في الأكوان المتعددة. القطب المقابل (الجوزاء 180°) يمنح هذا العصر قدرة خارقة على ربط هذه العوالم المتباعدة بشبكة تخاطرية وتواصلية واحدة تذوب فيها المسافات الفلكية.",
                polar_shadow: "التشتت في اتساع الفضاء المفرط، النزعة المغرورة بالتوسع دون رسوخ باطني، والغرور بالمعرفة الكونية."
            }},
            {{
                id: 11,
                era: "8,640 م – 10,800 م (استشراف مستقبلي)",
                title: "عصر العقرب (Scorpio) — التحول الجيني الأعظم، طائر الفينيق، والخلود الباطني",
                sign: "العقرب",
                glyph: "♏",
                polarity: "يقابله الثور ♉ (180° - الجسد والمادة وتثبيت الشكل الكوني)",
                polarity_sign: "الثور",
                polarity_glyph: "♉",
                ruler: "المريخ وبلوتو (التحول الجذري، الموت والبعث، والقدرة الباطنية) • العنصر: مائي 💧",
                prophet: "الشهود التام لحقيقة البرزخ والبعث وتلاشي حجاب المادة الكثيفة",
                monument: "حاضنات التحول البيولوجي والأثيري • مصفوفات حفظ الوعي غير الفاني • مراصد الثقوب السوداء",
                yuga: "مرحلة الاحتراق والتجدد الفينيقي (Transmutation)",
                alchemy: "الموت والبعث الخيميائي الأكبر (Mortificatio & Putrefactio -> Phoenix)",
                quran: "«كُلُّ نَفْسٍ ذَائِقَةُ الْمَوْتِ ۗ وَإِنَّمَا تُوَفَّوْنَ أُجُورَكُمْ يَوْمَ الْقِيَامَةِ» [آل عمران: 185] — «يُخْرِجُ الْحَيَّ مِنَ الْمَيِّتِ وَيُخْرِجُ الْمَيِّتَ مِنَ الْحَيِّ» [الروم: 19]",
                symbols: "طائر الفينيق (العنقاء) • النسر الصاعد • العقرب الباطني • جرعة التجدد • بوابة البرزخ الكبرى",
                category: "future",
                color: "#e11d48",
                angle: 120,
                oppAngle: 300,
                desc: "عصر الغوص في أعمق أسرار الوجود: لغز الموت والبعث والتحول من الكثافة المادية إلى اللطافة النورانية. يرتبط بالعقرب الذي يموت كزاحف ويولد من جديد كنسر طائر أو عنقاء فينيقية متسامية. تختبر البشرية فيه التحول الجيني والأثيري النهائي، حيث تسقط حدود الجسد العضوي الفاني، وتلتقي علوم الوعي بأسرار البرزخ الإلهي. القطب المقابل (الثور 180°) يعمل كمرساة تمنع الوعي من الذوبان الكامل وتذكره بقدسية المادة والتجسد الكوني.",
                polar_shadow: "الهوس بالسيطرة على قوى الحياة والموت، الانزلاق إلى الظلمات الباطنية، وخطر الفناء الروحي إن فُقدت بوصلة الإيمان."
            }},
            {{
                id: 12,
                era: "10,800 م – 12,960 م (استشراف مستقبلي)",
                title: "عصر الميزان (Libra) — الميزان الكوني الأخير، العدل التام، واكتمال الدورة العظمى",
                sign: "الميزان",
                glyph: "♎",
                polarity: "يقابله الحمل ♈ (180° - شعلة المبادأة والولادة الجديدة)",
                polarity_sign: "الحمل",
                polarity_glyph: "♈",
                ruler: "الزهرة (التناغم المطلق والسلام والجمال الكوني) • العنصر: هوائي 💨",
                prophet: "التوازن الإنساني الأقصى، سيادة القسط المطلق، والاستعداد للبدء من جديد",
                monument: "معبد التناغم الكوني الشامل • مجلس السلام الفضائي الأعظم • ساعة السنة الأفلاطونية المكتملة",
                yuga: "نهاية الدورة الكبرى والتهيئة لساتيا يوغا الجديدة (Golden Age Dawn)",
                alchemy: "الزواج الكيميائي الأعظم واكتمال الإكسير (Chymical Wedding / Conjunctio)",
                quran: "«وَالسَّمَاءَ رَفَعَهَا وَوَضَعَ الْمِيزَانَ * أَلَّا تَطْغَوْا فِي الْمِيزَانِ * وَأَقِيمُوا الْوَزْنَ بِالْقِسْطِ وَلَا تُخْسِرُوا الْمِيزَانَ» [الرحمن: 7-9]",
                symbols: "كفتا الميزان الذهبيتان • ريشة ماعت والحق المطلق • تاج التناغم الزهري • خاتم الدورة الكبرى • بوابة البدء الجديد",
                category: "future",
                color: "#38bdf8",
                angle: 90,
                oppAngle: 270,
                desc: "عصر ختام السنة الأفلاطونية العظمى (25,920 سنة)؛ عصر الميزان الذي يزن كل تجارب البشرية عبر الاثني عشر برجاً بميزان القسط الإلهي الدقيق. تسود فيه قيم السلام الشامل، التناغم الجمالي، والعدالة الكونية المكتملة بين كافة المخلوقات والعوالم. وعند نهاية هذا العصر، تقف البشرية على عتبة نقطة الانقلاب الكبرى، حيث يقابلها الحمل (180°) بشعلة المبادأة والولادة المتجددة، لتنطلق دورة كوزمولوجية جديدة من دورات الزمان الإلهي المقدر: ﴿كَمَا بَدَأْنَا أَوَّلَ خَلْقٍ نُّعِيدُهُ ۚ وَعْدًا عَلَيْنَا ۚ إِنَّا كُنَّا فَاعِلِينَ﴾.",
                polar_shadow: "التردد والشلل الحركي الناتج عن البحث عن كمال مستحيل في عالم الإمكان، قبل أن تنفجر شعلة الحمل بالولادة الجديدة."
            }}
        ];

        // 16 MASTER MANUSCRIPTS DATA ACROSS CIVILIZATIONS
        const MANUSCRIPTS_DATA = [
            {{
                name: "فصوص الحكم",
                author: "محيي الدين ابن عربي (ت 638 هـ)",
                summary: "27 فصاً حكمياً يشرح مطابقة كل فلك كوكبي لنبي من الأنبياء وتجلي الكمال الإلهي في دائرة الوجود.",
                chapters: "فص إدريس (الشمس)، فص هارون (المشتري)، فص إبراهيم (زحل)، فص يوسف (الزهرة)"
            }},
            {{
                name: "سفر أخنوخ (The Book of Enoch)",
                author: "منسوب للنبي إدريس (النسخة الأثيوبية بمكتبة بودليان)",
                summary: "كتاب مدارات النيرات السماوية، البوابات الست، التقويم الشمسي المقدس (364 يوماً)، وتدابير الملاك أوريئيل.",
                chapters: "الأصحاحات 72 - 82 (The Book of Luminaries) ورؤيا الأسابيع العشرة"
            }},
            {{
                name: "ألواح سومر وبابل (ملحمة جلجامش وأتراخاسيس)",
                author: "مكتبة آشور بانيبال (الألف الثاني ق.م - وادي الرافدين)",
                summary: "أقدم توثيق لطوفان الماء وأمر الإله إيا لحكيم البشر (أوتنابشتيم) ببناء السفينة والطلاء بالقار وركوب زوجين من كل كائن ورسو السفينة على الجبل.",
                chapters: "اللوح الحادي عشر من ملحمة جلجامش، وألواح ملحمة أتراخاسيس"
            }},
            {{
                name: "الفيدا والبورانا الهندية (ميتسيا بورانا ومانو)",
                author: "الحكماء الفيديون (الهند القديمة)",
                summary: "قصة طوفان الملك التقي ساتيافراتا (مانو)، وأمره ببناء الفلك وحمل بذور الحياة والحيوانات، ورسو السفينة على جبال الهيمالايا الشمالية.",
                chapters: "ميتسيا بورانا (فصول تجلي سمكة النجاة)، وشاتاباثا براهمانا"
            }},
            {{
                name: "بردية إيبوير (Ipuwer Papyrus) ومتون مصر",
                author: "مصر القديمة (متحف ليدن 344) وأفلاطون (طيماوس)",
                summary: "توثيق صاعق للضربات التسع وخروج بني إسرائيل: تحول النيل لدماء، هلاك القصور، وسقوط حضارة الاستكبار؛ ومحاورات أفلاطون حول كوارث الطوفان والنار.",
                chapters: "بردية إيبوير الهيراطيقية، ومحاورة طيماوس (حوار صولون وكهنة سايس)"
            }},
            {{
                name: "مخطوطات نجع حمادي والبحر الميت",
                author: "مغارات الصعيد وقمران (القرن 1 - 4 الميلادي)",
                summary: "نصوص غنوصية وبحر ميت تكشف تطابقاً نادراً مع القرآن: نفي صلب المسيح (رؤيا بطرس الغنوصي)، وبشارات إنجيل برنابا، واعتزال طائفة النور (الأسينيين).",
                chapters: "Codex VII (رؤيا بطرس)، إنجيل توما، ومخطوطة حرب أبناء النور"
            }},
            {{
                name: "سفر يتسيراه (Sefer Yetzirah)",
                author: "كتاب التكوين الباطني القديم",
                summary: "أقدم نص يربط الحروف الأبجدية الـ 22 بالأبراج الـ 12 والكواكب السبعة وأسباط بني إسرائيل الـ 12.",
                chapters: "الأصحاح الرابع (الحروف المزدوجة السبعة والكواكب السبعة)"
            }},
            {{
                name: "مطحنة هاملت (Hamlet's Mill)",
                author: "جورجيو دي سانتيلانا (MIT) وهيرثا فون ديشيند",
                summary: "إثبات أكاديمي ضخم بأن كل أساطير ونبوات العالم القديم هي شيفرات فلكية لترنح المحور ودورات الـ 2,160 سنة.",
                chapters: "الفصول 5 - 11 (محور الاعتدالين، الكبش الموسوي، والسمكة)"
            }},
            {{
                name: "كتاب الملل والدول (القِرانات الكبرى)",
                author: "أبو معشر جعفر بن محمد البلخي (ت 272 هـ)",
                summary: "المرجع الفلكي السياسي الأعظم لربط اقتران زحل والمشتري وانتقال المثلثات بظهور الأنبياء وسقوط الممالك.",
                chapters: "المقالات 1 و 2 (القِران الصغير 20 سنة، الأوسط 240 سنة، الأعظم 960 سنة)"
            }},
            {{
                name: "رسائل إخوان الصفا وخلان الوفا",
                author: "جماعة الحكماء بالبصرة (القرن 4 هـ)",
                summary: "موسوعة من 52 رسالة تربط تركيب جسد الإنسان كعالم صغير بتشريح الأفلاك والطبائع والمقامات النبوية.",
                chapters: "الرسالة 3 (الأفلاك)، الرسالة 21 (الإنسان عالم صغير)، ورسالة الأدوار والأكوار"
            }},
            {{
                name: "الكيباليون (The Kybalion)",
                author: "المبتدئون الثلاثة (Three Initiates)",
                summary: "استخلاص المبادئ الهرمسية السبعة الكونية وتطبيقاتها في ترددات الوعي والقطبية والسببية والاهتزاز.",
                chapters: "الفصول 2 - 9 (العقلانية، التناظر، الاهتزاز، القطبية، الإيقاع، السببية، النوع)"
            }},
            {{
                name: "الآثار الباقية عن القرون الخالية",
                author: "أبو الريحان البيروني (ت 440 هـ)",
                summary: "تحقيق مقارن لتقاويم الأمم وأدوار الكواكب وتواريخ ظهور الأنبياء والملل عند الفرس والهنود واليهود.",
                chapters: "أبواب أدوار الكواكب وسني الطوفان والتواريخ الفلكية للرسالات"
            }},
            {{
                name: "الأسترونوميكا (Astronomica)",
                author: "ماركوس مانيليوس (روما، القرن الأول الميلادي)",
                summary: "أقدم توثيق شعري روماني لمنظومة الميلوثيسيا وتوزيع أعضاء الجسد البشري من الحمل إلى الحوت.",
                chapters: "الكتاب الثاني والرابع (تشريح الجسد الفلكي الكوني)"
            }},
            {{
                name: "يافانا جاتاكا (Yavanajātaka)",
                author: "سفوجيدفاجا (الهند، القرن 3 الميلادي)",
                summary: "تجسيد الإله كالا براجاباتي كإنسان كوني مقسم على البروج الاثني عشر، متطابقاً مع التراث الروماني والإسلامي.",
                chapters: "تجسيد كالا بوروشا (Kala Purusha) والطب الفلكي الهندي"
            }},
            {{
                name: "أصل جميع العبادات (Origine de tous les cultes)",
                author: "شارل فرانسوا دوبوي (Charles Dupuis)",
                summary: "التحليل الموسوعي الشامل لتطابق قصص الأنبياء والشخصيات الدينية مع الرموز الفلكية لعصور البروج.",
                chapters: "المجلد الثالث (عصر الحمل، عصر الحوت، والشمس المخلصة)"
            }},
            {{
                name: "كتب الموازين وسر الخليقة",
                author: "جابر بن حيان الكوفي (ت 200 هـ)",
                summary: "علم ميزان الحروف والطبائع، والتحقيق العربي الأقدم للوح الزمرد وتناظر المعادن السبعة مع الكواكب السبعة.",
                chapters: "ميزان الطبائع، الكبريت والزئبق، والمعادن السبعة"
            }}
        ];

        // CRITIQUE & DISCREPANCIES DATA (FOR MURSHID)
        const CRITIQUE_DATA = [
            {{
                title: "1. طوفان نوح: نزاهة النبوة مقابل بهتان التوراة وضعف آلهة بابل",
                tag: "أولو العزم • عصر السرطان",
                isUrgent: true,
                quran: "<strong>بيان القرآن الكريم المحكم:</strong> نوح عبد شكور معصوم («إِنَّهُ كَانَ عَبْدًا شَكُورًا»). صنع الفلك بوحي الله وأعينه («وَاصْنَعِ الْفُلْكَ بِأَعْيُنِنَا وَوَحْيِنَا»). الطوفان تطهير إلهي شامل للفساد، ورست السفينة على «الجودي». والابن هلك لكفره إعلاءً لرابطة العقيدة على رابطة الدم.",
                manuscript: "<strong>سقطات وتناقضات المخطوطات القديمة:</strong><br>• <em>التوراة (تكوين 9):</em> تزعم شرب نوح للخمر وسكره وتعريه داخل خيمته ولعنه لكنعان!<br>• <em>ملحمة جلجامش (بابل):</em> الآلهة خافت وصعدت تبكي كالكيلاب وتجمعت كالذباب حول القربان!<br>• <em>الموقع الجغرافي:</em> التوراة تذكر جبال أرارات (أرمينيا)، بينما القرآن يدقق جبل الجودي.",
                murshid: "<strong>ملاحظة وتحقيق للعرض على المرشد:</strong> عصمة الأنبياء في العقيدة الإسلامية أصل قطعي. نصوص التوراة تعكس إسقاطات بشرية تسيء لمقام النبوة، بينما نصوص بابل تثبت الحقيقة التاريخية للحدث الكوني ولكن بوعي وثني منحرف عجز عن التوحيد الخالص."
            }},
            {{
                title: "2. إدريس عليه السلام: عصمة الملائكة مقابل أسطورة سقوط المراقبين (سفر أخنوخ)",
                tag: "السماء الرابعة • فلك الشمس",
                isUrgent: true,
                quran: "<strong>بيان القرآن الكريم المحكم:</strong> «وَرَفَعْنَاهُ مَكَانًا عَلِيًّا» • «إِنَّهُ كَانَ صِدِّيقًا نَّبِيًّا». والملائكة خلق نوراني معصوم: «لَّا يَعْصُونَ اللَّهَ مَا أَمَرَهُمْ وَيَفْعَلُونَ مَا يُؤْمَرُونَ» [التحريم: 6]، لا يتناسلون ولا يشتهون ولا يسقطون في الزنا.",
                manuscript: "<strong>تناقض واختلاق سفر أخنوخ (The Watchers):</strong><br>يزعم سفر أخنوخ (الأصحاح 6-10) أن 200 من ملائكة السماء نزلوا واشتهوا بنات البشر وتزوجوهن وولدوا عمالقة سفكوا الدماء، وعلموا البشر صناعة السيوف والأسلحة والسحر وصبغ الحواجب!",
                murshid: "<strong>ملاحظة وتحقيق للعرض على المرشد:</strong> سفر أخنوخ يحتوي علوماً فلكية صحيحة في مدارات النيرات وبوابات الشمس، لكن أسطورة سقوط الملائكة دَسّ وثني تسلل من الميثولوجيا السومرية والإغريقية (أبناء الآلهة). المفسدون في الأرض هم شياطين الجن وليس ملائكة الرحمن."
            }},
            {{
                title: "3. إبراهيم الخليل: هوية الذبيح وبطلان تهمة الكذب والجبن",
                tag: "أولو العزم • فلك زحل",
                isUrgent: true,
                quran: "<strong>بيان القرآن الكريم المحكم:</strong> إبراهيم إمام الحنفاء («إِنَّ إِبْرَاهِيمَ كَانَ أُمَّةً قَانِتًا لِّلَّهِ حَنِيفًا»). حطم عبادة الكواكب بالدليل العقلي («لَا أُحِبُّ الْآفِلِينَ»). الذبيح هو ابنه البكر إسماعيل الذي بنى معه الكعبة بمكة وفُدي بالكبش، ثم بعد ذلك بُشر بإسحاق.",
                manuscript: "<strong>تحريفات التوراة العبرية (تكوين 22):</strong><br>• تزعم التوراة أن الذبيح هو «إسحاق، وحيدك الذي تحبه»، وهو تناقض تاريخي لأن إسماعيل كان الابن الوحيد لـ 14 سنة قبل ولادة إسحاق!<br>• تزعم التوراة والتلمود أن إبراهيم كذب وقال عن سارة أختي خوفاً من فرعون مصر.",
                murshid: "<strong>ملاحظة وتحقيق للعرض على المرشد:</strong> نقل التوراة لصفة الذبيح من إسماعيل إلى إسحاق هو انحراف دافعه التعصب العرقي لبني إسرائيل لطمس شرف فرع إسماعيل الذي خرج منه النبي الخاتم محمد ﷺ في مكة المكرمة حيث نُحر فداء الكبش العظيم."
            }},
            {{
                title: "4. موسى الكليم: براءة هارون وتحديد شخصية السامري صانع العجل",
                tag: "أولو العزم • عصر الحمل والحديد",
                isUrgent: true,
                quran: "<strong>بيان القرآن الكريم المحكم:</strong> تنزيل ألواح التوراة والوصايا العشر لإقامة ميزان العدل. صانع العجل المفتري هو رجل منافق يُدعى «السامري»، وهارون عليه السلام بريء تماماً بل نهى القوم بشدة: «يَا قَوْمِ إِنَّمَا فُتِنتُم بِهِ وَإِنَّ رَبَّكُمُ الرَّحْمَٰنُ فَاتَّبِعُونِي».",
                manuscript: "<strong>الفريحة التوراتية الكبرى (خروج 32):</strong><br>تنسب التوراة العبرية صناعة العجل الذهبي بنفسه وجمع الذهب وبناء المذبح له إلى النبي هارون عليه السلام أخي موسى!",
                murshid: "<strong>ملاحظة وتحقيق للعرض على المرشد:</strong> القرآن الكريم يصحح تاريخ الأنبياء تصحيحاً حاسماً وينقذ مقام هارون من تهمة الشرك وصناعة الأصنام، ويحدد بدقة تاريخية مدهشة أن الصانع ساحر ذو أصل سامري استغل بقايا طاقة عبادة العجل (عصر الثور البائد)."
            }},
            {{
                title: "5. السيد المسيح عيسى: نفي الصلب والتأليه وشهادة مخطوطات نجع حمادي",
                tag: "أولو العزم • فلك الشمس والعذراء",
                isUrgent: true,
                quran: "<strong>بيان القرآن الكريم المحكم:</strong> «وَمَا قَتَلُوهُ وَمَا صَلَبُوهُ وَلَٰكِن شُبِّهَ لَهُمْ... بَل رَّفَعَهُ اللَّهُ إِلَيْهِ» [النساء: 157-158]. المسيح رسول وعبد لله أُلقيت إليه كلمة الله والروح، ومريم صدّيقة طاهرة، ونفي التثليث والألوهية («مَّا الْمَسِيحُ ابْنُ مَرْيَمَ إِلَّا رَسُولٌ»).",
                manuscript: "<strong>التناقض الكنسي وشهادة المخطوطات الغنوصية:</strong><br>• الأناجيل الرسمية جعلت عقيدة الخلاص بالدم على خشبة الصليب ولعنة الموت.<br>• <em>مخطوطات نجع حمادي (رؤيا بطرس الغنوصي):</em> تشهد حرفياً بأن المسيح كان يبتسم فوق الشجرة ولم يُصلب، وأن شخصاً بديلاً أُلقي عليه شبهه وصُلب مكانه!<br>• <em>إنجيل برنابا:</em> يثبت أن يهوذا هو من صُلب، ويبشر باسم أحمد رسول الله.",
                murshid: "<strong>ملاحظة وتحقيق للعرض على المرشد:</strong> اكتشاف مخطوطات نجع حمادي عام 1945 في صعيد مصر قدم أكبر دليل أثري مستقل يؤكد ما أخبر به القرآن قبل 1400 عام من أن المسيحيين الأوائل كان بينهم تيار أصيل ينفي الصلب ويثبت الشبه والرفع."
            }},
            {{
                title: "6. التنجيم الوثني والسحر مقابل الكوزمولوجيا التوحيدية القرآنية",
                tag: "المنظومة المعرفية الكلية",
                isUrgent: false,
                quran: "<strong>بيان القرآن الكريم المحكم:</strong> الأفلاك والكواكب والبروج مخلوقات مسخرة بأمر الله لا تملك لنفسها ولا لغيرها نفعاً ولا ضراً: «وَالشَّمْسَ وَالْقَمَرَ وَالنُّجُومَ مُسَخَّرَاتٍ بِأَمْرِهِ ۗ أَلَا لَهُ الْخَلْقُ وَالْأَمْرُ» [الأعراف: 54]. والتوحيد لا يشرك مع الله كوكباً ولا روحانية فلكية.",
                manuscript: "<strong>انزلاقات شمس المعارف والبيكاتريكس (غاية الحكيم):</strong><br>الخلط بين الطبائع الفيزيائية والتأثير الإشعاعي للأجرام، وبين طلب الحوائج من أرواح الكواكب واستنزالها بالعزائم والبخور، وهو عين الشرك البابلي والصابئي الذي جاء إبراهيم والأنبياء لهدمه.",
                murshid: "<strong>ملاحظة وتحقيق للعرض على المرشد:</strong> نضع هذا الفارق الجوهري تحت نظر المرشد: دراستنا للأفلاك والأبراج هي دراسة للنواميس الكونية المودعة والآيات التكوينية الدالة على عظمة الخالق، وليست تنجيماً حتمياً ولا استجلاباً لروحانيات محرمة شرعاً."
            }},
            {{
                title: "7. إرم ذات العماد وقوم عاد: شهادة ناسا وأقمار الرادار وجغرافيا بطليموس",
                tag: "أركيولوجيا • إعجاز تاريخي",
                isUrgent: false,
                quran: "<strong>بيان القرآن الكريم المحكم:</strong> «أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ * إِرَمَ ذَاتِ الْعِمَادِ * الَّتِي لَمْ يُخْلَقْ مِثْلُهَا فِي الْبِلَادِ» [الفجر: 6-8]. مدينة الأعمدة العملاقة المفقودة في الرمال.",
                manuscript: "<strong>الشواهد التاريخية والأركيولوجية غير المباشرة:</strong><br>• <em>كتاب الجغرافيا لبطليموس (القرن 2 م):</em> ذكر واحة وقبيلة «أوباريتاي» (Ubaritae) في صحراء جنوب الربع الخالي.<br>• <em>استكشافات ناسا الرادارية (1992):</em> كشفت صور المكوك الفضائي شبكة طرق قوافل تجارية مطمورة تقود لمدينة «أوبار / إرم» ذات الأبراج الثمانية المنهارة في هوة صخرية عملاقة تحت الرمال، بعد قرون من إنكار المستشرقين لوجودها!",
                murshid: "<strong>ملاحظة وتحقيق للعرض على المرشد:</strong> هذا الشاهد يثبت أن تفرد القرآن بذكر «إرم ذات العماد» - التي لم تذكرها التوراة ولا الأناجيل - كان نبوءة أركيولوجية معجزة كشفتها التقنيات الحديثة مصدقة للوحي الإلهي."
            }},
            {{
                title: "8. أصداء طوفان نوح في أقصى الشرق (الصين) وحضارات أمريكا القديمة (المايا)",
                tag: "أساطير الشعوب • كوزمولوجيا عالمية",
                isUrgent: false,
                quran: "<strong>بيان القرآن الكريم المحكم:</strong> «فَفَتَحْنَا أَبْوَابَ السَّمَاءِ بِمَاءٍ مُّنْهَمِرٍ * وَفَجَّرْنَا الْأَرْضَ عُيُونًا» • «وَاصْنَعِ الْفُلْكَ بِأَعْيُنِنَا». طوفان الماء كحدث كوني استئصالي وتطهيري عالمي.",
                manuscript: "<strong>المتون الصينية والأمريكية القديمة:</strong><br>• <em>كتاب الوثائق الصيني (Shu Jing):</em> انهيار ركائز السماء الأربع وتفجر المياه العميقة، وإنقاذ السلالة البشرية على يد «نووا Nüwa» و«يو العظيم».<br>• <em>كتاب البوبول فوه (Popol Vuh - المايا):</em> طوفان أسود هائل جرف البشر القدماء بسبب انحرافهم وتكبرهم على الخالق الأعظم ولم ينج إلا قلة مؤمنة في قارب خيزران صلب.",
                murshid: "<strong>ملاحظة وتحقيق للعرض على المرشد:</strong> تواتر قصة الطوفان بأدق تفاصيلها (فوران المياه، صناعة فلك النجاة، انقراض الأشرار) عبر قارات معزولة جغرافياً يثبت تاريخية دعوة نوح كأب ثانٍ للإنسانية كما قرر القرآن."
            }},
            {{
                title: "9. مركزية كعبة إبراهيم: شهادة المؤرخ اليوناني ديودوروس وألواح إبلا السورية",
                tag: "أور الكلدانيين • البيت العتيق",
                isUrgent: false,
                quran: "<strong>بيان القرآن الكريم المحكم:</strong> «إِنَّ أَوَّلَ بَيْتٍ وُضِعَ لِلنَّاسِ لَلَّذِي بِبَكَّةَ مُبَارَكًا وَهُدًى لِّلْعَالَمِينَ» [آل عمران: 96]، وتطهير إبراهيم وإسماعيل للقواعد من الشرك.",
                manuscript: "<strong>الشواهد الإغريقية والسورية القديمة:</strong><br>• <em>المؤرخ ديودوروس الصقلي (القرن 1 ق.م):</em> يسجل في كتابه التاريخي وجود معبد ومزار عريق فائق القداسة في غرب الجزيرة العربية تعظمه وتشد الرحال إليه كافة القبائل العربية.<br>• <em>ألواح مملكة إبلا (2400 ق.م):</em> تذكر مدناً وأسماء آباء إبراهيم وتؤكد تمركز عبادة الثالوث الكوكبي (القمر، الشمس، والزهرة) في أور وحران، وهي عين الكواكب التي حاجج بها إبراهيم قومه.",
                murshid: "<strong>ملاحظة وتحقيق للعرض على المرشد:</strong> اعتراف المؤرخين اليونانيين بقداسة الكعبة قبل الإسلام بخمسة قرون، وتطابق ألواح إبلا مع أسماء أنساب الخليل في سورة الأنعام، يؤكد أصالة البيت العتيق ومحورية ملة إبراهيم الحنيفية."
            }},
            {{
                title: "10. البشارات غير المباشرة بالنبي الخاتم محمد ﷺ في متون فارس والبوذية",
                tag: "الختام الكوني • شمس الرسالات",
                isUrgent: false,
                quran: "<strong>بيان القرآن الكريم المحكم:</strong> «الَّذِينَ يَتَّبِعُونَ الرَّسُولَ النَّبِيَّ الْأُمِّيَّ الَّذِي يَجِدُونَهُ مَكْتُوبًا عِندَهُمْ فِي التَّوْرَاةِ وَالْإِنجِيلِ» • «وَمَا أَرْسَلْنَاكَ إِلَّا رَحْمَةً لِّلْعَالَمِينَ».",
                manuscript: "<strong>المخطوطات الفارسية والهندية القديمة:</strong><br>• <em>كتاب الدساتير (زند أوستا - الزرادشتية):</em> نص صريح بنبوءة ظهور رجل في جزيرة العرب يكسر أصنام النار ويوجه أمته لبيت إبراهيم ويسقط دولة ساسان.<br>• <em>مخطوطات ديغا نيكايا (البوذية القديمة):</em> نبوءة بوذا بظهور المعلم الختامي المبارك «مايتريا Maitreya» (رحمة للعالمين / المحمود).",
                murshid: "<strong>ملاحظة وتحقيق للعرض على المرشد:</strong> نرفع للمرشد هذه البشارات العالمية المودعة في نصوص الهند وفارس التي لم تخضع لتحريفات أحبار أهل الكتاب، والتي تشهد بأن النور المحمدي كان مرتقباً ومبشراً به في كافة تقاليد الوعي الإنساني."
            }}
        ];

        // 1. Tab Switching Function
        function switchTab(tabId) {{
            document.querySelectorAll('.tab-section').forEach(sec => sec.classList.remove('active'));
            document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
            document.getElementById('tab-' + tabId).classList.add('active');
            event.target.classList.add('active');

            if (tabId === 'graph') {{
                setTimeout(() => {{
                    if (cosmicNetwork) cosmicNetwork.fit();
                }}, 100);
            }}
        }}

        // 2. Interactive Force Network (Vis.js Engine) - Defensive Initialization
        var nodesDataSet = null;
        var edgesDataSet = null;
        var cosmicNetwork = null;
        var activeGraphCategory = 'ALL';
        var drawer = null;
        var drawerTitle = null;
        var drawerMeta = null;
        var drawerBody = null;
        var drawerConns = null;

        try {{
            drawer = document.getElementById('reader-drawer');
            drawerTitle = document.getElementById('drawer-title');
            drawerMeta = document.getElementById('drawer-meta');
            drawerBody = document.getElementById('drawer-body');
            drawerConns = document.getElementById('drawer-connections-pills');

            const container = document.getElementById('cosmic-network-canvas');
            if (container && typeof vis !== 'undefined' && typeof rawGraphData !== 'undefined') {{
                nodesDataSet = new vis.DataSet(rawGraphData.nodes || []);
                edgesDataSet = new vis.DataSet(rawGraphData.edges || []);

                const networkOptions = {{
                    nodes: {{
                        shape: 'dot',
                        font: {{
                            size: 11,
                            color: '#f0f6fc',
                            face: 'Segoe UI, Tahoma',
                            strokeWidth: 3,
                            strokeColor: '#05070b'
                        }},
                        borderWidth: 2,
                        shadow: {{ enabled: true, color: 'rgba(0,0,0,0.8)', size: 10 }}
                    }},
                    edges: {{
                        arrows: {{ to: {{ enabled: true, scaleFactor: 0.55 }} }},
                        smooth: {{ type: 'continuous', roundness: 0.4 }},
                        selectionWidth: 3
                    }},
                    physics: {{
                        solver: 'barnesHut',
                        barnesHut: {{
                            gravitationalConstant: -8500,
                            centralGravity: 0.015,
                            springLength: 220,
                            springConstant: 0.03,
                            damping: 0.28,
                            avoidOverlap: 1
                        }},
                        stabilization: {{ iterations: 200 }}
                    }},
                    interaction: {{ hover: true, tooltipDelay: 150, zoomView: true }}
                }};

                cosmicNetwork = new vis.Network(container, {{ nodes: nodesDataSet, edges: edgesDataSet }}, networkOptions);

                cosmicNetwork.on("click", function (params) {{
                    if (params && params.nodes && params.nodes.length > 0) {{
                        const nodeData = (rawGraphData.nodes || []).find(n => n.id === params.nodes[0]);
                        if (nodeData) openDrawer(nodeData);
                    }} else {{
                        closeDrawer();
                    }}
                }});
            }}
        }} catch(eNet) {{
            console.warn("cosmicNetwork initialization deferred or non-critical:", eNet);
        }}

        function openDrawer(nodeData) {{
            if (!drawer || !nodeData) return;
            if (drawerTitle) drawerTitle.innerText = nodeData.label || '';
            if (drawerMeta) {{
                drawerMeta.innerHTML = `
                    <span class="meta-tag">🏷️ ${{nodeData.category || ''}}</span>
                    <span class="meta-tag">🔗 ${{nodeData.degree || 0}} روابط</span>
                    ${{((nodeData.tags || [])).map(t => `<span class="meta-tag">#${{t}}</span>`).join('')}}
                `;
            }}
            if (drawerBody) {{
                if (typeof marked !== 'undefined') {{
                    drawerBody.innerHTML = marked.parse(nodeData.body || nodeData.snippet || 'لا يوجد محتوى.');
                }} else {{
                    drawerBody.innerText = nodeData.body || nodeData.snippet || 'لا يوجد محتوى.';
                }}
            }}
            if (drawerConns) {{
                const connectedIds = cosmicNetwork ? cosmicNetwork.getConnectedNodes(nodeData.id) : [];
                drawerConns.innerHTML = connectedIds.map(cid => {{
                    const targetNode = (rawGraphData.nodes || []).find(n => n.id === cid);
                    const lbl = targetNode ? targetNode.label : cid;
                    return `<span class="conn-pill" onclick="focusOnNode('${{cid}}')">${{lbl}}</span>`;
                }}).join('');
            }}
            drawer.classList.add('open');
            highlightNeighborhood(nodeData.id);
        }}

        function closeDrawer() {{
            if (drawer) drawer.classList.remove('open');
            resetFocus();
        }}

        function highlightNeighborhood(nodeId) {{
            if (!cosmicNetwork || !nodesDataSet || !edgesDataSet) return;
            const connectedNodes = new Set(cosmicNetwork.getConnectedNodes(nodeId));
            connectedNodes.add(nodeId);
            const connectedEdges = new Set(cosmicNetwork.getConnectedEdges(nodeId));

            nodesDataSet.forEach(node => {{
                if (connectedNodes.has(node.id)) {{
                    nodesDataSet.update({{ id: node.id, opacity: 1, font: {{ color: '#ffffff' }} }});
                }} else {{
                    nodesDataSet.update({{ id: node.id, opacity: 0.12, font: {{ color: 'rgba(255,255,255,0.1)' }} }});
                }}
            }});
            edgesDataSet.forEach(edge => {{
                if (connectedEdges.has(edge.id)) {{
                    edgesDataSet.update({{ id: edge.id, color: {{ color: '#00f0ff', opacity: 1 }}, width: 2.5 }});
                }} else {{
                    edgesDataSet.update({{ id: edge.id, color: {{ color: 'rgba(255,255,255,0.03)' }}, width: 0.5 }});
                }}
            }});
        }}

        function resetFocus() {{
            if (!nodesDataSet || !edgesDataSet) return;
            nodesDataSet.forEach(node => nodesDataSet.update({{ id: node.id, opacity: 1, font: {{ color: '#f0f6fc' }} }}));
            edgesDataSet.forEach(edge => edgesDataSet.update({{ id: edge.id, color: {{ color: 'rgba(90, 105, 120, 0.35)' }}, width: 1.3 }}));
        }}

        function focusOnNode(nodeId) {{
            const nodeData = (rawGraphData.nodes || []).find(n => n.id === nodeId);
            if (!nodeData) return;
            if (cosmicNetwork) cosmicNetwork.focus(nodeId, {{ scale: 1.25, animation: {{ duration: 600 }} }});
            openDrawer(nodeData);
        }}

        function filterGraphCategory(catName) {{
            activeGraphCategory = catName;
            document.querySelectorAll('.filter-pill').forEach(btn => {{
                btn.classList.toggle('active', btn.innerText.includes(catName) || (catName === 'ALL' && btn.innerText.includes('الكل')));
            }});

            if (!nodesDataSet) return;
            if (catName === 'ALL') {{
                nodesDataSet.forEach(n => nodesDataSet.update({{ id: n.id, hidden: false }}));
            }} else {{
                nodesDataSet.forEach(n => {{
                    nodesDataSet.update({{ id: n.id, hidden: (n.category !== catName) }});
                }});
            }}
            if (cosmicNetwork) cosmicNetwork.fit({{ animation: true }});
        }}

        try {{
            const searchInput = document.getElementById('graph-search-input');
            if (searchInput) {{
                searchInput.addEventListener('input', function(e) {{
                    const query = e.target.value.toLowerCase().trim();
                    if (!nodesDataSet) return;
                    if (!query) {{
                        if (activeGraphCategory === 'ALL') {{
                            nodesDataSet.forEach(n => nodesDataSet.update({{ id: n.id, hidden: false }}));
                        }} else {{
                            filterGraphCategory(activeGraphCategory);
                        }}
                        return;
                    }}
                    let firstMatch = null;
                    nodesDataSet.forEach(node => {{
                        const match = (node.label && node.label.toLowerCase().includes(query)) || 
                                      (node.id && node.id.toLowerCase().includes(query)) ||
                                      (node.tags && node.tags.some(t => t.toLowerCase().includes(query))) ||
                                      (node.category && node.category.toLowerCase().includes(query));
                        nodesDataSet.update({{ id: node.id, hidden: !match }});
                        if (match && !firstMatch) firstMatch = node.id;
                    }});
                    if (firstMatch && cosmicNetwork) cosmicNetwork.focus(firstMatch, {{ scale: 1.1, animation: true }});
                }});
            }}
        }} catch(eSearch) {{
            console.warn("graph-search-input listener non-critical:", eSearch);
        }}

        let cosmicPhysicsRunning = true;
        function toggleCosmicPhysics() {{
            if (!cosmicNetwork) return;
            cosmicPhysicsRunning = !cosmicPhysicsRunning;
            cosmicNetwork.setOptions({{ physics: {{ enabled: cosmicPhysicsRunning }} }});
            const btn = document.getElementById('physics-toggle-btn');
            if (btn) btn.innerHTML = cosmicPhysicsRunning ? '⏸ تثبيت الحركة' : '▶ تحريك الأجرام';
        }}

        // CHAKRAS & PROPHETIC BODILY CENTRES DATA (GLOBAL CIVILIZATIONAL SYNTHESIS)
        var CHAKRAS_DATA = window.CHAKRAS_DATA = [
            {{
                id: 8,
                name: "الهالة المحيطة الكبرى (The Auric Field / الحقيقة المحمدية)",
                sanskrit: "أورا براكاشا (Aura Prakasha) • النور الأكبر المحيط",
                sufiLatifa: "اللطيفة الأحدية / مقام العرش الأطلس وسدرة المنتهى",
                colorName: "النور الأبيض اللؤلؤي المتوهج بالذهب الأثيري (White & Gold)",
                colorHex: "#ffffff",
                prophet: "النبي الخاتم محمد صلى الله عليه وسلم (الحقيقة المحمدية)",
                sphere: "فلك العرش الكلي المحيط الأكبر ما وراء السماوات السبع",
                metal: "الأثير الكوني الخالص (الجوهر الفرد / Quintessence)",
                organ: "الحقل الحيوي الكهرومغناطيسي الشامل المحيط بالجسد والروح",
                freqHz: "963 Hz / 432 Hz",
                gland: "منظومة التزامن الهرموني العصبي الشامل (Endocrine Axis)",
                plexus: "الحقل الكهرومغناطيسي الحلقي (Biofield Torus)",
                dantian: "حقل الوي تشي المحيط الأكبر (Wei Qi Protective Field)",
                bija: "AUM / كُنْ (The Creative Word)",
                sefirot: "عين صوف (Ein Sof / النور اللانهائي المحيط بالشجرة)",
                quran: "«وَإِنَّكَ لَعَلَىٰ خُلُقٍ عَظِيمٍ» [القلم: 4] • «ثُمَّ دَنَا فَتَدَلَّىٰ * فَكَانَ قَابَ قَوْسَيْنِ أَوْ أَدْنَىٰ» [النجم: 8-9] • «يَا أَيُّهَا النَّبِيُّ إِنَّا أَرْسَلْنَاكَ شَاهِدًا وَمُبَشِّرًا وَنَذِيرًا * وَدَاعِيًا إِلَى اللَّهِ بِإِذْنِهِ وَسِرَاجًا مُّنِيرًا» [الأحزاب: 45-46].",
                shift: "وعي الكمال الإنساني الجامع (الإنسان الكامل): ختام النبوات، جمع دائرة البروج الاثني عشر والمقامات السبعة في نقطة التوحيد المطلق، والتحول من التشتت في العوالم المخلوقة إلى مقام السراج المنير الذي يفيض الرحمة الشاملة على الأكوان أجمعين.",
                proof: "«فص حكمة فردية في كلمة محمدية» — ابن عربي في الفصوص: الحقيقة المحمدية هي الفلك المحيط الأعظم وأول التعينات النورانية، وبها انشقت الأكوان وتنزلت سائر المقامات والنبوات.",
                vedic_kundalini: "في فلسفة اليوغا المتقدمة، يُعرف هذا الحقل بـ (Aura / Koshas الخمسة المحيطة). إنه الغلاف النوراني الأسمى (Anandamaya Kosha - غلاف الغبطة الأبدية) المحيط بكامل الهيكل، حيث تتلاشى ثنائية الرائي والمرئي ويتحقق طور الانعتاق (Moksha) في محيط الوعي الكوني الواحد.",
                chinese_tao: "في الخيمياء الطاوية الداخلية (Neidan)، يمثل هذا المستوى طور «العودة إلى الفراغ العظيم» (Lian Shen Huan Xu). تمثل الهالة طاقة «الوي تشي» (Wei Qi) المنقاة لأقصى درجاتها، حيث تتحد قوى الجوهر (Jing) والطاقة (Qi) والروح (Shen) في مجال كروي يحمي الهيكل الإنساني.",
                neuro_endocrine: "في الفيزياء الحيوية والتشريح العصبي المتقدم، يولد القلب والدماغ حقلاً كهرومغناطيسياً حلقياً (Toroidal Biofield) يمتد لأمتار خارج الجلد. في حالات التبتل والمحبة، يحدث تناغم تام (Heart-Brain Coherence) مع سيطرة موجات غاما عالية التزامن (>40 Hz).",
                sufi_sefirot: "في العرفان المقارن (الجيلي والسمناني)، تقابل هذه الهالة «اللطيفة الأحدية» ومقام «قاب قوسين». وفي القبالاه العتيقة، تطابق «أور عين صوف» (Ohr Ein Sof - النور المنبثق من اللانهائي) الذي يسبق انبثاق السفيرات العشر ويحويها جميعاً في كينونته."
            }},
            {{
                id: 7,
                name: "شاكرا التاج (Sahasrara - ساهاسرارا / زهرة اللوتس)",
                sanskrit: "ساهاسرارا (Sahasrara) • اللوتس ذات الألف بتلة",
                sufiLatifa: "لطيفة سر السر (Sirr al-Sirr) • الخفاء والتوحid الصرف",
                colorName: "البنفسجي الملكي المتوج بالأبيض النقي الشفاف (Violet & White)",
                colorHex: "#a855f7",
                prophet: "النبي إبراهيم الخليل عليه السلام (إمام الحنفاء)",
                sphere: "فلك زحل (السماء السابعة عند البيت المعمور)",
                metal: "الرصاص العتيق (Lead - Pb) • سر التحول الخيميائي",
                organ: "قبة الجمجمة واليافوخ، الغدة الصنوبرية، القشرة المخية العليا",
                freqHz: "963 Hz / 147.85 Hz",
                gland: "الغدة الصنوبرية (Pineal Gland) • سيدة الإيقاع الحيوي والميلاتونين",
                plexus: "القشرة الدماغية والشبكة العصبية المركزية (Cerebral Cortex)",
                dantian: "الدانتيان العلوي الأسمى (نقطة بايهوي GV-20 ملتقى المائة مسار)",
                bija: "OM / الصمت الأبدي (Silent AUM)",
                sefirot: "سفيرة التاج (Keter - كيتر / الإرادة الإلهية الباطنة)",
                quran: "«إِنِّي وَجَّهْتُ وَجْهِيَ لِلَّذِي فَطَرَ السَّمَاوَاتِ وَالْأَرْضَ حَنِيفًا وَمَا أَنَا مِنَ الْمُشْرِكِينَ» [الأنعام: 79] • كسر أصنام الكواكب والرسوخ التام عند البيت المعمور في السماء السابعة.",
                shift: "وعي التوحيد المفارق والصمت الأبدي: التجرد المطلق من التعلق بالصور والوسائط والأصنام العقلية، ملامسة مكعب التوحيد الخالص (الكعبة المشرفة)، وفناء الأوهام والظنون في شهود قيومية الحق.",
                proof: "«فص حكمة مهيمية في كلمة إبراهيمية» — ابن عربي في الفصوص: إبراهيم سُمي خليلاً لتخلل محبة الحق جميع ذرات كيانه، ومقامه الفلك السابع زحل لأنه فلك الصمت الأبدي والتجرد وبناء البيت المعمور.",
                vedic_kundalini: "تعد ساهاسرارا تاج الكونداليني ومقر الشيفا (Shiva - الوعي الخالص). باختراق طاقة الشاكتي للبتلات الألف، يختبر السالك طور (السامادهي - Samadhi)، حيث يزول وهم الانفصال ويسيل رحيق الخلود الأثيري (Amrita) من قمة الرأس مغذياً الجسد.",
                chinese_tao: "في الطب الصيني والكيغونغ، تسمى قمة الرأس «بايهوي» (Baihui GV-20 - مجمع المئات)، وهي بوابة تلقي طاقة يانغ السماوية (Tian Qi). هنا يكتمل استقرار «الجنين الخالد» (Shengtai) في الدانتيان العلوي وتتحول طاقة الروح (Shen) إلى سكينة صافية.",
                neuro_endocrine: "ترتبط تشريحياً بالغدة الصنوبرية (Pineal Gland) التي تفرز الميلاتونين وتتحكم في الإيقاع اليومي (Circadian Rhythm) وإنتاج جزيئات البصيرة الداخلية. يظهر تخطيط الدماغ في هذه الحالة نمط موجات ثيتا ودلتا متزامنة وبطفرات هدوء عصبي عميقة.",
                sufi_sefirot: "يقابل هذا المركز في سلم السمناني «اللطيفة الخفية» وعند الجيلي «سر السر». وفي شجرة السفيرات، يتطابق مع سفيرة (كيتر Keter - التاج الأسمى) التي تمثل النقطة الأولى لفيض النور الإلهي من الغيب المطلق إلى عوالم الإمكان."
            }},
            {{
                id: 6,
                name: "شاكرا العين الثالثة (Ajna - آجنا / مركز البصيرة)",
                sanskrit: "آجنا (Ajna) • مركز الأمر والبصيرة اللدنية الكلية",
                sufiLatifa: "لطيفة الأخفى (Al-Akhfa) • البصيرة اللدنية والسر المصون",
                colorName: "الأزرق النيلي العميق المشع (Deep Indigo Blue)",
                colorHex: "#3b82f6",
                prophet: "النبي موسى وهارون عليهما السلام (الكليم والشريعة الإلهية)",
                sphere: "فلك المشتري (السماء السادسة) • فلك العدالة والرحمة والحكمة الكلية",
                metal: "القصدير (Tin - Sn) • معدن الاتساع والعدل",
                organ: "الجبهة بين الحاجبين، الغدة النخامية، العينان والأعصاب البصرية",
                freqHz: "852 Hz / 183.58 Hz",
                gland: "الغدة النخامية (Pituitary Gland) • سيدة الغدد الصماء والمتحكمة بالهرمونات",
                plexus: "الضفيرة السباتية والكهفية (Carotid & Cavernous Plexus)",
                dantian: "الدانتيان العلوي (Shang Dantian - قصر نيوان / Niwan Palace)",
                bija: "KSHAM / AUM (أوم الحكيمة)",
                sefirot: "سفيرتا الحكمة والفهم (Chokhmah & Binah - البصيرة والتمييز)",
                quran: "«وَلَمَّا جَاءَ مُوسَىٰ لِمِيقَاتِنَا وَكَلَّمَهُ رَبُّهُ» [الأعراف: 143] • «وَكَتَبْنَا لَهُ فِي الْأَلْوَاحِ مِن كُلِّ شَيْءٍ مَّوْعِظَةً وَتَفْصِيلًا لِّكُلِّ شَيْءٍ» [الأعراف: 145].",
                shift: "وعي البصيرة الكلية وتنزيل الناموس: الترفع عن الرؤية البصرية الحسية المحدودة إلى الرؤية الباطنية اللدنية، استيعاب قوانين العدل والقدر، وإدراك حكمة التشريع وتسيير مآلات الأمم قبل وقوعها.",
                proof: "«فص حكمة علوية في كلمة هارونية» وفص الحكمة الإمامية الموسوية — ابن عربي: الجمع بين نور البصيرة المشترية التشريعية وحكمة تدبير الأمة بالحق المبين.",
                vedic_kundalini: "تتكون شاكرا آجنا من بتلتين تماثلان التقاء القناتين القمريتين والشمسيتين (Ida & Pingala) في مسار الشوشومنا. هنا تتجاوز الذات ثنائية العقل وتتحقق رؤية النور الأزرق (Nila Bindu) المعبر عن الحكمة اللدنية الفائقة للحواس.",
                chinese_tao: "في الطب الصيني، يقع هذا المركز في قصر «نيوان» (Niwan Palace) ونقطة «يينتانغ» (Yintang EX-HN3). وهو مستقر طاقة الروح (Shen). عندما يصفو هذا المركز من شوائب القلق تنفتح «عين السماء» (Tian Mu) التي تكشف بواطن الأمور.",
                neuro_endocrine: "تطابق شاكرا آجنا الغدة النخامية (Pituitary Gland) المرتبطة بالمهاد (Hypothalamus) عبر المحور النخامي (HPA Axis). يتحكم هذا المركز في التوازنات الهرمونية، ويمثل فسيولوجياً جسر الترجمة بين الوعي العصبي والإفراز الكيميائي.",
                sufi_sefirot: "تقابل «لطيفة الأخفى» الموصوفة بالنور الأزرق الصافي. وفي القبالاه الهرمسية، تقابل اقتران سفيرة الحكمة (Chokhmah) بسفيرة الفهم (Binah) خلف حجاب المعرفة (Da'at)، رمزاً لاكتمال الإدراك العقلي الروحي الشامل."
            }},
            {{
                id: 5,
                name: "شاكرا الحنجرة والنطق (Vishuddha - فيشودها / الكلمة النافذة)",
                sanskrit: "فيشودها (Vishuddha) • النقاء والتطهير بالتردد الصوتي",
                sufiLatifa: "لطيفة الخفي (Al-Khafi) • سر النطق والكلمة التكوينية",
                colorName: "الأزرق الفيروزي السماوي الرائق (Sky Turquoise Cyan)",
                colorHex: "#00f0ff",
                prophet: "النبي داود وسليمان عليهما السلام (صهر الحديد ومزامير التسبيح)",
                sphere: "فلك المريخ (السماء الخامسة) • فلك الشدة والبأس ونفوذ التردد الصوتي",
                metal: "الحديد (Iron - Fe) • «وَأَلَنَّا لَهُ الْحَدِيدَ»",
                organ: "الحنجرة، الحبال الصوتية، الغدة الدرقية وجارات الدرقية، الرقبة",
                freqHz: "741 Hz / 144.72 Hz",
                gland: "الغدة الدرقية وجارات الدرقية (Thyroid & Parathyroid) • منظمات الأيض والكالسيوم",
                plexus: "الضفيرة البلعومية والعنقية (Pharyngeal & Cervical Plexus)",
                dantian: "نقطة تيانتو (Tiantu CV-22) ومسار الرين ماي (Ren Mai الحلقي)",
                bija: "HAM (هام المنقية الصافية)",
                sefirot: "سفيرة الجبوراه (Gevurah - القوة والفرقان والصرامة الحقة)",
                quran: "«يَا جِبَالُ أَوِّبِي مَعَهُ وَالطَّيْرَ ۖ وَأَلَنَّا لَهُ الْحَدِيدَ» [سبأ: 10] • «وَشَدَدْنَا مُلْكَهُ وَآتَيْنَاهُ الْحِكْمَةَ وَفَصْلَ الْخِطَابِ» [ص: 20].",
                shift: "وعي الكلمة النافذة وسلطان الحق: تسخير الاهتزاز الصوتي والتسبيح لإعادة تشكيل المادة الكثيفة (تليين الحديد)، قول الحق بشجاعة لا تعرف المواربة، وتطابق النطق البشري مع الأمر الإلهي التكويني.",
                proof: "«رسائل إخوان الصفا»: النغمات الصوتية الموزونة تحاكي نغمات حركات الأفلاك وتحدث اهتزازاً أثيرياً يفكك كثافة المواد ويطهر النفوس من كدورات الطبيعة.",
                vedic_kundalini: "تمتلك فيشودها 16 بتلة تمثل الحروف الصوتية السنسكريتية وعنصرها الأثير الكوني (Akasha). هنا يتم تطهير السالك من سموم الكذب والرياء، ويولد صوت الحقيقة الصادق وتتحقق موهبة (Vak Siddhi - صدق الكلمة ونفوذها في الواقع).",
                chinese_tao: "في الطب الصيني، تمر بالحلق مسارات هامة كنهر التشي الأمامي (Ren Mai). تعتبر نقطة «تيانتو» صمام تنفيس طاقة الرئة والقلب؛ وإذا كُتم التعبير احتقن تشي الكبد مسبباً «عقدة البرقوق» (Mei He Qi). طهارة هذا المركز تضمن سلاسة التعبير.",
                neuro_endocrine: "ترتبط بالغدة الدرقية (Thyroid) المفرزة للثيروكسين (T4 و T3) المتحكمين بالأيض وإنتاج الطاقة الحيوية. عصبياً، يغذيها العصب المبهم (Vagus Nerve) عبر الفرع الحنجري، وهو أساس استجابة التعبير الصوتي والتنفس الهادئ.",
                sufi_sefirot: "تقابل «لطيفة الخفي» المرتبطة بسر النطق والكلمة. وفي شجرة السفيرات، تتناظر مع (جبوراه Gevurah - القوة والفرقان الإلهي الحاكم)، حيث تكون الكلمة سيفاً فاصلاً بين الحق والباطل."
            }},
            {{
                id: 4,
                name: "شاكرا القلب والصدر (Anahata - أناهاتا / شمس الروح والمحبة)",
                sanskrit: "أناهاتا (Anahata) • الصوت الذي لا يُقرع • المركز الكوني التكاملي",
                sufiLatifa: "لطيفة السر (Al-Sirr) • شمس الروح والمحبة والفيض الرحماني",
                colorName: "الأخضر الزمردي المتألق بنور الذهب الشمسي (Emerald & Solar Gold)",
                colorHex: "#10b981",
                prophet: "السيد المسيح عيسى عليه السلام والنبي إدريس (المحبة والرفع)",
                sphere: "فلك الشمس (السماء الرابعة) • قلب المنظومة الكونية وميزان الاعتدال",
                metal: "الذهب الخالص (Gold - Au) • معدن الكمال والضياء",
                organ: "القلب العضوي، الغدة الزعترية (Thymus)، الرئتان، مركز الصدر",
                freqHz: "639 Hz / 126.22 Hz / 528 Hz",
                gland: "الغدة الزعترية / التيموس (Thymus Gland) • حصن المناعة وتمييز الخلايا التائية",
                plexus: "الضفيرة القلبية الرئوية (Cardiac & Pulmonary Plexus)",
                dantian: "الدانتيان الأوسط (Zhong Dantian - نقطة شانزونغ CV-17)",
                bija: "YAM (يام المحبة الكونية)",
                sefirot: "سفيرة التيفئيريت (Tiferet - الجمال والتناغم والمركز القلبي النابض)",
                quran: "«وَآتَيْنَا عِيسَى ابْنَ مَرْيَمَ الْبَيِّنَاتِ وَأَيَّدْنَاهُ بِرُوحِ الْقُدُسِ» [البقرة: 87] • «وَرَفَعْنَاهُ مَكَانًا عَلِيًّا» [مريم: 57] • «أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ» [الرعد: 28].",
                shift: "وعي شمس الروح والمحبة غير المشروطة: ولادة الإنسان الروحي الجديد في باطن الهيكل، التحرر من حرفية الناموس القاتلة لصالح روح الإحياء والنفخة الإلهية، وتحقيق التوازن الذهبي بين عوالم السماء والأرض.",
                proof: "«فص حكمة روحية في كلمة عيسوية» — ابن عربي في الفصوص: عيسى هو النفس الإلهي النازل بالروح، مقامه فلك الشمس الذي يمد سائر الكواكب بالحياة والنور، كمد القلب للأعضاء بالحياة.",
                vedic_kundalini: "تتكون أناهاتا من 12 بتلة وعنصرها الهواء (Vayu)، وفي مركزها الينترا السداسية الجامعة لمثلث النور ومثلث المادة. هي الجسر الحرج بين الشاكرات الأرضية الثلاث والشاكرات العلوية الثلاث، ومستقر الصوت الصامت الأزلي (Anahata Nada).",
                chinese_tao: "في الطب الصيني، القلب هو «الإمبراطور الأعظم» (Jun Zhu) الذي يستقر فيه الشين (Shen). والمركز هو الدانتيان الأوسط عند نقطة «شانزونغ» (CV-17). إذا عم السلام هذا المركز سكنت العواطف وصفت البصيرة الداخلية.",
                neuro_endocrine: "يحتوي القلب على أكثر من 40,000 خلية عصبية تشكل «دماغ القلب» (Heart Brain)، ويفرز هرموني الأوكسيتوسين وANP. ينتج نبض القلب حقلاً كهرومغناطيسياً أقوى بآلاف المرات من الدماغ، وهو مركز التناغم الفسيولوجي التام (Heart Coherence).",
                sufi_sefirot: "تطابق «لطيفة السر» والقلب الصوفي الحقيقي مظهر الأنوار. وفي شجرة السفيرات، تتطابق حرفياً مع (تيفئيريت Tiferet - الجمال والتناغم) المحتلة للمركز الدقيق للشجرة والجامعة بين الرحمة (Chesed) والشدة (Gevurah)."
            }},
            {{
                id: 3,
                name: "شاكرا الضفيرة الشمسية (Manipura - مانيبورا / مدينة الجواهر)",
                sanskrit: "مانيبورا (Manipura) • مدينة الجواهر والحرارة والتحويل",
                sufiLatifa: "لطيفة القلب الظاهر / النفس المطمئنة وسيادة الإرادة",
                colorName: "الأصفر الشمسي الذهبي المتوهج (Solar Golden Yellow)",
                colorHex: "#f59e0b",
                prophet: "النبي يوسف الصديق عليه السلام (جمال الملك وتأويل الرؤى)",
                sphere: "فلك الزهرة (السماء الثالثة) • فلك الجمال والتناغم والتدبير الحكيم",
                metal: "النحاس (Copper - Cu) • موصل الطاقة والحرارة",
                organ: "فم المعدة، الكبد، البنكرياس، الطحال، الجهاز الهضمي والتمثيل الغذائي",
                freqHz: "528 Hz / 221.23 Hz",
                gland: "البنكرياس (Pancreas) والجزر اللانغرهانسية • منظم السكر وطاقة الأيض",
                plexus: "الضفيرة الشمسية والبطنية (Celiac & Solar Plexus)",
                dantian: "منطقة البطن العلوي (Zhongwan CV-12) وموقد الهضم الأوسط",
                bija: "RAM (رام النارية المحولة)",
                sefirot: "سفيرتا النيتساخ والهود (Netzach & Hod - النصر والمجد وتدبير القوى)",
                quran: "«إِنِّي رَأَيْتُ أَحَدَ عَشَرَ كَوْكَبًا وَالشَّمْسَ وَالْقَمَرَ رَأَيْتُهُمْ لِي سَاجِدِينَ» [يوسف: 4] • «قَالَ اجْعَلْنِي عَلَىٰ خَزَائِنِ الْأَرْضِ ۖ إِنِّي حَفِيظٌ عَلِيمٌ» [يوسف: 55].",
                shift: "وعي السيادة وتسامي الرغبات الحسية: تحويل إرادة القوة والأطماع الدنيوية إلى بهاء حكم وحفظ موارد، العفة أمام المغريات العاصفة، والتمكن من إدارة خزائن الأرض بعلم وحكمة وتأويل الرؤى.",
                proof: "«فص حكمة نورية في كلمة يوسفية» — ابن عربي في الفصوص: يوسف تجلت له معاني الغيب متجسدة في عالم المثال، فتحكم في رغبات النفس وتسامى بها حتى سجدت له عوالم التدبير.",
                vedic_kundalini: "تمتلك مانيبورا 10 بتلات وعنصرها النار (Agni). هي محرك الاستقلاب والتحويل الحراري في الجسد (Samana Vayu). عند استنارتها، يمتلك السالك عزيمة فولاذية وشجاعة ذاتية، وتتحول رغبات الأنا إلى رغبة في خدمة الخير الكلي.",
                chinese_tao: "في الطب الصيني، تمثل هذه المنطقة «الموقد الأوسط» (Middle Sanjiao) الذي يحكمه الطحال والمعدة (عنصر الأرض). وهي المسؤولة عن تحويل الغذاء إلى «تشي مكتسب» (Gu Qi). صفاء هذا المركز يمنح الذهن ثقة وقدرة على الهضم الفكري للأحداث.",
                neuro_endocrine: "تتطابق مع الضفيرة الشمسية (Celiac Plexus) المسماة «الدماغ البطني»، وتتحكم بإفراز الأنسولين والجلوكاجون وإنزيمات الكبد الهضمية. هذا المركز هو بؤرة استجابة الكر والفر (Fight or Flight) واستقرار هرمونات التوتر كالكورتيزول.",
                sufi_sefirot: "ترتبط في العرفان بانتقال النفس من أمارة إلى لوامة ثم مطمئنة مستقرة. وفي السفيرات، تقابل محوري (نيتساخ وهود Netzach & Hod) اللذين يمثلان التناغم التنفيذي والنصر العملي في المادة."
            }},
            {{
                id: 2,
                name: "شاكرا العجز والرحم المائي (Svadhisthana - سفاديستانا / سفينة النجاة)",
                sanskrit: "سفاديستانا (Svadhisthana) • المستقر الذاتي والرحم المائي",
                sufiLatifa: "لطيفة النفس (Al-Nafs) • التطهير من طوفان الشهوات وفلك النجاة",
                colorName: "البرتقالي المتوهج الدافئ (Vibrant Radiant Orange)",
                colorHex: "#f97316",
                prophet: "النبي نوح عليه السلام (شيخ أولي العزم وفلك النجاة في الطوفان)",
                sphere: "فلك عطارد والماء الكوني • فلك الفلك المشحون والتدفق والذكاء التكيفي",
                metal: "الزئبق المائي (Quicksilver - Hg)",
                organ: "أسفل السرة، الحوض، الرحم والمبيضان / الخصيتان، المثانة، الكليتان",
                freqHz: "417 Hz / 141.27 Hz",
                gland: "الغدد التناسلية (Gonads / Testes & Ovaries) • صانعة الهرمونات الجنسية والإخصاب",
                plexus: "الضفيرة الخثلية والعجزية (Hypogastric & Sacral Plexus)",
                dantian: "الدانتيان السفلي الحيوي (Xia Dantian - نقطة غوانيوان CV-4)",
                bija: "VAM (فام المائية المطهرة)",
                sefirot: "سفيرة الييسود (Yesod - الأساس والأسمنت الرابط للفيض الإلهي)",
                quran: "«وَاصْنَعِ الْفُلْكَ بِأَعْيُنِنَا وَوَحْيِنَا» • «حَتَّىٰ إِذَا جَاءَ أَمْرُنَا وَفَارَ التَّنُّورُ قُلْنَا احْمِلْ فِيهَا مِن كُلٍّ زَوْجَيْنِ اثْنَيْنِ» [هود: 37-40] • «وَقِيلَ يَا أَرْضُ ابْلَعِي مَاءَكِ وَيَا سَمَاءُ أَقْلِعِي» [هود: 44].",
                shift: "وعي النجاة وحفظ بذور الفطرة: التطهير من طوفان المشاعر الغامرة والانفعالات النفسية المنفلتة، تشييد فلك العقل واليقين لحمل بذور الطهارة، والولادة الجديدة للإنسانية بعد انحسار ماء الهوى.",
                proof: "«فص حكمة سبوحية في كلمة نوحية» — ابن عربي في الفصوص: دعوة نوح جمعت بين التنزيه والتشبيه، وفلكه هو سر النجاة في بحار الهيولى وطوفان الكثرة لتطهير العالم المائي الباطني.",
                vedic_kundalini: "تمتلك سفاديستانا 6 بتلات وعنصرها الماء (Jala). هي خزان الطاقة الجنسية والإبداعية ومستودع الانطباعات الباطنية (Samskaras). عند تنقيتها، يتحول الانجذاب الحسي السفلي إلى طاقة إبداع وتدفق عاطفي راقٍ.",
                chinese_tao: "في الطاوية، هذا المركز هو موضع «الدانتيان السفلي» (Lower Dantian) ونقطة «غوانيوان» (CV-4 - بوابة الأصل). هنا يُخزن جوهر الحياة الأصلي (Yuan Jing). تبدأ ممارسة تدوير التشي (Microcosmic Orbit) بتسخين هذا الموقد لتحويل الجوهر إلى طاقة.",
                neuro_endocrine: "تتصل بالضفيرة الخثلية (Hypogastric Plexus) والغدد التناسلية المفرزة للإستروجين والبروجستيرون والتستوستيرون. يحكم هذا المركز وظائف التكاثر والاستجابة للذة والتوازن السائلي عبر الكلى والجهاز البولي.",
                sufi_sefirot: "تقابل مجاهدة النفس لترويض نوازعها الحيوانية والعبور بها إلى بر السلامة. وفي شجرة السفيرات، تتطابق مع (ييسود Yesod - الأساس) التي تجمع طاقات السفيرات العليا وتسكبها في العالم المادي السفلي (Malkuth)."
            }},
            {{
                id: 1,
                name: "شاكرا الجذر والقاعدة الأرضية (Muladhara - مولادارا / معبد التجسد)",
                sanskrit: "مولادارا (Muladhara) • الجذر والأساس الراسخ للوجود المادي",
                sufiLatifa: "لطيفة القالب والجسد الترابي (Al-Qalib) • سر الاستخلاف في الأرض",
                colorName: "الأحمر الياقوتي الأرضي العميق (Deep Grounding Ruby Red)",
                colorHex: "#ef4444",
                prophet: "النبي آدم عليه السلام (أبو البشرية وسر القبضة الترابية والأسماء)",
                sphere: "فلك القمر (السماء الأولى) • مجمع العناصر الأربعة وعالم التجسد والشهادة",
                metal: "الفضة والصلصال الترابي (Silver & Sacred Clay)",
                organ: "قاعدة العمود الفقري، العجان (Perineum)، العصعص، الساقان والقدمان والعظام",
                freqHz: "396 Hz / 210.42 Hz",
                gland: "الغدتان الكظريتان (Adrenal Glands) • مصنع الأدرينالين واستجابة البقاء",
                plexus: "الضفيرة العصعصية (Coccygeal Plexus)",
                dantian: "نقطة هويين (Huiyin CV-1 - ملتقى الين وقاع الجذع)",
                bija: "LAM (لام الأرضية الراسخة)",
                sefirot: "سفيرة الملكوت (Malkuth - التجلي المادي للأمر الإلهي على الأرض)",
                quran: "«وَإِذْ قَالَ رَبُّكَ لِلْمَلَائِكَةِ إِنِّي جَاعِلٌ فِي الْأَرْضِ خَلِيفَةً» [البقرة: 30] • «وَعَلَّمَ آدَمَ الْأَسْمَاءَ كُلَّهَا» [البقرة: 31] • «خَلَقَ الْإِنسَانَ مِن صَلْصَالٍ كَالْفَخَّارِ» [الرحمن: 14].",
                shift: "وعي التجسد والاستخلاف في الأرض: إدراك قدسية الهيكل الجسدي المادي كمعبد حامل للروح، التحرر الجذري من مخاوف الفناء والفقر والموت، وفك شفرة الأسماء الإلهية المودعة في طينة الخليقة.",
                proof: "«كتاب الإنسان الكامل» — عبد الكريم الجيلي: آدم عليه السلام هو النسخة الكاملة الأولى التي جمعت حقائق الأسماء الإلهية في قالب الطين، وقاعدته ترابية تنبثق منها سائر المعارج الروحية.",
                vedic_kundalini: "تمتلك مولادارا 4 بتلات تمثل أركان المادة وعنصرها الأرض (Prithvi). في قعرها تنام حية الكونداليني (Kundalini Shakti) ملتفة ثلاث لفات ونصف حول اللينغام. إيقاظ هذا المركز بالطهارة والاستقامة شرط أساسي لصعود الطاقة دون اختلال.",
                chinese_tao: "في الطب الصيني، ترتبط بنقطة «هويين» (Huiyin CV-1 - التقاء الين) وقناة الحاكم (Du Mai). وهي مقر طاقة الأرض (Di Qi) وبوابة تجذير الجسد مع كوكب الأرض لحفظ توازن طاقات اليانغ العلوية.",
                neuro_endocrine: "تتصل بالغدتين الكظريتين (Adrenal Glands) المفرزتين للأدرينالين والنورأدرينالين، والضفيرة العصعصية. هذا المركز هو المسؤول بيولوجياً عن غريزة البقاء الأساسية، والشعور بالأمان الحركي، وتكوين نقي العظام.",
                sufi_sefirot: "يقابل «لطيفة القالب» الترابي المأمور بتزكيته ليكون أهلاً لسكنى الروح القدسية. وفي شجرة السفيرات، يتطابق حرفياً مع (ملكوت Malkuth - المملكة)، المحطة الأرضية التي تتجلى فيها الإرادة الإلهية في عالم الأجسام."
            }}
        ];

        function renderChakras() {{
            const data = (typeof CHAKRAS_DATA !== 'undefined' && Array.isArray(CHAKRAS_DATA)) ? CHAKRAS_DATA : (window.CHAKRAS_DATA || []);
            if (!data || !data.length) return;

            // Populate Quick Selector Pills Bar
            const pillsBar = document.getElementById('chakra-pills-bar');
            if (pillsBar) {{
                pillsBar.innerHTML = data.map(c => `
                    <button class="c-pill-btn ${{c.id === 8 ? 'active' : ''}}" id="c-pill-${{c.id}}" onclick="selectChakra(${{c.id}})">
                        <span style="color:${{c.colorHex}};">●</span> ${{c.name.split('(')[0].trim()}}
                    </button>
                `).join('');
            }}

            // Populate Panoramic Comparative Matrix Table
            const tableBody = document.getElementById('panoramic-chakras-tbody');
            if (tableBody) {{
                tableBody.innerHTML = data.map(c => `
                    <tr>
                        <td><b style="color:${{c.colorHex}};">${{c.name.split('(')[0].trim()}}</b><br><span style="font-size:0.75rem; color:var(--text-muted);">${{c.sanskrit.split('•')[0].trim()}}</span></td>
                        <td><b style="color:#fff;">${{c.sufiLatifa.split('•')[0].trim()}}</b></td>
                        <td><span style="color:var(--gold); font-weight:700;">${{c.prophet.split('(')[0].trim()}}</span></td>
                        <td>${{c.sphere.split('(')[0].trim()}}</td>
                        <td><span class="badge-hz" style="background:rgba(148, 163, 184,0.12); color:var(--gold); border:1px solid rgba(148, 163, 184,0.3); padding:2px 8px; border-radius:10px; font-weight:700;">${{c.freqHz}}</span></td>
                        <td><b>${{c.gland.split('•')[0].trim()}}</b></td>
                        <td>${{c.plexus.split('(')[0].trim()}}</td>
                        <td>${{c.dantian.split('(')[0].trim()}}</td>
                        <td><span style="color:var(--cyan); font-weight:700;">${{c.bija.split('/')[0].trim()}}</span></td>
                        <td>${{c.sefirot.split('(')[0].trim()}}</td>
                        <td style="white-space:normal; min-width:240px; font-size:0.82rem; line-height:1.5;">${{c.shift}}</td>
                    </tr>
                `).join('');
            }}

            selectChakra(8);
        }}

        function selectChakra(id) {{
            const data = (typeof CHAKRAS_DATA !== 'undefined' && Array.isArray(CHAKRAS_DATA)) ? CHAKRAS_DATA : (window.CHAKRAS_DATA || []);
            const c = data.find(x => x.id === id);
            if (!c) return;

            // Sync Hologram SVG Node Buttons
            document.querySelectorAll('.chakra-point-btn').forEach(btn => btn.classList.remove('active'));
            const activeNode = document.getElementById('chakra-node-' + id);
            if (activeNode) activeNode.classList.add('active');

            // Sync Quick Selector Pills
            document.querySelectorAll('.c-pill-btn').forEach(btn => btn.classList.remove('active'));
            const activePill = document.getElementById('c-pill-' + id);
            if (activePill) activePill.classList.add('active');

            // Render Comprehensive Dossier
            const container = document.getElementById('chakra-detail-card');
            if (!container) return;
            container.innerHTML = `
                <div class="chakra-main-header">
                    <div class="chakra-names">
                        <h2><span style="color:${{c.colorHex}}; font-size:1.8rem;">●</span> ${{c.name}}</h2>
                        <div class="chakra-sub-names">${{c.sanskrit}} • <b>اللطيفة السلوكية:</b> ${{c.sufiLatifa}}</div>
                    </div>
                    <div class="chakra-prophet-badge">👑 ${{c.prophet}}</div>
                </div>

                <div class="chakra-specs-grid">
                    <div class="c-spec-item">
                        <div class="c-spec-label">الفلك الكوكبي والمقام السماوي</div>
                        <div class="c-spec-val">${{c.sphere}}</div>
                    </div>
                    <div class="c-spec-item">
                        <div class="c-spec-label">اللون والتردد بالهرتز (Hz)</div>
                        <div class="c-spec-val" style="color:${{c.colorHex}};">${{c.colorName}} • ${{c.freqHz}}</div>
                    </div>
                    <div class="c-spec-item">
                        <div class="c-spec-label">المعدن الخيميائي وعضو الجسد</div>
                        <div class="c-spec-val">${{c.metal}} • ${{c.organ}}</div>
                    </div>
                    <div class="c-spec-item">
                        <div class="c-spec-label">الغدة الصماء المقابلة</div>
                        <div class="c-spec-val">${{c.gland}}</div>
                    </div>
                    <div class="c-spec-item">
                        <div class="c-spec-label">الضفيرة العصبية ومسار التشي</div>
                        <div class="c-spec-val">${{c.plexus}} • ${{c.dantian}}</div>
                    </div>
                    <div class="c-spec-item">
                        <div class="c-spec-label">صوت البذور (Bija) وسفيرة القبالاه</div>
                        <div class="c-spec-val">${{c.bija}} • ${{c.sefirot}}</div>
                    </div>
                </div>

                <div class="c-box quran-box" style="margin-bottom: 20px;">
                    <div class="c-step-badge c-step-quran">📖 الشاهد والسر القرآني الحاكم</div>
                    <div style="font-size:0.95rem; font-weight:600; line-height:1.8;">${{c.quran}}</div>
                </div>

                <!-- GLOBAL CIVILIZATIONAL CONSENSUS BOX -->
                <div class="global-consensus-box" style="margin-bottom: 20px;">
                    <div class="consensus-header">
                        <h4><i class="fa-solid fa-earth-americas"></i> الإجماع الحضاري والعلمي الشامل لهذا المركز الطاقي</h4>
                        <span style="font-size:0.78rem; color:var(--cyan); background:rgba(0,240,255,0.1); padding:3px 10px; border-radius:12px; border:1px solid rgba(0,240,255,0.25);">مضاهاة الشرق والغرب والطب الحديث</span>
                    </div>
                    <div class="consensus-grid">
                        <div class="civ-card">
                            <div class="civ-card-title">🇮🇳 الفيدا والكونداليني (Vedic Kundalini)</div>
                            <div class="civ-card-text">${{c.vedic_kundalini}}</div>
                        </div>
                        <div class="civ-card">
                            <div class="civ-card-title">🇨🇳 الخيمياء الصينية والطب الإمبراطوري (Taoism & TCM)</div>
                            <div class="civ-card-text">${{c.chinese_tao}}</div>
                        </div>
                        <div class="civ-card">
                            <div class="civ-card-title">🧬 التشريح العصبي والغدد الصماء (Neuro-Endocrine Axis)</div>
                            <div class="civ-card-text">${{c.neuro_endocrine}}</div>
                        </div>
                        <div class="civ-card">
                            <div class="civ-card-title">📜 اللطائف العرفانية وشجرة السفيرات (Sufi Lata'if & Hermetica)</div>
                            <div class="civ-card-text">${{c.sufi_sefirot}}</div>
                        </div>
                    </div>
                </div>

                <div class="chakra-deep-desc">
                    <div style="color:var(--gold); font-weight:700; margin-bottom:8px;">🌟 النقلة في الوعي الإنساني ومستوى الاستنارة الباطنية:</div>
                    ${{c.shift}}
                </div>

                <div class="chakra-proof-quote">
                    <strong>📜 الشاهد من أمهات المخطوطات والكتب (الفصوص / الكيباليون / إخوان الصفا / الجيلي / السمناني):</strong><br>
                    ${{c.proof}}
                </div>
            `;
        }}

        // 3. Spheres Ladder Renderer & Dossier Generator
        function renderSpheres() {{
            const data = (typeof SPHERES_DATA !== 'undefined' && Array.isArray(SPHERES_DATA)) ? SPHERES_DATA : (window.SPHERES_DATA || []);
            if (!data || !data.length) return;

            const listContainer = document.getElementById('spheres-list');
            if (listContainer) {{
                listContainer.innerHTML = data.map((s, idx) => `
                    <div class="sphere-card ${{idx === 0 ? 'active' : ''}}" 
                         style="--sphere-color: ${{s.color}}" 
                         onclick="selectSphere(${{s.id}})">
                        <div class="sphere-rank">${{s.id}}</div>
                        <div class="sphere-info">
                            <h3>${{s.name}}</h3>
                            <span>${{s.prophet}} • ${{s.metal}} • <b style="color:var(--gold);">${{s.freqHz ? s.freqHz.split(' ')[0] + ' Hz' : ''}}</b></span>
                        </div>
                    </div>
                `).join('');
            }}

            // Also render the panoramic matrix table
            const tableBody = document.getElementById('panoramic-spheres-tbody');
            if (tableBody) {{
                tableBody.innerHTML = data.map(s => `
                    <tr>
                        <td><b style="color:${{s.color}}">${{s.name}}</b></td>
                        <td>${{s.rank}}</td>
                        <td><b style="color:#fff;">${{s.prophet}}</b></td>
                        <td><span class="badge-hz">${{s.freqHz ? s.freqHz.split(' ')[0] + ' Hz' : s.note}}</span></td>
                        <td><b>${{s.metal}}</b></td>
                        <td>${{s.chakra}}</td>
                        <td>${{s.gland || '—'}}</td>
                        <td>${{s.angel || '—'}}</td>
                        <td style="white-space:normal; min-width:180px; font-size:0.8rem; line-height:1.4;">${{s.china_tao ? s.china_tao.split('•')[0] : '—'}}</td>
                        <td style="white-space:normal; min-width:180px; font-size:0.8rem; line-height:1.4;">${{s.vedic_india ? s.vedic_india.split('•')[0] : '—'}}</td>
                        <td style="white-space:normal; min-width:180px; font-size:0.8rem; line-height:1.4;">${{s.greek_phil ? s.greek_phil.split('•')[0] : '—'}}</td>
                        <td style="white-space:normal; min-width:180px; font-size:0.8rem; line-height:1.4;">${{s.kabbalah_enoch ? s.kabbalah_enoch.split('•')[0] : '—'}}</td>
                        <td style="white-space:normal; min-width:240px; font-size:0.82rem; line-height:1.5;">${{s.titleDesc}}</td>
                    </tr>
                `).join('');
            }}

            selectSphere(8);
        }}

        function selectSphere(id) {{
            const data = (typeof SPHERES_DATA !== 'undefined' && Array.isArray(SPHERES_DATA)) ? SPHERES_DATA : (window.SPHERES_DATA || []);
            const s = data.find(x => x.id === id);
            if (!s) return;
            document.querySelectorAll('.sphere-card').forEach(c => {{
                const r = c.querySelector('.sphere-rank');
                if (r) c.classList.toggle('active', r.innerText == id);
            }});
            const detailContainer = document.getElementById('sphere-detail');
            if (!detailContainer) return;
            detailContainer.innerHTML = `
                <div class="detail-header">
                    <div>
                        <h2>${{s.name}}</h2>
                        <div style="font-size:0.85rem; color:var(--text-muted); margin-top:4px;">${{s.patriarch || ''}}</div>
                    </div>
                    <div style="display:flex; gap:8px; align-items:center;">
                        <span class="detail-badge">${{s.rank}}</span>
                        <span class="badge-hz">${{s.freqHz ? s.freqHz.split(' ')[0] + ' Hz' : s.note}}</span>
                    </div>
                </div>

                <div class="prophet-banner">
                    <div class="prophet-avatar" style="background: linear-gradient(135deg, ${{s.color}}, #94a3b8);">👑</div>
                    <div class="prophet-desc">
                        <h4>${{s.prophet}}</h4>
                        <p>${{s.titleDesc}}</p>
                    </div>
                </div>

                ${{s.quran ? `
                <div class="quran-box">
                    <div style="font-size:0.8rem; color:var(--gold); margin-bottom:4px; font-weight:700;">﴿ المرتكز القرآني المحكم ﴾</div>
                    ${{s.quran}}
                </div>
                ` : ''}}

                ${{s.hadith ? `
                <div class="hadith-box">
                    <div class="hadith-box-header">
                        <i class="fa-solid fa-scroll"></i>
                        <span>نص حديث المعراج النبوي المسند (صحيح البخاري وصحيح مسلم):</span>
                    </div>
                    <div>${{s.hadith}}</div>
                </div>
                ` : ''}}

                ${{s.secret ? `
                <div class="secret-box">
                    <div class="secret-box-header">
                        <i class="fa-solid fa-gem"></i>
                        <span>السر العرفاني والباطني (الفتوحات المكية وفصوص الحكم):</span>
                    </div>
                    <div>${{s.secret}}</div>
                </div>
                ` : ''}}

                <div class="specs-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));">
                    <div class="spec-box"><div class="spec-label">الشاكرا واللطيفة الروحية</div><div class="spec-value">${{s.chakra}}</div></div>
                    <div class="spec-box"><div class="spec-label">الغدة الصماء المقابلة</div><div class="spec-value">${{s.gland || '—'}}</div></div>
                    <div class="spec-box"><div class="spec-label">المعدن الخيميائي الكوني</div><div class="spec-value">${{s.metal}}</div></div>
                    <div class="spec-box"><div class="spec-label">التردد الصوتي والمداري</div><div class="spec-value">${{s.freqHz || s.note}}</div></div>
                    <div class="spec-box"><div class="spec-label">الملاك الموكل بالسماء</div><div class="spec-value">${{s.angel || '—'}}</div></div>
                    <div class="spec-box"><div class="spec-label">المبدأ الهرمسي الكوني</div><div class="spec-value">${{s.hermetic}}</div></div>
                </div>

                ${{s.orbit ? `
                <div class="orbit-box">
                    <div class="orbit-box-header">
                        <i class="fa-solid fa-satellite"></i>
                        <span>الميكانيكا الفلكية والفيزياء المدارية (Kepler & Astrometry):</span>
                    </div>
                    <div>${{s.orbit}}</div>
                </div>
                ` : ''}}

                ${{s.china_tao || s.vedic_india || s.greek_phil || s.kabbalah_enoch ? `
                <div class="global-consensus-box">
                    <div class="consensus-header">
                        <h4><i class="fa-solid fa-earth-americas"></i> الإجماع الكوزمولوجي العالمي ومطابقة الحضارات الكبرى</h4>
                        <span style="font-size:0.78rem; color:var(--cyan); background:rgba(0,240,255,0.1); padding:3px 10px; border-radius:12px; border:1px solid rgba(0,240,255,0.25);">شهادة الشرق والغرب</span>
                    </div>
                    <div class="consensus-grid">
                        <div class="civ-card">
                            <div class="civ-card-title">🇨🇳 الصين والطاوية (Wuxing & Beidou)</div>
                            <div class="civ-card-text">${{s.china_tao || '—'}}</div>
                        </div>
                        <div class="civ-card">
                            <div class="civ-card-title">🇮🇳 الفيدا والهندوسية (Sapta Loka & Vedas)</div>
                            <div class="civ-card-text">${{s.vedic_india || '—'}}</div>
                        </div>
                        <div class="civ-card">
                            <div class="civ-card-title">🏛️ بابل وسومر واليونان (Mesopotamia & Hellenic)</div>
                            <div class="civ-card-text">${{s.babylon ? s.babylon + '<br>' : ''}}${{s.greek_phil || '—'}}</div>
                        </div>
                        <div class="civ-card">
                            <div class="civ-card-title">📜 الهرمسية وأخنوخ والقبالاه (Hermetica & Kabbalah)</div>
                            <div class="civ-card-text">${{s.kabbalah_enoch || '—'}}</div>
                        </div>
                    </div>
                </div>
                ` : ''}}

                <div style="margin-bottom: 20px; font-size: 0.95rem; line-height: 1.8; color: var(--text-main);">
                    <strong style="color:var(--gold); display:block; margin-bottom:6px;">التحليل المعرفي والتركيبي:</strong>
                    ${{s.desc}}
                </div>

                <div class="textual-proof">
                    <strong style="color:var(--cyan); display:block; margin-bottom:6px;">الشاهد والتوثيق من المخطوطات الأصلية:</strong>
                    ${{s.proof}}
                </div>
            `;
        }}

        // ========================================================
        // GRAND COSMIC ODYSSEY & CIVILIZATION SYNTHESIS (DATA & RENDERER)
        // ========================================================
        const ODYSSEY_STAGES = [
            {{
                id: 1,
                name: "البوابة الأولى: بوابة الفطرة ونشأة المادة وسماء آدم",
                badge: "السماء الأولى • فلك القمر • شاكرا الجذر (Muladhara) • الفضة والماء • 210.42 Hz",
                icon: "🌙",
                color: "#c0c0c0",
                essence: "هنا تلتقي بداية الوجود العيني للإنسان. نقطة التماس المباشرة بين عالم الأثير العلوي وقشرة الأرض المادية؛ حيث رأت كافة الأمم في القمر مرآة التحول والانعكاس الكوني، عاكسةً نور الشمس كما يعكس الجسد الطيني نفخة الروح الأزلية.",
                propheticScene: "في صحيح البخاري، لقي النبي ﷺ في السماء الأولى آدم عليه السلام؛ فرأى عن يمينه أسودة (أرواح بنيه السعداء) إذا نظر إليها ضحك واستبشر، وعن شماله أسودة (أرواح الأشقياء) إذا نظر إليها بكى حزناً. إنه مشهد الأصل الطيني الأول الذي تفرعت منه الخليقة كلها، واستقبال الأب الحنون لنبيه الخاتم: «مرحباً بالابن الصالح والنبي الصالح».",
                easternVeda: "في الصين الطاوية، يرتبط فلك القمر بعنصر الماء الأولي (Shui) ومبدأ 'الين' (Yin) الحاضن للحياة في الأرحام. وفي الفيدا، هذا الفلك هو 'بهور-لوكا' (Bhur-loka) وشاكرا الجذر 'مولادارا' (Muladhara) عنصر الأرض والصلصال، حيث تكمن الطاقة الحيوية في سباتها قبل أن تُبعث بنفخة الإيقاظ والوعي.",
                babylonHellenic: "في بابل، شُيدت قاعدة الزقورة مكسوة بصفائح الفضة تكريماً للإله 'سين' (Sin) حارس الأشهر وتدفق السوائل. وفي متون هرمس (Poimandres)، تسلّم الروح الصاعدة في فلك القمر 'طاقة التغير والانفعال والغرائز الحيوانية'، لتتطهر من الوهم الأرضي قبل ارتقاء العقل.",
                microcosmReflection: "في تكوينك، يقابل هذا الفلك العظم العصعصي، غدة الكظر، ونبض السوائل الحيوية. هذا هو مركز الأمان الفطري؛ بتطهيره يزول الخوف من الفقد والفقر، ويدرك الإنسان أنه قبضة تراب شرّفها الله بنفخة روح قدسية.",
                epiphanyAyah: "﴿وَالْقَمَرَ قَدَّرْنَاهُ مَنَازِلَ حَتَّىٰ عٰادَ كَالْعُرْجُونِ الْقَدِيمِ﴾ [يس: 39]",
                epiphanyWisdom: "سبحان من جعل تقلب القمر دليلاً قاطعاً على زوال الدنيا، وجعل في سماء الطين الأولى استقبال أبي البشرية لكل سائر يبتغي معراج الروح إلى خالقه!"
            }},
            {{
                id: 2,
                name: "البوابة الثانية: بوابة الكلمة والبيان وسماء عيسى ويحيى",
                badge: "السماء الثانية • فلك عطارد • شاكرا العجز (Svadhisthana) • الزئبق • 141.27 Hz",
                icon: "☿",
                color: "#00f0ff",
                essence: "فلك العقل الرابط والسيولة البيانية. لا يمكن للروح أن تصعد بعد سماء التراب إلا بتطهير المنطق والنطق. هنا يجتمع ابنا الخالة (يحيى وعيسى) ليمثلا ثنائية الطهارة والكلمة؛ فيحيى هو الحصور المبرأ من الرعونة، وعيسى هو كلمة الله الملقاة وروح منه.",
                propheticScene: "في السماء الثانية، استقبل النبي ﷺ عيسى بن مريم ويحيى بن زكريا عليهما السلام؛ رمزا التزكية والشفاء اللدني. دعا له بالبركة والخير، في مقام برزخي يجمع بين علم الشريعة الصارم (يحيى) وروحانية النفحة الإلهية الشافية التي تُحيي الموتى بإذن الله (عيسى).",
                easternVeda: "في التراث الصيني، عطارد هو 'شين شينغ' (Chenxing) كوكب الحكمة المائية السائلة وسرعة الفهم. وفي الفيدا، هذا الفلك هو 'بهوفار-لوكا' (Bhuvar-loka) وشاكرا 'سفادستانا' (Svadhisthana)، مركز السيولة الإبداعية والذكاء التكيفي، حيث يتطهر المرء من أوهام الانفعال الرغائبي.",
                babylonHellenic: "في بلاد الرافدين، هذا هو فلك 'نابو' (Nabu) إله الرقيم، الكتابة، والبلاغة. وفي اليونان، هو 'هرمس' رسول الآلهة المجنح رمز التواصل بين الغيب والشهادة. وفي متون هرمس، تسلّم الروح في هذا الفلك 'حيل المكر والحجج الزائفة والجدل الفارغ'، ليصفو العقل خالصاً لمعرفة الحقائق المجردة.",
                microcosmReflection: "في تكوينك، يقابل عطارد الغدد التناسلية والجهاز العصبي الحركي واللسان. تطهير هذا المقام يمنحك 'الحكمة وفصل الخطاب'؛ فلا ينطق لسانك إلا حقاً، ولا يسترسل عقلك في وساوس الجدل.",
                epiphanyAyah: "﴿إِذْ قَالَتِ الْمَلَائِكَةُ يَا مَرْيَمُ إِنَّ اللَّهَ يُبَشِّرُكِ بِكَلِمَةٍ مِّنْهُ اسْمُهُ الْمَسِيحُ عِيسَى ابْنُ مَرْيَمَ﴾ [آل عمران: 45]",
                epiphanyWisdom: "تبارك الذي جعل الكلمة مفتاح المعرفة، وجعل العقل رسول الفهم بين الطين والنور، وجعل نقاء المنطق شرطاً لازماً لشهود الجمال الأبدي!"
            }},
            {{
                id: 3,
                name: "البوابة الثالثة: بوابة شطر الحسن والتجلي الجمالي وسماء يوسف",
                badge: "السماء الثالثة • فلك الزهرة • شاكرا الضفيرة (Manipura) • النحاس • 221.23 Hz",
                icon: "♀",
                color: "#10b981",
                essence: "مقام التوازن والتجلي التناسبي في الكون. بعد اكتمال العقل، ترتقي الروح إلى عالم الصور والمثال (عالم البرزخ الخيالي). هنا يوسف الصديق، مظهر النصف التام من جمال الخلق؛ ليعلم السالك أن كل بهاء في الكائنات ليس إلا لمعة من نور الجمال الإلهي الأزلي.",
                propheticScene: "قال ﷺ في حديث الإسراء: «ففُتح لنا فإذا أنا بيوسف ﷺ، وإذا هو قد أُعطي شطر الحسن!»، فرحب بالنبي ﷺ ودعا له. والسر العرفاني عند ابن عربي هو أن يوسف صاحب 'تأويل الأحاديث' ورؤية المعاني متجسدة في صور حسية، لأن فلك الزهرة هو فلك الخيال المنضبط بالنبوة.",
                easternVeda: "في الفلك الإمبراطوري الصيني، الزهرة هي 'تايباي' (Taibai) كوكب عنصر المعدن (Jin) الأبيض الناصع، رمز النقاء والانسجام والعدالة الأخلاقية. وفي الفيدا، هذا هو عالم 'سفار-لوكا' (Svar-loka) وشاكرا الضفيرة 'مانيبورا' (Manipura)، حيث تتحول طاقة الرغبة السفلى إلى وهج بهاء ونور داخلي.",
                babylonHellenic: "في بابل، هذا معبد 'عشتار' (Ishtar) نجمة الصباح والمساء، المكسو باللازورد والنحاس المشع. وفي اليونان، هي 'أفروديت' التي فسّرها أفلوطين بأنها 'الجمال المعقول' المفيض على المادة نظامها الهندسي. وفي متون بويماندريس، تتخلى الروح هنا عن 'خديعة الشهوة المادية الزائفة' لتدرك الجمال الباقي الذي لا يعقبه فناء.",
                microcosmReflection: "يقابل هذا الفلك في جسدك البنكرياس والضفيرة الشمسية. هو مركز قوة الهوية والتقدير؛ بتزكيته، يرى الإنسان جمال صنع الله في كل ذرة، ويتحرر من أسر الصور الفانية ليعشق خالق البهاء سبحانه.",
                epiphanyAyah: "﴿صُنْعَ اللَّهِ الَّذِي أَتْقَنَ كُلَّ شَيْءٍ ۚ إِنَّهُ خَبِيرٌ بِمَا تَفْعَلُونَ﴾ [النمل: 88]",
                epiphanyWisdom: "سبحان من صاغ هندسة الوجود بأبهى نسبة ذهبية، وجعل جمال الأكوان دليلاً يقطع دابر الشك على كمال صانعه وجلال ذاته!"
            }},
            {{
                id: 4,
                name: "البوابة الرابعة: بوابة قلب العالم وسراج النور وسماء إدريس",
                badge: "السماء الرابعة • فلك الشمس • شاكرا القلب (Anahata) • الذهب الخالص • 126.22 Hz",
                icon: "☉",
                color: "#94a3b8",
                essence: "قلب المنظومة الكونية ومحور الاتزان الأكبر. تتوسط السماء الرابعة السماوات السبع (ثلاث تحتها وثلاث فوقها)، تماماً كما تتوسط الشمس المجموعة الشمسية، وكما يتوسط القلب قفص الصدر. هنا النبي إدريس (هرمس الأول)، أول من خط بالقلم وعلّم الحكمة، الذي رفعه الله مكاناً علياً.",
                propheticScene: "لقي النبي ﷺ في السماء الرابعة إدريس عليه السلام، مصداقاً لقوله تعالى: ﴿وَرَفَعْنَاهُ مَكَانًا عَلِيًّا﴾. توسطه في سماء الشمس يطابق رتبته العرفانية كقطب للأرواح التعليمية؛ فمن الشمس تقتبس كل الكواكب السفلى والعليا ضياءها، ومن إدريس تفرعت أصول الحكمة النبوية والفلكية.",
                easternVeda: "في الطاوية، الشمس هي جوهر 'اليانغ' (Yang) الأعظم ومصدر الطاقة الحيوية الشاملة (Qi). وفي الكونيات الفيدية، هي 'ماهار-لوكا' (Mahar-loka) وسكنى الحكماء والريشي (Rishis)، المقابلة لشاكرا القلب 'أناهاتا' (Anahata)، مركز الرنين الصوتي النقي (Anahata Nada) الذي لا يصحبه قرع ولا اصطدام.",
                babylonHellenic: "في زقورة بابل، زُينت طبقة الشمس بالذهب الخالص للإله 'شمش' (Shamash) قاضي السماوات والأرض الذي يكشف كل سر مستور. وفي مغزل الضرورة عند أفلاطون، مدار الشمس هو السراج الموقد الذي يعطي الرؤية لجميع الأفلاك. وفي متون هرمس، تسلّم الروح في هذا الفلك 'شهوة السيطرة والكبرياء'، لتتحول الأنا إلى عبودية محضة لنور النور.",
                microcosmReflection: "في صدرك، يقابل هذا الفلك عضلة القلب والغدة الزعترية (Thymus). هو قطب الروح الذي تتجمع عنده اللطائف؛ إذا صلح صلح الجسد كله، وإذا نُوّر بنور الإيمان أشرق فيك التوحيد كالشمس في رابعة النهار.",
                epiphanyAyah: "﴿وَجَعَلْنَا سِرَاجًا وَهَّاجًا﴾ [النبأ: 13] • ﴿اللَّهُ نُورُ السَّمَاوَاتِ وَالْأَرْضِ﴾ [النور: 35]",
                epiphanyWisdom: "عظمة لا تُدانى لخالق جعل قلباً نابضاً بالذهب في مركز السماء والأجساد، ليدرك العبد أن مداره الحقيقي هو التوجه نحو شمس التوحيد!"
            }},
            {{
                id: 5,
                name: "البوابة الخامسة: بوابة البأس والفرقان وتسكين الحدة وسماء هارون",
                badge: "السماء الخامسة • فلك المريخ • شاكرا الحلق (Vishuddha) • الحديد • 144.72 Hz",
                icon: "♂",
                color: "#ef4444",
                essence: "فلك القوة التنفيذية والحدة الصارمة. إن الصعود لا يكتمل إلا باختبار عنصر النار والحديد. ولقد تجلت الحكمة الإلهية في وضع نبي المحبة والسكينة (هارون عليه السلام) في هذا الفلك الناري ليُسكّن بأس المريخ بنفحة الود والكهانة النبوية، محولاً طاقة الغضب إلى ثبات على الحق.",
                propheticScene: "في السماء الخامسة، استقبل هارون عليه السلام رسول الله ﷺ مرحباً وداعياً. وهارون المحبب في قومه يمثل ترويض الاندفاع وحفظ بني إسرائيل من الشتات بحلمه، ليعلم السالك أن القوة الحقيقية ليست في البطش، بل في ضبط النفس بالحق المبين.",
                easternVeda: "في التراث الصيني، المريخ هو 'هو شينغ' (Huo Xing) كوكب عنصر النار الحامية والمحاربة الحارقة. وفي الفيدا، هذا الفلك هو 'جانا-لوكا' (Jana-loka) وشاكرا الحنجرة 'فيشودها' (Vishuddha) المرتبطة بالتعبير الصادق والتطهير التام من شوائب الباطل.",
                babylonHellenic: "في بابل، شُيدت الطبقة الخامسة بالآجر الأحمر للإله 'نيرغال' (Nergal) سيد البأس والحروب. وعند اليونان هو 'آريس'. وفي المتون الهرمسية، تسلّم النفس الصاعدة في فلك المريخ 'الجرأة الطائشة وحمية الغضب غير الموجه'، لتتحول نيران المريخ إلى نار مقدسة تحرق حجب الأوهام.",
                microcosmReflection: "في جسدك، يقابل المريخ الغدة الدرقية والحنجرة وعنصر الحديد في هيموجلوبين الدم. هذا المركز يحكم الشجاعة وقول الحق؛ بتزكيته، يمتلك المؤمن بصيرة الفرقان فلا يهاب إلا الله.",
                epiphanyAyah: "﴿وَأَنزَلْنَا الْحَدِيدَ فِيهِ بَأْسٌ شَدِيدٌ وَمَنَافِعُ لِلنَّاسِ وَلِيَعْلَمَ اللَّهُ مَن يَنصُرُهُ وَرُسُلَهُ بِالْغَيْبِ﴾ [الحديد: 25]",
                epiphanyWisdom: "تنزيه لمن قدّر طبائع العناصر وألجم غليان النار بحكمة الأنبياء، وجعل الشدة خادمة للحق لا طغياناً في الأرض!"
            }},
            {{
                id: 6,
                name: "البوابة السادسة: بوابة العدل والفيض والتشريع الإلهي وسماء موسى",
                badge: "السماء السادسة • فلك المشتري • شاكرا العين الثالثة (Ajna) • القصدير • 183.58 Hz",
                icon: "♃",
                color: "#3b82f6",
                essence: "سعد الأفلاك الأكبر وعالم الرحابة والاتساع. فلك الحكمة الإلهية المنزلة في الألواح والشرائع الكبرى. هنا كليم الله موسى عليه السلام، صاحب التوراة والصعق في الطور؛ يمثل مقام العقل الملكوتي الذي يربط النواميس السماوية بإصلاح الحياة الأرضية.",
                propheticScene: "استقبل موسى ﷺ النبي محمداً في السماء السادسة؛ وبكى حين جاوزه ﷺ لا حسداً بل شفقة ورغبة في كثرة المهتدين قائلاً: «غلامٌ بُعث بعدي يدخل الجنة من أمته أكثر ممن يدخلها من أمتي». وكان موسى هو المشير الرحيم في مراجعة فرض الصلاة حتى خُففت من خمسين إلى خمس بصلاة وثواب خمسين!",
                easternVeda: "في الصين، المشتري هو 'سوي شينغ' (Suixing) كوكب عنصر الخشب المتفرع الحامل للنمو والبركة وإصلاح العمران. وفي الفيدا، هذا الفلك هو 'تاباس-لوكا' (Tapas-loka) وشاكرا الجبين والبصيرة 'أجنا' (Ajna)، حيث تنكشف أسرار القدر وحكمة الشرائع الإلهية المعصومة.",
                babylonHellenic: "في بابل، هو فلك 'مردوخ' (Marduk) سيد الآلهة وحامي القانون الكوني. وفي اليونان هو 'زيوس' الأب الحاكم. وفي متون هرمس، تسلّم الروح في هذا الفلك 'أطماع التوسع الأناني واحتكار السلطة'، لتنفتح البصيرة على سعة فضل الله الذي وسع كرسيه السماوات والأرض.",
                microcosmReflection: "في رأسك، يقابل المشتري الغدة النخامية (سيدة الغدد) ومركز البصيرة بين العينين. هو فلك الرؤية الشاملة وحسن التقدير؛ بالارتقاء إليه ينال العبد الحكمة: ﴿وَمَن يُؤْتَ الْحِكْمَةَ فَقَدْ أُوتِيَ خَيْرًا كَثِيرًا﴾.",
                epiphanyAyah: "﴿وَكَتَبْنَا لَهُ فِي الْأَلْوَاحِ مِن كُلِّ شَيْءٍ مَّوْعِظَةً وَتَفْصِيلًا لِّكُلِّ شَيْءٍ﴾ [الأعراف: 145]",
                epiphanyWisdom: "إجلال لرب العزة الذي أحكم شريعته كما أحكم مدارات كواكبه، وجعل فوق كل ذي علم عليم حتى ينتهي العلم كله إلى علام الغيوب!"
            }},
            {{
                id: 7,
                name: "البوابة السابعة: بوابة التوحيد الصافي ونهاية الآفاق وسماء إبراهيم",
                badge: "السماء السابعة • فلك زحل • شاكرا التاج (Sahasrara) • الرصاص العتيق • 147.85 Hz",
                icon: "♄",
                color: "#a855f7",
                essence: "أعلى الأفلاك الكوكبية السبعة وأبعدها عن أرض المادة. فلك الصمت الكوني، السكون والرسوخ الأبدي. هنا شيخ الأنبياء وإمام الحنفاء إبراهيم الخليل عليه السلام، مسنداً ظهره إلى البيت المعمور، محاذياً للكعبة المشرفة في خط استقامة كوني يخرق السماوات؛ رمزا للتوحيد المحض الذي حطم كل أصنام الشك والظنون.",
                propheticScene: "رأى النبي ﷺ إبراهيم عليه السلام مسنداً ظهره إلى البيت المعمور الذي يدخله كل يوم 70,000 ملك للتعبد لا يعودون إليه. قال إبراهيم لمحمد ﷺ: «يا محمد، أقرئ أمتك مني السلام، وأخبرهم أن الجنة طيبة التربة عذبة الماء، وأنها قيعان، وأن غراسها: سبحان الله والحمد لله ولا إله إلا الله والله أكبر».",
                easternVeda: "في الطاوية، زحل هو 'تشن شينغ' (Zhenxing) كوكب عنصر الأرض والمركز والرسوخ الأقصى. وفي الفيدا، هذا الفلك هو 'ساتيا-لوكا' (Satya-loka) سماء الحقيقة المطلقة المقابلة لشاكرا التاج 'ساهاسرارا' (Sahasrara - اللوتس ذو الألف بتلة)، حيث تسقط كل التمايزات وتنتهي مسيرة النفس الفردية.",
                babylonHellenic: "في بابل، الطبقة السابعة مكسوة بالسواد الداكن لـ 'نينورتا' (Ninurta) حارس الزمن والحدود النهائية. وفي سلم ميثرا هو درجة الرصاص. وفي متون هرمس، تسلّم الروح هنا 'رذيلة المكر الكوني والحدود الزمانية'، لتتطهر بالكامل وتتهيأ لعبور الفلك الثامن (Ogdoad) نحو عالم الأنوار الخالصة.",
                microcosmReflection: "يقابل زحل في جسدك الغدة الصنوبرية وقبة الرأس (اليافوخ). هو بوابة الاتصال بالغيب والسكينة المطلقة؛ حين يبلغ الإنسان هذا المقام في صلاته وسجوده، يتلاشى إحساسه بالزمن ويعيش في رحاب الأبدية.",
                epiphanyAyah: "﴿إِنِّي وَجَّهْتُ وَجْهِيَ لِلَّذِي فَطَرَ السَّمَاوَاتِ وَالْأَرْضَ حَنِيفًا وَمَا أَنَا مِنَ الْمُشْرِكِينَ﴾ [الأنعام: 79]",
                epiphanyWisdom: "ما أعظم الخالق الذي جعل نهاية سلم الأفلاك مسندة لظهر خليل الرحمن في تسبيح لا ينقطع، ليعلم العبد أن غاية السفر هي التوحيد الخالص!"
            }},
            {{
                id: 8,
                name: "المقام الأسمى: سدرة المنتهى والكرسي وعرش الرحمن (ما وراء الأفلاك)",
                badge: "فلك الأفلاك والمحيط الأعظم • قاب قوسين أو أدنى • سدرة المنتهى • 432 / 528 Hz",
                icon: "👑",
                color: "#f4b41a",
                essence: "هنا تنكسر كل أدوات القياس البشري، وتصمت الفلسفات، وتنتهي مسارات العروج الكوكبي. هذا حد عالم الشهادة وبداية عالم الغيب الخالص. سدرة المنتهى حيث يغشاها من نور الله ما لا يستطيع بشر وصفه، والكرسي الذي وسع السماوات والأرض كحلقة في فلاة، والعرش المجيد المحيط بالوجود كله حيث استوى الرحمن استواءً يليق بجلاله وعظمته.",
                propheticScene: "تجاوز النبي ﷺ السماوات كلها بصحبة جبريل حتى انتهى إلى سدرة المنتهى؛ فوقف جبريل وقال: «يا محمد، لو تقدمتُ قيد أنملة لاحترقت بالأنوار، وتقدم أنت فإنك مدعو». فدنا فتدلى فكان قاب قوسين أو أدنى، وكلّمه ربه كفاحاً، وأعطاه خواتيم سورة البقرة، وفُرضت الصلاة خمسين ثم خُففت إلى خمس بأجر خمسين، وغُفر لأمته كبائر الذنوب ما لم يشركوا بالله شيئاً!",
                easternVeda: "في الفلسفة الطاوية، هذا هو 'الداو الأزلي الذي لا يُسمى' (Wuji - الفراغ الأولي المحيط بكل وجود). وفي الفيدا الهندية، هو 'بارابراهما' (Parabrahman) والنيرفانا / موكشا (Moksha)، حيث ينتهي وهم الانفصال وتسبح الروح في محيط الوعي الكوني الواحد.",
                babylonHellenic: "في الأفلاطونية المحدثة، هو 'الواحد الأحد' (The One) الذي لا تدركه العقول، منبع الوجود والخير المحض. وفي المتون الهرمسية، هو الفلك الثامن والتاسع (Ogdoad & Ennead) وحضرة النور غير المخلوق. وفي القبالاه القديمة، هي سفيرة 'كيتر' (Keter - التاج الإلهي المحيط بعين صوف Ein Sof).",
                microcosmReflection: "في الإنسان، هذا هو مقام 'سر السر' والفناء في محبة الله وبقاء البقاء، حيث يشهد العبد بقلبه وروحه أن لا إله إلا الله، فيغمره سلام كوني لا تزعزعه عواصف الدنيا، ويدرك حقيقة وجوده كخليفة لله في الأرض.",
                epiphanyAyah: "﴿الرَّحْمَٰنُ عَلَى الْعَرْشِ اسْتَوَىٰ ۝ لَهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ وَمَا بَيْنَهُمَا وَمَا تَحْتَ الثَّرَىٰ﴾ [طه: 5-6]",
                epiphanyWisdom: "الله أكبر كبيراً، والحمد لله كثيراً، وسبحان الله بكرةً وأصيلاً! لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير!"
            }}
        ];

        let activeOdysseyIndex = 0;

        function renderOdyssey() {{
            const nav = document.getElementById('odyssey-nav');
            if (!nav) return;
            nav.innerHTML = ODYSSEY_STAGES.map((st, idx) => `
                <button class="odyssey-nav-btn ${{idx === activeOdysseyIndex ? 'active' : ''}}" onclick="selectOdysseyStage(${{idx}})">
                    <span style="font-size:1.1rem;">${{st.icon}}</span>
                    <span>${{st.name.split(':')[0]}}</span>
                </button>
            `).join('');

            renderActiveOdysseyStage();
        }}

        function selectOdysseyStage(idx) {{
            activeOdysseyIndex = idx;
            document.querySelectorAll('.odyssey-nav-btn').forEach((btn, i) => {{
                btn.classList.toggle('active', i === idx);
            }});
            renderActiveOdysseyStage();
        }}

        function renderActiveOdysseyStage() {{
            const container = document.getElementById('odyssey-stage-container');
            if (!container) return;
            const st = ODYSSEY_STAGES[activeOdysseyIndex];
            const prevIdx = (activeOdysseyIndex - 1 + ODYSSEY_STAGES.length) % ODYSSEY_STAGES.length;
            const nextIdx = (activeOdysseyIndex + 1) % ODYSSEY_STAGES.length;

            container.innerHTML = `
                <div class="odyssey-stage-card">
                    <div class="odyssey-stage-top">
                        <div class="odyssey-title-group">
                            <h3>
                                <span style="font-size:1.6rem; filter:drop-shadow(0 0 10px ${{st.color}})">${{st.icon}}</span>
                                <span style="color:${{st.color}}">${{st.name}}</span>
                            </h3>
                            <span>${{st.badge}}</span>
                        </div>
                        <span class="detail-badge" style="background:${{st.color}}22; color:${{st.color}}; border-color:${{st.color}}44;">
                            المرحلة ${{st.id}} من 8
                        </span>
                    </div>

                    <div class="odyssey-essence-callout">
                        <strong><i class="fa-solid fa-atom"></i> الجوهر الكوني الواحد وخلاصة الإجماع الإنساني:</strong>
                        ${{st.essence}}
                    </div>

                    <div class="odyssey-symphony-grid">
                        <div class="sym-card">
                            <div class="sym-card-title"><i class="fa-solid fa-scroll"></i> المشهد النبوي والمعراج الروحي</div>
                            <div class="sym-card-content">${{st.propheticScene}}</div>
                        </div>
                        <div class="sym-card">
                            <div class="sym-card-title"><i class="fa-solid fa-yin-yang"></i> صوت الشرق: الطاوية والفيدا الهندية</div>
                            <div class="sym-card-content">${{st.easternVeda}}</div>
                        </div>
                        <div class="sym-card">
                            <div class="sym-card-title"><i class="fa-solid fa-landmark"></i> بابل واليونان الفلسفية وهرمس</div>
                            <div class="sym-card-content">${{st.babylonHellenic}}</div>
                        </div>
                        <div class="sym-card">
                            <div class="sym-card-title"><i class="fa-solid fa-heart-pulse"></i> أنت والكون: الأثر في الجسد والروح</div>
                            <div class="sym-card-content">${{st.microcosmReflection}}</div>
                        </div>
                    </div>

                    <div class="odyssey-epiphany-box">
                        <div class="odyssey-epiphany-ayah">${{st.epiphanyAyah}}</div>
                        <div class="odyssey-epiphany-wisdom">${{st.epiphanyWisdom}}</div>
                    </div>

                    <div class="odyssey-nav-controls">
                        <button class="odyssey-ctrl-btn" onclick="selectOdysseyStage(${{prevIdx}})">
                            <i class="fa-solid fa-arrow-right"></i>
                            <span>${{ODYSSEY_STAGES[prevIdx].name.split(':')[0]}}</span>
                        </button>
                        <span style="font-size:0.82rem; color:var(--text-muted);">انقر للتنقل بين بوابات المعراج الكوني</span>
                        <button class="odyssey-ctrl-btn" onclick="selectOdysseyStage(${{nextIdx}})">
                            <span>${{ODYSSEY_STAGES[nextIdx].name.split(':')[0]}}</span>
                            <i class="fa-solid fa-arrow-left"></i>
                        </button>
                    </div>
                </div>
            `;
        }}

        // 4. Zodiac Master Renderers & Interactive Hologram (Nourished Occult Edition)
        function renderZodiac(filter = 'ALL') {{
            // Populate Quick Selector Pills Bar
            const pillsBar = document.getElementById('zodiac-pills-bar');
            if (pillsBar) {{
                pillsBar.innerHTML = ZODIAC_12_DATA.map(z => `
                    <button class="z-pill-btn ${{z.id === 1 ? 'active' : ''}}" id="z-pill-${{z.id}}" onclick="selectZodiac(${{z.id}})">
                        <span style="color:${{z.colorHex}};">${{z.glyph}}</span> ${{z.name.split('(')[0].trim()}}
                    </button>
                `).join('');
            }}

            // Populate Panoramic Comparative Matrix Table
            const tableBody = document.getElementById('panoramic-zodiac-tbody');
            if (tableBody) {{
                tableBody.innerHTML = ZODIAC_12_DATA.map(z => `
                    <tr>
                        <td><b style="color:${{z.colorHex}}; font-size:1.05rem;">${{z.glyph}} ${{z.name.split('(')[0].trim()}}</b><br><span style="font-size:0.75rem; color:var(--text-muted);">${{z.latin.split('(')[0].trim()}}</span></td>
                        <td><span class="zodiac-element ${{z.elemClass}}">${{z.element}}</span><br><span style="font-size:0.75rem; color:var(--text-muted);">${{z.quality.split('(')[0].trim()}}</span></td>
                        <td><b style="color:var(--cyan);">${{z.ruler.split('•')[0].trim()}}</b></td>
                        <td style="white-space:normal; min-width:180px; font-size:0.8rem; line-height:1.4;">
                            <span style="color:var(--cyan); font-weight:700;">${{z.angelic_ruler.split('•')[0].trim()}}</span><br>
                            <span style="color:var(--gold); font-size:0.75rem;">${{z.terrestrial_servant.split('(')[0].trim()}}</span>
                        </td>
                        <td style="white-space:normal; min-width:170px; font-size:0.8rem; line-height:1.4; color:#c084fc;">${{z.lunar_mansions.split('•')[0].trim()}}...</td>
                        <td><b>${{z.organ}}</b></td>
                        <td>${{z.gland_system.split('(')[0].trim()}}</td>
                        <td><span style="color:var(--gold); font-weight:700;">${{z.tribe.split('(')[0].trim()}}</span></td>
                        <td><b style="color:#fff;">${{z.letter.split('/')[0].trim()}}</b></td>
                        <td><span style="color:var(--rose); font-weight:600;">${{z.opposing.split('(')[0].trim()}}</span></td>
                        <td style="white-space:normal; min-width:170px; font-size:0.8rem; line-height:1.4;">${{z.china_tao.split(';')[0].trim()}}</td>
                        <td style="white-space:normal; min-width:170px; font-size:0.8rem; line-height:1.4;">${{z.vedic_rashi.split(';')[0].trim()}}</td>
                        <td style="white-space:normal; min-width:240px; font-size:0.82rem; line-height:1.5;">${{z.shift}}</td>
                    </tr>
                `).join('');
            }}

            // Populate Zodiac Cards Grid
            const gridContainer = document.getElementById('zodiac-grid');
            if (gridContainer) {{
                const filtered = filter === 'ALL' ? ZODIAC_12_DATA : ZODIAC_12_DATA.filter(z => z.element.includes(filter));
                gridContainer.innerHTML = filtered.map(z => `
                    <div class="zodiac-card" style="border-top: 3px solid ${{z.colorHex}};">
                        <div>
                            <div class="zodiac-card-header">
                                <div class="zodiac-glyph" style="color:${{z.colorHex}};">${{z.glyph}}</div>
                                <span class="zodiac-element ${{z.elemClass}}">${{z.element}} • ${{z.quality.split('(')[0].trim()}}</span>
                            </div>
                            <h3 class="zodiac-name">${{z.name.split('(')[0].trim()}}</h3>
                            <div class="zodiac-latin">${{z.latin}} — يقابله: <b style="color:var(--rose);">${{z.opposing.split('(')[0].trim()}}</b></div>
                            
                            <div class="z-prop-list">
                                <div class="z-prop-row"><span class="z-prop-lbl">الكوكب الحاكم:</span><span class="z-prop-val">${{z.ruler.split('•')[0].trim()}}</span></div>
                                <div class="z-prop-row"><span class="z-prop-lbl">الملاك العلوي:</span><span class="z-prop-val" style="color:var(--cyan); font-weight:700;">${{z.angelic_ruler.split('(')[0].trim()}}</span></div>
                                <div class="z-prop-row"><span class="z-prop-lbl">الخادم الأرضي:</span><span class="z-prop-val" style="color:var(--gold); font-weight:700;">${{z.terrestrial_servant.split('(')[0].trim()}}</span></div>
                                <div class="z-prop-row"><span class="z-prop-lbl">العضو الجسدي:</span><span class="z-prop-val">${{z.organ}}</span></div>
                                <div class="z-prop-row"><span class="z-prop-lbl">منازل القمر:</span><span class="z-prop-val" style="color:#c084fc;">${{z.lunar_mansions.split('•')[0].trim()}}...</span></div>
                                <div class="z-prop-row"><span class="z-prop-lbl">السبط الرسالي:</span><span class="z-prop-val">${{z.tribe.split('(')[0].trim()}}</span></div>
                            </div>

                            <p class="zodiac-desc" style="font-size:0.88rem; line-height:1.75; color:#475569; margin-top:10px;">${{z.desc}}</p>

                            <div style="background:rgba(168,85,247,0.08); border:1px solid rgba(168,85,247,0.25); border-radius:10px; padding:10px 12px; margin-top:12px; font-size:0.82rem; line-height:1.6; color:#e2e8f0;">
                                <div style="color:#c084fc; font-weight:700; margin-bottom:3px; display:flex; align-items:center; gap:6px;">
                                    <span>🕊️ الروحانية والبخور والمعدن:</span>
                                </div>
                                <div><b>البخور والمعدن:</b> ${{z.sacred_incense}}</div>
                                <div style="font-size:0.78rem; color:#94a3b8; margin-top:2px;"><b>الحاكم العلوي:</b> ${{z.angelic_ruler.split('•')[0].trim()}}</div>
                            </div>

                            <button class="c-pill-btn" style="width:100%; justify-content:center; margin-top:14px; border-color:${{z.colorHex}}44; color:${{z.colorHex}};" onclick="selectZodiac(${{z.id}}); document.getElementById('zodiac-detail-card').scrollIntoView({{behavior:'smooth'}});">
                                <span>عرض الملف الموسوعي والأملاك والخدام</span>
                                <i class="fa-solid fa-arrow-up-right-from-square"></i>
                            </button>
                        </div>
                    </div>
                `).join('');
            }}

            selectZodiac(1);
        }}

        function selectZodiac(id) {{
            const z = ZODIAC_12_DATA.find(x => x.id === id);
            if (!z) return;

            // Sync Wheel Nodes
            document.querySelectorAll('.zodiac-wheel-node').forEach(n => n.classList.remove('active'));
            const activeNode = document.getElementById('zodiac-wheel-node-' + id);
            if (activeNode) activeNode.classList.add('active');

            // Sync Pills
            document.querySelectorAll('.z-pill-btn').forEach(b => b.classList.remove('active'));
            const activePill = document.getElementById('z-pill-' + id);
            if (activePill) activePill.classList.add('active');

            // Render Master Dossier
            const container = document.getElementById('zodiac-detail-card');
            if (!container) return;

            container.innerHTML = `
                <div class="chakra-main-header">
                    <div class="chakra-names">
                        <h2><span style="color:${{z.colorHex}}; font-size:1.8rem;">${{z.glyph}}</span> ${{z.name}}</h2>
                        <div class="chakra-sub-names">${{z.latin}} • <b>العنصر والطبيعة:</b> ${{z.element}} (${{z.quality}}) • <b>الحرف التكويني:</b> ${{z.letter}}</div>
                    </div>
                    <div class="chakra-prophet-badge" style="border-color:${{z.colorHex}}; color:${{z.colorHex}};">
                        👑 ${{z.tribe.split('(')[0].trim()}}
                    </div>
                </div>

                <div class="chakra-specs-grid">
                    <div class="c-spec-item">
                        <div class="c-spec-label">الكوكب الحاكم والشرف والوبال</div>
                        <div class="c-spec-val" style="color:var(--cyan);">${{z.ruler}}</div>
                    </div>
                    <div class="c-spec-item">
                        <div class="c-spec-label">العضو الجسدي (الميلوثيسيا الطبية)</div>
                        <div class="c-spec-val">${{z.organ}}</div>
                    </div>
                    <div class="c-spec-item">
                        <div class="c-spec-label">الجهاز الحيوي والغدة الصماء</div>
                        <div class="c-spec-val">${{z.gland_system}}</div>
                    </div>
                    <div class="c-spec-item">
                        <div class="c-spec-label">السبط الرسالي (الرؤيا اليوسفية)</div>
                        <div class="c-spec-val">${{z.tribe}}</div>
                    </div>
                    <div class="c-spec-item">
                        <div class="c-spec-label">الحرف التكويني (الفتوحات المكية)</div>
                        <div class="c-spec-val" style="color:var(--gold); font-weight:700;">${{z.letter}}</div>
                    </div>
                    <div class="c-spec-item">
                        <div class="c-spec-label">القطب المقابل المحوري (180°)</div>
                        <div class="c-spec-val" style="color:var(--rose);">${{z.opposing}}</div>
                    </div>
                </div>

                <div class="c-box quran-box" style="margin-bottom: 20px;">
                    <div class="c-step-badge c-step-quran">📖 الشاهد والسر القرآني الحاكم</div>
                    <div style="font-size:0.95rem; font-weight:600; line-height:1.8;">${{z.quran}}</div>
                </div>

                <!-- OCCULT SPIRITUAL SERVANTS & LUNAR MANSIONS BOX -->
                <div class="c-box occult-box" style="margin-bottom: 20px; background: rgba(168, 85, 247, 0.05); border: 1px solid rgba(168, 85, 247, 0.35); border-right: 4px solid #a855f7; border-radius: 14px; padding: 20px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:8px; flex-wrap:wrap; gap:8px;">
                        <div class="c-step-badge" style="background: rgba(168, 85, 247, 0.2); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.4); margin:0;">
                            🕊️ الروحانية والأملاك والخدام ومنازل القمر (شمس المعارف / غاية الحكيم / الفتوحات)
                        </div>
                        <span style="font-size:0.78rem; color:var(--gold); font-weight:700;">النواميس الروحانية والطلسمية الكونية</span>
                    </div>
                    <div style="display:grid; grid-template-columns: repeat(2, 1fr); gap:12px; font-size:0.88rem; line-height:1.7;">
                        <div style="background:rgba(0,0,0,0.3); padding:10px 14px; border-radius:8px; border:1px solid rgba(255,255,255,0.05);">
                            <strong style="color:var(--cyan); display:block; margin-bottom:3px;">الملاك الروحاني العلوي الحاكم:</strong>
                            <span style="color:#fff; font-weight:600;">${{z.angelic_ruler}}</span>
                        </div>
                        <div style="background:rgba(0,0,0,0.3); padding:10px 14px; border-radius:8px; border:1px solid rgba(255,255,255,0.05);">
                            <strong style="color:var(--gold); display:block; margin-bottom:3px;">الخادم الأرضي والملك الموكل:</strong>
                            <span style="color:#fff; font-weight:600;">${{z.terrestrial_servant}}</span>
                        </div>
                        <div style="background:rgba(0,0,0,0.3); padding:10px 14px; border-radius:8px; border:1px solid rgba(255,255,255,0.05);">
                            <strong style="color:#c084fc; display:block; margin-bottom:3px;">منازل القمر الـ 28 المندرجة:</strong>
                            <span style="color:#e2e8f0;">${{z.lunar_mansions}}</span>
                        </div>
                        <div style="background:rgba(0,0,0,0.3); padding:10px 14px; border-radius:8px; border:1px solid rgba(255,255,255,0.05);">
                            <strong style="color:var(--rose); display:block; margin-bottom:3px;">البخور التراثي والمعدن الطاقي:</strong>
                            <span style="color:#e2e8f0;">${{z.sacred_incense}}</span>
                        </div>
                    </div>
                    <div style="margin-top:12px; padding-top:10px; border-top:1px dashed rgba(168,85,247,0.25); font-size:0.85rem; color:#475569; line-height:1.7;">
                        <strong style="color:#94a3b8;">السر الحرفي والطلسمي في كتب الحكمة:</strong> ${{z.talisman_invocation}}
                    </div>
                </div>

                <!-- GLOBAL CIVILIZATIONAL CONSENSUS BOX -->
                <div class="global-consensus-box" style="margin-bottom: 20px;">
                    <div class="consensus-header">
                        <h4><i class="fa-solid fa-earth-americas"></i> الإجماع الحضاري العالمي الشامل لبرج ${{z.name.split('(')[0].trim()}}</h4>
                        <span style="font-size:0.78rem; color:var(--cyan); background:rgba(0,240,255,0.1); padding:3px 10px; border-radius:12px; border:1px solid rgba(0,240,255,0.25);">مضاهاة الشرق والغرب والآثار القديمة</span>
                    </div>
                    <div class="consensus-grid">
                        <div class="civ-card">
                            <div class="civ-card-title">🇨🇳 الصين والفرع الأرضي (Di Zhi & Wuxing)</div>
                            <div class="civ-card-text">${{z.china_tao}}</div>
                        </div>
                        <div class="civ-card">
                            <div class="civ-card-title">🇮🇳 الفيدا والراشي الهندي (Vedic Rashi & Nakshatra)</div>
                            <div class="civ-card-text">${{z.vedic_rashi}}</div>
                        </div>
                        <div class="civ-card">
                            <div class="civ-card-title">🏛️ بابل وزودياك دندرة المصري (Mul.Apin & Dendera)</div>
                            <div class="civ-card-text">${{z.babylon_egypt}}</div>
                        </div>
                        <div class="civ-card">
                            <div class="civ-card-title">📜 الهرمسية وقبالاه التكوين (Hermetica & Sefer Yetzirah)</div>
                            <div class="civ-card-text">${{z.hermetic_kabbalah}}</div>
                        </div>
                    </div>
                </div>

                <div class="chakra-deep-desc">
                    <div style="color:var(--gold); font-weight:700; margin-bottom:8px;">🌟 النقلة في الوعي الإنساني والارتقاء النفسي والروحي:</div>
                    ${{z.shift}}
                </div>

                <div class="chakra-proof-quote">
                    <strong>📜 الشاهد من أمهات المخطوطات والكتب (التفهيم للبيروني / القانون لابن سينا / الفتوحات لابن عربي / التيترابيبلوس لبطليموس):</strong><br>
                    ${{z.proof}}
                </div>
            `;
        }}

        function filterZodiac(cat) {{
            document.querySelectorAll('.z-filter-btn').forEach(b => {{
                b.classList.toggle('active', b.innerText.includes(cat) || (cat === 'ALL' && b.innerText.includes('جميع')));
            }});
            renderZodiac(cat);
        }}

        // 5. Timeline & Precession Engine Master Controller
        let currentSelectedEraId = 8; // Default: Aquarius Era

        function selectEra(eraId) {{
            currentSelectedEraId = eraId;
            const era = AGES_DATA.find(a => a.id === eraId) || AGES_DATA[0];

            // 1. Update Precession Nodes Active State
            document.querySelectorAll('.precession-node').forEach(node => {{
                node.classList.remove('active');
            }});
            const activeNode = document.getElementById('precession-node-' + eraId);
            if (activeNode) activeNode.classList.add('active');

            // 2. Update Pills Bar Active State
            document.querySelectorAll('.era-pill-btn').forEach(btn => {{
                btn.classList.remove('active');
            }});
            const activePill = document.getElementById('era-pill-' + eraId);
            if (activePill) activePill.classList.add('active');

            // 3. Highlight Card in Grid
            document.querySelectorAll('.age-card').forEach(card => {{
                card.classList.remove('active-era');
            }});
            const activeCard = document.getElementById('age-card-' + eraId);
            if (activeCard) activeCard.classList.add('active-era');

            // 4. Update Dynamic 180° Laser Line
            const laserLine = document.getElementById('polarity-laser-line');
            if (laserLine) {{
                const cx = 200, cy = 200, r = 145;
                const rad = era.angle * Math.PI / 180;
                const oppRad = era.oppAngle * Math.PI / 180;
                const x1 = (cx + r * Math.cos(rad)).toFixed(1);
                const y1 = (cy + r * Math.sin(rad)).toFixed(1);
                const x2 = (cx + r * Math.cos(oppRad)).toFixed(1);
                const y2 = (cy + r * Math.sin(oppRad)).toFixed(1);
                laserLine.setAttribute('x1', x1);
                laserLine.setAttribute('y1', y1);
                laserLine.setAttribute('x2', x2);
                laserLine.setAttribute('y2', y2);
                laserLine.setAttribute('stroke', era.color);
                laserLine.style.filter = `drop-shadow(0 0 10px ${{era.color}})`;
            }}

            // 5. Render Master Epoch Dossier
            const dossier = document.getElementById('era-detail-card');
            if (dossier) {{
                dossier.innerHTML = `
                    <div class="c-header">
                        <div class="c-num" style="background: rgba(255,255,255,0.06); border: 2px solid ${{era.color}}; color: ${{era.color}};">${{era.glyph}}</div>
                        <div class="c-title-group">
                            <span class="c-arabic-name" style="color: ${{era.color}};">${{era.title}}</span>
                            <span class="c-sanskrit-name">${{era.era}} • دورة الـ 2,160 سنة</span>
                        </div>
                    </div>

                    <div style="margin-bottom: 18px; display: flex; flex-wrap: wrap; gap: 8px;">
                        <span class="polarity-tag" style="background: rgba(255, 51, 102, 0.15); border-color: rgba(255, 51, 102, 0.4); color: #ff7597; font-size: 0.85rem;">
                            ⚡ النظير القطبي الحاكم: ${{era.polarity}}
                        </span>
                    </div>

                    <div class="c-meta-grid">
                        <div class="c-meta-item">
                            <span class="c-meta-lbl">🪐 الحاكم والعنصر</span>
                            <span class="c-meta-val" style="color: ${{era.color}};">${{era.ruler}}</span>
                        </div>
                        <div class="c-meta-item">
                            <span class="c-meta-lbl">🕊️ المقام النبوي</span>
                            <span class="c-meta-val" style="color: #34d399;">${{era.prophet}}</span>
                        </div>
                        <div class="c-meta-item">
                            <span class="c-meta-lbl">🏛️ الصرح / الحدث</span>
                            <span class="c-meta-val" style="color: #fbbf24;">${{era.monument}}</span>
                        </div>
                        <div class="c-meta-item">
                            <span class="c-meta-lbl">🕉️ مطابقة اليوغا</span>
                            <span class="c-meta-val" style="color: #00f0ff;">${{era.yuga}}</span>
                        </div>
                        <div class="c-meta-item">
                            <span class="c-meta-lbl">🧪 المرحلة الخيميائية</span>
                            <span class="c-meta-val" style="color: #475569;">${{era.alchemy}}</span>
                        </div>
                        <div class="c-meta-item">
                            <span class="c-meta-lbl">🌟 الرموز النموذجية</span>
                            <span class="c-meta-val" style="color: #a78bfa;">${{era.symbols}}</span>
                        </div>
                    </div>

                    <div class="c-box ayah-box" style="margin-top: 18px;">
                        <span class="c-box-title" style="color: var(--gold);">📖 الشاهد القرآني والإعجاز الكوني</span>
                        <p style="font-size: 0.95rem; line-height: 1.8; color: #fef08a; margin: 0; font-family: 'Amiri', serif;">${{era.quran}}</p>
                    </div>

                    <div class="c-box" style="margin-top: 16px; background: rgba(0,0,0,0.3); border-right: 3px solid ${{era.color}};">
                        <span class="c-box-title" style="color: ${{era.color}};">📜 التحليل الكوزمولوجي والتاريخي المعمق</span>
                        <p style="font-size: 0.88rem; line-height: 1.75; color: #e2e8f0; margin: 0; text-align: justify;">${{era.desc}}</p>
                    </div>

                    <div class="c-box" style="margin-top: 14px; background: rgba(255, 51, 102, 0.08); border-right: 3px solid var(--rose);">
                        <span class="c-box-title" style="color: var(--rose);">⚖️ ديناميكية الظل الكوني ومحور الأقطاب (180°)</span>
                        <p style="font-size: 0.85rem; line-height: 1.7; color: #fca5a5; margin: 0;">${{era.polar_shadow}}</p>
                    </div>
                `;
            }}
        }}

        function filterTimeline(cat) {{
            document.querySelectorAll('.e-filter-btn').forEach(btn => {{
                btn.classList.toggle('active', btn.getAttribute('onclick').includes(cat) || (cat === 'ALL' && btn.innerText.includes('جميع')));
            }});
            renderTimelineCards(cat);
        }}

        function renderTimelineCards(cat = 'ALL') {{
            const container = document.getElementById('timeline-grid');
            if (!container) return;
            const filtered = cat === 'ALL' ? AGES_DATA : AGES_DATA.filter(a => a.category === cat);
            container.innerHTML = filtered.map(a => `
                <div class="age-card ${{a.id === currentSelectedEraId ? 'active-era' : ''}}" id="age-card-${{a.id}}" onclick="selectEra(${{a.id}})">
                    <div>
                        <div class="age-card-top">
                            <span class="age-era">${{a.era}}</span>
                            <div class="age-glyph-badge" style="border-color: ${{a.color}}; color: ${{a.color}};">${{a.glyph}}</div>
                        </div>
                        <h3 class="age-title">${{a.title}}</h3>
                        <div class="polarity-tag">
                            <span>⚡</span>
                            <span>${{a.polarity}}</span>
                        </div>
                        <div class="age-meta-pills">
                            <span class="age-pill prophet-pill">🕊️ ${{a.prophet.split('—')[0].trim()}}</span>
                            <span class="age-pill monument-pill">🏛️ ${{a.monument.split('•')[0].trim()}}</span>
                            <span class="age-pill">🪐 ${{a.ruler.split('•')[0].trim()}}</span>
                        </div>
                        <p class="age-desc">${{a.desc}}</p>
                        <div class="age-shadow-box">
                            <strong>الظل القطبي:</strong> ${{a.polar_shadow}}
                        </div>
                    </div>
                    <div class="age-symbols">
                        <span style="color: var(--gold);">الرموز الكونية:</span>
                        <span>${{a.symbols}}</span>
                    </div>
                </div>
            `).join('');
        }}

        function renderTimeline(cat = 'ALL') {{
            // 1. Populate Pills Bar
            const pillsBar = document.getElementById('era-pills-bar');
            if (pillsBar) {{
                pillsBar.innerHTML = AGES_DATA.map(a => `
                    <button class="chakra-pill-btn era-pill-btn ${{a.id === currentSelectedEraId ? 'active' : ''}}" id="era-pill-${{a.id}}" onclick="selectEra(${{a.id}})">
                        <span>${{a.glyph}}</span>
                        <span>${{a.sign}}</span>
                    </button>
                `).join('');
            }}

            // 2. Populate Precession Nodes on Wheel
            const nodesContainer = document.getElementById('precession-nodes-container');
            if (nodesContainer) {{
                const cx = 200, cy = 200, r = 145;
                nodesContainer.innerHTML = AGES_DATA.map(a => {{
                    const rad = a.angle * Math.PI / 180;
                    const x = cx + r * Math.cos(rad);
                    const y = cy + r * Math.sin(rad);
                    const leftPct = (x / 400 * 100).toFixed(1);
                    const topPct = (y / 400 * 100).toFixed(1);
                    return `
                        <div class="precession-node ${{a.id === currentSelectedEraId ? 'active' : ''}}" id="precession-node-${{a.id}}" style="top: ${{topPct}}%; left: ${{leftPct}}%; color: ${{a.color}}; border-color: ${{a.color}};" onclick="selectEra(${{a.id}})" title="${{a.title}}">
                            ${{a.glyph}}
                            <span class="precession-node-label">${{a.sign}}</span>
                        </div>
                    `;
                }}).join('');
            }}

            // 3. Render Cards in Grid
            renderTimelineCards(cat);

            // 4. Render Panoramic Comparative Matrix Table
            const tbody = document.getElementById('panoramic-epochs-tbody');
            if (tbody) {{
                tbody.innerHTML = AGES_DATA.map(a => `
                    <tr>
                        <td>
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <span style="font-size: 1.3rem; color: ${{a.color}};">${{a.glyph}}</span>
                                <div>
                                    <strong style="color: #fff; display: block;">${{a.title.split('—')[0].trim()}}</strong>
                                    <small style="color: var(--gold);">${{a.sign}}</small>
                                </div>
                            </div>
                        </td>
                        <td><b style="color: var(--cyan);">${{a.era}}</b></td>
                        <td>${{a.ruler}}</td>
                        <td><span style="color: #ff7597; font-weight: 600;">${{a.polarity}}</span></td>
                        <td><b style="color: #34d399;">${{a.prophet}}</b></td>
                        <td><span style="color: #fbbf24;">${{a.monument}}</span></td>
                        <td><small style="color: #e2e8f0; line-height: 1.5; display: block; max-width: 240px;">${{a.desc.slice(0, 130)}}...</small></td>
                        <td><span style="color: #00f0ff;">${{a.yuga}}</span><br><small style="color: #475569;">${{a.alchemy}}</small></td>
                        <td><small style="color: #fef08a; font-family: 'Amiri', serif; line-height: 1.6; display: block; max-width: 220px;">${{a.quran.slice(0, 100)}}...</small></td>
                    </tr>
                `).join('');
            }}

            // 5. Select Default Era
            selectEra(currentSelectedEraId);
        }}

        // 6. Master Grand Unified Matrix Controller
        let currentMatrixRankId = 8; // Default: Primum Mobile & Divine Throne
        let currentMatrixDimension = 'ALL';

        function selectMatrixRank(rankId) {{
            currentMatrixRankId = rankId;
            const rank = SPHERES_DATA.find(s => s.id === rankId) || SPHERES_DATA[0];

            // 1. Update Rank Buttons
            document.querySelectorAll('.m-rank-btn').forEach(btn => {{
                btn.classList.remove('active');
            }});
            const activeBtn = document.getElementById('m-rank-btn-' + rankId);
            if (activeBtn) activeBtn.classList.add('active');

            // 2. Highlight Row in Table
            document.querySelectorAll('#matrix-tbody tr').forEach(row => {{
                row.classList.remove('active-matrix-row');
            }});
            const activeRow = document.getElementById('matrix-row-' + rankId);
            if (activeRow) activeRow.classList.add('active-matrix-row');

            // 3. Render Master Rank Dossier Panel
            const dossier = document.getElementById('matrix-detail-card');
            if (dossier) {{
                dossier.innerHTML = `
                    <div class="c-header">
                        <div class="c-num" style="background: rgba(255,255,255,0.06); border: 2px solid ${{rank.color}}; color: ${{rank.color}};">${{rank.id}}</div>
                        <div class="c-title-group">
                            <span class="c-arabic-name" style="color: ${{rank.color}};">${{rank.name}}</span>
                            <span class="c-sanskrit-name">${{rank.rank}}</span>
                        </div>
                    </div>

                    <div class="c-meta-grid">
                        <div class="c-meta-item">
                            <span class="c-meta-lbl">🕊️ المقام النبوي والرسالي</span>
                            <span class="c-meta-val" style="color: #34d399;">${{rank.prophet}}</span>
                        </div>
                        <div class="c-meta-item">
                            <span class="c-meta-lbl">👑 الملاك العلوي الحاكم</span>
                            <span class="c-meta-val" style="color: #fbbf24;">${{rank.angel.split('(')[0].trim()}}</span>
                        </div>
                        <div class="c-meta-item">
                            <span class="c-meta-lbl">🧘 الشاكرا واللطيفة</span>
                            <span class="c-meta-val" style="color: var(--cyan);">${{rank.chakra}}</span>
                        </div>
                        <div class="c-meta-item">
                            <span class="c-meta-lbl">🩺 العضو والغدة الحيوية</span>
                            <span class="c-meta-val" style="color: #e2e8f0;">${{rank.gland}}</span>
                        </div>
                        <div class="c-meta-item">
                            <span class="c-meta-lbl">🧪 المعدن الخيميائي</span>
                            <span class="c-meta-val" style="color: ${{rank.color}};">${{rank.metal}}</span>
                        </div>
                        <div class="c-meta-item">
                            <span class="c-meta-lbl">🎵 التردد والنغمة الحيوية</span>
                            <span class="c-meta-val" style="color: #a78bfa;">${{rank.freqHz}}</span>
                        </div>
                        <div class="c-meta-item">
                            <span class="c-meta-lbl">⚖️ المبدأ الهرمسي</span>
                            <span class="c-meta-val" style="color: #475569;">${{rank.hermetic}}</span>
                        </div>
                        <div class="c-meta-item">
                            <span class="c-meta-lbl">📜 البطريرك في التراث القديم</span>
                            <span class="c-meta-val" style="color: #fca5a5;">${{rank.patriarch}}</span>
                        </div>
                    </div>

                    <div class="c-box ayah-box" style="margin-top: 18px;">
                        <span class="c-box-title" style="color: var(--gold);">📖 الشاهد القرآني المحكم والبرهان المعصوم</span>
                        <p style="font-size: 0.95rem; line-height: 1.8; color: #fef08a; margin: 0; font-family: 'Amiri', serif;">${{rank.quran}}</p>
                    </div>

                    <div class="c-box" style="margin-top: 14px; background: rgba(0,0,0,0.35); border-right: 3px solid ${{rank.color}};">
                        <span class="c-box-title" style="color: ${{rank.color}};">🏛️ الإجماع الحضاري العالمي ومطابقة الأنساق</span>
                        <div style="font-size: 0.85rem; line-height: 1.7; color: #475569; display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px; margin-top: 8px;">
                            <div><strong style="color: #00f0ff;">🕉️ الفيدا ولوكاس:</strong> ${{rank.vedic_india}}</div>
                            <div><strong style="color: #34d399;">☯️ الطاوية والصين:</strong> ${{rank.china_tao}}</div>
                            <div><strong style="color: #fbbf24;">🏛️ بابل والرافدين:</strong> ${{rank.babylon}}</div>
                            <div><strong style="color: #a78bfa;">✡️ كابالا وأخنوخ:</strong> ${{rank.kabbalah_enoch}}</div>
                        </div>
                    </div>

                    <div class="c-box" style="margin-top: 14px; background: rgba(0, 240, 255, 0.05); border-right: 3px solid var(--cyan);">
                        <span class="c-box-title" style="color: var(--cyan);">✨ سر التحول والارتقاء الروحي الكوني</span>
                        <p style="font-size: 0.88rem; line-height: 1.7; color: #e2e8f0; margin: 0;">${{rank.secret}} — <em>${{rank.titleDesc}}</em></p>
                    </div>
                `;
            }}
        }}

        function setMatrixMode(mode) {{
            currentMatrixDimension = mode;
            document.querySelectorAll('.m-mode-btn').forEach(btn => {{
                btn.classList.toggle('active', btn.getAttribute('onclick').includes(mode));
            }});

            const table = document.getElementById('master-unified-matrix-table');
            if (!table) return;

            const allCols = ['col-prophetic', 'col-anatomy', 'col-alchemical', 'col-civilizations'];
            
            if (mode === 'ALL') {{
                allCols.forEach(col => {{
                    table.querySelectorAll('.' + col).forEach(el => el.style.display = '');
                }});
            }} else {{
                allCols.forEach(col => {{
                    const match = (mode === 'prophetic' && col === 'col-prophetic') ||
                                  (mode === 'anatomy' && col === 'col-anatomy') ||
                                  (mode === 'alchemical' && col === 'col-alchemical') ||
                                  (mode === 'civilizations' && col === 'col-civilizations');
                    table.querySelectorAll('.' + col).forEach(el => {{
                        el.style.display = match ? '' : 'none';
                    }});
                }});
            }}
        }}

        function filterMatrixTable() {{
            const query = (document.getElementById('matrix-search-input')?.value || '').trim().toLowerCase();
            const rows = document.querySelectorAll('#matrix-tbody tr');
            rows.forEach(row => {{
                const text = row.innerText.toLowerCase();
                row.style.display = text.includes(query) ? '' : 'none';
            }});
        }}

        function renderMatrix() {{
            // 1. Populate Ranks Bar
            const ranksBar = document.getElementById('matrix-ranks-bar');
            if (ranksBar) {{
                ranksBar.innerHTML = SPHERES_DATA.map(s => `
                    <button class="m-rank-btn ${{s.id === currentMatrixRankId ? 'active' : ''}}" id="m-rank-btn-${{s.id}}" onclick="selectMatrixRank(${{s.id}})">
                        <span style="color: ${{s.color}};">●</span>
                        <span>مرتبة ${{s.id}}: ${{s.name.split('(')[0].replace('فلك', '').trim()}}</span>
                    </button>
                `).join('');
            }}

            // 2. Populate 15-Column Master Table
            const tbody = document.getElementById('matrix-tbody');
            if (tbody) {{
                tbody.innerHTML = SPHERES_DATA.map(s => `
                    <tr id="matrix-row-${{s.id}}" onclick="selectMatrixRank(${{s.id}})" class="${{s.id === currentMatrixRankId ? 'active-matrix-row' : ''}}">
                        <td>
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <span style="font-size: 1.1rem; color: ${{s.color}};">●</span>
                                <div>
                                    <strong style="color: #fff; display: block;">${{s.name.split('(')[0].trim()}}</strong>
                                    <small style="color: ${{s.color}};">المرتبة ${{s.id}} • ${{s.rank.slice(0, 25)}}</small>
                                </div>
                            </div>
                        </td>
                        <td class="col-prophetic"><b style="color: #34d399;">${{s.prophet}}</b></td>
                        <td class="col-prophetic"><span style="color: #fbbf24;">${{s.angel.split('(')[0].slice(0, 35)}}</span></td>
                        <td class="col-prophetic"><small style="color: #fca5a5;">${{s.patriarch.slice(0, 40)}}</small></td>
                        <td class="col-anatomy"><span style="color: var(--cyan); font-weight: 600;">${{s.chakra}}</span></td>
                        <td class="col-anatomy"><small style="color: #e2e8f0;">${{s.gland}}</small></td>
                        <td class="col-alchemical"><b style="color: ${{s.color}};">${{s.metal}}</b></td>
                        <td class="col-alchemical"><small style="color: #475569;">${{s.hermetic.slice(0, 45)}}</small></td>
                        <td class="col-anatomy"><span style="color: #a78bfa; font-weight: 600;">${{s.freqHz}}</span></td>
                        <td class="col-civilizations"><small style="color: #00f0ff;">${{s.vedic_india.slice(0, 50)}}...</small></td>
                        <td class="col-civilizations"><small style="color: #34d399;">${{s.china_tao.slice(0, 50)}}...</small></td>
                        <td class="col-civilizations"><small style="color: #a78bfa;">${{s.kabbalah_enoch.slice(0, 50)}}...</small></td>
                        <td class="col-civilizations"><small style="color: #fbbf24;">${{s.babylon.slice(0, 50)}}...</small></td>
                        <td class="col-alchemical"><small style="color: #e2e8f0;">${{s.titleDesc}}</small></td>
                        <td class="col-prophetic"><small style="color: #fef08a; font-family: 'Amiri', serif; line-height: 1.5; display: block; max-width: 220px;">${{s.quran.slice(0, 75)}}...</small></td>
                    </tr>
                `).join('');
            }}

            // 3. Select Default Rank
            selectMatrixRank(currentMatrixRankId);
        }}

        // 7. Manuscripts Renderer
        function renderManuscripts() {{
            const container = document.getElementById('books-grid');
            container.innerHTML = MANUSCRIPTS_DATA.map(b => `
                <div class="book-card">
                    <div>
                        <div class="book-author">${{b.author}}</div>
                        <h3 class="book-name">📜 ${{b.name}}</h3>
                        <p class="book-summary">${{b.summary}}</p>
                    </div>
                    <div class="book-chapters"><strong>الأبواب المحللة:</strong> ${{b.chapters}}</div>
                </div>
            `).join('');
        }}

        // 8. Critique & Discrepancies Renderer (Vertical Step-by-Step for Murshid)
        function renderCritique() {{
            const container = document.getElementById('critique-grid');
            container.innerHTML = CRITIQUE_DATA.map(c => `
                <div class="critique-card ${{c.isUrgent ? 'urgent' : ''}}">
                    <div class="critique-header">
                        <div class="critique-title">${{c.title}}</div>
                        <span class="critique-tag">${{c.tag}}</span>
                    </div>
                    <div class="critique-sections">
                        <!-- الخطوة 1: بيان وحكم القرآن الكريم المحكم -->
                        <div class="c-box quran-box">
                            <div class="c-step-badge c-step-quran">📖 1. بيان وحكم القرآن الكريم المحكم (المرجع المعياري الأسمى)</div>
                            <div>${{c.quran}}</div>
                        </div>

                        <!-- الخطوة 2: نصوص ومرويات المخطوطات والكتب الأخرى -->
                        <div class="c-box manuscript-box">
                            <div class="c-step-badge c-step-manuscript">📜 2. نصوص ومرويات المخطوطات والكتب الأخرى (المسألة المتشابهة في التراث القديم)</div>
                            <div>${{c.manuscript}}</div>
                        </div>

                        <!-- الخطوة 3: مساحة التحقيق وقرار فضيلة المرشد -->
                        <div class="c-note-murshid">
                            <div class="c-step-badge c-step-murshid">⚖️ 3. تحقيق وتوجيه البصيرة (متروكة لفضيلة المرشد ليفصل ويقرر فيها)</div>
                            <div>${{c.murshid}}</div>
                            <div class="murshid-decision-box">
                                <span><strong>حالة المسألة في ميزان التحقيق:</strong></span>
                                <span class="decision-status-pill">${{c.isUrgent ? '⚠️ تتطلب فصل وتوجيه المرشد' : '✅ شواهد تاريخية مصدقة للقرآن'}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            `).join('');
        }}

        // Portal Security Authentication Logic
        const PORTAL_SECRET = "1234";
        function handlePortalAuth(e) {{
            e.preventDefault();
            const input = document.getElementById('auth-pass-input');
            const errorMsg = document.getElementById('auth-error-msg');
            const gate = document.getElementById('portal-auth-gate');
            
            if (input.value.trim() === PORTAL_SECRET) {{
                gate.classList.add('unlocked');
                sessionStorage.setItem('portal_unlocked', 'true');
                setTimeout(() => {{
                    if (cosmicNetwork) cosmicNetwork.fit();
                }}, 300);
            }} else {{
                errorMsg.style.display = 'block';
                input.style.borderColor = '#ff3366';
                input.value = '';
                input.focus();
            }}
        }}

        // Check if already authenticated in session
        if (sessionStorage.getItem('portal_unlocked') === 'true') {{
            const gate = document.getElementById('portal-auth-gate');
            if (gate) gate.classList.add('unlocked');
        }}

        // Safe System Initialization
        try {{ if (typeof renderSpheres === 'function') renderSpheres(); }} catch(e) {{ console.warn("renderSpheres deferred:", e); }}
        try {{ if (typeof renderOdyssey === 'function') renderOdyssey(); }} catch(e) {{}}
        try {{ if (typeof renderChakras === 'function') renderChakras(); }} catch(e) {{}}
        try {{ if (typeof renderZodiac === 'function') renderZodiac('ALL'); }} catch(e) {{}}
        try {{ if (typeof renderTimeline === 'function') renderTimeline(); }} catch(e) {{}}
        try {{ if (typeof renderMatrix === 'function') renderMatrix(); }} catch(e) {{}}
        try {{ if (typeof renderManuscripts === 'function') renderManuscripts(); }} catch(e) {{}}
        try {{ if (typeof renderCritique === 'function') renderCritique(); }} catch(e) {{}}
    
        // ========================================================
        // GRAPH DUAL MODE: THEORY ATLAS & ZERO-LAG CONTROLLER
        // ========================================================
        var currentGraphMode = 'theory';
        window.currentGraphMode = 'theory';

        function switchGraphMode(mode) {{
            currentGraphMode = mode;
            const btnTheory = document.getElementById('btn-mode-theory');
            const btnCanvas = document.getElementById('btn-mode-canvas');
            const theoryContainer = document.getElementById('graph-theory-container');
            const canvasContainer = document.getElementById('graph-canvas-container');

            if (mode === 'theory') {{
                if (btnTheory) btnTheory.classList.add('active');
                if (btnCanvas) btnCanvas.classList.remove('active');
                if (theoryContainer) theoryContainer.style.display = 'block';
                if (canvasContainer) canvasContainer.style.display = 'none';
                renderTheoryCards();
            }} else {{
                if (btnTheory) btnTheory.classList.remove('active');
                if (btnCanvas) btnCanvas.classList.add('active');
                if (theoryContainer) theoryContainer.style.display = 'none';
                if (canvasContainer) canvasContainer.style.display = 'block';
                // Trigger canvas redraw and fit
                setTimeout(() => {{
                    if (cosmicNetwork) {{
                        cosmicNetwork.redraw();
                        cosmicNetwork.fit();
                    }}
                }}, 100);
            }}
        }}

        function renderTheoryCards() {{
            const grid = document.getElementById('theory-cards-grid');
            if (!grid) return;

            const searchVal = (document.getElementById('graph-search-input')?.value || '').trim().toLowerCase();

            const filtered = rawGraphData.nodes.filter(n => {{
                const matchCat = (activeGraphCategory === 'ALL' || n.category === activeGraphCategory);
                const matchSearch = (!searchVal || n.label.toLowerCase().includes(searchVal) || (n.snippet && n.snippet.toLowerCase().includes(searchVal)) || (n.tags && n.tags.some(t => t.toLowerCase().includes(searchVal))));
                return matchCat && matchSearch;
            }});

            grid.innerHTML = filtered.map(node => `
                <div class="theory-node-card" onclick="openNodeById('${{node.id}}')">
                    <div>
                        <div class="theory-card-header">
                            <span class="theory-card-cat" style="background:${{node.color.background}}25; color:${{node.color.background}}; border:1px solid ${{node.color.border}};">
                                ${{node.category}}
                            </span>
                            <span class="theory-card-links">🔗 ${{node.degree || 0}} روابط</span>
                        </div>
                        <div class="theory-card-title">${{node.label}}</div>
                        <div class="theory-card-snippet">${{node.snippet || (node.body ? node.body.slice(0, 110) + '...' : 'مفهوم كوزمولوجي متصل بشبكة الوحي والنبوات.')}}</div>
                    </div>
                    <div class="theory-card-btn">
                        <span>قراءة التفاصيل والروابط</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </div>
                </div>
            `).join('');
        }}

        function handleGraphSearch(val) {{
            if (currentGraphMode === 'theory') {{
                renderTheoryCards();
            }} else {{
                // Filter canvas
                filterGraphCategory(activeGraphCategory);
            }}
        }}

        function openNodeById(nodeId) {{
            const nodeData = rawGraphData.nodes.find(n => n.id === nodeId);
            if (nodeData) {{
                openDrawer(nodeData);
            }}
        }}

        // Enhanced openDrawer with backdrop and seamless connected node pills
        const oldOpenDrawer = openDrawer;
        openDrawer = function(nodeData) {{
            drawerTitle.innerText = nodeData.label;
            drawerMeta.innerHTML = `
                <span class="meta-tag">🏷️ ${{nodeData.category}}</span>
                <span class="meta-tag">🔗 ${{nodeData.degree || 0}} روابط</span>
                ${{(nodeData.tags || []).map(t => `<span class="meta-tag">#${{t}}</span>`).join('')}}
            `;
            drawerBody.innerHTML = marked.parse(nodeData.body || nodeData.snippet || 'لا يوجد محتوى.');

            // Connected pills
            const connectedIds = cosmicNetwork ? cosmicNetwork.getConnectedNodes(nodeData.id) : (rawGraphData.links.filter(l => l.source === nodeData.id || l.target === nodeData.id).map(l => l.source === nodeData.id ? l.target : l.source));
            drawerConns.innerHTML = (connectedIds || []).map(cid => {{
                const targetNode = rawGraphData.nodes.find(n => n.id === cid);
                const lbl = targetNode ? targetNode.label : cid;
                return `<span class="conn-pill" onclick="openNodeById('${{cid}}')">🔗 ${{lbl}}</span>`;
            }}).join('');

            drawer.classList.add('open');
            const backdrop = document.getElementById('drawer-backdrop');
            if (backdrop) backdrop.classList.add('active');

            if (currentGraphMode === 'canvas') {{
                highlightNeighborhood(nodeData.id);
            }}
        }};

        const oldCloseDrawer = closeDrawer;
        closeDrawer = function() {{
            drawer.classList.remove('open');
            const backdrop = document.getElementById('drawer-backdrop');
            if (backdrop) backdrop.classList.remove('active');
            if (currentGraphMode === 'canvas') {{
                resetFocus();
            }}
        }};

        // Stabilization physics freeze for mobile performance
        window.addEventListener('load', () => {{
            if (window.innerWidth <= 768) {{
                switchGraphMode('theory');
            }} else {{
                switchGraphMode('canvas');
            }}

            if (cosmicNetwork) {{
                cosmicNetwork.on('stabilizationIterationsDone', () => {{
                    // Turn physics off to prevent continuous CPU consumption on mobile
                    cosmicNetwork.setOptions({{ physics: {{ enabled: false }} }});
                    const pBtn = document.getElementById('physics-toggle-btn');
                    if (pBtn) pBtn.innerText = '▶ تحريك الجراف';
                }});
            }}
        }});

    </script>
</body>
</html>
"""

    OUTPUT_HTML_1.write_text(html_template, encoding="utf-8")
    OUTPUT_HTML_2.write_text(html_template, encoding="utf-8")
    OUTPUT_HTML_WEB.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_HTML_WEB.write_text(html_template, encoding="utf-8")
    OUTPUT_JSON.write_text(json.dumps({"nodes": nodes, "links": links}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] Master Quranic Cosmic Architecture Engine v5.0 built successfully!")
    print(f"     - Total nodes: {{len(nodes)}}")
    print(f"     - Total connections: {{len(links)}}")
    print(f"     - Synchronized to: {{OUTPUT_HTML_1.name}}, {{OUTPUT_HTML_2.name}}, & {{OUTPUT_HTML_WEB.relative_to(OUTPUT_HTML_WEB.parent.parent)}}")


if __name__ == "__main__":
    nodes, links = scan_vault()
    generate_unified_html(nodes, links)
