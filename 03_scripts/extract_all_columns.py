import fitz, sys, re, json
sys.stdout.reconfigure(encoding="utf-8")

doc = fitz.open("15139.pdf")
print("Total pages:", len(doc))

# Pages 20 to 205 contain the transliteration & translation
# Let us dump pages 27 to 214
full_text = ""
for p in range(26, 214):
    full_text += f"\n<<<PAGE_{p+1}>>>\n" + doc[p].get_text("text")

with open("03_scripts/full_papyrus_text.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("Dumped full text, length:", len(full_text))