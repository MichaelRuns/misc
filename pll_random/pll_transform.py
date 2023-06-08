import csv

filename = 'input.csv'
dictionary = {}

with open(filename, 'r') as file:
    reader = csv.reader(file)

    for row_number, row in enumerate(reader):
        i = row_number // 16
        j = row_number % 16
        dictionary[(i, j)] = row
# Accessing values in the dictionary
example_value = dictionary[(0, 0)]
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for j in range(16):
        for i in range(5):
            writer.writerow(dictionary[(i, j)])
