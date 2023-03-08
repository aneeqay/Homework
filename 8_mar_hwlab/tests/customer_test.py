import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Clive", 50.0, 32)

    def test_customer_has_name(self):
        self.assertEqual("Clive", self.customer.name)

    def test_wallet_amount(self):
        self.assertEqual(50.0, self.customer.wallet)

    def test_customer_age(self):
        self.assertEqual(32, self.customer.age)    
    
    # def test_customer_drunkenness(self):
    #     drink1 = Drink("Martini", 9.99, 5)
    #     self.customer.drink_drink(drink1) 
    #     self.assertEqual(5, self.customer.drunkenness)


    # def test_drink_purchase(self):
    #     pub1 = Pub("Boozer", 1000.0)
    #     drink1 = Drink("Martini", 9.99)
    #     self.customer.buy_drink(pub1, drink1)
    #     self.assertEqual(40.01, self.customer.wallet)
    #     self.assertEqual(1009.99, pub1.till)