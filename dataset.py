import csv
import random
import calendar

# List of traits and descriptors
traits = ["friendly", "intelligent", "outgoing", "creative", "organized", "analytical", "adventurous", "empathetic", "resilient", "charismatic"]
descriptors = ["monk", "warrior", "delegate", "king", "commander", "explorer", "artist", "philosopher", "scholar", "pioneer"]

# Function to generate random traits and descriptors for an entry
def generate_traits_and_descriptors():
    # Randomly select one trait and one descriptor
    selected_trait = random.choice(traits)
    selected_descriptor = random.choice(descriptors)
    return selected_trait, selected_descriptor

# Function to generate a dataset
def generate_dataset(start_year, end_year):
    dataset = []
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            # Get the number of days in the current month and year
            num_days_in_month = calendar.monthrange(year, month)[1]
            for day in range(1, num_days_in_month + 1):
                trait, descriptor = generate_traits_and_descriptors()
                entry = {
                    "year": year,
                    "month": month,
                    "day": day,
                    "trait": trait,
                    "descriptor": descriptor
                }
                dataset.append(entry)
    return dataset

# Generate the dataset from 1970 to 2020
start_year = 1970
end_year = 2020
dataset = generate_dataset(start_year, end_year)

# Define the CSV file name
csv_file = "personality_dataset.csv"

# Write the dataset to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["year", "month", "day", "trait", "descriptor"])
    writer.writeheader()
    for entry in dataset:
        writer.writerow(entry)

print("CSV file generated successfully:", csv_file)
