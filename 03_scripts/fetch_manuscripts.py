"""
Manuscript & Core Text Downloader for Knowledge_Lab
Downloads authentic public-domain texts and core manuscripts
directly into 01_raw_pdf for analysis and pipeline ingestion.
"""

import os
import sys
import urllib.request
from pathlib import Path

# Force UTF-8 on Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_PDF_DIR = BASE_DIR / "01_raw_pdf"
RAW_PDF_DIR.mkdir(parents=True, exist_ok=True)

MANUSCRIPTS = [
    {
        "filename": "The_Book_of_Enoch_RH_Charles.txt",
        "url": "https://www.gutenberg.org/cache/epub/33034/pg33034.txt",
        "title": "سفر أخنوخ (The Book of Enoch - R.H. Charles Edition)",
        "desc": "أقدم نص تفصيلي عن الأفلاك السبعة، الملائكة العلوية، ونهايات العصور الكونية"
    },
    {
        "filename": "The_Kybalion_Hermetic_Philosophy.txt",
        "url": "https://www.gutenberg.org/cache/epub/14209/pg14209.txt",
        "title": "كتاب الكيباليون (The Kybalion - Three Initiates)",
        "desc": "المبادئ الهرمسية السبعة للكون وموسيقى الاهتزاز والقطبية"
    }
]


def download_all():
    print("[+] Starting download of primary manuscripts to 01_raw_pdf...\n")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    for item in MANUSCRIPTS:
        target_path = RAW_PDF_DIR / item["filename"]
        if target_path.exists() and target_path.stat().st_size > 1000:
            print(f"  [✔] Already exists: {item['title']}")
            continue
            
        print(f"  [↓] Downloading: {item['title']}...")
        try:
            req = urllib.request.Request(item["url"], headers=headers)
            with urllib.request.urlopen(req, timeout=20) as response:
                content = response.read()
                target_path.write_bytes(content)
            print(f"      [OK] Downloaded ({len(content) // 1024} KB) -> {target_path.name}")
        except Exception as e:
            print(f"      [!] Failed to download: {e}")


if __name__ == "__main__":
    download_all()
