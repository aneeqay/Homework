import unittest

from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.muffin = Food("muffin", 2.5, 2)

    def test_food_has_name(self):
        self.assertEqual("muffin", self.muffin.name)

    def test_food_has_price(self):
        self.assertEqual(2.5, self.muffin.price)

    def test_food_has_rejuvenation(self):
        self.assertEqual(2, self.muffin.rejuvenation)

    
