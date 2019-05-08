import csv


with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")

    for row in reader:
        item = row[2]
        profit_number = row[13]
        # cost_number = row[12]
        # revenue_number = row[11]
        # print("Total Profit: ", profit_number)
        # print("Total Cost: ", cost_number)
        # print("Total Revenue: ", revenue_number)

        if "Fruits" == item:
            profit_number = row[13]
            cost_number = row[12]
            revenue_number = row[11]
            print("Total Fruit Profit: ", profit_number)
            # print("Total Fruit Cost: ", cost_number)
            # print("Total Fruit Revenue: ", revenue_number)

            for profit_number in item:
