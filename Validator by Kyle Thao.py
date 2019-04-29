import csv


def validate(num: str):
    number = int(num)
    if int(number) is 16:
        return True
    if int(number) > 16:
        return False


with open("Book1.csv", 'r') as old_csv:
    with open("New One", 'w', newline='') as new_one_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_one_csv)
        print("Beep")

        for row in reader:
            old_number = 
            if validate(old_number):
                writer.writerow(row)
            print(old_number)

