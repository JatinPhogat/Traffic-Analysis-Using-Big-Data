import requests
import csv

# Define the API URL and parameters
api_url = "https://data.cityofchicago.org/resource/85ca-t3if.json"
params = {
    "$limit": 897648,  # Limit to 1000 rows per request
    "$offset": 0     # Start at row 0
}

# Define the CSV file name
csv_file = "Traffic_Crashes_-_Crashes_20241201"

# Make the request to fetch the first 1000 rows
response = requests.get(api_url, params=params)
data = response.json()

# Collect all possible headers by iterating through all rows
all_keys = set()
for row in data:
    all_keys.update(row.keys())

# Write the data to a CSV file
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=list(all_keys))
    writer.writeheader()  # Write the headers
    writer.writerows(data)  # Write the rows

print(f"Data successfully written to {csv_file}.")
