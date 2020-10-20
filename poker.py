#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PokerHand:
    def __init__(self, hand):
        self.hand = hand
    
    def compare_with(self, opponent):
        # Your code here
        return 0
    
    # This will be a helper function that will turn our string input of cards to a list, making it easier to compare later on
    def string_to_list(self):
        split_hand = self.hand.split()
        self.hand = split_hand
        return self.hand

    def check_flush(self):
        suits = [h[1] for h in self.hand]
        # if there is only one suit in the hand, then we know it must be a flush
        if len(set(suits)) == 1:
            return True
        # If there is more than one suit then we will return false
        return False


hand = PokerHand("TD 9S QS QH TH") # two pair returns three


# PSEUDOCODE

# I will need to write a function that compares one hand to another and sees which is better

# when we initialise the pokerhand function, it will contain a string with 5 cards, spaced out by one whitespace

# What am i looking for in my comparison

# I want to see if the current poker hand has a higher ranking than the opponent poker hand

# How do I do that?

# I may have to list out all of the different potentially ways to win and give them a ranking accordingly

# I could then say that if this ranking is greater than the other ranking then this person won

# How do I do that?

# I could put the rankings of each outcome into a hash table and their value would be their ranking?


# I am unsure how I will be able to iterate through this string with whitespace, so what I could do is turn it into a list and replace the white space with a comma dilimeter


# hand = PokerHand("TD 9S QS QH TH")  # 10 diamonds, 9 spades, queen spades, queen heart, 10 hearts # TWO PAIR

# this will return whether our hand is better than the opponents

# hand.compare_with("7D 4S JS KH 2H") # 7 diamonds, 4 spades, jack spades, king hearts, 2 hearts  # HIGH CARD

# TWO PAIR BEATS HIGH CARD SO WE BEAT OUR OPPONENT





# WHAT ARE THE TEXAS HOLD EM RULES

"""
I am assuming that based on the code given there is only one opponent, thus only one comparison needs to be made
All I have to do here is determine who has the winning hand at the showdown

"""