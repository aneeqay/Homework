class Pub:
    
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def sell_drink(self, customer, drink):
        customer.wallet -= drink.price
        self.till += drink.price
