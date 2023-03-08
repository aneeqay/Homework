import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Martini", 9.99, 5)
        self.drink2 = Drink("White Russian", 7.50, 3)
        self.drink3 = Drink("Shot", 2.50, 5)
        self.drink4 = Drink("Pint", 6.00, 2)

    def test_drink_name(self):
        self.assertEqual("Martini", self.drink1.name)
        self.assertEqual("White Russian", self.drink2.name)

    def test_drink_price(self):
        self.assertEqual(2.50, self.drink3.price)

