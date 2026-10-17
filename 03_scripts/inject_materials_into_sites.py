import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

with open("03_scripts/materials_block.html", "r", encoding="utf-8") as f:
    materials_block = f.read()

target_files = [
    "website/index.html",
    "docs/index.html",
    "index.html",
    "website/Grand_Occult_Cosmology_Codex.html",
    "Grand_Occult_Cosmology_Codex.html",
    "website/.vercel/output/static/index.html",
    "website/.vercel/output/static/Grand_Occult_Cosmology_Codex.html"
]

marker = "<!-- ======================================================================== -->\n            <!-- 📜 الأطروحة الأكاديمية الشاملة: بردية لندن وليدن السحرية الديموطيقية (15139) -->"

for fpath in target_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    if "demotic-materials-atlas" in content:
        # replace existing
        pat = re.compile(r'<!-- =+\s*-->\s*<!-- 🔬 الأطلس المادي والصيدلاني الشامل.*?<!-- =+\s*-->', re.DOTALL)
        if pat.search(content):
            content = pat.sub(materials_block, content)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated existing materials block in: {fpath}")
            continue

    pos = content.find("<!-- ======================================================================== -->\n            <!-- 📜 الأطروحة الأكاديمية الشاملة")
    if pos != -1:
        # insert after the doctoral chamber
        end_chamber = content.find("<!-- ======================================================================== -->", pos + 100)
        if end_chamber != -1:
            end_chamber_close = content.find("</div>", end_chamber - 200)
            # find end of demotic-papyrus-chamber div
            pos_div_close = content.find("<!-- ======================================================================== -->", end_chamber + 1)
            # let's insert right after the demotic-papyrus-chamber container
            insert_point = content.find("</div>\n            <!-- ======================================================================== -->", pos)
            if insert_point != -1:
                insert_point += len("</div>\n            <!-- ======================================================================== -->")
                content = content[:insert_point] + "\n" + materials_block + content[insert_point:]
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Injected materials block in: {fpath}")
                continue

    # fallback: insert before </section> of tab-manuscripts
    pos_sec = content.find("</section>", content.find("id=\"tab-manuscripts\""))
    if pos_sec != -1:
        content = content[:pos_sec] + "\n" + materials_block + "\n" + content[pos_sec:]
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Injected materials block via fallback in: {fpath}")
    else:
        print(f"Could not inject into: {fpath}")