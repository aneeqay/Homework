import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guest_list = []
        self.song_list = []
        self.pop = Room(self.guest_list, self.song_list)
        # self.rock = Room()
        # self.hiphop = Room()
        # self.rnb = Room()
        self.guest1 = Guest("Tom")

    def test_guest_check_in(self):
        self.pop.check_in(self.guest1)
        self.assertEqual([self.guest1], self.pop.guest_list)

    def test_guest_check_out(self):
        self.pop.check_in(self.guest1)
        self.pop.check_out(self.guest1)
        self.assertEqual([], self.pop.guest_list)
