import csv


def validate(num: str):
    if len(num) == 16:
        list_num = list(num)
        final_digit = list_num.pop(15)
        final_digit = int(final_digit)
        list_num.reverse()
        for index in range(len(list_num)):
            list_num[index] = int(list_num[index])
            if index % 2 == 0:
                list_num[index] *= 2
                if list_num[index] > 9:
                    list_num[index] -= 9
        total = sum(list_num)
        return total % 10 == final_digit
    return False


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]  # String
            if validate(old_number):
                writer.writerow(row)
        print("OK")
