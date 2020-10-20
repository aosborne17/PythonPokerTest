#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

# GLOBAL CONSTANTS

CARD_ORDER_VALUES = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}

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


    # We will create a function that will check the hands of both the user and the opponent, depending on what type of cards the user has we will return a number
    # A royal flush having the highest number and a high card having the lowest number
    # This means that when we pass this into the compare_with function, we will be able to know which has the better hand

    def check_hand(self):
        self.string_to_list()
        if self.check_royal_flush():
            return 10
        if self.check_straight_flush():
            return 9
        if self.check_four_of_a_kind():
            return 8
        if self.check_full_house():
            return 7
        if self.check_flush():
            return 6
        if self.check_straight():
            return 5
        if self.check_three_of_a_kind():
            return 4
        if self.check_two_pair():
            return 3
        if self.check_pair():
            return 2
        # if none of the above is met, we know the hand is simply a high card
        return 1

    def check_royal_flush(self):
        # first checking if this is a flush
        if self.check_flush():
            values = [i[0] for i in self.hand]
            value_counts = defaultdict(lambda:0)
            for v in values:
                value_counts[v]+=1
                # Checking if the royal flush pattern is present
                if set(values) == set(["T", "J", "Q", "K", "A"]):
                    return True
        else:
            return False
        return False

    def check_straight_flush(self):
        # If both the straight and flush functions return true, then the hand must be a straight flush
        if self.check_flush() and self.check_straight():
            return True
        else:
            return False

    def check_four_of_a_kind(self):
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values()) == [1,4]:
            return True
        return False


    def check_full_house(self):
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values()) == [2,3]:
            return True
        return False


    def check_flush(self):
        suits = [h[1] for h in self.hand]
        # if there is only one suit in the hand, then we know it must be a flush
        if len(set(suits)) == 1:
            return True
        # If there is more than one suit then we will return false
        return False

    def check_straight(self):
        # Taking the first letter for every hand in the list, thus taking the suit
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda:0)
        # we are adding each suit to the dictionary and how many times it occurs
        for v in values:
            value_counts[v] += 1
        # We are going through each suit in the dictionary and mapping the suit to a value that we have specified in the CARD_ORDER_VALUES data structure
        rank_values = [CARD_ORDER_VALUES[i] for i in values]
        # Here we are subtracting the largest value from the lowest, e.g. a hand of [10, 9, 8, 7, 6] is a straight and 10 - 6 == 4!
        value_range = max(rank_values) - min(rank_values)
        # We are saying that if there is only one suit and they range between a distance of four (meaning they must be contiguous) then the hand must be a straight
        if len(set(value_counts.values())) == 1 and (value_range==4):
            return True
        else:
            # As a straight can also occur with Ace being 1, we have specified a special case for a low ace hand 
            if set(values) == set(["A", "2", "3", "4", "5"]):
                return True
            return False


    def check_three_of_a_kind(self):
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if set(value_counts.values()) == set([3,1]):
            return True
        else:
            return False

    def check_two_pair(self):
        values = [i[0] for i in self.hand]
        # Creating a hash table where whatever key i specify will have a default value of 0 for now
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        # now we can sort the hash table and see if it follows a pattern that all two pair hands will follow, if it does then we know that our hand is a two pair
        # we are saying that if after sorting our hash table by the values it is equal to 1,2,2 then its a two pair
        if sorted(value_counts.values()) == [1, 2, 2]:
            return True
        return False


    def check_pair(self):
        values = [i[0] for i in self.hand]
        # Creating a hash table where whatever key i specify will have a default value of 0 for now
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        # now we can sort the hash table and see if it follows a pattern that all two pair hands will follow, if it does then we know that our hand is a two pair
        # we are saying that if after sorting our hash table by the values it is equal to 1,2,2 then its a two pair
        if sorted(value_counts.values()) == [1, 1, 1, 2]:
            return True
        return False

hand = PokerHand("TD 9S QS QH TH") # two pair returns three


"""
Helpful Links

https://stackoverflow.com/questions/8419401/python-defaultdict-and-lambda
https://www.accelebrate.com/blog/using-defaultdict-python
https://www.partypoker.com/en/how-to-play/hand-rankings
https://www.youtube.com/watch?v=JOomXP-r1wY&ab_channel=ClaremontsCasino
"""


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