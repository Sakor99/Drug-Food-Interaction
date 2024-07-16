import csv
def extract_food_impact_effect(interaction_text):
    food = ""
    interactions = []

    # Food extraction
    if interaction_text.startswith("Take with a full glass of water"):
        food = ""
    elif interaction_text.startswith("Drink"):
        food = ""
    elif interaction_text.startswith("Avoid") or interaction_text.startswith("Administer") or interaction_text.startswith(
            "Limit") or interaction_text.startswith("Take with foods containing") or interaction_text.startswith("Take with a"):
        food = interaction_text.split(".", 1)[0].split(maxsplit=1)[1]
    elif interaction_text.startswith("Do not take"):
        if "high-fat meal" in interaction_text:
            food = "fatty food"
        elif "high fiber foods" in interaction_text:
            food = "high fiber foods"
        else:
            food = ""
    elif interaction_text.startswith("Exercise caution with"):
        if "grapefruit products" in interaction_text:
            food = "grapefruit products"
        elif "St John's Wort" in interaction_text:
            food = "St John's Wort"
        else:
            food = ""
    elif 'foods high in furanocoumarins' in interaction_text:
        food = "furanocoumarins"

    # Impact and Effect extraction
    keywords = ["increased", "increases", "increasing", "increase", "reduces", "reduced", "reduce", "potentiated",
                "potentiates", "potentiate", "enhanced", "enhance", "impair", "decreases", "decreased", "decrease",
                "caused", "cause", "worsen", "aggravate"]

    sentences = interaction_text.split(".")
    for sentence in sentences:
        impact = ""
        effect = ""
        for keyword in keywords:
            if keyword in sentence.lower():
                impact = keyword
                effect_start_index = sentence.lower().find(keyword) + len(keyword)
                effect_end_index = len(sentence)
                effect = sentence[effect_start_index:effect_end_index].strip()
                interactions.append((food, impact, effect))

    return interactions




input_file = "drugBank_drug_food_interactions.csv"
output_file = "extracted_patterns.csv"

rows = []

with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Read the header row

    for row in reader:
        if len(row) == len(header):
            drug_id, drug_label, interaction = row
            interaction_text = interaction
            interactions = extract_food_impact_effect(interaction)
            for interaction in interactions:
                food, impact, effect = interaction
                rows.append([drug_id, drug_label, interaction, food, impact, effect,interaction_text])

# Write the extracted data to a new CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Drug ID", "Drug Label", "Interaction", "Food", "Impact", "Effect","interaction_text"])  # Write the header row
    writer.writerows(rows)

print("Extraction complete. The extracted data are saved in", output_file)

