class CoffeeShop:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def sell_coffee(self, consumer, coffee):
        if consumer.age >= 16 and consumer.energy < 10:
            consumer.wallet -= coffee.price
            self.till += coffee.price
    
    def coffee_list(self):
        # menu = []
        # for coffee in self.drinks:
        #     menu.append(coffee.name)

        menu = [coffee.name for coffee in self.drinks]
        return menu
    
    def drinks_consumer_can_afford(self, customer):
        # affordable_coffee = []
        # for coffee in self.drinks:
        #     if coffee.price <= customer.wallet:
        #         affordable_coffee.append(coffee)

        affordable_coffee = [coffee for coffee in self.drinks if coffee.price <= customer.wallet]
        return affordable_coffee