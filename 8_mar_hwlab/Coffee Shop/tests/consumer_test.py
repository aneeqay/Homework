import unittest

from src.consumer import Consumer
from src.coffee import Coffee
from src.food import Food

class TestConsumer(unittest.TestCase):

    def setUp(self):
        self.ted = Consumer("ted", 10, 30)
        self.ava = Consumer("ava", 5, 15)
        self.latte = Coffee("latte", 3, 5)
        self.muffin = Food("muffin", 2.5, 2)
    
    def test_consumer_has_name(self):
        self.assertEqual("ted", self.ted.name)
        self.assertEqual("ava", self.ava.name)
    
    def test_consumer_has_wallet(self):
        self.assertEqual(10, self.ted.wallet)
        self.assertEqual(5, self.ava.wallet)

    def test_consumer_has_age(self):
        self.assertEqual(30, self.ted.age)
        self.assertEqual(15, self.ava.age)

    def test_no_energy(self):
        self.assertEqual(0, self.ted.energy)
        self.assertEqual(0, self.ava.energy)

    def test_energy_increase(self):
        self.ted.drink_coffee(self.latte)
        self.assertEqual(5, self.ted.energy)

    def test_energy_decrease(self):
        self.ted.drink_coffee(self.latte)
        self.ted.eat_food(self.muffin)
        self.assertEqual(3, self.ted.energy)
