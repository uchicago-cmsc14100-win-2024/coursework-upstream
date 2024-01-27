"""
CMSC 14100
Winter 2024

Test code for Homework #5
"""

import copy
import json
import os
import sys
import traceback
import pytest
import helpers as helpers
import grid_helpers as gh


# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position
import hw5

MODULE = "hw5"

# Some useful color constants

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, color, expected",
    [("tests/blue_img.ppm", BLUE, 36),
     ("tests/blue_ish_img.ppm", BLUE, 29),
     ("tests/blue_ish_img.ppm", RED, 0),
     ("tests/blue_ish_img.ppm", (2, 10, 252), 14),
     ("tests/checkerboard_green.ppm", GREEN, 18),
     ("tests/checkerboard_green.ppm", WHITE, 6),
     ("tests/checkerboard_green.ppm", BLACK, 6),
     ("tests/cb_green_ish.ppm", GREEN, 14),
     ("tests/cb_green_ish.ppm", BLACK, 6),
     ("tests/cb_green_ish.ppm", WHITE, 5),
     ("tests/one_not_quite_yellow.ppm", YELLOW, 0),
     ("tests/one_not_quite_yellow.ppm", (247, 249, 1), 1)])
def test_count_close_colors(filename, color, expected):
    """
    Does one test for count_close_colors
    """
    recreate_msg = helpers.gen_recreate_commands(MODULE, [
        f"import grid_helpers as gh",
        f"img = gh.load_grid('{filename}')",
        f"actual = hw5.count_close_colors(img, {color})"
        ])

    # add code to check that the image was not modified.

    img = gh.load_grid(filename)
    img_copy = copy.deepcopy(img)

    try:
        actual = hw5.count_close_colors(img, color)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

    # verify that the student's code does not modify
    # the input
    err_msg = helpers.check_2D_list_unmodified("img", img_copy, img)
    if err_msg is not None:
        pytest.fail(err_msg + "\n" + recreate_msg)

    return None


@pytest.mark.timeout(60)
@pytest.mark.parametrize("n, m, expected_filename",
                         [(1, 1, "tests/id_1_1_mask.json"),
                          (6, 6, "tests/id_6_6_mask.json"),
                          (6, 5, "tests/id_6_5_mask.json")])
def test_gen_identity_mask(n, m, expected_filename):
    """
    Does one test for gen_identity_mask
    """

    expected = gh.load_grid(expected_filename)

    recreate_msg = helpers.gen_recreate_commands(MODULE, [
        f"expected = gh.load_grid('{expected_filename}')",
        f"actual = hw5.gen_identity_mask({n}, {m})"
        ])

    try:
        actual = hw5.gen_identity_mask(n, m)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_mask(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + "\n" + recreate_msg)

    if len(expected) > 1:
        err_msg = ("The rows of the mask must refer to separate lists.\n"
                   "There are at least two rows (row {} and row {}) that refer to the same list")
        for i, row1 in enumerate(actual):
            for j, row2 in enumerate(actual):
                if i != j and row1 is row2:
                    pytest.fail(err_msg.format(i, j) + "\n" + recreate_msg)                    



@pytest.mark.timeout(60)
@pytest.mark.parametrize("fg_filename, bg_filename, mask_filename, expected_filename",
                         [("tests/blue_ish_img.ppm", "tests/blue_img.ppm",
                           "tests/id_6_6_mask.json", "tests/blue_ish_img.ppm"),
                          ("tests/blue_ish_img.ppm", "tests/blue_img.ppm",
                           "tests/all_false_6_6_mask.json", "tests/blue_img.ppm"),
                          ("tests/blue_yellow_stripe.ppm", "tests/black_6_5_img.ppm", "tests/region_0.json","tests/by_black_0.ppm"),
                          ("tests/black_6_5_img.ppm", "tests/blue_yellow_stripe.ppm", "tests/region_0.json","tests/black_by_0.ppm"),
                          ("tests/blue_yellow_stripe.ppm", "tests/black_6_5_img.ppm", "tests/region_1.json","tests/by_black_1.ppm"),
                          ("tests/black_6_5_img.ppm", "tests/blue_yellow_stripe.ppm", "tests/region_1.json","tests/black_by_1.ppm"),
                          ("tests/blue_yellow_stripe.ppm", "tests/black_6_5_img.ppm", "tests/region_2.json","tests/by_black_2.ppm"),
                          ("tests/black_6_5_img.ppm", "tests/blue_yellow_stripe.ppm", "tests/region_2.json","tests/black_by_2.ppm"),
                          ("tests/blue_yellow_stripe.ppm", "tests/black_6_5_img.ppm", "tests/region_3.json","tests/by_black_3.ppm"),
                          ("tests/black_6_5_img.ppm", "tests/blue_yellow_stripe.ppm", "tests/region_3.json","tests/black_by_3.ppm"),
                          ("tests/blue_yellow_stripe.ppm", "tests/black_6_5_img.ppm", "tests/region_4.json","tests/by_black_4.ppm"),
                          ("tests/black_6_5_img.ppm", "tests/blue_yellow_stripe.ppm", "tests/region_4.json","tests/black_by_4.ppm"),
                          ("tests/blue_yellow_stripe.ppm", "tests/black_6_5_img.ppm", "tests/region_5.json","tests/by_black_5.ppm"),
                          ("tests/black_6_5_img.ppm", "tests/blue_yellow_stripe.ppm", "tests/region_5.json","tests/black_by_5.ppm")
                          ])
def test_combine_using_mask(fg_filename, bg_filename, mask_filename, expected_filename):
    """
    Does one test for combine_using_mask
    """

    image1 = gh.load_grid(fg_filename)
    image1_copy = copy.deepcopy(image1)
    image2 = gh.load_grid(bg_filename)
    image2_copy = copy.deepcopy(image2)
    mask = gh.load_grid(mask_filename)
    mask_copy = copy.deepcopy(mask)
    expected = gh.load_grid(expected_filename)

    recreate_msg = helpers.gen_recreate_commands(MODULE, [
        f"import grid_helpers as gh",
        f"image1 = gh.load_grid('{fg_filename}')",
        f"image2 = gh.load_grid('{bg_filename}')",
        f"mask = gh.load_grid('{mask_filename}')",
        f"expected = gh.load_grid('{expected_filename}')",
        f"actual = hw5.combine_using_mask(image1, image2, mask)"
        ])

    try:
        actual = hw5.combine_using_mask(image1, image2, mask)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
        
    # check the return value
    err_msg = helpers.check_image(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + "\n" + recreate_msg)


    # Verify that the inputs were not modified.
    err_msg = helpers.check_2D_list_unmodified("image1", image1_copy, image1)
    if err_msg is not None:
        pytest.fail(err_msg + "\n" + recreate_msg)

    err_msg = helpers.check_2D_list_unmodified("image2", image2_copy, image2)
    if err_msg is not None:
        pytest.fail(err_msg + "\n" + recreate_msg)

    err_msg = helpers.check_2D_list_unmodified("mask", mask_copy, mask)
    if err_msg is not None:
        pytest.fail(err_msg + "\n" + recreate_msg)
        


@pytest.mark.timeout(60)
@pytest.mark.parametrize("mask_filename, region, expected_filename",
    [("tests/id_6_5_mask.json", ((0, 0), (2, 2)), "tests/region_0.json"),
     ("tests/region_0.json", ((0, 0), (5, 4)), "tests/region_0_flipped.json"),
     ("tests/id_6_5_mask.json", ((2, 2), (5, 4)), "tests/region_1.json"),
     ("tests/region_1.json", ((0, 0), (5, 4)), "tests/region_1_flipped.json"),
     ("tests/id_6_5_mask.json", ((0, 0), (0, 4)), "tests/region_2.json"),
     ("tests/region_2.json", ((0, 0), (5, 4)), "tests/region_2_flipped.json"),
     ("tests/id_6_5_mask.json", ((5, 0), (5, 4)), "tests/region_3.json"),
     ("tests/region_3.json", ((0, 0), (5, 4)), "tests/region_3_flipped.json"),
     ("tests/id_6_5_mask.json", ((0, 0), (5, 0)), "tests/region_4.json"),
     ("tests/region_4.json", ((0, 0), (5, 4)), "tests/region_4_flipped.json"),
     ("tests/id_6_5_mask.json", ((0, 4), (5, 4)), "tests/region_5.json"),
     ("tests/region_5.json", ((0, 0), (5, 4)), "tests/region_5_flipped.json"),
     ])
def test_flip_region_in_mask(mask_filename, region, expected_filename):
    """
    Does one test for test_flip_region_in_mask
    """

    mask = gh.load_grid(mask_filename)
    expected = gh.load_grid(expected_filename)

    recreate_msg = helpers.gen_recreate_commands(MODULE, [
        f"mask = gh.load_grid('{mask_filename}')",
        f"expected_mask_after_flip = gh.load_grid('{expected_filename}')",
        f"hw5.flip_region_in_mask(mask, {region})"
        ])

    try:
        actual = hw5.flip_region_in_mask(mask, region)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_expected_none(actual, None)
    if err_msg is not None:
        pytest.fail(err_msg + "\n" + recreate_msg)

    err_msg = helpers.check_mask(mask, expected)
    if err_msg is not None:
        pytest.fail(err_msg + "\n" + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("grid_filename, loc, radius, expected",
    [("tests/id_6_5_mask.json", (3, 2), 0, ((3, 2), (3, 2))),
     ("tests/id_6_5_mask.json", (3, 2), 1, ((2, 1), (4, 3))),
     ("tests/id_6_5_mask.json", (3, 2), 2, ((1, 0), (5, 4))),

     ("tests/id_6_5_mask.json", (0, 0), 0, ((0, 0), (0, 0))),
     ("tests/id_6_5_mask.json", (0, 0), 1, ((0, 0), (1, 1))),
     ("tests/id_6_5_mask.json", (0, 0), 2, ((0, 0), (2, 2))),
     
     ("tests/id_6_5_mask.json", (5, 4), 0, ((5, 4), (5, 4))),
     ("tests/id_6_5_mask.json", (5, 4), 1, ((4, 3), (5, 4))),
     ("tests/id_6_5_mask.json", (5, 4), 2, ((3, 2), (5, 4))),
     ("tests/id_6_5_mask.json", (5, 4), 6, ((0, 0), (5, 4))),

     ("tests/blue_img.ppm", (3, 3), 0, ((3, 3), (3, 3))),
     ("tests/blue_img.ppm", (3, 3), 2, ((1, 1), (5, 5))),
     ("tests/blue_img.ppm", (3, 3), 4, ((0, 0), (5, 5)))
    ])
def test_loc_radius_to_region(grid_filename, loc, radius, expected):
    grid = gh.load_grid(grid_filename)
    grid_load_str = f"grid = gh.load_grid('{grid_filename}')"

    recreate_msg = helpers.gen_recreate_commands(MODULE, [
        f"import grid_helpers as gh",
        grid_load_str,
        f"hw5.loc_radius_to_region(grid, {loc}, {radius})"
    ])

    grid_copy = copy.deepcopy(grid)

    try:
        actual = hw5.loc_radius_to_region(grid, loc, radius)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)
    
    err_msg = helpers.check_2D_list_unmodified("grid", grid_copy, grid)
    if err_msg is not None:
        pytest.fail(err_msg + "\n" + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("img_filename, color, radius, expected_filename",
    [("tests/gs_example.ppm", GREEN, 0, "tests/gs_example_0_mask.json"),
     ("tests/gs_example.ppm", GREEN, 1, "tests/gs_example_1_mask.json"),    
     ("tests/blue_ish_img.ppm", BLUE, 0, "tests/blue_ish_0_mask.json"),
     ("tests/blue_ish_img.ppm", BLUE, 1, "tests/blue_ish_1_mask.json"),
     ("tests/blue_ish_img.ppm", BLUE, 2, "tests/blue_ish_2_mask.json"),
     ("tests/blue_ish_img.ppm", BLUE, 3, "tests/blue_ish_3_mask.json"),               
     ("tests/blue_yellow_stripe.ppm", BLUE, 0, "tests/by_stripe_blue_0_mask.json"),
     ("tests/blue_yellow_stripe.ppm", BLUE, 1, "tests/by_stripe_blue_1_mask.json"),
     ("tests/blue_yellow_stripe.ppm", BLUE, 2, "tests/by_stripe_blue_2_mask.json"),
     ("tests/blue_yellow_stripe.ppm", YELLOW, 0, "tests/by_stripe_yellow_0_mask.json"),
     ("tests/blue_yellow_stripe.ppm", YELLOW, 1, "tests/by_stripe_yellow_1_mask.json"),     
     ("tests/blue_yellow_stripe.ppm", YELLOW, 2, "tests/by_stripe_yellow_2_mask.json"),     
     ("tests/one_not_quite_yellow.ppm", (251, 253, 9), 0, "tests/id_1_1_mask.json"),
    ])
def test_gen_green_screen_mask(img_filename, color, radius, expected_filename):
    img = gh.load_grid(img_filename)
    img_copy = copy.deepcopy(img)

    expected = gh.load_grid(expected_filename)

    recreate_msg = helpers.gen_recreate_commands(MODULE, [
        f"import grid_helpers as gh",
        f"img = gh.load_grid('{img_filename}')",
        f"expected = gh.load_grid('{expected_filename}')",
        f"actual = hw5.gen_green_screen_mask(img, {color}, {radius})"
    ])

    try:
        actual = hw5.gen_green_screen_mask(img, color, radius)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    
    err_msg = helpers.check_mask(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + "\n" + recreate_msg)

    err_msg = helpers.check_2D_list_unmodified("image", img_copy, img)
    if err_msg is not None:
        pytest.fail(err_msg + "\n" + recreate_msg)
        
