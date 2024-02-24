"""
CMSC 14100
Winter 2024
Homework #8

We will be using anonymous grading, so please do NOT include your name
in this file.

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

# Exercise 1
class Doll:
    """
    A class for representing Matryoshka dolls (also known as Russian
    nesting dolls) where the values are integers.  Use Doll(None, None) to create
    an empty doll.
    """

    def __init__(self, val, doll_to_nest):
        """
        Constructor for Doll

        Inputs:
            val [str]: a value
            doll_to_nest [Doll]: an instance of the Doll class
        """
        assert val is not None or \
            doll_to_nest is None

        self.val = val
        self.nested_doll = doll_to_nest


    def is_empty(self):
        """ Is the doll empty """
        return self.val is None


    # Was called method1 in week 8 discussion
    def __len__(self):
        """ Computes the length of the Doll """
        if self.is_empty():
            return 0

        # alternative: return 1 + self.nested.__len__()
        return 1 + len(self.nested_doll)


    def __eq__(self, other):
        """
        Determine whether self and other represent the same doll.

        Inputs:
            self [Doll]: one M-doll
            other [Doll]: another M-doll

        Returns [bool]: True, if the two dolls are equal and False
          otherwise
        """
        # prevent students from using == in their solutions
        # to exercise 1.
        raise NotImplementedError

    def __repr__(self):
        """ Create a developer-facing string representation of a Doll """

        if self.is_empty():
            return "Doll(None, None)"

        return f"Doll({self.val}, {repr(self.nested_doll)})"


    # Exercise 1
    def diff_count(self, other):
        """
        Determine the number of spots at which two Dolls (self and
        other) differ.

        Inputs:
            self [Doll]: one M-doll
            other [Doll]: another M-doll

        Returns [int]: the number of spots at which the dolls differ.

        """
        # TODO: your code here
        raise NotImplementedError



# Helper function used by the tests.  You will not use
# this function in your solution.
def mk_doll_from_lst(vals):
    """
    Make a doll from a list of values

    Inputs:
        vals [List[str]]: the values for the doll.  Outermost
           value first.
    """
    doll = Doll(None, None)
    # build the doll from back to front
    for v in vals[::-1]:
        doll = Doll(v, doll)
    return doll


# Exercise 2
def find_path(p1, p2):
    """
    Determine whether it is possible traverse from p1 to p2 by
    repeatedly taking positive steps in the x direction and/or 
    positive steps in the y direction.  (One step at a time.)

    Inputs:
        p1 [Tuple[int, int]]: the starting point in cartesian coordinates
        p2 [Tuple[int, int]]: the target point in cartesian coordinates.

    Returns [List[Tuple[int, int]]]: a path from p1 to p2 if one exists,
      None otherwise.
    """
    # TODO: complete this function
    raise NotImplementedError


# Exercise 3
def neg_leaves(t):
    """
    Count the number of leaves with negative values in the tree

    Inputs:
        t [Tree]: a non-emty tree

    Returns [int]: the number of leaves with negative values.
    """
    # TODO: complete this function
    raise NotImplementedError    
        
# Exercise 4
def val_counts(N, t):
    """
    Given a tree where all the values are between 0 and N (inclusive),
    return a list where the ith element contains the number of times
    i occurs in the tree.

    Inputs:
        N [int]: a non-negative integer
        t [Tree]: a tree.

    Returns [List[int]]: a list where the ith value is a count of
      the number of times the value i occurred in the tree.
    """
    # TODO: complete this function
    raise NotImplementedError


# Exercise 5
def count_less_than_paths(t, target):
    """
    Count the number of root-to-leaf paths where weight of a
    path is strictly less than the specified target weight.

    Inputs:
        t [Tree]: a tree with non-negative values
        target [int]: a non-negative target weight

    Returns [int]: the number of root-to-leaf paths with weights
      strictly less than the target weight.

    """
    assert target >= 0
    # TODO: complete this function
    raise NotImplementedError    

# Exercise 6
def find_over_the_top_nodes(t, target):
    """
    Construct a list of the node identifiers for the over-the-top nodes
    in the tree.

    Inputs:
        t [Tree]: a tree with non-negative values
        target [int]: a non-negative target weight
    
    Returns [List[int]]: a list of the node identifiers for the
      over-the-top nodes in the tree.     
    """
    assert target >= 0
    # TODO: complete this function
    raise NotImplementedError

# Exercise 7
def find_less_than_paths(t, target):
    """
    Compute a list of the root-to-leaf paths with a weight
    strictly less than the specified target weight

    Inputs:
        t [Tree]: a tree with non-negative values
        target [int]: a non-negative target weight
    
    Returns [List[List[int]]]: a list of paths with weights strictly
      less than the target, where a path is represented by a list of
      node identifiers.
    """
    assert target >= 0
    # TODO: complete this function
    raise NotImplementedError


