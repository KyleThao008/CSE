class Burger(object):
    def __init__(self, patty, cheese, vegetables, toppings, eat):
        self.bun = True
        self.patty = patty
        self.cheese = cheese
        self.vegetables = vegetables
        self.toppings = toppings
        self.eat = eat

    def order(self):
        if self.cheese:
            if self.cheese:
                print("I want cheese on my burger.")
            elif self.cheese is False:
                print("I don't want cheese on my burger.")
        if self.patty:
            if self.patty:
                print("I want a beef patty on my burger.")
            else:
                print("I want a vegan patty.")
        if self.vegetables:
            if self.vegetables:
                print("I want vegetables on my burger.")
            else:
                print("I don't want vegetables.")
        if self.toppings:
            if self.toppings:
                print("I want ketchup and mustard on my burger.")
            else:
                print("I don't want ketchup and mustard on my burger.")
        if self.eat:
            if self.eat:
                print("You've eaten your burger.")
            else:
                print("Eat up before it gets cold.")


my_burger = Burger(True, True, False, False, True)
my_burger.order()
