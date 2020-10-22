# PSEUDOCODING THE FUNCTION LOGIC

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


# We will create a function that will check the hands of both the user and the opponent, depending on what type of cards the user has we will return a number
    # A royal flush having the highest number and a high card having the lowest number
    # This means that when we pass this into the compare_with function, we will be able to know which has the better hand


"""
Helpful Links

https://stackoverflow.com/questions/8419401/python-defaultdict-and-lambda
https://www.accelebrate.com/blog/using-defaultdict-python
https://www.partypoker.com/en/how-to-play/hand-rankings
https://www.youtube.com/watch?v=JOomXP-r1wY&ab_channel=ClaremontsCasino
"""

"""
I am assuming that based on the code given there is only one opponent, thus only one comparison needs to be made
All I have to do here is determine who has the winning hand at the showdown

"""