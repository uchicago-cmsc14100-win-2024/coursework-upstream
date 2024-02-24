"""
CMSC 14100
Autumn 2022

Test code for Homework #8
"""

import json
import os
import sys
import traceback
import pytest
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position
import tree
import hw8

MODULE = "hw8"

d0 = []
d1 = []

d2 = ["apple"]
d3 = ["apple"]
d4 = ["banana"]

d5 = ["apple", "banana", "pear", "plum", "peach", "kiwi", "grape"]
# diff at index 0
d6 = ["orange", "banana", "pear", "plum", "peach", "kiwi", "grape"]
# diff at last index 
d7 = ["apple", "banana", "pear", "grapefruit", "peach", "kiwi", "orange"]
# diff in middle
d8 = ["apple", "banana", "pear", "grapefruit", "peach", "kiwi", "grape"]
# multiple points of difference
d9 = ["orange", "banana", "pear", "grapefruit", "peach", "kiwi", "apple"]
d10 = ["orange", "banana"]

# @pytest.mark.timeout(60)
@pytest.mark.parametrize("doll1_lst, doll2_lst, expected",
                         [(d0, d1, 0),
                          (d2, d0, 1),
                          (d2, d3, 0),                       
                          (d3, d4, 1),
                          (d2, d5, 6),
                          (d5, d2, 6),
                          (d5, d6, 1),
                          (d5, d8, 1),
                          (d5, d9, 3),
                          (d10, d7, 6),
                          (d7, d10, 6)
                          ])
def test_diff_count(doll1_lst, doll2_lst, expected):
    steps = [
        f"doll1 = hw8.mk_doll_from_lst({doll1_lst})",
        f"doll2 = hw8.mk_doll_from_lst({doll2_lst})",
        f"doll1.diff_count(doll2)"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    doll1 = hw8.mk_doll_from_lst(doll1_lst)
    doll2 = hw8.mk_doll_from_lst(doll2_lst)

    try:
        actual = doll1.diff_count(doll2)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


def check_point(p):
    """ verify that a value is a valid point """
    return (isinstance(p, tuple) and
            len(p) == 2 and
            isinstance(p[0], int) and
            isinstance(p[1], int))

def validate_path(p1, p2, path):
    """ determine whether path is a valid path from p1 to p2 """
    err_msg = f"The actual path:\n    {path}\nis not a valid path from {p1} to {p2}."

    if not isinstance(path, list):
        return f"The actual path is not a list as required."

    if len(path) == 0:
        if p1 == p2:
            return None
        else:
            return err_msg

    for p in path:
        if not check_point(p):
            return "The actual path does not have the right type.  The expected type is: List[Tuple[int, int]]"

    # At this point, know length path is at least one.
    # Check the end points
    if path[0] != p1 or path[-1] != p2:
        return err_msg

    current = p1
    for p in path[1:]:
        a, b = current
        c, d = p
        diff1 = c - a
        diff2 = d - b
        if not ((diff1 == 1 and diff2 == 0) or
                (diff1 == 0 and diff2 == 1)):
            return err_msg
        current = (c, d)
    return None


# @pytest.mark.timeout(60)
@pytest.mark.parametrize("a, b, c, d, expected",  [
    (1, 1, 1, 1, True),
    (1, 1, 2, 1, True),
    (1, 1, 1, 2, True),    
    (1, 1, 5, 2, True),
    (1, 4, 5, 9, True),
    (4, 3, 3, 3, False),
    (20, 35, 22, 3, False),
    (1000, 1000, 0, 0, False)
])
def test_find_path(a, b, c, d, expected):
    """
    Test code for has_path
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "find_path", (a, b), (c, d))
    try:
        actual = hw8.find_path((a, b), (c, d))
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
        
    if not expected:
        err_msg = helpers.check_expected_none(actual, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
        else:
            return

    err_msg = validate_path((a, b), (c, d), actual)
    if err_msg is not None:
        pytest.fail(err_msg + "\n" + recreate_msg)


# @pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, expected", [
    ("sample_trees/t2.in", 1),        
    ("sample_trees/t3.in", 0),
    ("sample_trees/t1.in", 2),
    ("sample_trees/t4.in", 0),
    ("sample_trees/t5.in", 1),
    ("sample_trees/t6.in", 7)    
])
def test_neg_leaves(input_filename, expected):
    """
    Test code for neg_leaves
    """
    t = tree.load_tree(input_filename)
    if t is None:
        pytest.fail(f"Cannot open file: '{input_filename}'")

    steps = [
        f"import tree",
        f"t = tree.load_tree('{input_filename}')",
        f"actual = hw8.neg_leaves(t)"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw8.neg_leaves(t)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

            
@pytest.mark.parametrize("input_filename, N, expected", [
    ('sample_trees/t8.in', 0, [1]),
    ('sample_trees/t8.in', 3, [1, 0, 0, 0]),
    ('sample_trees/t10.in', 3, [1, 1, 1, 1]),
    ('sample_trees/t9.in', 10, [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2]),
    ('sample_trees/t3.in', 25, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]),
    ('sample_trees/t3.in', 20, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),
    ('sample_trees/t7.in', 20, [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2]),
    ])
# @pytest.mark.timeout(60)
def test_val_counts(input_filename, N, expected):
    """
    Test code for val_counts
    """
    t = tree.load_tree(input_filename)
    if t is None:
        pytest.fail(f"Cannot open file: '{input_filename}'")

    steps = [
        f"import tree",
        f"t = tree.load_tree('{input_filename}')",
        f"actual = hw8.val_counts({N}, t)"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw8.val_counts(N, t)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_1d_iterable(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)
            

# @pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, target, expected", [
    ('sample_trees/t3.in', 21, 1),
    ('sample_trees/t3.in', 20, 0),
    ('sample_trees/t12.in', 50, 5),
    ('sample_trees/t12.in', 15, 3),
    ('sample_trees/t12.in', 9, 0),        
    ('sample_trees/t11.in', 8, 1),
    ('sample_trees/t7.in', 40, 4),
    ('sample_trees/t7.in', 35, 3),
    ('sample_trees/t7.in', 20, 2),
])
def test_count_less_than_paths(input_filename, target, expected):
    """
    Test code for count_less_than_paths
    """
    t = tree.load_tree(input_filename)
    if t is None:
        pytest.fail(f"Cannot open file: '{input_filename}'")

    steps = [
        f"import tree",
        f"t = tree.load_tree('{input_filename}')",
        f"actual = hw8.count_less_than_paths(t, {target})"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw8.count_less_than_paths(t, target)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)
        

# @pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, threshold, expected", [
    ("sample_trees/t3.in", 21, []),
    ("sample_trees/t3.in", 20, [200]),
    ("sample_trees/t3.in", 17, [200]),      
    ('sample_trees/t12.in', 15, [2, 11]),
    ('sample_trees/t12.in', 9, [2, 60, 70, 89, 11]),
    ('sample_trees/t12.in', 50, []),

    ('sample_trees/t12.in', 9, [2, 11, 60, 70, 89]),        
    ("sample_trees/t11.in", 0, [1]),
    ("sample_trees/t11.in", 7, [4]),
    ("sample_trees/t11.in", 8, []),
    ("sample_trees/t7.in", 40, []),
    ("sample_trees/t7.in", 35, [22]),
    ("sample_trees/t7.in", 20, [22, 8]),
    ("sample_trees/t7.in", 15, [2, 6, 8]),
    ("sample_trees/t7.in", 10, [2, 6, 7, 8]),                              
    ("sample_trees/t7.in", 2, [2, 40]),
])
def test_find_over_the_top_nodes(input_filename, threshold, expected):
    """
    Test code for find_monotonic_paths
    """
    t = tree.load_tree(input_filename)
    if t is None:
        pytest.fail(f"Cannot open file: '{input_filename}'")

    steps = [
        f"import tree",
        f"t = tree.load_tree('{input_filename}')",
        f"hw8.find_over_the_top_nodes(t, {threshold})"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw8.find_over_the_top_nodes(t, threshold)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_not_none(actual, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

    # sort the results in case the student does the list concatenation
    # in a different order
    expected = sorted(expected)
    actual = sorted(actual)
    err_msg = helpers.check_1d_iterable(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)
        
        
# @pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, N, expected", [
    ('sample_trees/t3.in', 21, [[200]]),
    ('sample_trees/t3.in', 20, []),
    ('sample_trees/t11.in', 8, [[1, 2, 3, 4]]),
    ('sample_trees/t7.in', 40, [[10, 2, 22], [10, 40, 67, 6], [10, 40, 7], [10, 40, 8]]),
    ('sample_trees/t7.in', 35, [[10, 40, 67, 6], [10, 40, 7], [10, 40, 8]]),
    ('sample_trees/t7.in', 20, [[10, 40, 67, 6], [10, 40, 7]])
])
def test_find_less_than_paths(input_filename, N, expected):
    t = tree.load_tree(input_filename)
    if t is None:
        pytest.fail(f"Cannot open file: '{input_filename}'")

    steps = [
        f"import tree",
        f"t = tree.load_tree('{input_filename}')",
        f"hw8.find_less_than_paths(t, {N})"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw8.find_less_than_paths(t, N)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_2d_iterable(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)
