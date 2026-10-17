import fitz, sys, re
sys.stdout.reconfigure(encoding="utf-8")

with open("03_scripts/full_papyrus_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let us search for key recipe blocks in Recto and Verso
recipe_matches = []

keywords = [
    "shrew-mouse", "gall", "blood of", "dung", "lizard", "hawk", "hoopoe",
    "henbane", "mandragora", "poppy", "opium", "crocus", "alum", "colchicum",
    "frankincense", "myrrh", "styrax", "rue", "ivy", "apple", "grape",
    "olive oil", "oasis oil", "white lamp", "wild cat", "beetle", "frog",
    "eye-paint", "sleeping draught", "stater", "drachm", "hin"
]

for kw in keywords:
    count = len(re.findall(re.escape(kw), text, re.I))
    print(f"Keyword '{kw}': {count} occurrences")