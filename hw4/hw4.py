"""
CMSC 14100
Winter 2024
Homework #4

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
# Important note: some of the tasks in this      #
#  assignment have task-specific                 #
#  reqirements/restrictions                      #
#  on the language constructs that you are       #
#  allowed to use in your solution.  See the     #
#  assignment writeup for details.               #
#                                                #
##################################################

# Exercise 1
def cards_equal(card1, card2):
    """
    Determine whether or not two cards are equal.

    Input:
        card1 [tuple]: first card
        card2 [tuple]: second card

    Returns [boolean]: True if the cards are equal, False otherwise.
    """
    ### TODO: Your code here
    ### Remove the pass statement in the next line
    pass


# Exercise 2
def create_deck(size):
    """
    Create a deck of cards of a given size. A deck is made of
        cards with values 1 to size of black cards and 1 to size of
        red cards.

    Input:
        size [int]: the size of the deck

    Returns [List[tuple]]: A deck of cards.
    """
    ### TODO: Your code here
    ### Remove the pass statement in the next line
    pass

# Exercise 3
def cut_deck(deck):
    """
    Split the deck of cards in half. If the deck has an odd
        number of cards, the second half should get the
        extra card.

    Input:
        deck [List[tuple]]: the deck

    Returns [List[tuple]], [List[tuple]]: Two halves of the deck.
    """
    ### TODO: Your code here
    ### Remove the pass statement in the next line
    pass


# Exercise 4
def flip_color(cards):
    """
    Flip the color (black to red, red to black) of each card
        in a list of cards in-place.

    Input:
        cards [List[tuple]]: a list of cards

    Returns [None]: Nothing, modifies the list of cards in-place.
    """
    ### TODO: Your code here
    ### Remove the pass statement in the next line
    pass


# Exercise 5
def change_value(cards, num):
    """
    Create a list of cards with each card's original value
        incremented by a number.

    Input:
        cards [List[tuple]]: a list of cards
        num [int]: the number to increment

    Returns [List[tuple]]: A list of cards with new values.
    """
    ### TODO: Your code here
    ### Remove the pass statement in the next line
    pass


# Exercise 6
def split_by_color(cards):
    """
    Split the black and red cards in a list of cards
        into two separate lists.

    Input:
        cards [List[tuple]]: a list of cards

    Returns [List[tuple]], [List[tuple]]: A list of black cards
        and a list of red cards.
    """
    ### TODO: Your code here
    ### Remove the pass statement in the next line
    pass


# Exercise 7
def lose_points(cards, target):
    """
    Change the points on the target card to zero in-place.

    Input:
        cards [List[tuple]]: a list of cards
        target [tuple]: the target card

    Returns [None]: Nothing, modifies the list of cards in-place.
    """
    ### TODO: Your code here
    ### Remove the pass statement in the next line
    pass


# Exercise 8
def remove_from_middle(cards, start, end):
    """
    Create a list of cards from the middle of a list of
        cards, from start to end, inclusive. Create a list
        of the remaining cards.

    Input:
        cards [List[tuple]]: a list of cards
        start [int]: the starting card
        end [int]: the ending card

    Returns [List[tuple]], [List[tuple]]: A list of cards from the
        middle and a list of the remaining cards.
    """
    assert start >= 0
    assert end < len(cards)
    assert start <= end
    assert len(cards) > 0

    ### TODO: Your code here
    ### Remove the pass statement in the next line
    pass


# Exercise 9
def count_longest_run(cards):
    """
    Find the number of cards in the longest run of
        cards of the same color.

    Input:
        cards [List[tuple]]: a list of cards

    Returns [int]: The number of the longest run of
        cards of the same color.
    """
    ### TODO: Your code here
    ### Remove the pass statement in the next line
    pass
