"""
CMSC 14100
Winter 2024
Homework #7

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
class Color:
    """
    Class to represent a color.
    """

    def __init__(self, r, g, b):
        ### YOUR CODE HERE
        pass

    def __repr__(self):
        ### YOUR CODE HERE
        return None

    def __eq__(self, other):
        ### YOUR CODE HERE
        return None


class Image:
    """
    Class to represent an image.
    """

    def __init__(self, pixels):
        ### YOUR CODE HERE
        pass

    def __repr__(self):
        ### YOUR CODE HERE
        return None

    def __eq__(self, other):
        ### YOUR CODE HERE
        return None

    def greyscale(self):
        """
        Convert the image to greyscale.
        
        Inputs:
            None

        Returns [None]: Nothing, converts the image to greyscale in place.
        """
        ### YOUR CODE HERE
        return None

    def blur(self, region, R):
        """
        Blur the image over a region.

        Inputs:
            region [Tuple[Tuple[int, int]], Tuple[int, int]]: the region to blur
            R [int]: the radius to blur

        Returns [None]: Nothing, blurs the image in-place.
        """
        ### YOUR CODE HERE
        return None
