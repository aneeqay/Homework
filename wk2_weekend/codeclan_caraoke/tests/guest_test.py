import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Tom")

    def test_guest_has_name(self):
        self.assertEqual("Tom", self.guest1.name)
        