import csv


def validate(num: str):
        first_num = int(num[0])
        if first_num is 4:
            writer.writerow(row)
            return True
        return False

# with open("Book1.csv", 'r') as old_csv:
#     reader = csv.reader(old_csv)
#     for row in reader:
#         old_number = row[0]
#         print(old_number + "1")


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFIle.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]  # this is a string
            if validate(old_number):
                writer.writerow(row)
        print("OK.")
