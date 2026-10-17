import re, sys, json
sys.stdout.reconfigure(encoding="utf-8")

with open("03_scripts/full_papyrus_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let us find all sections
# Recto has Col. I to XXIX
# Verso has Verso Col. I to XXXIII

print("Analyzing structure...")
# Let us extract columns by searching COL.
cols = re.split(r'<<<\s*PAGE_\d+\s*>>>', text)
print(f"Total page chunks: {len(cols)}")