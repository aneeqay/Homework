import unittest

from src.high_scores import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):

    def setUp(self): 
        self.scores = [200, 50, 70, 90]
    

    # Test latest score (the last thing in the list)

    def test_return_latest_score(self):
        self.assertEqual(90, latest(self.scores))

    # Test personal best (the highest score in the list)
    
    def test_return_highest_score(self):
        self.assertEqual(200, personal_best(self.scores))

    # Test top three from list of scores

    def test_personal_top_three(self):
        self.assertEqual([200, 90, 70], personal_top_three(self.scores))
    
    # Test ordered from highest tp lowest
    def test_ordered_list(self):
        self.assertEqual([200, 90, 70, 50], ordered_list(self.scores))

    # Test top three when there is a tie
    def test_top_three_tie(self):
        scores1 = [200, 90, 90, 70]
        scores2 = [200, 90, 70, 70]
        self.assertEqual([200, 90, 90], personal_top_three(scores1))
        self.assertEqual([200, 90, 70], personal_top_three(scores2))
    
    # Test top three when there are less than three
    def test_top_three_less_than_three(self):
        scores1 = [200, 90]
        self.assertEqual([200, 90], personal_top_three(scores1))

    # Test top three when there is only one
    def test_top_three_less_than_three(self):
        scores1 = [200]
        self.assertEqual([200], personal_top_three(scores1))
