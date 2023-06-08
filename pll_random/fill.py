import csv

# Specify the file name
filename = "input.csv"

# Generate data for each row
data = [[(i, j) for k in range(28)] for i in range(5) for j in range(16)]

# Write data to CSV file
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully.")
