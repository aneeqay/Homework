class Customer:
    
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    # def drink_drink(self, drink):
    #     if self.drunkenness <= 15:
    #         self.drunkenness += drink.alcohol_units

    # def buy_drink(self, pub, drink):
    #         self.wallet -= drink.price
    #         pub.till += drink.price
        
