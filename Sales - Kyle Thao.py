import csv


with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")
    fruit_total = 0
    clothes_total = 0
    meat_profit = 0
    beverages_profit = 0
    office_profit = 0
    cosmetics_profit = 0
    snacks_profit = 0
    personal_profit = 0
    household_profit = 0
    vegetables_profit = 0
    baby_food_profit = 0
    cereal_profit = 0

    for row in reader:
        if row[0] == "Region":
            continue
        item = row[2]
        profit_number = float(row[13])
        cost_number = row[12]
        revenue_number = row[11]
        # print("Total Profit: ", profit_number)
        # print("Total Cost: ", cost_number)
        # print("Total Revenue: ", revenue_number)

        if "Fruits" == item:
            fruit_total += profit_number
        if "Clothes" == item:
            clothes_total += profit_number
        if "Meat" == item:
            meat_profit += profit_number
        if "Office Supplies" == item:
            office_profit += profit_number
        if "Baby Food" == item:
            baby_food_profit += profit_number
        if "Beverages" == item:
            beverages_profit += profit_number
        if "Cosmetics" == item:
            cosmetics_profit += profit_number
        if "Snacks" == item:
            snacks_profit += profit_number
        if "Personal Care" == item:
            personal_profit += profit_number
        if "Household" == item:
            household_profit += profit_number
        if "Cereal" == item:
            cereal_profit += profit_number
        if "Vegetables" == item:
            vegetables_profit += profit_number
    print("Total Fruit Profit", round(fruit_total, 2))
    print("Total Clothes Profit", round(clothes_total, 2))
    print("Total Meat Profit", round(meat_profit, 2))
    print("Total Office Profit", round(office_profit, 2))
    print("Total Baby Food Profit", round(baby_food_profit, 2))
    print("Total Beverages", round(beverages_profit, 2))
    print("Total Cosmetic Profit", round(cosmetics_profit, 2))
    print("Total Snacks Profit", round(snacks_profit, 2))
    print("Total Personal Care Profit", round(personal_profit, 2))
    print("Total Household Profit", round(household_profit, 2))
    print("Total Cereal Profit", round(cereal_profit, 2))
    print("Total Vegetable Profit", round(vegetables_profit, 2))

profits = [fruit_total, cereal_profit, clothes_total, meat_profit, office_profit, beverages_profit, baby_food_profit,
           vegetables_profit, personal_profit, cosmetics_profit, snacks_profit, household_profit]

names = ["Fruits", "Cereal", "Clothes", "Meat", "Office Supplies", "Beverages", "Baby Food", "Vegetables",
         "Personal Care", "Cosmetics", "Snacks", "Household"]

index = profits.index(max(profits))

print("The biggest profit is", names[index], "with a", max(profits), "profit.")
