import csv


def validate(num: str):
    number = num
    if len(number) == 16:
        list_form = list(num)
        list_form.pop(15)
        last_digit = [::15]
        print(list_form)

    return False

def reverse_number(number):
    return [::-1]


print(validate("4556737586899855"))

# with open("Book1.csv", 'r') as old_csv:
#     with open("New One.csv", 'w', newline='') as new_one_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_one_csv)
#         print("Beep")
#
#         for row in reader:
#             old_number = row[0]
#             if validate(old_number):
#                 writer.writerow(row)
#             print(old_number)
