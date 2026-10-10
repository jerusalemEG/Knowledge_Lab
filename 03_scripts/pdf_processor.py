"""
PDF & Manuscript Extraction Pipeline for Knowledge_Lab (v2.0 Universal)
Processes both PDF and TXT manuscripts, extracts astronomical & cosmological data,
generates atomic notes in 02_vault, and links them into the Knowledge Graph.
"""

import os
import re
import sys
from pathlib import Path

# Force UTF-8 on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "01_raw_pdf"
VAULT_DIR = BASE_DIR / "02_vault"
EXTRACTED_DIR = VAULT_DIR / "06_Extracted_Books"
EXTRACTED_DIR.mkdir(parents=True, exist_ok=True)


def get_existing_vault_concepts():
    concepts = {}
    for f in VAULT_DIR.rglob("*.md"):
        if ".obsidian" in str(f):
            continue
        stem = f.stem
        clean_name = stem.replace("_", " ").lower()
        concepts[clean_name] = stem
        try:
            txt = f.read_text(encoding="utf-8", errors="ignore")
            title_m = re.search(r"title:\s*(.*)", txt)
            if title_m:
                t = title_m.group(1).strip().strip('"').strip("'")
                concepts[t.lower()] = stem
        except Exception:
            pass
    return concepts


def extract_txt_data(txt_path: Path):
    print(f"\n[+] جارٍ فحص وتحليل المخطوطة النصية: {txt_path.name}...")
    content = txt_path.read_text(encoding="utf-8", errors="ignore")
    lines = content.splitlines()
    
    # Extract title from text or filename
    title = txt_path.stem.replace("_", " ")
    for line in lines[:30]:
        line_clean = line.strip()
        if line_clean.lower().startswith("title:"):
            title = line_clean.split(":", 1)[1].strip()
            break
            
    # Sample meaningful text
    meaningful = [l.strip() for l in lines if len(l.strip()) > 30 and not l.strip().startswith("***") and "gutenberg" not in l.lower()]
    sample_text = "\n\n".join(meaningful[:25])
    
    return {
        "title": title,
        "filename": txt_path.name,
        "total_chars": len(content),
        "total_lines": len(lines),
        "has_text": True,
        "is_scanned": False,
        "sample": sample_text,
        "full_text": content
    }


def auto_link_text(content: str, existing_concepts: dict) -> str:
    linked = content
    keyword_map = {
        "أبو معشر": "Abu_Mashar_al_Balkhi",
        "القزويني": "Zakariya_al_Qazwini",
        "إخوان الصفا": "Ikhwan_al_Safa",
        "الميلوثيسيا": "Melothesia_Body_Cosmos_Mapping",
        "ترنح المحور": "Axial_Precession_25920",
        "السنة الأفلاطونية": "Axial_Precession_25920",
        "لوح الزمرد": "Hermes_Trismegistus_Emerald_Tablet",
        "الكيباليون": "Seven_Hermetic_Principles_Kybalion",
        "عصر الثور": "Age_of_Taurus_Scorpio_Polarity",
        "عصر الحمل": "Age_of_Aries_Libra_Polarity",
        "عصر الحوت": "Age_of_Pisces_Virgo_Polarity",
        "عصر الدلو": "Age_of_Aquarius_Leo_Polarity",
        "سفر أخنوخ": "The_Book_of_Enoch_Astronomical_Secrets",
        "Enoch": "The_Book_of_Enoch_Astronomical_Secrets",
        "Kybalion": "Seven_Hermetic_Principles_Kybalion",
        "Hermes": "Hermes_Trismegistus_Emerald_Tablet"
    }
    
    for kw, node_id in keyword_map.items():
        if f"[[{node_id}]]" not in linked:
            pattern = re.compile(rf"(?<!\[\[)({re.escape(kw)})(?!\]\])", re.IGNORECASE)
            linked = pattern.sub(f"[[{node_id}|\\1]]", linked)
            
    return linked


def generate_vault_note(data: dict, existing_concepts: dict):
    slug = re.sub(r"[^\w\u0600-\u06FF]+", "_", data["filename"]).strip("_")
    out_file = EXTRACTED_DIR / f"{slug}.md"
    
    linked_sample = auto_link_text(data["sample"][:4000], existing_concepts)

    content = f"""---
title: "{data['title']}"
type: source_manuscript
source_file: "{data['filename']}"
status: processed
tags:
  - source
  - manuscript
  - astronomy
  - perennial_philosophy
created: 2026-10-10
connections:
  - "[[Universal_Esoteric_Map_of_Consciousness]]"
  - "[[MOC_Grand_Knowledge_Synthesis]]"
  - "[[Seven_Hermetic_Principles_Kybalion]]"
---

# {data['title']}

> **بيانات المخطوطة الأصلية:**
> - **اسم الملف:** `{data['filename']}`
> - **الحجم والإحصاء:** {data.get('total_lines', 'N/A')} سطر / {data.get('total_chars', 0) // 1024} كيلوبايت.
> - **التصنيف المعرفي:** متون تأسيسية في فلك النبوات والكوزمولوجيا الباطنية.

---

## 1. جوهر النص والمقاطع المستخلصة
{linked_sample}

---

## 2. التقاطعات الكبرى مع منظومة المعرفة
- [[Universal_Esoteric_Map_of_Consciousness]]: موقع المخطوطة في سلم ارتقاء الوعي والأفلاك.
- [[MOC_Grand_Knowledge_Synthesis]]: الفهرس البانورامي الشامل.
- [[Axial_Precession_25920]]: تقاطع الحسابات مع ترنح المحور والسنة الأفلاطونية.
"""

    out_file.write_text(content, encoding="utf-8")
    print(f"    [✔] تم توليد النوتة الذرية: {out_file.name}")
    return out_file


def process_all_files():
    existing_concepts = get_existing_vault_concepts()
    
    # Process TXT files
    txt_files = list(RAW_DIR.glob("*.txt"))
    for tf in txt_files:
        data = extract_txt_data(tf)
        generate_vault_note(data, existing_concepts)
        
    # Process PDF files if any
    try:
        import fitz
        pdf_files = list(RAW_DIR.glob("*.pdf"))
        for pf in pdf_files:
            print(f"\n[+] جارٍ معالجة PDF: {pf.name}...")
            doc = fitz.open(pf)
            texts = [p.get_text() for p in doc[:20]]
            sample = "\n\n".join(texts)
            data = {
                "title": pf.stem.replace("_", " "),
                "filename": pf.name,
                "total_lines": len(doc),
                "total_chars": sum(len(t) for t in texts),
                "sample": sample
            }
            generate_vault_note(data, existing_concepts)
    except Exception as e:
        pass
        
    print("\n[+] تحديث شبكة المعرفة الكلية...")
    import graph_builder
    nodes, links = graph_builder.scan_vault()
    graph_builder.generate_html_viewer(nodes, links)
    print("[✔] تم تحديث شبكة المعرفة وعرض المتصفح بالكامل!")


if __name__ == "__main__":
    process_all_files()
