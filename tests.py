#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from poker import PokerHand

class TestCase(unittest.TestCase):

    def setUp(self):
        self.hand = PokerHand("TD 9S QS QH TH")

    def test_win(self):
        self.assertEqual(self.hand.compare_with("TD TS TC QH 3H"), 2) # three of a kind beats two pair, should return 2 meaning we lost

    def test_list_change(self):
        self.assertIsInstance(self.hand.string_to_list(), list)

    # Making sure that the function returns a number in the range of 1 to 10 depending on what hand pattern the user has
    def test_check_hand(self):
        self.assertIn(self.hand.check_hand(), range(1, 10))

# class TestCase(unittest.TestCase):
#     def test_higher_two_pair_wins(self):
#         hand = PokerHand("TD 9S QS QH TH")
#         opponent = PokerHand("5D 5S QC 9H QH")
#         self.assertEqual(hand.compare_with(opponent), 1)
    
    # A function to make sure a hand consists of five cards
if __name__ == '__main__':
    unittest.main()
