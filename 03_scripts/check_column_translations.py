import fitz, sys, re, json
sys.stdout.reconfigure(encoding="utf-8")

with open("03_scripts/full_papyrus_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let us see how the translation is structured per column in Griffith & Thompson
# In the book, translation is presented with line numbers (1), (2), (3)...
# Let us check how Col. I, Col. IV, Col. XIII, Verso Col. I are translated
print("Length of full_papyrus_text:", len(text))

# Let us verify if there are headers like "COL. I", "COL. II", etc.
for col_num in ["I", "II", "III", "IV", "V", "XIII", "XIX", "XXIV", "XXIX"]:
    pos = text.find(f"COL. {col_num}")
    print(f"Found COL. {col_num} at {pos}")