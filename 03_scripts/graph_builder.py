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
        return "أولو العزم من الرسل", "prophets", "#ffd166"
    elif "00_index" in path_lower or "quranic" in path_lower or nd_type in ["index", "master_blueprint"]:
        return "الهيكل القرآني والمصفوفات", "index", "#ff4d6d"
    elif "09_zodiac" in path_lower or nd_type == "zodiac_sign":
        return "دائرة البروج الاثني عشر", "zodiac", "#ff9f1c"
    elif "01_cycles" in path_lower or nd_type == "cycle":
        return "الدورات الكونية والفلك", "astronomy", "#00b4d8"
    elif "02_eras" in path_lower or nd_type == "era":
        return "العصور والرسالات التاريخية", "eras", "#ffb703"
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
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>أطلس الكوزمولوجيا القرآنية وشبكة المعرفة الشاملة — Quranic Cosmic Atlas</title>
    <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        :root {{
            --bg-space: #05070b;
            --panel-bg: rgba(11, 15, 23, 0.94);
            --border-glass: rgba(255, 255, 255, 0.12);
            --text-main: #f0f6fc;
            --text-muted: #8b949e;
            --gold: #f4b41a;
            --gold-glow: rgba(244, 180, 26, 0.3);
            --cyan: #00f0ff;
            --rose: #ff3366;
            --purple: #9d4edd;
            --emerald: #06d6a0;
        }}
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }}
        body {{
            background-color: var(--bg-space);
            color: var(--text-main);
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(0, 240, 255, 0.05) 0%, transparent 45%),
                radial-gradient(circle at 90% 80%, rgba(244, 180, 26, 0.05) 0%, transparent 45%);
            min-height: 100vh;
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
            border: 1px solid rgba(255, 209, 102, 0.35);
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
            border-color: rgba(255, 209, 102, 0.4);
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

        /* 4. Timeline View */
        .timeline-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 24px;
        }}
        .age-card {{
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            border-radius: 16px;
            padding: 24px;
            transition: all 0.3s ease;
        }}
        .age-card:hover {{
            transform: translateY(-5px);
            border-color: var(--cyan);
            box-shadow: 0 12px 30px rgba(0, 240, 255, 0.15);
        }}
        .age-era {{ font-size: 0.8rem; color: var(--gold); font-weight: 700; margin-bottom: 8px; }}
        .age-title {{ font-size: 1.3rem; color: #fff; margin-bottom: 12px; }}
        .polarity-tag {{
            background: rgba(255, 51, 102, 0.12);
            color: var(--rose);
            padding: 4px 10px;
            border-radius: 8px;
            font-size: 0.75rem;
            display: inline-block;
            margin-bottom: 14px;
            border: 1px solid rgba(255, 51, 102, 0.3);
        }}
        .age-desc {{ font-size: 0.88rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 16px; }}
        .age-symbols {{ border-top: 1px solid var(--border-glass); padding-top: 12px; font-size: 0.8rem; color: #a0aec0; }}

        /* 5. Matrix Table */
        .table-wrapper {{
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            border-radius: 16px;
            overflow-x: auto;
            box-shadow: 0 16px 40px rgba(0,0,0,0.5);
        }}
        table {{ width: 100%; border-collapse: collapse; text-align: right; min-width: 950px; }}
        th, td {{ padding: 16px 20px; border-bottom: 1px solid var(--border-glass); font-size: 0.9rem; }}
        th {{ background: rgba(0, 0, 0, 0.4); color: var(--gold); font-weight: 700; }}
        tr:hover {{ background: rgba(255, 255, 255, 0.02); }}

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
            color: #ffd166;
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
            background: radial-gradient(circle at center, #0e1628 0%, #050810 100%);
            border: 1px solid var(--border-glass);
            border-radius: 20px;
            padding: 30px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            box-shadow: 0 16px 45px rgba(0,0,0,0.7);
        }}
        .silhouette-canvas {{
            width: 380px;
            height: 640px;
            position: relative;
            display: flex;
            justify-content: center;
        }}
        .human-figure-svg {{
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            height: 100%;
            opacity: 0.32;
            filter: drop-shadow(0 0 15px rgba(0, 240, 255, 0.25));
            pointer-events: none;
        }}
        .central-sushumna-line {{
            position: absolute;
            top: 55px;
            bottom: 60px;
            left: 50%;
            width: 4px;
            transform: translateX(-50%);
            background: linear-gradient(180deg, #ffffff, #a855f7, #3b82f6, #00f0ff, #10b981, #f59e0b, #f97316, #ef4444);
            box-shadow: 0 0 15px rgba(255,255,255,0.7);
            border-radius: 4px;
            z-index: 2;
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
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: 2px solid rgba(255,255,255,0.8);
            box-shadow: 0 0 20px currentColor;
            background: rgba(11, 15, 23, 0.85);
            font-size: 1.15rem;
            color: #fff;
        }}
        .chakra-point-btn:hover, .chakra-point-btn.active {{
            transform: translate(-50%, -50%) scale(1.3);
            border-color: #ffffff;
            box-shadow: 0 0 35px currentColor, inset 0 0 12px currentColor;
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
            background: linear-gradient(135deg, var(--gold), #ffb703);
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
                        <button class="filter-pill" style="border-color:#ffd166; color:#ffd166;" onclick="filterGraphCategory('أولو العزم من الرسل')">أولو العزم من الرسل 👑</button>
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
                        <button class="g-btn" onclick="cosmicNetwork.fit({{animation: {{duration: 700}}}})">🔍 ضبط المشهد</button>
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

        <!-- TAB 2: SPHERES ASCENSION LADDER -->
        <section id="tab-spheres" class="tab-section">
            <div class="hero">
                <div class="quran-ayah">«سَنُرِيهِمْ آيَاتِنَا فِي الْآفَاقِ وَفِي أَنفُسِهِمْ حَتَّىٰ يَتَبَيَّنَ لَهُمْ أَنَّهُ الْحَقُّ»</div>
                <h1>سلم الصعود الباطني: الأفلاك ومقامات الأنبياء</h1>
                <p>تطابق مراتب الوجود الكونية من فلك القمر (آدم) مروراً بشمس الروح (عيسى) وزحل (إبراهيم) وصولاً لفلك العرش المحيط الأكبر للنبي الخاتم محمد ﷺ.</p>
            </div>
            <div class="spheres-container">
                <div class="ladder-list" id="spheres-list"></div>
                <div class="sphere-detail-panel" id="sphere-detail"></div>
            </div>
        </section>

        <!-- TAB CHAKRAS: PROPHETIC BODY & 7 CHAKRAS HOLOGRAPHIC VISUALIZER -->
        <section id="tab-chakras" class="tab-section">
            <div class="hero">
                <div class="quran-ayah">«وَفِي أَنفُسِكُمْ ۚ أَفَلَا تُبْصِرُونَ» [الذاريات: 21] — «لَقَدْ خَلَقْنَا الْإِنسَانَ فِي أَحْسَنِ تَقْوِيمٍ»</div>
                <h1 style="color: #00f0ff;">مجسم التشاكرات السبعة واللطائف ومقامات الأنبياء (العالم الصغير)</h1>
                <p>تطابق مراكز الطاقة السبعة وألوانها الترددية في الإنسان مع السماوات السبع، ومقامات الأنبياء، والمعادن الخيميائية، واللطائف الصوفية السبع في علم السلوك العرفاني.</p>
            </div>

            <div class="chakras-container">
                <!-- Human Silhouette Hologram -->
                <div class="body-silhouette-wrapper">
                    <div style="font-size: 0.95rem; font-weight: 700; color: var(--gold); margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                        <span>🧘 مجسم الجسد الأثيري ومسار الشوشومنا (قناة النور)</span>
                    </div>

                    <div class="silhouette-canvas" id="silhouette-canvas">
                        <!-- Meditating Human Silhouette SVG -->
                        <svg class="human-figure-svg" viewBox="0 0 300 500" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <!-- Head & Crown Aura -->
                            <circle cx="150" cy="70" r="38" stroke="#00f0ff" stroke-width="2" />
                            <ellipse cx="150" cy="50" rx="55" ry="30" stroke="#f4b41a" stroke-width="1.5" stroke-dasharray="4 4" />
                            <!-- Neck & Shoulders -->
                            <path d="M135 106 L110 135 L60 165 L40 250 L65 260 L85 190 L115 170" stroke="#00f0ff" stroke-width="2" />
                            <path d="M165 106 L190 135 L240 165 L260 250 L235 260 L215 190 L185 170" stroke="#00f0ff" stroke-width="2" />
                            <!-- Torso & Spine -->
                            <path d="M115 170 L110 280 L90 340 L50 430 L80 460 L130 380 L140 330 L150 330 L160 330 L170 380 L220 460 L250 430 L210 340 L190 280 L185 170" stroke="#00f0ff" stroke-width="2" />
                            <!-- Heart & Ribs Geometric Flow -->
                            <circle cx="150" cy="225" r="45" stroke="rgba(244, 180, 26, 0.2)" stroke-width="1" />
                            <polygon points="150,185 185,245 115,245" stroke="rgba(16, 185, 129, 0.3)" stroke-width="1" />
                            <polygon points="150,265 185,205 115,205" stroke="rgba(16, 185, 129, 0.3)" stroke-width="1" />
                        </svg>

                        <!-- Central Energy Spine -->
                        <div class="central-sushumna-line"></div>

                        <!-- 7 Chakra Pulsating Interactive Nodes + Universal Halo -->
                        <div class="chakra-point-btn" id="chakra-node-8" style="top: 45px; color: #ffffff; border-color: #f4b41a; background: radial-gradient(#fff, #f4b41a);" onclick="selectChakra(8)" title="الهالة المحيطة — النبي محمد ﷺ">👑</div>
                        <div class="chakra-point-btn" id="chakra-node-7" style="top: 85px; color: #a855f7;" onclick="selectChakra(7)" title="شاكرا التاج — إبراهيم الخليل">🟣</div>
                        <div class="chakra-point-btn" id="chakra-node-6" style="top: 135px; color: #3b82f6;" onclick="selectChakra(6)" title="شاكرا العين الثالثة — موسى وهارون">👁️</div>
                        <div class="chakra-point-btn" id="chakra-node-5" style="top: 185px; color: #00f0ff;" onclick="selectChakra(5)" title="شاكرا الحنجرة — داود وسليمان">🗣️</div>
                        <div class="chakra-point-btn" id="chakra-node-4" style="top: 245px; color: #10b981;" onclick="selectChakra(4)" title="شاكرا القلب — عيسى المسيح وإدريس">💚</div>
                        <div class="chakra-point-btn" id="chakra-node-3" style="top: 310px; color: #f59e0b;" onclick="selectChakra(3)" title="شاكرا الضفيرة الشمسية — يوسف الصديق">🟡</div>
                        <div class="chakra-point-btn" id="chakra-node-2" style="top: 380px; color: #f97316;" onclick="selectChakra(2)" title="شاكرا العجز — نوح عليه السلام">🟠</div>
                        <div class="chakra-point-btn" id="chakra-node-1" style="top: 455px; color: #ef4444;" onclick="selectChakra(1)" title="شاكرا الجذر — آدم عليه السلام">🔴</div>
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
        </section>

        <!-- TAB 3: 12 ZODIAC SIGNS -->
        <section id="tab-zodiac" class="tab-section">
            <div class="hero">
                <div class="quran-ayah">«وَالسَّمَاءِ ذَاتِ الْبُرُوجِ» — «تَبَارَكَ الَّذِي جَعَلَ فِي السَّمَاءِ بُرُوجًا»</div>
                <h1>دائرة البروج الاثني عشر: التشريح الباطني والرموز الرسالية</h1>
                <p>الربط المعرفي الدقيق لكل برج من الأبراج الاثني عشر: العناصر، الحكام الكوكبيين، أسباط بني إسرائيل الـ 12 في الرؤيا اليوسفية، وتناظر أعضاء الجسد (الميلوثيسيا).</p>
            </div>

            <div class="zodiac-filter-bar">
                <button class="z-filter-btn active" onclick="filterZodiac('ALL')">جميع البروج (12) 🌐</button>
                <button class="z-filter-btn" onclick="filterZodiac('ناري')">البروج النارية (الحمل، الأسد، القوس) 🔥</button>
                <button class="z-filter-btn" onclick="filterZodiac('ترابي')">البروج الترابية (الثور، العذراء، الجدي) 🌍</button>
                <button class="z-filter-btn" onclick="filterZodiac('هوائي')">البروج الهوائية (الجوزاء، الميزان، الدلو) 💨</button>
                <button class="z-filter-btn" onclick="filterZodiac('مائي')">البروج المائية (السرطان، العقرب، الحوت) 💧</button>
            </div>

            <div class="zodiac-grid" id="zodiac-grid"></div>
        </section>

        <!-- TAB 4: AGES TIMELINE -->
        <section id="tab-timeline" class="tab-section">
            <div class="hero">
                <div class="quran-ayah">«وَتِلْكَ الْأَيَّامُ نُدَاوِلُهَا بَيْنَ النَّاسِ»</div>
                <h1>تعاقب العصور والرسالات ومحور الأقطاب (180°)</h1>
                <p>دورة الـ 2,160 سنة وترنح الاعتدالين؛ كيف تنزلت الرسالات الكبرى بالتطابق مع البرج الحاكم والبرج المقابل من طوفان نوح إلى شريعة موسى ورسالة عيسى إلى العصر الخاتم لمحمد ﷺ.</p>
            </div>
            <div class="timeline-grid" id="timeline-grid"></div>
        </section>

        <!-- TAB 5: MASTER MATRIX -->
        <section id="tab-matrix" class="tab-section">
            <div class="hero">
                <div class="quran-ayah">«وَكُلَّ شَيْءٍ أَحْصَيْنَاهُ كِتَابًا» — «إِنَّا كُلَّ شَيْءٍ خَلَقْنَاهُ بِقَدَرٍ»</div>
                <h1>المصفوفة المعمارية الشاملة عبر كل المستويات الكونية</h1>
                <p>جدول المقارنة الشامل يجمع 9 مستويات كونية متطابقة في شاشة واحدة.</p>
            </div>
            <div class="table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th>المرتبة</th>
                            <th>الفلك والرمز</th>
                            <th>المقام النبوي والرسالي</th>
                            <th>البطريرك في التراث القديم</th>
                            <th>المبدأ الهرمسي</th>
                            <th>الشاكرا واللطيفة</th>
                            <th>المعدن الخيميائي</th>
                            <th>مستوى التحول الروحي</th>
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
        // Master Graph Data Injected from Vault
        const rawGraphData = {graph_data_json};

        // SPHERES DATA
        const SPHERES_DATA = [
            {{
                id: 8,
                name: "فلك العرش الأطلس (الفلك المحيط الأعظم)",
                color: "#ff3366",
                rank: "فلك ما وراء السماوات السبع (سدرة المنتهى)",
                prophet: "النبي الخاتم محمد صلى الله عليه وسلم",
                patriarch: "الحقيقة الجامعة ونور الأنوار",
                hermetic: "سر الكل الأعظم — مجمع النواميس والرسالات",
                chakra: "الهالة الكلية النورانية المحيطة (Auric Field)",
                metal: "الأثير الكوني الخالص (Quintessence)",
                note: "الصوت الأولي الجامع (الكلمة الأولى)",
                titleDesc: "مقام قاب قوسين أو أدنى، خاتم النبوة، والكمال الإنساني الجامع لجميع البروج",
                desc: "الفلك المحيط الذي يدير ويحوي جميع الأفلاك السبعة والبروج الاثني عشر تحته. في معراج النبي، جاوز السماوات السبع من القمر إلى زحل وبلغ سدرة المنتهى متجاوزاً حدود الزمان والمكان ليكون رحمة للعالمين.",
                proof: "«فص حكمة فردية في كلمة محمدية» — ابن عربي: الحقيقة المحمدية هي الفلك المحيط الأعظم بالوجود، وهو أول التعينات النورانية وخاتم الرسل في عالم الشهادة."
            }},
            {{
                id: 7,
                name: "فلك زحل (Saturn ♄)",
                color: "#a855f7",
                rank: "السماء السابعة",
                prophet: "النبي إبراهيم الخليل عليه السلام",
                patriarch: "الآدم الأعلى (Adam Kadmon)",
                hermetic: "مبدأ العقلانية الكلية (Mentalism) — الكل عقل",
                chakra: "التاج (ساهاسرارا / سر السر في الرأس)",
                metal: "الرصاص (Lead - Pb)",
                note: "سي (Si / B)",
                titleDesc: "مقام التوحيد المطلق، مكعب الحق (الكعبة)، والصمت الأبدي",
                desc: "فلك الحدود الكونية وهيكل البناء الأبدي. تجرد الروح من الأوهام المادية للوصول إلى مكعب التوحيد الخالص (مقام الخليل باني بيت الله).",
                proof: "«فص حكمة مهيمية في كلمة إبراهيمية» — ابن عربي: إبراهيم هو المستور بالحق، وزحل هو فلك التجرد الأقصى الذي تلتقي عنده البدايات بالنهايات."
            }},
            {{
                id: 6,
                name: "فلك المشتري (Jupiter ♃)",
                color: "#3b82f6",
                rank: "السماء السادسة",
                prophet: "النبي هارون وموسى عليهما السلام",
                patriarch: "إبراهيم (التوسع والرحمة في الكابالا)",
                hermetic: "مبدأ التناظر والتماثل (Correspondence) — كما في الأعلى كذلك في الأدنى",
                chakra: "العين الثالثة (آجنا / لطيفة الأخفى)",
                metal: "القصدير (Tin - Sn)",
                note: "لا (La / A)",
                titleDesc: "مقام البصيرة الكلية، الكهانة، والحكمة والعدالة التوسعية",
                desc: "كوكب الرحمة والعدالة الكونية. يمنح النفس القدرة على رؤية النواميس الخفية وترابط الأحداث التاريخية قبل وقوعها.",
                proof: "«فص حكمة علوية في كلمة هارونية» — ابن عربي: هارون مقام الخلافة الكهنوتية والجمال المحفوف برحمة المشتري."
            }},
            {{
                id: 5,
                name: "فلك المريخ (Mars ♂)",
                color: "#ef4444",
                rank: "السماء الخامسة",
                prophet: "النبي داود وموسى عليهما السلام",
                patriarch: "إسحاق (الشدة والقوة الجبروتية)",
                hermetic: "مبدأ السبب والنتيجة (Cause & Effect) — لكل فعل رد فعل",
                chakra: "الحنجرة والنطق (فيشودها / الخفي)",
                metal: "الحديد (Iron - Fe)",
                note: "صول (Sol / G)",
                titleDesc: "مقام البأس وصهر الحديد والشجاعة والكلمة الصارمة",
                desc: "فلك القوة التنفيذية وكسر أصنام الباطل. «وألنا له الحديد»؛ تسخير القوة الصلبة لتنفيذ الإرادة الإلهية والحزم.",
                proof: "«عجائب المخلوقات» — القزويني: الملاك كلكائيل موكل بالسماء الخامسة لتصريف قوى الشدة وحماية الحدود."
            }},
            {{
                id: 4,
                name: "فلك الشمس (Sol ☉) — شمس الروح",
                color: "#eab308",
                rank: "السماء الرابعة (المركز الكوني)",
                prophet: "السيد المسيح عيسى عليه السلام والنبي إدريس",
                patriarch: "يعقوب / يوسف (شمس السيادة والروح)",
                hermetic: "مبدأ الإيقاع والنبض (Rhythm) — البندول الكوني",
                chakra: "مركز القلب والصدر (أناهاتا / السر الروحي)",
                metal: "الذهب الخالص (Gold - Au)",
                note: "فا (Fa / F)",
                titleDesc: "المسيح روح الله: شمس المحبة المطلقة، إحياء الموتى، ومحور الحوت والعذراء",
                desc: "عيسى هو «روح الله وكلمته»، مقامه فلك الشمس مفيض الروح والحياة. ويرتبط ارتباطاً وثيقاً ببرج العذراء (الولادة الإعجازية من مريم، وبيت لحم = بيت الخبز وسنبلة العذراء Spica)، ومحور الحوت المقابل (رمز السمكة وتكثير الخبز والسمك).",
                proof: "«فص حكمة روحية في كلمة عيسوية» — ابن عربي: عيسى هو النفس الإلهي النازل بالروح، مقامه فلك الشمس الذي يبعث الحياة في الجماد."
            }},
            {{
                id: 3,
                name: "فلك الزهرة (Venus ♀)",
                color: "#10b981",
                rank: "السماء الثالثة",
                prophet: "النبي يوسف الصديق عليه السلام",
                patriarch: "موسى (الجمال المنير)",
                hermetic: "مبدأ القطبية والتناغم (Polarity)",
                chakra: "الضفيرة الشمسية (مانيبورا)",
                metal: "النحاس (Copper - Cu)",
                note: "مي (Mi / E)",
                titleDesc: "مقام الجمال المطلق، تسامي الشهوات، والتناغم الإلهي",
                desc: "فلك المحبة والفنون والتناغم الجمالي. ترويض الرغبات الحسية وتحويلها إلى عشق إلهي خالص كما تجسد في قصة يوسف الصديق.",
                proof: "«فص حكمة نورية في كلمة يوسفية» — ابن عربي: يوسف خزانة الجمال الإلهي الذي يُرى في مرآة الزهرة."
            }},
            {{
                id: 2,
                name: "فلك عطارد (Mercury ☿)",
                color: "#06b6d4",
                rank: "السماء الثانية",
                prophet: "النبي يحيى والنبي إدريس عليهما السلام",
                patriarch: "يوسف (تأويل الأحاديث والفهم)",
                hermetic: "مبدأ الاهتزاز والتردد (Vibration)",
                chakra: "العجز وأسفل البطن (سفاديستانا)",
                metal: "الزئبق (Quicksilver - Hg)",
                note: "ري (Re / D)",
                titleDesc: "مقام البيان والذكاء الفكري وفك شيفرات الأقلام والخط",
                desc: "رسول الآلهة وسر الأبجدية والخط بالقلم. يمثل الذكاء المنطقي السريع وسرعة الانتقال المعرفي وفك الرموز.",
                proof: "«سفر يتسيراه»: كوكب عطارد خلق به العقل وسر الحركة والنطق والتمييز بين الحق والباطل."
            }},
            {{
                id: 1,
                name: "فلك القمر (Moon ☽)",
                color: "#94a3b8",
                rank: "السماء الأولى (الدنيا)",
                prophet: "النبي آدم عليه السلام (أبو البشر)",
                patriarch: "داود (الملك الأرضي)",
                hermetic: "مبدأ النوع والتوالد (Gender)",
                chakra: "قاعدة العمود الفقري (مولادارا)",
                metal: "الفضة (Silver - Ag)",
                note: "دو (Do / C)",
                titleDesc: "مقام الهبوط، الغرائز، وتثبيت الروح في الطين",
                desc: "الفلك الأدنى المحاذي للأرض. تصريف السوائل، والتناسل، وانعكاس نور الشمس على العالم المادي السفلي.",
                proof: "«رسائل إخوان الصفا»: القمر خادم عالم الكون والفساد، به ينمو النبات وينزل المطر وتتغذى الأجساد."
            }}
        ];

        // 12 ZODIAC SIGNS DATA
        const ZODIAC_12_DATA = [
            {{
                name: "برج الحمل",
                latin: "Aries ♈",
                glyph: "♈",
                element: "ناري",
                elemClass: "elem-fire",
                quality: "منقلب (Cardinal)",
                ruler: "المريخ ♂ (وشرفه في الشمس)",
                organ: "الرأس والدماغ والعينان",
                tribe: "سبط يهوذا / جاد",
                letter: "الهاء (هـ) / الذال",
                opposing: "الميزان (180°)",
                desc: "برج المبادأة والريادة النارية؛ صهر الحديد، الحرب، ورمزية الكبش المقدس والشوفار في رسالة موسى الخروج."
            }},
            {{
                name: "برج الثور",
                latin: "Taurus ♉",
                glyph: "♉",
                element: "ترابي",
                elemClass: "elem-earth",
                quality: "ثابت (Fixed)",
                ruler: "الزهرة ♀ (وشرفه في القمر)",
                organ: "العنق والحنجرة والغدة الدرقية",
                tribe: "سبط يوسف / إفرايم",
                letter: "الواو (و) / الضاد",
                opposing: "العقرب (180°)",
                desc: "الاستقرار الأرضي والبناء الميغاليثي الضخم؛ تقديس عجل أبيس والثور البابلي، ويقابله في العقرب هوس المقابر والتحنيط والأهرامات."
            }},
            {{
                name: "برج الجوزاء",
                latin: "Gemini ♊",
                glyph: "♊",
                element: "هوائي",
                elemClass: "elem-air",
                quality: "متقلب (Mutable)",
                ruler: "عطارد ☿ (وشرفه في الرأس)",
                organ: "الكتفان والذراعان والرئتان والجهاز العصبي",
                tribe: "سبط زبولون / بنيامين",
                letter: "الزاي (ز) / الظاء",
                opposing: "القوس (180°)",
                desc: "برج التوأمين والتدوين الصوري واللغات والتجارة المفتوحة؛ يرمز لنشأة الأساطير التأسيسية كقابيل وهابيل وجلجامش وإنكيدو."
            }},
            {{
                name: "برج السرطان",
                latin: "Cancer ♋",
                glyph: "♋",
                element: "مائي",
                elemClass: "elem-water",
                quality: "منقلب (Cardinal)",
                ruler: "القمر ☽ (وشرفه في المشتري)",
                organ: "الصدر والثديان والمعدة",
                tribe: "سبط يساكر / رأوبين",
                letter: "الحاء (ح) / الغين",
                opposing: "الجدي (180°)",
                desc: "برج الرحم المائي والحفظ الأسري؛ طوفان ذوبان الجليد وسفينة نوح التي حفظت البذور، ونشأة أولى القرى المائية كأريحا."
            }},
            {{
                name: "برج الأسد",
                latin: "Leo ♌",
                glyph: "♌",
                element: "ناري",
                elemClass: "elem-fire",
                quality: "ثابت (Fixed)",
                ruler: "الشمس ☉ (موطنها ومقر السيادة)",
                organ: "القلب والعمود الفقري والشرايين",
                tribe: "سبط يهوذا (أسد يهوذا الملكي)",
                letter: "الطاء (ط) / الألف",
                opposing: "الدلو (180°)",
                desc: "برج السيادة الفردية وشعلة الروح الذاتية والذهب؛ نحت تمثال أبو الهول بالجيزة شاخصاً نحو شروق شمس برجه في 10,500 ق.م."
            }},
            {{
                name: "برج العذراء",
                latin: "Virgo ♍",
                glyph: "♍",
                element: "ترابي",
                elemClass: "elem-earth",
                quality: "متقلب (Mutable)",
                ruler: "عطارد ☿ (موطنه وشرفه)",
                organ: "البطن والأمعاء والجهاز الهضمي والتصفية",
                tribe: "سبط أشير / نفتالي",
                letter: "الياء (ي) / الباء",
                opposing: "الحوت (180°)",
                desc: "برج السيدة العذراء مريم وسر ميلاد السيد المسيح: الولادة البتولية الإعجازية؛ ولادته في «بيت لحم» (بيت الخبز؛ والنجم الأسطع في العذراء هو السِّماك الأعزل Spica أي سنبلة القمح مادة الخبز)، وتكامله مع قطب الحوت المقابل (معجزة تكثير السمك والخبز والرهبنة)."
            }},
            {{
                name: "برج الميزان",
                latin: "Libra ♎",
                glyph: "♎",
                element: "هوائي",
                elemClass: "elem-air",
                quality: "منقلب (Cardinal)",
                ruler: "الزهرة ♀ (وشرفه في زحل)",
                organ: "الكليتان وأسفل الظهر والتوازن الأسموزي",
                tribe: "سبط دان / لاوي (القضاء والكهانة)",
                letter: "الكاف (ك) / الجيم",
                opposing: "الحمل (180°)",
                desc: "كفتا العدل والميزان الأخلاقي؛ ألواح الوصايا العشر لموسى، والقوانين الصارمة للجمهوريات والدول لموازنة نار الحرب."
            }},
            {{
                name: "برج العقرب",
                latin: "Scorpio ♏",
                glyph: "♏",
                element: "مائي",
                elemClass: "elem-water",
                quality: "ثابت (Fixed)",
                ruler: "المريخ وبلوتو (وشرفه في أورانوس)",
                organ: "الأعضاء التناسلية وجهاز الإخراج والتجدد الخلوي",
                tribe: "سبط دان / شمعون",
                letter: "اللام (ل) / الدال",
                opposing: "الثور (180°)",
                desc: "عالم الموت والبعث والتحول الخيميائي وطائر الفينيق؛ كتاب الموتى في مصر وسحر العوالم السفلية وسر الخلود الكيميائي."
            }},
            {{
                name: "برج القوس",
                latin: "Sagittarius ♐",
                glyph: "♐",
                element: "ناري",
                elemClass: "elem-fire",
                quality: "متقلب (Mutable)",
                ruler: "المشتري ♃ (وشرفه في الذنب)",
                organ: "الفخذان والوركان والعصب الوركي",
                tribe: "سبط نفتالي / منسى",
                letter: "الميم (م) / الهاء",
                opposing: "الجوزاء (180°)",
                desc: "القنطور والسهم المنطلق نحو النجوم؛ الفلسفة الكونية الكبرى، استكشاف الآفاق، التعليم العالي، والحكمة النبوية العابرة للأقطار."
            }},
            {{
                name: "برج الجدي",
                latin: "Capricorn ♑",
                glyph: "♑",
                element: "ترابي",
                elemClass: "elem-earth",
                quality: "منقلب (Cardinal)",
                ruler: "زحل ♄ (وشرفه في المريخ)",
                organ: "الركبتان والهيكل العظمي والجلد والمفاصل",
                tribe: "سبط بنيامين / زبولون",
                letter: "النون (ن) / الواو",
                opposing: "السرطان (180°)",
                desc: "الماعز الجبلي الصاعد نحو قمة الهرم؛ الهياكل الصلبة، صرامة الزمان والحدود والمؤسسات والتحمل الصخري الشديد."
            }},
            {{
                name: "برج الدلو",
                latin: "Aquarius ♒",
                glyph: "♒",
                element: "هوائي",
                elemClass: "elem-air",
                quality: "ثابت (Fixed)",
                ruler: "زحل وأورانوس (وشرفه في نبتون)",
                organ: "الساقان والكاحلان والدورة الدموية والجهاز الكهربائي",
                tribe: "سبط رأوبين / دان",
                letter: "السين (س) / الزاي",
                opposing: "الأسد (180°)",
                desc: "سكب ماء المعرفة للبشرية جمعاء دون وسيط كهنوتي؛ عصر الذكاء الاصطناعي، الاتصال الشبكي، اللامركزية، والوعي الكوني."
            }},
            {{
                name: "برج الحوت",
                latin: "Pisces ♓",
                glyph: "♓",
                element: "مائي",
                elemClass: "elem-water",
                quality: "متقلب (Mutable)",
                ruler: "المشتري ونبتون (وشرفه في الزهرة)",
                organ: "القدمان وجهاز المناعة اللمفاوي",
                tribe: "سبط شمعون / يوسف",
                letter: "العين (ع) / الحاء",
                opposing: "العذراء (180°)",
                desc: "محور رسالة السيد المسيح والمحبة المطلقة: السمكتان السابحتان في محيط الروحانية، اتخاذ السمكة (Ichthys) شعاراً للمؤمنين، دعوة تلاميذه ليكونوا صيادي الناس، والتكامل التام مع قطب العذراء المقابل (تكثير السمك والخبز والرهبنة)."
            }}
        ];

        // AGES DATA
        const AGES_DATA = [
            {{
                era: "10,500 ق.م – 8,000 ق.م",
                title: "عصر الأسد (Leo)",
                polarity: "يقابله الدلو (180°)",
                desc: "نهاية العصر الجليدي وشروق شمس النور. ربطه العلماء بنحت تمثال أبو الهول المتجه لشروق شمس برجه.",
                symbols: "الشمس • الذهب • السيادة الفردية • أبو الهول"
            }},
            {{
                era: "8,000 ق.م – 6,000 ق.م",
                title: "عصر السرطان (Cancer)",
                polarity: "يقابله الجدي (180°)",
                desc: "ذوبان الجليد وطوفان المياه العالمي (طوفان نوح وسفينة النجاة). اتخاذ القرى المائية الأولى وحماية البذور في سفينة الرحم.",
                symbols: "القمر • الماء • الرحم • الفلك والسفينة • أريحا"
            }},
            {{
                era: "6,000 ق.م – 4,000 ق.م",
                title: "عصر الجوزاء (Gemini)",
                polarity: "يقابله القوس (180°)",
                desc: "نشأة اللغات والتدوين الصوري الأولي، وظهور أساطير التوائم المؤسسين (قابيل وهابيل، جلجامش وإنكيدو).",
                symbols: "عطارد • التوأمان • الألواح الطينية • التجارة والتنقل"
            }},
            {{
                era: "4,000 ق.م – 2,000 ق.م",
                title: "عصر الثور (Taurus)",
                polarity: "يقابله العقرب (180° - عالم الموت والبعث)",
                desc: "الاستقرار في وادي النيل والرافدين، عبادة عجل أبيس، والبناء الحجري الميغاليثي. القطب المقابل فجر هوس التحنيط والأهرامات.",
                symbols: "الزهرة • الثور المجنح • عجل أبيس • الأهرامات والمقابر"
            }},
            {{
                era: "2,000 ق.م – مطلع الميلاد",
                title: "عصر الحمل (Aries)",
                polarity: "يقابله الميزان (180° - القانون والشريعة)",
                desc: "عصر صهر أسلحة الحديد والحروب؛ رسالة النبي موسى، التضحية بالكبش ونفخ الشوفار، ونزول ألواح الوصايا العشر.",
                symbols: "المريخ • الكبش المقدس • الشوفار • ألواح الشريعة • روما"
            }},
            {{
                era: "مطلع الميلاد – ~2000 م",
                title: "عصر الحوت (Pisces)",
                polarity: "يقابلها العذراء (180° - النقاء والخدمة)",
                desc: "رسالة السيد المسيح، الإيمان والزهد والمحبة؛ رمزية السمكة، والولادة العذرية من مريم وتكريس الرهبنة والمشافي.",
                symbols: "المشتري ونبتون • السمكة (Ichthys) • الخبز والخمر • العذراء مريم"
            }},
            {{
                era: "2000 م – المستقبل (~4160 م)",
                title: "عصر الدلو (Aquarius)",
                polarity: "يقابله الأسد (180° - السيادة الفردية والقلب)",
                desc: "العصر الحالي؛ انفجار المعرفة وسكب ماء العلم للجميع، الذكاء الاصطناعي، الشبكات، وتحدي الحفاظ على شعلة الروح.",
                symbols: "أورانوس وزحل • جرة المعرفة • الذكاء الاصطناعي • اللامركزية"
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

        // 2. Interactive Force Network (Vis.js Engine)
        const container = document.getElementById('cosmic-network-canvas');
        const nodesDataSet = new vis.DataSet(rawGraphData.nodes);
        const edgesDataSet = new vis.DataSet(rawGraphData.edges);

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

        const cosmicNetwork = new vis.Network(container, {{ nodes: nodesDataSet, edges: edgesDataSet }}, networkOptions);

        let activeGraphCategory = 'ALL';
        const drawer = document.getElementById('reader-drawer');
        const drawerTitle = document.getElementById('drawer-title');
        const drawerMeta = document.getElementById('drawer-meta');
        const drawerBody = document.getElementById('drawer-body');
        const drawerConns = document.getElementById('drawer-connections-pills');

        function openDrawer(nodeData) {{
            drawerTitle.innerText = nodeData.label;
            drawerMeta.innerHTML = `
                <span class="meta-tag">🏷️ ${{nodeData.category}}</span>
                <span class="meta-tag">🔗 ${{nodeData.degree}} روابط</span>
                ${{(nodeData.tags || []).map(t => `<span class="meta-tag">#${{t}}</span>`).join('')}}
            `;
            drawerBody.innerHTML = marked.parse(nodeData.body || nodeData.snippet || 'لا يوجد محتوى.');
            const connectedIds = cosmicNetwork.getConnectedNodes(nodeData.id);
            drawerConns.innerHTML = connectedIds.map(cid => {{
                const targetNode = rawGraphData.nodes.find(n => n.id === cid);
                const lbl = targetNode ? targetNode.label : cid;
                return `<span class="conn-pill" onclick="focusOnNode('${{cid}}')">${{lbl}}</span>`;
            }}).join('');
            drawer.classList.add('open');
            highlightNeighborhood(nodeData.id);
        }}

        function closeDrawer() {{
            drawer.classList.remove('open');
            resetFocus();
        }}

        function highlightNeighborhood(nodeId) {{
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
            nodesDataSet.forEach(node => nodesDataSet.update({{ id: node.id, opacity: 1, font: {{ color: '#f0f6fc' }} }}));
            edgesDataSet.forEach(edge => edgesDataSet.update({{ id: edge.id, color: {{ color: 'rgba(90, 105, 120, 0.35)' }}, width: 1.3 }}));
        }}

        function focusOnNode(nodeId) {{
            const nodeData = rawGraphData.nodes.find(n => n.id === nodeId);
            if (!nodeData) return;
            cosmicNetwork.focus(nodeId, {{ scale: 1.25, animation: {{ duration: 600 }} }});
            openDrawer(nodeData);
        }}

        cosmicNetwork.on("click", function (params) {{
            if (params.nodes.length > 0) {{
                const nodeData = rawGraphData.nodes.find(n => n.id === params.nodes[0]);
                if (nodeData) openDrawer(nodeData);
            }} else {{
                closeDrawer();
            }}
        }});

        function filterGraphCategory(catName) {{
            activeGraphCategory = catName;
            document.querySelectorAll('.filter-pill').forEach(btn => {{
                btn.classList.toggle('active', btn.innerText.includes(catName) || (catName === 'ALL' && btn.innerText.includes('الكل')));
            }});

            if (catName === 'ALL') {{
                nodesDataSet.forEach(n => nodesDataSet.update({{ id: n.id, hidden: false }}));
            }} else {{
                nodesDataSet.forEach(n => {{
                    nodesDataSet.update({{ id: n.id, hidden: (n.category !== catName) }});
                }});
            }}
            cosmicNetwork.fit({{ animation: true }});
        }}

        document.getElementById('graph-search-input').addEventListener('input', function(e) {{
            const query = e.target.value.toLowerCase().trim();
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
                const match = node.label.toLowerCase().includes(query) || 
                              node.id.toLowerCase().includes(query) ||
                              (node.tags && node.tags.some(t => t.toLowerCase().includes(query))) ||
                              node.category.toLowerCase().includes(query);
                nodesDataSet.update({{ id: node.id, hidden: !match }});
                if (match && !firstMatch) firstMatch = node.id;
            }});
            if (firstMatch) cosmicNetwork.focus(firstMatch, {{ scale: 1.1, animation: true }});
        }});

        let cosmicPhysicsRunning = true;
        function toggleCosmicPhysics() {{
            cosmicPhysicsRunning = !cosmicPhysicsRunning;
            cosmicNetwork.setOptions({{ physics: {{ enabled: cosmicPhysicsRunning }} }});
            const btn = document.getElementById('physics-toggle-btn');
            btn.innerHTML = cosmicPhysicsRunning ? '⏸ تثبيت الحركة' : '▶ تحريك الأجرام';
        }}

        // CHAKRAS & PROPHETIC BODILY CENTRES DATA
        const CHAKRAS_DATA = [
            {{
                id: 8,
                name: "الهالة المحيطة الكبرى (The Auric Field / نور النبوة)",
                sanskrit: "أورا براكاشا (Aura Prakasha) • النور الأكبر",
                sufiLatifa: "اللطيفة الأحدية / مقام العرش الأطلس وسدرة المنتهى",
                colorName: "النور الأبيض اللؤلؤي المتوهج بالذهب (White & Gold)",
                colorHex: "#ffffff",
                prophet: "النبي الخاتم محمد صلى الله عليه وسلم (الحقيقة المحمدية)",
                sphere: "فلك العرش الكلي المحيط الأكبر ما وراء السماوات السبع",
                metal: "الأثير الكوني الخالص (الجوهر الفرد / Quintessence)",
                organ: "الهالة النورانية المحيطة بكامل الجسد والروح",
                quran: "«وَإِنَّكَ لَعَلَىٰ خُلُقٍ عَظِيمٍ» [القلم: 4] • «ثُمَّ دَنَا فَتَدَلَّىٰ * فَكَانَ قَابَ قَوْسَيْنِ أَوْ أَدْنَىٰ» [النجم: 8-9] • «يَا أَيُّهَا النَّبِيُّ إِنَّا أَرْسَلْنَاكَ شَاهِدًا وَمُبَشِّرًا وَنَذِيرًا * وَدَاعِيًا إِلَى اللَّهِ بِإِذْنِهِ وَسِرَاجًا مُّنِيرًا».",
                shift: "وعي الكمال الإنساني الجامع (الإنسان الكامل): ختام النبوات، جمع دائرة البروج الاثني عشر تحت نور واحد، التحول من التشتت في العوالم إلى مقام السراج المنير الذي يفيض الرحمة على الخلائق أجمعين.",
                proof: "«فص حكمة فردية في كلمة محمدية» — ابن عربي في الفصوص: الحقيقة المحمدية هي الفلك المحيط الأعظم، وأول التعينات النورانية، وبها تتنزل الأنوار على سائر الأفلاك والأنبياء والمقامات."
            }},
            {{
                id: 7,
                name: "شاكرا التاج (Sahasrara - ساهاسرارا)",
                sanskrit: "زهرة اللوتس ذات الألف بتلة (Sahasrara)",
                sufiLatifa: "سر السر (Sirr al-Sirr) • الخفاء والتوحيد الصرف",
                colorName: "البنفسجي الملكي والأبيض الشفاف (Violet & Pure White)",
                colorHex: "#a855f7",
                prophet: "النبي إبراهيم الخليل عليه السلام (إمام الحنفاء)",
                sphere: "فلك زحل (السماء السابعة عند البيت المعمور)",
                metal: "الرصاص (Lead - Pb) • أصل التحول الخيميائي",
                organ: "أعلى الرأس، الغدة الصنوبرية (Pineal Gland)، القشرة الدماغية",
                quran: "«إِنِّي وَجَّهْتُ وَجْهِيَ لِلَّذِي فَطَرَ السَّمَاوَاتِ وَالْأَرْضَ حَنِيفًا وَمَا أَنَا مِنَ الْمُشْرِكِينَ» [الأنعام: 79] • كسر أصنام الكواكب والوصول إلى خالق الأكوان.",
                shift: "وعي التوحيد المفارق والصمت الأبدي: التجرد المطلق من التعلق بالصور والآفات الزائلة، ملامسة مكعب التوحيد الخالص (الكعبة المشرفة)، وفناء الأوهام في نور الحق.",
                proof: "«فص حكمة مهيمية في كلمة إبراهيمية» — ابن عربي: إبراهيم هو الخليل الذي تخللت محبته كل ذرات الوجود، مقامه زحل (التجرد والصمت الأبدي وبناء بيت الله الحرام)."
            }},
            {{
                id: 6,
                name: "شاكرا العين الثالثة (Ajna - آجنا)",
                sanskrit: "مركز البصيرة والأمر (Ajna)",
                sufiLatifa: "لطيفة الأخفى (Al-Akhfa) • البصيرة اللدنية",
                colorName: "الأزرق النيلي العميق (Indigo)",
                colorHex: "#3b82f6",
                prophet: "النبي موسى وهارون عليهما السلام (الكليم والشريعة)",
                sphere: "فلك المشتري (السماء السادسة) • كوكب العدالة والرحمة",
                metal: "القصدير (Tin - Sn)",
                organ: "الجبهة بين الحاجبين، الغدة النخامية (Pituitary)، العينان",
                quran: "«وَلَمَّا جَاءَ مُوسَىٰ لِمِيقَاتِنَا وَكَلَّمَهُ رَبُّهُ» [الأعراف: 143] • تنزيل ألواح التوراة والوصايا العشر لإقامة ميزان العدل والحكمة الكلية.",
                shift: "وعي البصيرة الكلية والناموس: تجاوز الرؤية البصرية الظاهرة إلى الرؤية الباطنية، إدراك نواميس القضاء والقدر، وقراءة مقادير الأحداث ومآلات الأمم قبل وقوعها.",
                proof: "«فص حكمة علوية في كلمة هارونية» — ابن عربي: هارون وموسى جمعا بين نور البصيرة المشترية التشريعية وحكمة تدبير الأمة."
            }},
            {{
                id: 5,
                name: "شاكرا الحنجرة والنطق (Vishuddha - فيشودها)",
                sanskrit: "مركز النقاء والتطهير بالصوت (Vishuddha)",
                sufiLatifa: "لطيفة الخفي (Al-Khafi) • سر الكلمة الإلهية",
                colorName: "الأزرق الفيروزي السماوي (Cyan / Sky Blue)",
                colorHex: "#00f0ff",
                prophet: "النبي داود وسليمان عليهما السلام (صهر الحديد والمزامير)",
                sphere: "فلك المريخ (السماء الخامسة) • فلك الشدة والبأس والتردد الصوتي",
                metal: "الحديد (Iron - Fe) • «وَأَلَنَّا لَهُ الْحَدِيدَ»",
                organ: "الحنجرة، الحبال الصوتية، الغدة الدرقية، الرقبة",
                quran: "«يَا جِبَالُ أَوِّبِي مَعَهُ وَالطَّيْرَ ۖ وَأَلَنَّا لَهُ الْحَدِيدَ» [سبأ: 10] • تسبيح الجبال مع مزامير داود (فيزياء الهارموني والتردد الصوتي الكوني).",
                shift: "وعي الكلمة الصادقة الحاكمة وسلطان الحق: تسخير الترددات الصوتية لتغيير المادة الفيزيائية (تليين الحديد)، قول الحق بشجاعة دون خوف من الطغاة، ومطابقة النطق لمراد الله.",
                proof: "«رسائل إخوان الصفا»: النغمات الموسيقية والأصوات الموزونة تحاكي نغمات حركات الأفلاك وتطهر النفس من كدر الطبيعة."
            }},
            {{
                id: 4,
                name: "شاكرا القلب والصدر (Anahata - أناهاتا)",
                sanskrit: "الصوت الذي لا يُقرع • المركز الكوني (Anahata)",
                sufiLatifa: "لطيفة السر (Al-Sirr) • شمس الروح والمحبة الخالصة",
                colorName: "الأخضر الزمردي المتألق بالذهب الشمسي (Emerald & Gold)",
                colorHex: "#10b981",
                prophet: "السيد المسيح عيسى عليه السلام والنبي إدريس",
                sphere: "فلك الشمس (السماء الرابعة) • قلب المنظومة الكونية",
                metal: "الذهب الخالص (Gold - Au)",
                organ: "القلب العضوي، التيموس (Thymus)، الرئتان والدورة الدموية",
                quran: "«وَآتَيْنَا عِيسَى ابْنَ مَرْيَمَ الْبَيِّنَاتِ وَأَيَّدْنَاهُ بِرُوحِ الْقُدُسِ» [البقرة: 87] • إحياء الموتى وإبراء الأكمه والأبرص بالنفخة الروحية القلبية.",
                shift: "وعي شمس الروح والمحبة غير المشروطة: ولادة الإنسان الحقيقي في باطن الجسد، التسامي فوق الحرفية القاتلة للناموس لصالح روح الإحياء، والشفاء الذاتي وفيض الرحمة.",
                proof: "«فص حكمة روحية في كلمة عيسوية» — ابن عربي: عيسى هو النفس الإلهي النازل بالروح، مقامه فلك الشمس الذي يفيض الحياة على الوجود كله."
            }},
            {{
                id: 3,
                name: "شاكرا الضفيرة الشمسية (Manipura - مانيبورا)",
                sanskrit: "مدينة الجواهر والحرارة (Manipura)",
                sufiLatifa: "لطيفة القلب الظاهر / النفس المطمئنة",
                colorName: "الأصفر الشمسي الذهبي (Solar Yellow)",
                colorHex: "#f59e0b",
                prophet: "النبي يوسف الصديق عليه السلام (شمس الرؤى والجمال)",
                sphere: "فلك الزهرة (السماء الثالثة) • فلك الجمال والتناغم",
                metal: "النحاس (Copper - Cu)",
                organ: "فم المعدة، الكبد، البنكرياس، الجهاز الهضمي والتمثيل الغذائي",
                quran: "«إِنِّي رَأَيْتُ أَحَدَ عَشَرَ كَوْكَبًا وَالشَّمْسَ وَالْقَمَرَ رَأَيْتُهُمْ لِي سَاجِدِينَ» [يوسف: 4] • «مَعَاذَ اللَّهِ ۖ إِنَّهُ رَبِّي أَحْسَنَ مَثْوَايَ».",
                shift: "وعي السيادة وتسامي الرغبات الحسية: ترويض إرادة القوة والشهوات الدنيوية، تحويل طاقة الانجذاب الغريزي إلى بهاء جمالي روحي خالص، وحكمة إدارة موارد الأرض في سنين الشدة.",
                proof: "«فص حكمة نورية في كلمة يوسفية» — ابن عربي: يوسف تجلت فيه مرآة الجمال المطلق، فعف عن المعصية وساد بالعلم وتأويل الرؤى."
            }},
            {{
                id: 2,
                name: "شاكرا العجز وأسفل البطن (Svadhisthana - سفاديستانا)",
                sanskrit: "المستقر الذاتي والرحم المائي (Svadhisthana)",
                sufiLatifa: "لطيفة النفس (Al-Nafs) • التطهير من طوفان الشهوات",
                colorName: "البرتقالي المتوهج الناري (Vibrant Orange)",
                colorHex: "#f97316",
                prophet: "النبي نوح عليه السلام (شيخ أولي العزم والنجاة)",
                sphere: "فلك عطارد والماء الكوني • فلك الفلك المشحون والسرطان",
                metal: "الزئبق المائي (Quicksilver - Hg)",
                organ: "أسفل السرة، الحوض، المثانة، الأعضاء التناسلية الداخلية",
                quran: "«وَاصْنَعِ الْفُلْكَ بِأَعْيُنِنَا وَوَحْيِنَا» • «حَتَّىٰ إِذَا جَاءَ أَمْرُنَا وَفَارَ التَّنُّورُ قُلْنَا احْمِلْ فِيهَا مِن كُلٍّ زَوْجَيْنِ اثْنَيْنِ» [هود: 37-40].",
                shift: "وعي النجاة وحفظ بذور الحياة: التطهير من طوفان المشاعر الغامرة والغرائز المنفلتة، بناء فلك النجاة الروحي لحمل بذور الفطرة السليمة، والعبور إلى عهد الإنسانية الجديد.",
                proof: "«فص حكمة سبوحية في كلمة نوحية» — ابن عربي: فلك نوح هو سر النجاة في طوفان الكثرة، وهو تطهير عالم الماء الباطني لولادة العهد الجديد."
            }},
            {{
                id: 1,
                name: "شاكرا الجذر والقاعدة (Muladhara - مولادارا)",
                sanskrit: "الجذر الأساسي للوجود (Muladhara)",
                sufiLatifa: "لطيفة القالب والجسد الترابي (Al-Qalib)",
                colorName: "الأحمر الياقوتي الأرضي (Deep Ruby Red)",
                colorHex: "#ef4444",
                prophet: "النبي آدم عليه السلام (أبو البشرية وبداية التجسد)",
                sphere: "فلك القمر (السماء الدنيا) • مجمع الطينات وعالم الكون والفساد",
                metal: "الفضة والصلصال الفخاري (Silver & Clay)",
                organ: "قاعدة العمود الفقري، العجان، عظم العجز، الساقان والعظام",
                quran: "«إِنِّي جَاعِلٌ فِي الْأَرْضِ خَلِيفَةً» • «وَعَلَّمَ آدَمَ الْأَسْمَاءَ كُلَّهَا» [البقرة: 30-31] • «خَلَقَ الْإِنسَانَ مِن صَلْصَالٍ كَالْفَخَّارِ».",
                shift: "وعي التجسد والاستخلاف في الأرض: إدراك قدسية الجسد المادي كمعبد للروح، التحرر من الخوف من الموت والفقر، وفك شيفرة أسماء الكائنات والمفاهيم الكونية.",
                proof: "«الإنسان الكامل» — الجيلي: آدم هو مظهر الاسم الإلهي 'الله' في عالم الأجسام، وقاعدته ترابية تنبثق منها سائر المراتب الروحية."
            }}
        ];

        function renderChakras() {{
            selectChakra(8);
        }}

        function selectChakra(id) {{
            const c = CHAKRAS_DATA.find(x => x.id === id);
            if (!c) return;
            document.querySelectorAll('.chakra-point-btn').forEach(btn => btn.classList.remove('active'));
            const activeNode = document.getElementById('chakra-node-' + id);
            if (activeNode) activeNode.classList.add('active');

            const container = document.getElementById('chakra-detail-card');
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
                        <div class="c-spec-label">اللون والتردد في المتون القديمة</div>
                        <div class="c-spec-val" style="color:${{c.colorHex}};">${{c.colorName}}</div>
                    </div>
                    <div class="c-spec-item">
                        <div class="c-spec-label">المعدن الخيميائي وعضو الجسد</div>
                        <div class="c-spec-val">${{c.metal}} • ${{c.organ}}</div>
                    </div>
                </div>

                <div class="c-box quran-box" style="margin-bottom: 20px;">
                    <div class="c-step-badge c-step-quran">📖 الشاهد والسر القرآني الحاكم</div>
                    <div style="font-size:0.95rem; font-weight:600; line-height:1.8;">${{c.quran}}</div>
                </div>

                <div class="chakra-deep-desc">
                    <div style="color:var(--gold); font-weight:700; margin-bottom:8px;">🌟 النقلة في الوعي الإنساني ومستوى الاستنارة الباطنية:</div>
                    ${{c.shift}}
                </div>

                <div class="chakra-proof-quote">
                    <strong>📜 الشاهد من أمهات المخطوطات والكتب (الفصوص / الكيباليون / إخوان الصفا / الجيلي):</strong><br>
                    ${{c.proof}}
                </div>
            `;
        }}

        // 3. Spheres Ladder Renderer
        function renderSpheres() {{
            const listContainer = document.getElementById('spheres-list');
            listContainer.innerHTML = SPHERES_DATA.map((s, idx) => `
                <div class="sphere-card ${{idx === 0 ? 'active' : ''}}" 
                     style="--sphere-color: ${{s.color}}" 
                     onclick="selectSphere(${{s.id}})">
                    <div class="sphere-rank">${{s.id}}</div>
                    <div class="sphere-info">
                        <h3>${{s.name}}</h3>
                        <span>${{s.prophet}} • ${{s.metal}}</span>
                    </div>
                </div>
            `).join('');
            selectSphere(8);
        }}

        function selectSphere(id) {{
            const s = SPHERES_DATA.find(x => x.id === id);
            if (!s) return;
            document.querySelectorAll('.sphere-card').forEach(c => {{
                c.classList.toggle('active', c.querySelector('.sphere-rank').innerText == id);
            }});
            const detailContainer = document.getElementById('sphere-detail');
            detailContainer.innerHTML = `
                <div class="detail-header">
                    <h2>${{s.name}}</h2>
                    <span class="detail-badge">${{s.rank}}</span>
                </div>
                <div class="prophet-banner">
                    <div class="prophet-avatar">👑</div>
                    <div class="prophet-desc">
                        <h4>${{s.prophet}}</h4>
                        <p>${{s.titleDesc}}</p>
                    </div>
                </div>
                <div class="specs-grid">
                    <div class="spec-box"><div class="spec-label">الشاكرا والمركز الجسدي</div><div class="spec-value">${{s.chakra}}</div></div>
                    <div class="spec-box"><div class="spec-label">المعدن الخيميائي</div><div class="spec-value">${{s.metal}}</div></div>
                    <div class="spec-box"><div class="spec-label">المبدأ الهرمسي</div><div class="spec-value">${{s.hermetic}}</div></div>
                    <div class="spec-box"><div class="spec-label">النوتة والتردد الصوتي</div><div class="spec-value">${{s.note}}</div></div>
                </div>
                <div style="margin-bottom: 20px; font-size: 0.95rem; line-height: 1.7; color: var(--text-main);">${{s.desc}}</div>
                <div class="textual-proof"><strong>الشاهد من المخطوط الأصلي:</strong><br>${{s.proof}}</div>
            `;
        }}

        // 4. Zodiac Renderer
        function renderZodiac(filter = 'ALL') {{
            const container = document.getElementById('zodiac-grid');
            const filtered = filter === 'ALL' ? ZODIAC_12_DATA : ZODIAC_12_DATA.filter(z => z.element.includes(filter));
            container.innerHTML = filtered.map(z => `
                <div class="zodiac-card">
                    <div>
                        <div class="zodiac-card-header">
                            <div class="zodiac-glyph">${{z.glyph}}</div>
                            <span class="zodiac-element ${{z.elemClass}}">${{z.element}} • ${{z.quality}}</span>
                        </div>
                        <h3 class="zodiac-name">${{z.name}}</h3>
                        <div class="zodiac-latin">${{z.latin}} — يقابله: <b style="color:var(--rose);">${{z.opposing}}</b></div>
                        
                        <div class="z-prop-list">
                            <div class="z-prop-row"><span class="z-prop-lbl">الكوكب الحاكم:</span><span class="z-prop-val">${{z.ruler}}</span></div>
                            <div class="z-prop-row"><span class="z-prop-lbl">العضو الجسدي:</span><span class="z-prop-val">${{z.organ}}</span></div>
                            <div class="z-prop-row"><span class="z-prop-lbl">السبط الكابالي:</span><span class="z-prop-val">${{z.tribe}}</span></div>
                            <div class="z-prop-row"><span class="z-prop-lbl">حرف التكوين:</span><span class="z-prop-val">${{z.letter}}</span></div>
                        </div>

                        <p class="zodiac-desc">${{z.desc}}</p>
                    </div>
                </div>
            `).join('');
        }}

        function filterZodiac(cat) {{
            document.querySelectorAll('.z-filter-btn').forEach(b => {{
                b.classList.toggle('active', b.innerText.includes(cat) || (cat === 'ALL' && b.innerText.includes('جميع')));
            }});
            renderZodiac(cat);
        }}

        // 5. Timeline Renderer
        function renderTimeline() {{
            const container = document.getElementById('timeline-grid');
            container.innerHTML = AGES_DATA.map(a => `
                <div class="age-card">
                    <div class="age-era">${{a.era}}</div>
                    <h3 class="age-title">${{a.title}}</h3>
                    <div class="polarity-tag">${{a.polarity}}</div>
                    <p class="age-desc">${{a.desc}}</p>
                    <div class="age-symbols"><strong>الرموز:</strong> ${{a.symbols}}</div>
                </div>
            `).join('');
        }}

        // 6. Matrix Renderer
        function renderMatrix() {{
            const tbody = document.getElementById('matrix-tbody');
            tbody.innerHTML = SPHERES_DATA.map(s => `
                <tr>
                    <td><b>${{s.id}}</b></td>
                    <td><b style="color:${{s.color}}">${{s.name}}</b></td>
                    <td><b>${{s.prophet}}</b></td>
                    <td>${{s.patriarch}}</td>
                    <td>${{s.hermetic.split('(')[0]}}</td>
                    <td>${{s.chakra}}</td>
                    <td><b>${{s.metal}}</b></td>
                    <td>${{s.titleDesc}}</td>
                </tr>
            `).join('');
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

        // Initialize All Systems
        renderSpheres();
        renderChakras();
        renderZodiac('ALL');
        renderTimeline();
        renderMatrix();
        renderManuscripts();
        renderCritique();
    
        // ========================================================
        // GRAPH DUAL MODE: THEORY ATLAS & ZERO-LAG CONTROLLER
        // ========================================================
        let currentGraphMode = 'theory';

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
