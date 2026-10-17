import fitz, sys, re, json
sys.stdout.reconfigure(encoding="utf-8")

# Let us read full_papyrus_text and search for English translation sections
with open("03_scripts/full_papyrus_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# The book prints Demotic transliteration on left/odd or top, and English translation on right/even or below.
# English lines typically have line numbers like (1), (2), (3)...
# Let us search for sections that contain lists of ingredients and directions

matches = []
for p in re.finditer(r'(COL\.\s*[I|V|X|L|C]+|VERSO\s*COL\.\s*[I|V|X|L|C]+)', text):
    matches.append((p.start(), p.group(0)))

print(f"Total Column markers found: {len(matches)}")
for idx, (pos, name) in enumerate(matches[:25]):
    print(f" {idx+1}. {name} at position {pos}")