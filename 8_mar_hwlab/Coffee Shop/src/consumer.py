class Consumer:

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy = 0

    def drink_coffee(self, coffee):
        self.energy += coffee.caffeine

    def eat_food(self, food):
        self.energy -= food.rejuvenation
