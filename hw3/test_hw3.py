"""
CMSC 14100
Winter 2024

Test code for Homework #3
"""
import random
import os
import sys

import hw3

import pytest
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw3"

@pytest.mark.parametrize("num_matches, target, expected",
                         [(0, 10, hw3.ZERO_SCORE),
                          (1, 10, hw3.ONE_SCORE),
                          (2, 10, hw3.SOME_SCORE), 
                          (9, 10, hw3.SOME_SCORE),
                          (10, 10, hw3.ALL_SCORE),               
                          (0, 100, hw3.ZERO_SCORE),
                          (1, 100, hw3.ONE_SCORE),
                          (2, 100, hw3.SOME_SCORE), 
                          (99, 100, hw3.SOME_SCORE),
                          (100, 100, hw3.ALL_SCORE),               
                          # check the case where target is one
                          (1, 1, hw3.ALL_SCORE),
                         ])
def test_report_score(num_matches, target, expected):
    """
    Do a test for Exercise 1
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "report_score", num_matches, target)
    try:
        actual = hw3.report_score(num_matches, target)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


# make some longer tests.
l1 = list(range(-4, 20))
random.shuffle(l1)
l2 = list(range(-4, 20))
random.shuffle(l2)
@pytest.mark.parametrize("cards, lb, ub, expected", [
    # empty list
    ([], 0, 10, 0),
    # different variants of one element lists
    ([0], 0, 10, 1), 
    ([5], 0, 10, 1),        
    ([10], 0, 10, 1),        
    ([20], 5, 10, 0),
    # multi-element list, no duplicates
    ([5, 1, 2, 3], 0, 5, 4),
    ([5, 1, 2, 3], 1, 5, 4),
    ([5, 1, 2, 3], 2, 4, 2),
    ([5, 1, 2, 3], 10, 20, 0),
    # multi-element list with duplicates
    ([5, 1, 2, 3, 5], 0, 5, 5),
    ([5, 1, 2, 3, 5], 2, 4, 2),
    ([5, 6, 2, 3, 5, 9], -5, 20, 6),
    # random examples
    (l1, 4, 10, 7),
    (l2, 4, 15, 12)])
def test_count_cards(cards, lb, ub, expected):
    """
    Do a test for Exercise 2
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "count_cards", cards, lb, ub)
    try:
        actual = hw3.count_cards(cards, lb, ub)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

        
has_card_tests = [
    # Empty list
    ([], 5, False),
    # One element lists
    ([5], 5, True),
    ([7], 10, False),
    # multi-element lists, no duplicates
    # 1st element in the list
    ([5, 7, 3, 2, 1], 5, True),
    # last element in the list
    ([5, 7, 3, 2, 1], 1, True),
    # a middle element 
    ([5, 7, 3, 2, 1], 2, True),
    # not in list
    ([5, 7, 3, 2, 1], 10, False),        
    (l1, -4, True),
    (l1, -20, False),
    (l1, 20, False),
    (l1, 1000, False),        
    # multi-element list
    ([5, 7, 3, 5, 2, 1, 7, 7, 7, 10], 7, True),
    ]
@pytest.mark.parametrize("cards, target_card, expected",
                         has_card_tests)
def test_has_card_v1(cards, target_card, expected):
    """
    Do a test for Exercise 3
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "has_card_v1", cards, target_card)
    try:
        actual = hw3.has_card_v1(cards, target_card)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("cards, target_card, expected",
                         has_card_tests)
def test_has_card_v2(cards, target_card, expected):
    """
    Do a test for Exercise 4
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "has_card_v2", cards, target_card)
    try:
        actual = hw3.has_card_v2(cards, target_card)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)



hand1 = []
hand2 = [5]
hand3 = [7, 5, 10, 20, 6]
hand4 = list(range(0, 21))
random.shuffle(hand4)

need1 = [5]
need2 = [10]
need3 = [25]
need4 = [5, 20, 7]
need5 = [6, 7]
need6 = [5, 6, 7, 10, 20]
need7 = [4, 5, 6, 7, 10, 20, 25]
need8 = sorted(hand4)
need9 = [50, 30, 40]
need10 = [6]

@pytest.mark.parametrize("cards_on_hand, cards_to_match, expected", [
    (hand1, need1, False),
    (hand1, need7, False),
    (hand2, need1, True),
    (hand2, need2, False),
    (hand3, need1, True),
    (hand3, need10, True),
    (hand3, need3, False),
    (hand4, need4, True),
    (hand4, need9, False),    
    (hand4, need5, True),
])
def test_has_at_least_one(cards_on_hand, cards_to_match, expected):
    """
    Do a test for Exercise 5
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "find_has_at_least_one", cards_on_hand, cards_to_match)
    try:
        actual = hw3.has_at_least_one(cards_on_hand, cards_to_match)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("cards_on_hand, cards_to_match, expected", [
    (hand1, need1, False),
    (hand1, need7, False),
    (hand2, need1, True),
    (hand2, need2, False),
    (hand2, need6, False),

    (hand3, need1, True),
    (hand3, need2, True),
    (hand3, need10, True),
    (hand3, need3, False),
    (hand3, need4, True),
    (hand3, need6, True),
    (hand3, need7, False),    

    (hand4, need4, True),
    (hand4, need7, False),
    (hand4, need8, True),
    (hand4, need9, False)
])
def test_has_all(cards_on_hand, cards_to_match, expected):
    """
    Do a test for Exercise 6
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "has_all", cards_on_hand, cards_to_match)
    try:
        actual = hw3.has_all(cards_on_hand, cards_to_match)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

@pytest.mark.parametrize("cards_on_hand, cards_to_match, expected", [
    (hand1, need1, False),
    (hand1, need7, False),

    (hand2, need1, True),
    (hand2, need2, False),

    (hand3, need1, True),
    (hand3, need2, True),
    (hand3, need10, True),
    (hand3, need3, False),
    (hand3, need4, False),
    (hand3, need6, False),
    (hand3, need7, False),
    (hand3, [5, 25, 30], True),
    (hand3, [25, 7, 30], True),
    (hand3, [25, 30, 6], True),        
])
def test_has_exactly_one(cards_on_hand, cards_to_match, expected):
    """
    Do a test for Exercise 7
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "has_exactly_one", cards_on_hand, cards_to_match)
    try:
        actual = hw3.has_exactly_one(cards_on_hand, cards_to_match)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
        

@pytest.mark.parametrize("cards_on_hand, cards_to_match, expected", [
    (hand1, need1, hw3.ZERO_SCORE),
    (hand1, need7, hw3.ZERO_SCORE),

    (hand2, need1, hw3.ALL_SCORE),
    (hand2, need2, hw3.ZERO_SCORE),

    (hand3, need1, hw3.ALL_SCORE),
    (hand3, need3, hw3.ZERO_SCORE),
    (hand3, need10, hw3.ALL_SCORE),
    (hand3, need4, hw3.ALL_SCORE),
    (hand3, need7, hw3.SOME_SCORE),
    (hand3, [5, 25, 7], hw3.SOME_SCORE),
    (hand3, [10, 7, 30], hw3.SOME_SCORE),
    (hand3, [25, 30, 6], hw3.ONE_SCORE),

    (hand4, need8, hw3.ALL_SCORE),
    (need8, hand4, hw3.ALL_SCORE),
    (hand4, need4, hw3.ALL_SCORE),
    (need8, [0, 100], hw3.ONE_SCORE),
    (need8, [1000, 20], hw3.ONE_SCORE),
    (need8, [17, 25, 38], hw3.ONE_SCORE),        
    (hand4, need9, hw3.ZERO_SCORE),
    (hand4, need7, hw3.SOME_SCORE),

    ([5, 7, 3, 5, 2, 1, 7, 7, 10], [4, 10, 0], hw3.ONE_SCORE),
    ([5, 7, 3, 5, 2, 1, 7, 7, 10, 4], [4, 10, 0], hw3.SOME_SCORE),    

])
def test_compute_score(cards_on_hand, cards_to_match, expected):
    """
    Do a test for Exercise 8
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "compute_score", cards_on_hand, cards_to_match)
    try:
        actual = hw3.compute_score(cards_on_hand, cards_to_match)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
        

card_index_tests = [
    # Empty list
    ([], 5, None),
    # One element lists
    ([5], 5, 0),
    ([7], 10, None),
    # multi-element lists, no duplicates
    # 1st element in the list
    ([5, 7, 3, 2, 1], 5, 0),
    # last element in the list
    ([5, 7, 3, 2, 1], 1, 4),
    # a middle element 
    ([5, 7, 3, 2, 1], 2, 3),
    # not in list
    ([5, 7, 3, 2, 1], 10, None),        
    # random tests -- students cannot
    # use index in their solutions
    (l1, -4, l1.index(-4)),
    (l1, -20, None),
    (l1, 1000, None),        
    # multi-element list
    ([5, 7, 3, 5, 2, 1, 7, 7, 7, 10], 7, 1),
    ([5, 7, 3, 5, 2, 1, 7, 7, 7, 10], 1, 5),
]
@pytest.mark.parametrize("cards, target_card, expected",
                         card_index_tests)
def test_card_index_v1(cards, target_card, expected):
    """
    Do a test for Exercise 9
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "card_index_v1", cards, target_card)
    try:
        actual = hw3.card_index_v1(cards, target_card)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("cards, target_card, expected",
                         card_index_tests)
def test_card_index_v2(cards, target_card, expected):
    """
    Do a test for Exercise 10
    """
    recreate_msg = helpers.gen_recreate_msg(
        MODULE, "card_index_v2", cards, target_card)
    try:
        actual = hw3.card_index_v2(cards, target_card)
        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
