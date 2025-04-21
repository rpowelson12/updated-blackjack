import unittest

from main import evaluate_hand
from cards import Card

class TestHands(unittest.TestCase):
    

    def test_hands(self):
        hand = [Card("Ace", "Spades"), Card("Four", "Diamonds"), Card("Ace", "Hearts"), Card("Queen", "Diamonds"), Card("Two", "Clubs"), Card("Four", "Hearts")]
        self.assertEqual(evaluate_hand(hand), 22)

if __name__ == '__main__':
    unittest.main()