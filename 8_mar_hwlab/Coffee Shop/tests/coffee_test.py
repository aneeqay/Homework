import unittest

from src.coffee import Coffee

class TestCoffee(unittest.TestCase):

    def setUp(self):
        self.mocha = Coffee("mocha", 3.5, 5)
        self.americano = Coffee("americano", 2.50, 5)
        self.latte = Coffee("latte", 3, 5)
    
    def test_coffee_has_name(self):
        self.assertEqual("mocha", self.mocha.name)
        self.assertEqual("americano", self.americano.name)
        self.assertEqual("latte", self.latte.name)

    def test_coffee_caffeine(self):
        self.assertEqual(5, self.mocha.caffeine)
        self.assertEqual(5, self.americano.caffeine)
        self.assertEqual(5, self.latte.caffeine)