import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

with open("03_scripts/interactive_translation_block.html", "r", encoding="utf-8") as f:
    block = f.read()

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
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    if "demotic-translation-grand-chamber" in content:
        pat = re.compile(r'<!-- =+\s*-->\s*<!-- 🏛️ الديوان المترجم الشامل.*?<!-- =+\s*-->', re.DOTALL)
        if pat.search(content):
            content = pat.sub(block, content)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated interactive block in: {fpath}")
            continue

    pos = content.find("class=\"demotic-materials-atlas\"")
    if pos != -1:
        # find end of demotic-materials-atlas
        end_atlas = content.find("<!-- ======================================================================== -->", pos)
        if end_atlas != -1:
            end_atlas_close = content.find("</div>\n            <!-- ======================================================================== -->", pos)
            if end_atlas_close != -1:
                insert_pt = end_atlas_close + len("</div>\n            <!-- ======================================================================== -->")
                content = content[:insert_pt] + "\n" + block + content[insert_pt:]
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Injected interactive block after materials atlas in: {fpath}")
                continue

    # fallback: insert before </section> in tab-manuscripts
    pos_sec = content.find("</section>", content.find("id=\"tab-manuscripts\""))
    if pos_sec != -1:
        content = content[:pos_sec] + "\n" + block + "\n" + content[pos_sec:]
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Injected interactive block via fallback in: {fpath}")
    else:
        print(f"Could not inject into: {fpath}")