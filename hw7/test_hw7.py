"""
CMSC 14100
Winter 2024

Test code for Homework #7
"""

import json
import os
import sys
import pytest
import helpers
from hw7 import Color, Image
import grid_helpers as gh
import hw7

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw7"

# EXERCISE 1: COLOR INIT (CHECK INPUT)
@pytest.mark.timeout(60)
@pytest.mark.parametrize("r, g, b",
                         [("hello", 0, 0),
                          (0, "bye", 0),
                          (0, 0, "hi"),
                          (2.5, 0, 0),
                          (2.5, 0, 6.2),
                          (2.5, 7.9, 6.2),
                          (300, 0, 0),
                          (0, -10, 0),
                          (-1, 0, 256)])
def test_color_init_valid(r, g, b):

    if isinstance(r, str): r = f"'{r}'" # so the string prints with quotes
    if isinstance(g, str): g = f"'{g}'"
    if isinstance(b, str): b = f"'{b}'"

    steps = [f"color = hw7.Color({r}, {g}, {b})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        Color(r, g, b)
    except Exception as AssertionError:
        return # correct
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = "Color constructor called with invalid input."
    err_msg += "\n  Expected: AssertionError"

    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

# EXERCISE 1: COLOR INIT (SET ATTRIBUTES)
@pytest.mark.timeout(60)
@pytest.mark.parametrize("r, g, b",
                         [(0, 0, 0),
                          (255, 0, 0),
                          (0, 140, 0),
                          (0, 0, 12),
                          (10, 58, 172),
                          (217, 5, 199)])
def test_color_init_attributes(r, g, b):

    steps = [f"color = hw7.Color({r}, {g}, {b})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        color = Color(r, g, b)
        actual = ((r == color._Color__r) and 
                  (g == color._Color__g) and
                  (b == color._Color__b))
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, True, recreate_msg)
    if err_msg is not None:
        err_msg = "Color attribute not set correctly."
        err_msg += f"\n  Expected: __r = {r}"
        err_msg += f"\n            __g = {g}"
        err_msg += f"\n            __b = {b}"
        err_msg += f"\n  Actual: __r = {color._Color__r}"
        err_msg += f"\n          __g = {color._Color__g}"
        err_msg += f"\n          __b = {color._Color__b}"

        pytest.fail(err_msg + recreate_msg)

# EXERCISE 2: COLOR REPR
@pytest.mark.timeout(60)
@pytest.mark.parametrize("r, g, b, expected",
                         [(0, 0, 0, "Color(0, 0, 0)"), 
                          (0, 0, 255, "Color(0, 0, 255)"),
                          (0, 255, 0, "Color(0, 255, 0)"),
                          (255, 0, 0, "Color(255, 0, 0)"),
                          (255, 255, 255, "Color(255, 255, 255)"),
                          (10, 58, 172, "Color(10, 58, 172)"),
                          (217, 5, 199, "Color(217, 5, 199)")])
def test_color_repr(r, g, b, expected):

    steps = [f"color = hw7.Color({r}, {g}, {b})",
             f"s = repr(color)",
             f"print(s)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        color = Color(r, g, b)
        actual = repr(color)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

# EXERCISE 2: COLOR EQ
@pytest.mark.timeout(60)
@pytest.mark.parametrize("color1, color2, expected",
                         [(Color(0, 0, 0), Color(0, 0, 0), True),
                          (Color(255, 255, 255), Color(255, 255, 255), True),
                          (Color(12, 198, 72), Color(12, 198, 72), True),
                          (Color(12, 198, 72), Color(12, 198, 71), False),
                          (Color(12, 198, 72), Color(12, 199, 72), False),
                          (Color(12, 198, 72), Color(13, 198, 72), False),
                          (Color(12, 197, 72), Color(12, 198, 72), False),
                          (Color(15, 197, 72), Color(12, 198, 72), False),
                          (Color(15, 190, 78), Color(12, 198, 72), False)])
def test_color_eq(color1, color2, expected):

    steps = [f"color1 = {repr(color1)}",
             f"color2 = {repr(color2)}",
             f"color1 == color2"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        actual = color1 == color2
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

# EXERCISE 3: IMAGE INIT (CHECK INPUT)
image1 = [[Color(0, 0, 0), Color(0, 0, 0), "hello"], [Color(0, 0, 0), Color(0, 0, 0), Color(0, 0, 0)]] # some elements aren't colors
image2 = [[Color(0, 0, 0), "hi", Color(0, 0, 0)], [Color(0, 0, 0), Color(0, 0, 0), Color(0, 0, 0)]] 
image3 = [[Color(0, 0, 0), Color(0, 0, 0), Color(0, 0, 0)], ["hi", Color(0, 0, 0), Color(0, 0, 0)]] 
image4 = [[Color(0, 0, 0), Color(0, 0, 0), Color(0, 0, 0)], [Color(0, 0, 0), 5, Color(0, 0, 0)]] 
image5 = [[Color(0, 0, 0), Color(0, 0, 0), Color(0, 0, 0)], [Color(0, 0, 0), Color(0, 0, 0), -2]] 
image6 = [[Color(0, 0, 0), Color(0, 0, 0)], [Color(0, 0, 0), Color(0, 0, 0), Color(0, 0, 0)]] 
image7 = [[Color(0, 0, 0), Color(0, 0, 0), Color(0, 0, 0)], [Color(0, 0, 0), Color(0, 0, 0)]] # not rectangular
image8 = [[Color(0, 0, 0), Color(0, 0, 0)], [Color(0, 0, 0), Color(0, 0, 0)], [Color(0, 0, 0)]] 
image9 = [[Color(0, 0, 0), Color(0, 0, 0), Color(0, 0, 0)], [Color(0, 0, 0), Color(0, 0, 0)], [Color(0, 0, 0), Color(0, 0, 0), Color(0, 0, 0)]] 
image10 = [[Color(0, 0, 0), Color(0, 0, 0)], [Color(0, 0, 0), Color(0, 0, 0), Color(0, 0, 0)], [Color(0, 0, 0), Color(0, 0, 0), Color(0, 0, 0)]] 
@pytest.mark.timeout(60)
@pytest.mark.parametrize("pixels",
                         [(image1),
                          (image2),
                          (image3),
                          (image4),
                          (image5),
                          (image6),
                          (image7),
                          (image8),
                          (image9),
                          (image10)])
def test_image_init_valid(pixels):

    for i, row in enumerate(pixels):
        for j, value in enumerate(row):
            if isinstance(value, str):
                pixels[i][j] = f"'{value}'" # so strings print with quotes

    steps = [f"pixels = {pixels}", f"image = hw7.Image(pixels)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        Image(pixels)
    except Exception as AssertionError:
        return # correct
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = "Image constructor called with invalid input."
    err_msg += "\n  Expected: AssertionError"

    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

# EXERCISE 3: IMAGE INIT (SET ATTRIBUTES)
image1 = [[Color(0, 0, 0), Color(0, 0, 0)], [Color(0, 0, 0), Color(0, 0, 0)], [Color(0, 0, 0), Color(0, 0, 0)]] 
image2 = [[Color(0, 0, 0), Color(0, 0, 0), Color(0, 0, 0)], [Color(0, 0, 0), Color(0, 0, 0), Color(0, 0, 0)]] 
image3 = [[Color(0, 0, 0), Color(0, 0, 0), Color(0, 0, 0)], [Color(0, 0, 0), Color(0, 0, 0), Color(0, 0, 0)], [Color(0, 0, 0), Color(0, 0, 0), Color(0, 0, 0)]] 
@pytest.mark.timeout(60)
@pytest.mark.parametrize("pixels, M, N",
                         [(image1, 3, 2),
                          (image2, 2, 3),
                          (image3, 3, 3)])
def test_image_init_attributes_M_N(pixels, M, N):

    steps = [f"pixels = {pixels}", f"image = hw7.Image(pixels)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        image = Image(pixels)
        actual = ((image.M == M) and
                  (image.N == N))
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, True, recreate_msg)
    if err_msg is not None:
        err_msg = "Image attribute not set correctly."
        err_msg += f"\n  Expected: M = {M}"
        err_msg += f"\n            N = {N}"
        err_msg += f"\n  Actual: M = {image.M}"
        err_msg += f"\n          N = {image.N}"

        pytest.fail(err_msg + recreate_msg)

@pytest.mark.timeout(60)
@pytest.mark.parametrize("pixels",
                         [(image1),
                          (image2),
                          (image3)])
def test_image_init_attributes_pixels(pixels):

    steps = [f"pixels = {pixels}", f"image = hw7.Image(pixels)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        image = Image(pixels)
        actual = ((image.pixels == pixels) and
                  (id(image.pixels) != id(pixels)))
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, True, recreate_msg)
    if err_msg is not None:
        err_msg = "Image attribute not set correctly."
        err_msg += f"\n  Expected: pixels = {pixels}"
        err_msg += f"\n  Actual: pixels = {image.pixels}"

        if id(image.pixels) == id(pixels):
            err_msg += f"\nDid you remember to copy the input list?"

        pytest.fail(err_msg + recreate_msg)

@pytest.mark.timeout(60)
@pytest.mark.parametrize("image_filename, expected",
                         [("tests/test1.ppm", '4 x 4\nColor(0, 0, 0) Color(255, 255, 255) Color(0, 0, 0) Color(255, 255, 255)\nColor(255, 0, 0) Color(0, 0, 0) Color(255, 0, 0) Color(0, 0, 0)\nColor(0, 0, 0) Color(0, 255, 0) Color(0, 0, 0) Color(0, 255, 0)\nColor(0, 0, 255) Color(0, 0, 0) Color(0, 0, 255) Color(0, 0, 0)'),
                          ("tests/test2.ppm", '6 x 5\nColor(0, 0, 0) Color(255, 255, 255) Color(0, 0, 0) Color(255, 255, 255) Color(0, 0, 0)\nColor(255, 255, 255) Color(0, 0, 0) Color(255, 255, 255) Color(0, 0, 0) Color(255, 255, 255)\nColor(100, 150, 200) Color(255, 255, 255) Color(100, 150, 200) Color(255, 255, 255) Color(100, 150, 200)\nColor(255, 255, 255) Color(200, 150, 50) Color(255, 255, 255) Color(200, 150, 50) Color(255, 255, 255)\nColor(100, 200, 150) Color(255, 255, 255) Color(100, 200, 150) Color(255, 255, 255) Color(100, 200, 150)\nColor(255, 255, 255) Color(150, 100, 200) Color(255, 255, 255) Color(150, 100, 200) Color(255, 255, 255)'),
                          ("tests/test1-greyscale.ppm", '4 x 4\nColor(0, 0, 0) Color(255, 255, 255) Color(0, 0, 0) Color(255, 255, 255)\nColor(77, 77, 77) Color(0, 0, 0) Color(77, 77, 77) Color(0, 0, 0)\nColor(0, 0, 0) Color(149, 149, 149) Color(0, 0, 0) Color(149, 149, 149)\nColor(29, 29, 29) Color(0, 0, 0) Color(29, 29, 29) Color(0, 0, 0)'),
                          ("tests/test2-greyscale.ppm", '6 x 5\nColor(0, 0, 0) Color(255, 255, 255) Color(0, 0, 0) Color(255, 255, 255) Color(0, 0, 0)\nColor(255, 255, 255) Color(0, 0, 0) Color(255, 255, 255) Color(0, 0, 0) Color(255, 255, 255)\nColor(141, 141, 141) Color(255, 255, 255) Color(141, 141, 141) Color(255, 255, 255) Color(141, 141, 141)\nColor(255, 255, 255) Color(154, 154, 154) Color(255, 255, 255) Color(154, 154, 154) Color(255, 255, 255)\nColor(164, 164, 164) Color(255, 255, 255) Color(164, 164, 164) Color(255, 255, 255) Color(164, 164, 164)\nColor(255, 255, 255) Color(126, 126, 126) Color(255, 255, 255) Color(126, 126, 126) Color(255, 255, 255)'),
                          ("tests/test1-blur-R1-all.ppm", '4 x 4\nColor(128, 64, 64) Color(149, 53, 53) Color(110, 51, 51) Color(155, 76, 76)\nColor(89, 62, 20) Color(81, 54, 21) Color(83, 83, 22) Color(58, 78, 25)\nColor(28, 62, 49) Color(31, 57, 69) Color(28, 59, 44) Color(28, 79, 58)\nColor(15, 30, 93) Color(17, 35, 85) Color(17, 38, 85) Color(18, 44, 47)'),
                          ("tests/test1-blur-R2-all.ppm", '4 x 4\nColor(85, 57, 28) Color(92, 90, 45) Color(78, 76, 27) Color(76, 103, 36)\nColor(64, 40, 51) Color(41, 55, 44) Color(43, 58, 46) Color(28, 74, 38)\nColor(34, 53, 63) Color(34, 70, 56) Color(36, 58, 59) Color(36, 70, 50)\nColor(28, 37, 92) Color(29, 43, 63) Color(31, 46, 68) Color(31, 53, 47)')
                          ])
def test_image_repr(image_filename, expected):

    steps = [f"import grid_helpers as gh",
             f"image = gh.get_image_from_file('{image_filename}')",
             f"s = repr(image)",
             f"print(s)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        image = gh.get_image_from_file(image_filename)
        actual = repr(image)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

@pytest.mark.timeout(60)
@pytest.mark.parametrize("image1_filename, image2_filename, expected",
                         [("tests/test1.ppm", "tests/test1.ppm", True),
                          ("tests/test2.ppm", "tests/test2.ppm", True),
                          ("tests/test1.ppm", "tests/test2.ppm", False),
                          ("tests/test1.ppm", "tests/test1-greyscale.ppm", False),
                          ("tests/test2.ppm", "tests/test2-greyscale.ppm", False),
                          ("tests/test1.ppm", "tests/test1-blur-R1-all.ppm", False),
                          ("tests/test1.ppm", "tests/test1-blur-R1-all.ppm", False)])
def test_image_eq(image1_filename, image2_filename, expected):

    steps = [f"import grid_helpers as gh",
             f"image1 = gh.get_image_from_file('{image1_filename}')",
             f"image2 = gh.get_image_from_file('{image2_filename}')",
             f"image1 == image2"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        image1 = gh.get_image_from_file(image1_filename)
        image2 = gh.get_image_from_file(image2_filename)
        actual = image1 == image2
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, expected_filename",
                         [("tests/test1.ppm", "tests/test1-greyscale.ppm"),
                          ("tests/test2.ppm", "tests/test2-greyscale.ppm")])
def test_image_greyscale(input_filename, expected_filename):

    steps = [f"import grid_helpers as gh",
             f"image = gh.get_image_from_file('{input_filename}')",
             f"image.greyscale()"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        test = gh.get_image_from_file(input_filename)
        expected = gh.get_image_from_file(expected_filename)

        test.greyscale()
        actual = test == expected
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, True, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, region, R, expected_filename",
                         [("tests/test1.ppm", ((0, 0), (3, 3)), 1, "tests/test1-blur-R1-all.ppm"),
                          ("tests/test2.ppm", ((0, 0), (5, 4)), 1, "tests/test2-blur-R1-all.ppm"),
                          ("tests/test1.ppm", ((0, 0), (3, 3)), 2, "tests/test1-blur-R2-all.ppm"),
                          ("tests/test2.ppm", ((0, 0), (5, 4)), 2, "tests/test2-blur-R2-all.ppm"),
                          ("tests/test1.ppm", ((0, 2), (1, 3)), 1, "tests/test1-blur-R1-top-right.ppm"),
                          ("tests/test2.ppm", ((0, 3), (1, 4)), 1, "tests/test2-blur-R1-top-right.ppm"),
                          ("tests/test1.ppm", ((0, 2), (1, 3)), 2, "tests/test1-blur-R2-top-right.ppm"),
                          ("tests/test2.ppm", ((0, 3), (1, 4)), 2, "tests/test2-blur-R2-top-right.ppm"),
                          ("tests/test1.ppm", ((2, 0), (3, 2)), 1, "tests/test1-blur-R1-bottom.ppm"),
                          ("tests/test2.ppm", ((3, 0), (5, 2)), 1, "tests/test2-blur-R1-bottom.ppm"),
                          ("tests/test1.ppm", ((2, 0), (3, 2)), 2, "tests/test1-blur-R2-bottom.ppm"),
                          ("tests/test2.ppm", ((3, 0), (5, 2)), 2, "tests/test2-blur-R2-bottom.ppm")])
def test_image_blur(input_filename, R, region, expected_filename):
    
    steps = [f"import grid_helpers as gh",
             f"image = gh.get_image_from_file('{input_filename}')",
             f"image.blur({region}, {R})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        test = gh.get_image_from_file(input_filename)
        expected = gh.get_image_from_file(expected_filename)

        test.blur(region, R)
        actual = test == expected
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, True, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)