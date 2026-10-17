import os, sys
sys.stdout.reconfigure(encoding="utf-8")

target_files = [
    "website/index.html",
    "docs/index.html",
    "index.html",
    "website/Grand_Occult_Cosmology_Codex.html",
    "Grand_Occult_Cosmology_Codex.html",
    "website/.vercel/output/static/index.html",
    "website/.vercel/output/static/Grand_Occult_Cosmology_Codex.html"
]

for fpath in target_files:
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
        has_doc = "الأطروحة الأكاديمية الشاملة" in c
        print(f"{fpath} -> Contains Doctoral Chamber: {has_doc} (Size: {len(c)} bytes)")