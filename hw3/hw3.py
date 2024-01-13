"""
CMSC 14100
Winter 2024
Homework #3

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URL of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

##################################################
#                                                #
#  IMPORTANT: all of the tasks in this           #
#  assignment have task-specific                 #
#  reqirements/restrictions concerning           #
#  the language constructs that you are          #
#  allowed to use in your solution.  See the     #
#  assignment writeup for details.               #
#                                                #
##################################################

ZERO_SCORE = 0
ONE_SCORE = 3
SOME_SCORE = 5
ALL_SCORE = 10

# Exercise 1
def report_score(num_matches, target):
    """
    Report the score for a given number of matches.

    Inputs:
        num_matches [int]: the number of matches
        target [int]: the target number of matches

    Returns [int]: the score for the specified number of
      matches and target.
    """
    assert target > 0
    ### TODO: Your code here
    ### Remove the pass statement in the next line
    pass


# Exercise 2
def count_cards(cards, lb, ub):
    """
    YOUR DOCSTRING HERE
    """
    assert lb <= ub

    ### TODO: Your code here
    ### Remove the pass statement in the next line
    pass


# Exercise 3
def has_card_v1(cards, target_card):
    """
    YOUR DOCSTRING HERE
    """
    ### TODO: Your code here
    ### Remove the pass statement in the next line
    pass


# Exercise 4
def has_card_v2(cards, target_card):
    """
    YOUR DOCSTRING HERE
    """
    ### TODO: Your code here
    ### Remove the pass statement in the next
    pass


# Exercise 5
def has_at_least_one(cards_on_hand, cards_to_match):
    """
    YOUR DOCSTRING HERE
    """
    # assume there is at least one card to match
    # and that the cards to match are unique
    N = len(cards_to_match)
    assert N >= 1
    assert len(set(cards_to_match)) == N

    ### TODO: Your code here
    ### Remove the pass statement in the next line
    pass


# Exercise 6
def has_all(cards_on_hand, cards_to_match):
    """
    YOUR DOCSTRING HERE
    """
    # assume there is at least one card to match
    # and that the cards to match are unique
    N = len(cards_to_match)
    assert N >= 1
    assert len(set(cards_to_match)) == N

    ### TODO: Your code here
    ### Remove the pass statement in the next line
    pass


# Exercise 7
def has_exactly_one(cards_on_hand, cards_to_match):
    """
    YOUR DOCSTRING HERE
    """
    # assume there is at least one card to match
    # and that the cards to match are unique
    N = len(cards_to_match)
    assert N >= 1
    assert len(set(cards_to_match)) == N

    ### TODO: Your code here
    ### Remove the pass statement in the next line
    pass


# Exercise 8
def compute_score(cards_on_hand, cards_to_match):
    """
    YOUR DOCSTRING HERE
    """
    # assume there is at least one card to match
    # and that the cards to match are unique
    N = len(cards_to_match)
    assert N >= 1
    assert len(set(cards_to_match)) == N

    ### TODO: Your code here
    ### Remove the pass statement in the next line
    pass


# Exercise 9
def card_index_v1(cards, target_card):
    """
    YOUR DOCSTRING HERE
    """
    ### TODO: Your code here
    ### Replace the -1 in the return statement with an appropiate value
    return -1


# Exercise 10
def card_index_v2(cards, target_card):
    """
    YOUR DOCSTRING HERE
    """
    ### TODO: Your code here
    ### Replace the -1 in the return expression with an appropiate value
    return -1
