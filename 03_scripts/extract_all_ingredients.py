import fitz, sys, re, json
sys.stdout.reconfigure(encoding="utf-8")

doc = fitz.open("15139.pdf")
print("Total pages:", len(doc))

# Let us scan the text for ingredients, plants, animals, minerals, recipes, dosages, preparations
# Let us dump all verso lines and specific recto recipe lines
lines_with_ingredients = []

# Verso starts around page 178 to 214
verso_text = ""
for p in range(177, 214):
    verso_text += f"\n=== PAGE {p+1} ===\n" + doc[p].get_text("text")

with open("03_scripts/verso_raw_text.txt", "w", encoding="utf-8") as f:
    f.write(verso_text)

print("Dumped verso_raw_text.txt, length:", len(verso_text))