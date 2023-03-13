import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.pop = Room(2, 5, 100)
        self.song1 = Song("Toxic", "Britney Spears")
        self.guest1 = Guest("Tom", self.song1, 50)
        self.guest2 = Guest("Dan", self.song1, 10)
        self.guest3 = Guest("Una", self.song1, 5)

    def test_guest_check_in(self):
        self.pop.check_in(self.guest1)
        self.assertEqual([self.guest1], self.pop.guest_list)

    def test_guest_check_out(self):
        self.pop.check_in(self.guest1)
        self.pop.check_out(self.guest1)
        self.assertEqual([], self.pop.guest_list)

    def test_add_song(self):
        self.pop.add_song(self.song1)
        self.assertEqual([self.song1], self.pop.song_list)

    def test_full_capacity(self):
        self.pop.check_in(self.guest1)
        self.pop.check_in(self.guest2)
        self.pop.check_in(self.guest3)
        self.assertEqual(2, len(self.pop.guest_list))

    def test_charge_entry_fee(self):
        self.pop.charge_entry_fee(self.guest1)
        self.assertEqual(45, self.guest1.wallet)
        self.assertEqual(105, self.pop.till)

    def test_check_in_charges_guest(self):
        self.pop.check_in(self.guest1)
        self.assertEqual([self.guest1], self.pop.guest_list)
        self.assertEqual(45, self.guest1.wallet)
        self.assertEqual(105, self.pop.till)


