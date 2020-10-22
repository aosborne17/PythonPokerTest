#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

# GLOBAL CONSTANTS

# Creating a dictionary which will describe the value of each card in integer format
CARD_ORDER_VALUES = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}


class PokerHand:
    def __init__(self, hand):
        self.hand = hand
        self.string_to_list()
    

    def compare_with(self, opponent):
        # Your code here

        player_score = hand.check_hand() # Setting a variable equal to whatever hand the user has
        opponent_hand = opponent # Initialising another object for the opponents hand, this will be passed in as an argument of the compare_with function
        opponent_score = opponent_hand.check_hand() #Setting another variable equal to whatever hand the opponent has

        if player_score > opponent_score: # if we beat the opponent a 1 is returned
            return 1
        elif opponent_score > player_score: # two is returned if we lose
            return 2
        else:
            return 0 # 0 is returned if we tie the match
    
    
    def string_to_list(self): # This will be a helper function that will turn our string input of cards to a list, making it easier to compare later on
        split_hand = self.hand.split()
        self.hand = split_hand
        return self.hand


    # The main function
    def check_hand(self): # This will check from top to bottom which function the user and opponent hands are
                          # Important to start from the top otherwise e.g. the flush function would be returned before we got to the royal flush
        # self.string_to_list()       # This helper function turns the string to a list, thus allowing each hand to be traversed much easier
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
            values = [i[0] for i in self.hand] # Taking the first char of each hand e.g. the '4' of '4D' and putting all five into a list
            # print(values) # For a royal flush the list would look like: ['T', 'J', 'Q', 'K', 'A']
            value_counts = defaultdict(lambda:0) # We are creating a default dictionary and giving any the key that is added to have the default value of 0
            for v in values:                     # This stops the key error that would result from a normal dict
                value_counts[v]+=1 # incrementing the key by one for every time e.g. a Jack is present in the hand
                # Checking if the royal flush pattern is present
                if set(values) == set(["T", "J", "Q", "K", "A"]):
                    return True
        else:
            return False
        return False


    def check_straight_flush(self):
        
        if self.check_flush() and self.check_straight(): # If both the straight and flush functions return true, then the hand must be a straight flush; no need to write additional logic
            return True
        else:
            return False

    def check_four_of_a_kind(self):
        values = [i[0] for i in self.hand]
        # Creating hash tables with default value of 0 for all keys
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values()) == [1,4]: # For a hand to be four of a kind it must have four of the same numbers, thus it would follow such a pattern seen here
            return True
        return False


    def check_full_house(self):
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values()) == [2,3]: # Similar to the above, a full house card would have a three of the same and a two of the same
            return True
        return False


    def check_flush(self):
        suits = [i[1] for i in self.hand] # As opposed to the other functions, for this one we want the second character of each card in the hand, thus we take the 1st index and put in in a list
        # print(suits) # For a flush of diamonds, the list would look like so: ['D', 'D', 'D', 'D', 'D']
        # if there is only one suit in the hand, then we know it must be a flush
        if len(set(suits)) == 1: # Sets dont take duplicate values so as they are all 'D' the set should only be a length of 1
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


    def check_three_of_a_kind(self): # 3, 1, 1
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if set(value_counts.values()) == set([3,1]): # Similar logic to the other functions, a three of a kind would follow a pattern of 3,1,1 (only 3,1 in this case as we are using a set which doesn't take duplicates)
            return True
        else:
            return False


    def check_two_pair(self):
        values = [i[0] for i in self.hand]
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
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        # now we can sort the hash table and see if it follows a pattern that all two pair hands will follow, if it does then we know that our hand is a two pair
        # we are saying that if after sorting our hash table by the values it is equal to 1,2,2 then its a two pair
        if sorted(value_counts.values()) == [1, 1, 1, 2]:
            return True
        return False


hand = PokerHand("TD JD QD KD AD") # Testing Royal Flush
opponent = PokerHand("TC 7C 4C 5C QC")
result = hand.compare_with(opponent) # Passing the opponent PokerHand object as an arguement for the compare_with function


print(result) # Should print 1 as we would have won the game