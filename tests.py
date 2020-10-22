#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from poker import PokerHand


class TestCase(unittest.TestCase):

    def setUp(self):
        # self.hand = PokerHand("TD 9S QS QH TH")
        self.hand = PokerHand("TD 9S QS QH TH")
        self.opponent = PokerHand("5D 5S QC 9H QH")


    def test_win(self):
        self.assertEqual(self.hand.compare_with(self.opponent), 1)


    # Making sure that the function returns a number in the range of 1 to 10 depending on what hand pattern the user has, range is set to 11 as the last number is not included
    def test_check_hand(self):
        self.assertIn(self.hand.check_hand(), range(1, 11))


if __name__ == '__main__':
    unittest.main()