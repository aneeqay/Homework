import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Song("Toxic", "Britney Spears")
        self.guest1 = Guest("Tom", self.song1, 50)
        self.pop = Room(2, 5)

    def test_guest_has_name(self):
        self.assertEqual("Tom", self.guest1.name)

    def test_guest_fave_song(self):
        self.assertEqual(self.song1, self.guest1.fave_song)

    def test_whoo_for_fave_song(self):
        self.pop.add_song(self.song1)
        self.assertEqual("Whoo!", self.guest1.fave_song_exclamation(self.pop))

    def test_pay_entry_fee(self):
        self.guest1.pay_entry_fee(self.pop)
        self.assertEqual(45, self.guest1.wallet)
