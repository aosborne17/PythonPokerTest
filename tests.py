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

if __name__ == '__main__':
    unittest.main()
