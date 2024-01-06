"""
CMSC 14100
Winter 2024

Test code for Homework #2
"""
import hw2
import os
import sys

import pytest
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw2"

@pytest.mark.parametrize("a, x, expected",
                         [(0, 0, 0),
                          (5, 2, 12),
                          (5, 0, 0),
                          (9, 1, 10),
                          (9, -2, -20),
                          (-11, 2, -20)])
def test_add_one_and_multiply(a, x, expected):
    """
    Do a single test for Exercise 1: add_one_and_multiply
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "add_one_and_multiply",
                                            a, x)
    actual = hw2.add_one_and_multiply(a, x)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


@pytest.mark.parametrize("a, b, expected",
                         [(1, 1, True),
                          (2, 2, True),
                          (1, 2, False),
                          (4, 10, True),
                          (5, 10, False),
                          (-1, -2, False),
                          (-2, 20, True),
                          (5, -7, True)])
def test_same_parity(a, b, expected):
    """
    Do a single test for Exercise 2: same_parity
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "same_parity", a, b,)
    actual = hw2.same_parity(a, b)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


@pytest.mark.parametrize("n, d, expected",
                         [(1, 3, 1/3),
                          (2, 3, 2/3),
                          (3, 2, 1/2),
                          (50, 7, 1/7), 
                          (51, 7, 2/7), 
                          (3, 3, float(0))])
def test_fractional_part(n, d, expected):
    """
    Do a single test for Exercise 3: fractional_part
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "fractional_part", n, d,)
    actual = hw2.fractional_part(n, d)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


@pytest.mark.parametrize("p, e, expected",
                         [(1, 3, True),
                          (3, 1, False),
                          (0, 1, False),
                          (1, 0, False),
                          (1, 2, False),
                          (2, 3, False)])
def test_peep(p, e, expected):
    """
    Do a single test for Exercise 4: peep
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "peep", p, e,)
    actual = hw2.peep(p, e)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


@pytest.mark.parametrize("r, g, b, expected",
                         [(0, 0, 0, True),
                          (255, 255, 0, True),
                          (0, 255, 0, True),
                          (255, -10, 0, False),
                          (0, 255, 256, False),
                          (0.5, 0, 0, False)])
def test_is_valid_color(r, g, b, expected):
    """
    Do a single test for Exercise 5: is_valid_color
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "is_valid_color", r, g, b,)
    actual = hw2.is_valid_color(r, g, b)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


@pytest.mark.parametrize("r, g, b, expected",
                         [(0, 0, 0, True),
                          (255, 255, 0, False),
                          (0, 255, 0, False),
                          (0, 255, 255, False),
                          (10, 10, 10, True),
                          (101, 101, 101, True)])
def test_is_grey(r, g, b, expected):
    """
    Do a single test for Exercise 6: is_grey
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "is_grey", r, g, b,)
    actual = hw2.is_grey(r, g, b)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


@pytest.mark.parametrize("r, g, b, expected",
                         [(0, 0, 0, 0),
                          (255, 255, 255, 255),
                          (0, 255, 255, 170),
                          (255, 0, 0, 85),
                          (85, 85, 85, 85),
                          (0, 0, 85, 28)])
def test_make_greyscale(r, g, b, expected):
    """
    Do a single test for Exercise 7: make_greyscale
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "make_greyscale", r, g, b,)
    actual = hw2.make_greyscale(r, g, b)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


@pytest.mark.parametrize("r, g, b, expected",
                         [(0, 0, 0, float(0)),
                          (255, 255, 255, 254.99999999999997),
                          (0, 255, 0, 183.6),
                          (10, 10, 10, 9.999999999999998),
                          (0, 100, 255, 89.85),
                          (200, 200, 10, 186.7),
                          (200, 200, 255, 203.85),
                          (201, 201, 199, 200.86),
                          (201, 255, 100, 232.81)])
def test_brightness(r, g, b, expected):
    """
    Do a single test for Exercise 8: brightness
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "brightness", r, g, b,)
    actual = hw2.brightness(r, g, b)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


@pytest.mark.parametrize("r, g, b, expected",
                         [(0, 0, 0, False),
                          (255, 255, 255, True),
                          (0, 255, 0, False),
                          (10, 10, 10, False),
                          (200, 200, 10, False),
                          (200, 200, 255, True),
                          (201, 201, 199, True),
                          (201, 255, 100, True),
                          (201, 209, 100, False)])
def test_is_bright(r, g, b, expected):
    """
    Do a single test for Exercise 9: is_bright
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "is_bright", r, g, b,)
    actual = hw2.is_bright(r, g, b)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


@pytest.mark.parametrize("r, g, b, expected",
                         [(0, 0, 0, False),
                          (255, 0, 0, True),
                          (10, 0, 0, False),
                          (0, 255, 0, True),
                          (0, 10, 0, False),
                          (0, 0, 255, True),
                          (0, 0, 10, False),
                          (255, 255, 0, False),
                          (0, 255, 255, False),
                          (255, 0, 255, False)])
def test_is_primary(r, g, b, expected):
    """
    Do a single test for Exercise 10: is_primary
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "is_primary", r, g, b,)
    actual = hw2.is_primary(r, g, b)
    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)