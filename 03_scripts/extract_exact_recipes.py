import fitz, sys, re
sys.stdout.reconfigure(encoding="utf-8")

with open("03_scripts/full_papyrus_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let us extract exact blocks of instructions: "You take...", "Take...", "Put..."
recipes = re.findall(r'(\(\d+\)\s*(?:You take|If you wish|A remedy|Prescription|Another to follow).*?)(?=\(\d+\)\s*(?:You take|If you wish|A remedy|Prescription|Another|Formula|\nCOL|\nVERSO)|\Z)', text, re.DOTALL | re.I)

print(f"Extracted {len(recipes)} recipe chunks")

with open("03_scripts/extracted_recipes.txt", "w", encoding="utf-8") as f:
    for i, r in enumerate(recipes[:40], 1):
        clean_r = re.sub(r'\s+', ' ', r).strip()
        f.write(f"=== RECIPE {i} ===\n{clean_r}\n\n")

print("Saved first 40 recipes to 03_scripts/extracted_recipes.txt")