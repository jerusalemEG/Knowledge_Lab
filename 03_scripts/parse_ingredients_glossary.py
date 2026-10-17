import fitz, sys, re, json
sys.stdout.reconfigure(encoding="utf-8")

with open("03_scripts/verso_raw_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let us find all plant, mineral, animal names and medical recipes
# Let us print out sections from verso
print("Verso sample lines:")
lines = text.split("\n")
for l in lines[:100]:
    if any(k in l.lower() for k in ["recipe", "take", "plant", "oil", "blood", "wine", "dung", "seed", "leaf", "root", "mineral", "gall", "heart"]):
        print("  ->", l.strip()[:100])