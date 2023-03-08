import unittest

from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("Boozer", 1000.0)
    
    def test_pub_has_name(self):
        self.assertEqual("Boozer", self.pub.name)

    def test_till_value(self):
        self.assertEqual(1000.0, self.pub.till)

    def test_drink_purchase(self):
        customer1 = Customer("Clive", 50.0)
        drink1 = Drink("Martini", 9.99)
        self.pub.sell_drink(customer1, drink1)
        self.assertEqual(40.01, customer1.wallet)
        self.assertEqual(1009.99, self.pub.till)