"""
CMSC 14100
Winter 2024
Homework #5

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.

[RESUBMISSIONS ONLY: Explain how you addressed the grader's comments
 for your original submission.  If you did not submit a solution for the
 initial deadline, please state that this submission is new.]
"""

COLOR_SIMILARITY_THRESHOLD = 10
GREEN_SCREEN_THRESHOLD = 0.7

# Exercise 1: basic lists of lists practice
def count_close_colors(img, target_color):
    """
    Count the number of cells that hold a color close to
    the target color.  Count within the region only, if
    specified.

    Inputs:
        img [List[List[Tuple(int, int, int)]]: an image
        target_color [Tuple[int, int, int]]: a color

    Returns [int]: the number of cells that are within threshold
      distance of the target color
    """
    ### TODO: replace pass with your code.
    pass


# Exercise 2: practice with constructing a list of list
def gen_identity_mask(N, M):
    """
    Generate a mask with N rows and M colors where every
    entry is True.

    Inputs:
        N [int]: the number of rows
        M [int]: the number of columns

    Returns [List[List[bool]]: an N x M identity mask
    """
    ### TODO: replace pass with your code.
    pass


# Exercise 3
def combine_using_mask(image1, image2, mask):
    """
    Creates an image where the color in location (i, j) of the result
    is the color from location (i, j) in image1 if the mask value in
    location (i, j) is True and color from location (i, j) in image2
    otherwise.

    Inputs:
        image1 [List[List[Tuple[int, int, int]]]]: the first image
        image2 [List[List[Tuple[int, int, int]]]]: the second image    

    Returns [List[List[Tuple[int, int, int]]]]: the combined image.
    """
    ### TODO: replace pass with your code.
    pass
    

# Exercise 4
def flip_region_in_mask(mask, region):
    """
    Flip the mask locations in a region in-place.
    
    Inputs:
        img [List[List[Tuple(int, int, int)]]: an image
        region [Tuple[Tuple[int, int], Tuple[int, int]]]: a region defined using two locations.
    """
    ### TODO: replace pass with your code


# Exercise 5
def loc_radius_to_region(grid, loc, radius):
    """
    Given a grid, a location within that grid, and a radius,
    compute the two-location representation of the region with the specified
    radious around the location.

    Inputs:
        grid [List[List[Any]]]: the grid of interest
        loc [Tuple[int, int]]: the location
        radius [int]: the radius

    Returns [Tuple[Tuple[int, int], Tuple[int, int]]]: the
        two-location representation of the region.

    """
    ### TODO: replace pass with your code    
    pass

# Exercise 6
def gen_green_screen_mask(img, green_screen_color, radius):
    """
    Generate mask where the mask entry corresponding to a pixel
    will be True if the pixel is close to the green screen color AND
    more than 50% of the cells in its region are close to the green
    screen color and False otherwise.

    Inputs:
        img [List[List[Tuple[int, int, int]]]]: an RGB image
        green_screen_color [Tuple[int, int, int]]: the RGB color of the green screen
        radius [int]: the radius defining a region.
        
    Returns [List[List[bool]]: a mask where cells that close to the
      green screen colors and mostly near cells with colors close to
      the green screen color are True and all other cells are False.

    """
    ### TODO: replace pass with your code
    pass

