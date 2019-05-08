import csv


with open("Sales Records.csv", 'r') as old_csv:
    with open("Sales.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]  # this is a string
            writer.writerow(row)
        print("OK. 41895")

        if 