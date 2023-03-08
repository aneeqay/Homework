class CoffeeShop:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def sell_coffee(self, consumer, coffee):
        if consumer.age >= 16 and consumer.energy < 10:
            consumer.wallet -= coffee.price
            self.till += coffee.price