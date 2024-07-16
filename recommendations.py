import csv
import re

# Function to extract Recommendation from the interaction text
def extract_recommendation(interaction_text):
    # List of phrases that represent Recommendations
    recommendations = [
        "Avoid", "Drink", "Administer", "Limit",
        "Take on an empty stomach", "Take", "Do not take", "Exercise caution","Ensure"
    ]

    recommendation = ""


    for rec_phrase in recommendations:
        if rec_phrase in interaction_text:
            if rec_phrase == "Take on an empty stomach":
                recommendation = "Do not take"
            else:
                recommendation = rec_phrase

            break

    return recommendation

# Function to extract Foods after "Examples include" and return a list of Foods
def extract_foods(interaction_text):
    foods = []
    if "Examples include" in interaction_text:
        examples_index = interaction_text.find("Examples include")
        remaining_text = interaction_text[examples_index + len("Examples include"):]
        food_matches = re.findall(r"\b[A-Za-z\s]+(?=[,.])", remaining_text)

        for food in food_matches:
            foods.append(food.strip())

    return foods

# Function to extract Time information
def extract_time(interaction_text):
    time_patterns = [
        r"\b1\s+hour before or (\d+)\s+hours after\b",
        r"\b(\d+)\s+hours before or 1\s+hour after\b",
        r"\b(\d+)\s+hours before or (\d+)\s+hours after\b",
        r"\b(\d+)\s+minutes to (\d+)\s+hours before\b",
        r"\b(\d+)-(\d+)\s+minutes (before|after)\b",
        r"\b2\s+hours before or after\b",
        r"\b(\d+)\s+minutes before\b",
        r"\b(\d+)\s+hour before\b",
        r"\b(\d+)\s+hours before\b",
        r"\b(\d+)\s+hours after\b",
        r"\bsame time every day\b"
    ]

    for pattern in time_patterns:
        match = re.search(pattern, interaction_text)
        if match:
            time = match.group(0)
            return time

    return ""

# Function to fill in Food based on keywords in interaction text
def fill_food(interaction_text):
    if "fluids" in interaction_text:
        return "Fluids"
    elif "same time every day" in interaction_text:
        return ""
    elif "antacids" in interaction_text:
        return "antacids"
    elif "calcium supplements" in interaction_text:
        return "calcium supplements"
    elif "Vitamin K" in interaction_text:
        return "Vitamin K"
    elif "stomach" in interaction_text:
        return "Food"
    elif "Food" in interaction_text or "meal" in interaction_text:
        return "Food"
    elif "food" in interaction_text or "meals" in interaction_text:
        return "Food"
    else:
        return ""

# Main function to process the original CSV and create a new one
def process_interactions(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Assuming the headers of the input CSV are "Drug", "Food", "Interaction"
        header = next(reader)
        writer.writerow(["Drug", "Food", "Recommendation", "Time"])

        for row in reader:
            drug = row[0]
            food = row[3]
            interaction_text = row[2]

            if interaction_text != "No food interactions are expected.":
                recommendation = extract_recommendation(interaction_text)
                time = extract_time(interaction_text)

                if not food:
                # Fill in Food based on keywords in interaction text
                    food = fill_food(interaction_text)

                if "Examples include" not in interaction_text:
                # Write the extracted data to the new CSV file (keeping the Food column from the original file)
                    writer.writerow([drug, food, recommendation, time, interaction_text])
                else:
                # If "Examples include" is present, extract Foods and create new rows with the same Drug, Recommendation, and Time
                    foods = extract_foods(interaction_text)
                    for new_food in foods:
                        writer.writerow([drug, new_food, recommendation, time, interaction_text])

    print("Extraction and writing to the new CSV file completed!")

# Example usage
input_csv_file = "Drug-Food_Recommendation.csv"
output_csv_file = "recomm_output.csv"
process_interactions(input_csv_file, output_csv_file)
