import unittest

from src.consumer import Consumer

class TestConsumer(unittest.TestCase):

    def setUp(self):
        self.ted = Consumer("ted", 10, 30)
        self.ava = Consumer("ava", 5, 15)
    
    def test_consumer_has_name(self):
        self.assertEqual("ted", self.ted.name)
        self.assertEqual("ava", self.ava.name)
    
    def test_consumer_has_wallet(self):
        self.assertEqual(10, self.ted.wallet)
        self.assertEqual(5, self.ava.wallet)

    def test_consumer_has_age(self):
        self.assertEqual(30, self.ted.age)
        self.assertEqual(15, self.ava.age)

    def test_customer_no_energy(self):
        self.assertEqual(0, self.ted.energy)
        self.assertEqual(0, self.ava.energy)

    