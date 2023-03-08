import unittest

from src.coffee_shop import CoffeeShop
from src.coffee import Coffee
from src.consumer import Consumer

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.beans = CoffeeShop("beans", 100)
        self.mocha = Coffee("mocha", 3.5, 5)
        self.americano = Coffee("americano", 2.50, 5)
        self.latte = Coffee("latte", 3, 5)
        self.beans.drinks = [self.mocha, self.americano, self.latte]
        self.ted = Consumer("ted", 10, 30)
        self.ava = Consumer("ava", 5, 15)
    
    def test_shop_has_name(self):
        self.assertEqual("beans", self.beans.name)
    
    def test_shop_till_value(self):
        self.assertEqual(100, self.beans.till)

    def test_shop_has_drinks(self):
        self.assertEqual([self.mocha, self.americano, self.latte], self.beans.drinks)

    def test_shop_has_drinks2(self):
        self.assertEqual(3, len(self.beans.drinks))

    def test_sell_coffee(self):
        self.beans.sell_coffee(self.ted, self.latte)
        self.assertEqual(7, self.ted.wallet)
        self.assertEqual(103, self.beans.till)

    def test_sell_underage(self):
        self.beans.sell_coffee(self.ava, self.mocha)
        self.assertEqual(5, self.ava.wallet)
        self.assertEqual(100, self.beans.till)

    def test_sell_10_energy(self):
        self.ted.drink_coffee(self.mocha)
        self.ted.drink_coffee(self.latte)
        self.beans.sell_coffee(self.ted, self.americano)
        self.assertEqual(10, self.ted.wallet)
        self.assertEqual(100, self.beans.till)


    
