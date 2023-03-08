class Pub:
    
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def sell_drink(self, customer, drink):
        if customer.age >= 18 and customer.drunkenness <= 15:
            customer.wallet -= drink.price
            self.till += drink.price
            customer.drunkenness += drink.alcohol_units
        # else:
        #     print("YOU'RE BARRED")

        # def drink_drink(self, drink):
        # self.drunkenness += drink.alcohol_units
