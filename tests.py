#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from poker import PokerHand

class TestCase(unittest.TestCase):
    def test_higher_two_pair_wins(self):
        hand = PokerHand("TD 9S QS QH TH")
        opponent = PokerHand("5D 5S QC 9H QH")
        self.assertEqual(hand.compare_with(opponent), 1)

if __name__ == '__main__':
    unittest.main()
