import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

with open("03_scripts/doctoral_block.html", "r", encoding="utf-8") as f:
    new_block = f.read()

target_files = [
    "website/index.html",
    "docs/index.html",
    "index.html",
    "website/Grand_Occult_Cosmology_Codex.html",
    "Grand_Occult_Cosmology_Codex.html",
    "website/.vercel/output/static/index.html",
    "website/.vercel/output/static/Grand_Occult_Cosmology_Codex.html"
]

pattern = re.compile(r'<!-- =+\s*-->\s*<!-- 📜 دراسة ومخطوطة بردية لندن.*?<!-- =+\s*-->', re.DOTALL)

for fpath in target_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    if pattern.search(content):
        content = pattern.sub(new_block, content)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Replaced old block with full doctoral block in: {fpath}")
    else:
        # Check if old block wasn't present, try books-grid
        if "demotic-papyrus-chamber" not in content:
            pos = content.find("id=\"books-grid\"></div>")
            if pos != -1:
                insert_pos = pos + len("id=\"books-grid\"></div>")
                content = content[:insert_pos] + "\n" + new_block + content[insert_pos:]
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Inserted fresh doctoral block in: {fpath}")
        else:
            # Replace whatever demotic-papyrus-chamber is there
            pat2 = re.compile(r'<div class="demotic-papyrus-chamber".*?<!-- =+\s*-->', re.DOTALL)
            if pat2.search(content):
                content = pat2.sub(new_block, content)
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Replaced via pat2 in: {fpath}")
            else:
                print(f"Could not match pattern in: {fpath}")