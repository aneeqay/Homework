import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Song("Toxic", "Britney Spears")
        self.song2 = Song("Light My Fire", "The Doors")
        self.song3 = Song("Still Dre", "Dr Dre")
        self.song4 = Song("Yeah", "Usher")
    
    def test_song_has_name(self):
        self.assertEqual("Toxic", self.song1.name)

    def test_song_has_artist(self):
        self.assertEqual("Usher", self.song4.artist)
