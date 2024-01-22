"""
CMSC 14100
Winter 2024

Test code for Homework #4
"""

import hw4
import json
import os
import sys
import pytest
import helpers
import copy


# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw4"

@pytest.mark.parametrize("card1, card2, expected",
                         [((1, True), (1, True), True),
                          ((7, False), (7, False), True),
                          ((1, True), (1, False), False),
                          ((2, True), (3, False), False),
                          ((1, True), (2, True), False)])
def test_cards_equal(card1, card2, expected):

    recreate_msg = helpers.gen_recreate_msg(MODULE, "cards_equal", card1, card2,)

    try:
        actual = hw4.cards_equal(card1, card2)

        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("size, expected",
                         [(0, []),
                          (1, [(1, True), (1, False)]),
                          (2, [(1, True), (1, False), (2, True), (2, False)]),
                          (3, [(1, True), (1, False), (2, True), (2, False), (3, True), (3, False)]),
                          (4, [(1, True), (1, False), (2, True), (2, False), (3, True), (3, False), (4, True), (4, False)])])
def test_create_deck(size, expected):

    recreate_msg = helpers.gen_recreate_msg(MODULE, "create_deck", size,)

    try:
        actual = hw4.create_deck(size)

        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    


@pytest.mark.parametrize("deck, expected",
                         [([], ([], [])),
                          ([(1, False)], ([], [(1, False)])),
                          ([(1, False), (2, True)], ([(1, False)], [(2, True)])),
                          ([(1, False), (2, True), (6, False)], ([(1, False)], [(2, True), (6, False)])),
                          ([(1, False), (2, True), (6, True), (4, True)], ([(1, False), (2, True)], [(6, True), (4, True)])),
                          ([(1, False), (2, True), (6, True), (4, True), (5, False)], ([(1, False), (2, True)], [(6, True), (4, True), (5, False)]))])
def test_cut_deck(deck, expected):

    recreate_msg = helpers.gen_recreate_msg(MODULE, "cut_deck", deck,)

    try:
        c = copy.deepcopy(deck)
        actual = hw4.cut_deck(deck)

        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

        err_msg = helpers.check_list_unmodified("deck", c, deck, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("cards, expected",
                         [([], []),
                          ([(2, False)], [(2, True)]),
                          ([(2, True)], [(2, False)]),
                          ([(2, True), (5, True)], [(2, False), (5, False)]),
                          ([(2, False), (5, False)], [(2, True), (5, True)]),
                          ([(2, True), (5, False)], [(2, False), (5, True)]),
                          ([(2, False), (5, True)], [(2, True), (5, False)]),
                          ([(2, True), (3, False), (7, True), (2, True), (5, False)], [(2, False), (3, True), (7, False), (2, False), (5, True)]),
                          ([(2, False), (3, True), (7, True), (2, True), (5, False)], [(2, True), (3, False), (7, False), (2, False), (5, True)])])
def test_flip_color(cards, expected):

    recreate_msg = helpers.gen_recreate_commands(MODULE, [f"lst = {cards}", f"{MODULE}.flip_color(lst)"])

    try:
        hw4.flip_color(cards)

        err_msg = helpers.check_result(cards, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("cards, num, expected",
                         [([], 1, []),
                          ([(1, True)], 0, [(1, True)]), 
                          ([(1, True)], 1, [(2, True)]), 
                          ([(1, True)], 10, [(11, True)]),
                          ([(1, True)], -2, [(-1, True)]),
                          ([(1, False)], 1, [(2, False)]), 
                          ([(1, False)], 10, [(11, False)]),
                          ([(1, False)], -2, [(-1, False)]),
                          ([(1, True), (5, False)], 1, [(2, True), (6, False)]), 
                          ([(1, False), (5, False)], 1, [(2, False), (6, False)]), 
                          ([(2, False), (3, True), (7, True), (2, True)], 0, [(2, False), (3, True), (7, True), (2, True)]),
                          ([(2, False), (3, True), (7, True), (2, True)], -1, [(1, False), (2, True), (6, True), (1, True)]),
                          ([(2, False), (3, True), (7, True), (2, True)], 2, [(4, False), (5, True), (9, True), (4, True)]),
                          ([(2, False), (3, True), (7, True), (2, True)], 8, [(10, False), (11, True), (15, True), (10, True)])])
def test_change_value(cards, num, expected):

    recreate_msg = helpers.gen_recreate_msg(MODULE, "change_value", cards, num,)

    try:
        c = copy.deepcopy(cards)
        actual = hw4.change_value(cards, num)

        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

        err_msg = helpers.check_list_unmodified("cards", c, cards, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("cards, expected",
                         [([], ([], [])),
                          ([(2, True)], ([(2, True)], [])),
                          ([(2, False)], ([], [(2, False)])),
                          ([(2, True), (7, True)], ([(2, True), (7, True)], [])),
                          ([(2, False), (7, False)], ([], [(2, False), (7, False)])),
                          ([(2, True), (7, False)], ([(2, True)], [(7, False)])),
                          ([(2, False), (7, True)], ([(7, True)], [(2, False)])),
                          ([(2, True), (3, True), (7, True), (1, False), (2, False)], ([(2, True), (3, True), (7, True)], [(1, False), (2, False)])),
                          ([(2, False), (3, False), (7, True), (1, True), (2, True)], ([(7, True), (1, True), (2, True)], [(2, False), (3, False)])),
                          ([(2, False), (3, True), (7, False), (1, False), (2, True)], ([(3, True), (2, True)], [(2, False), (7, False), (1, False)])),
                          ([(2, False), (3, True), (7, True), (1, False), (2, True)], ([(3, True), (7, True), (2, True)], [(2, False), (1, False)]))])
def test_split_by_color(cards, expected):

    recreate_msg = helpers.gen_recreate_msg(MODULE, "split_by_color", cards,)

    try:
        c = copy.deepcopy(cards)
        actual = hw4.split_by_color(cards)

        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

        err_msg = helpers.check_list_unmodified("cards", c, cards, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("cards, target, expected",
                         [([], (1, True), []),
                          ([(1, True)], (1, True), [(0, True)]),
                          ([(9, True)], (9, True), [(0, True)]),
                          ([(1, False)], (1, False), [(0, False)]),
                          ([(6, False)], (6, False), [(0, False)]),
                          ([(1, False)], (1, True), [(1, False)]),
                          ([(3, False)], (1, True), [(3, False)]),
                          ([(1, True)], (7, True), [(1, True)]),
                          ([(7, True), (3, True), (3, False), (2, True), (5, False)], (7, True), [(0, True), (3, True), (3, False), (2, True), (5, False)]), # beginning
                          ([(2, False), (3, True), (7, True), (2, True), (5, False)], (7, True), [(2, False), (3, True), (0, True), (2, True), (5, False)]), # middle
                          ([(2, False), (3, True), (4, False), (2, True), (7, True)], (7, True), [(2, False), (3, True), (4, False), (2, True), (0, True)]), # end
                          ([(2, False), (3, True), (4, False), (2, True), (9, True)], (7, True), [(2, False), (3, True), (4, False), (2, True), (9, True)])])
def test_lose_points(cards, target, expected):

    recreate_msg = helpers.gen_recreate_commands(MODULE, [f"lst = {cards}", f"{MODULE}.lose_points(lst, {target})"])

    try:
        hw4.lose_points(cards, target)

        err_msg = helpers.check_result(cards, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("cards, start, end, expected",
                         [([(6, True)], 0, 0, ([(6, True)], [])),
                          ([(6, True), (3, False)], 0, 0, ([(6, True)], [(3, False)])),
                          ([(6, True), (3, False)], 1, 1, ([(3, False)], [(6, True)])),
                          ([(6, True), (3, False)], 0, 1, ([(6, True), (3, False)], [])),
                          ([(2, False), (3, True), (7, True), (1, False), (5, True), (4, False)], 0, 0, ([(2, False)], [(3, True), (7, True), (1, False), (5, True), (4, False)])),
                          ([(2, False), (3, True), (7, True), (1, False), (5, True), (4, False)], 0, 1, ([(2, False), (3, True)], [(7, True), (1, False), (5, True), (4, False)])),
                          ([(2, False), (3, True), (7, True), (1, False), (5, True), (4, False)], 0, 2, ([(2, False), (3, True), (7, True)], [(1, False), (5, True), (4, False)])),
                          ([(2, False), (3, True), (7, True), (1, False), (5, True), (4, False)], 0, 5, ([(2, False), (3, True), (7, True), (1, False), (5, True), (4, False)], [])),
                          ([(2, False), (3, True), (7, True), (1, False), (5, True), (4, False)], 5, 5, ([(4, False)], [(2, False), (3, True), (7, True), (1, False), (5, True)])),
                          ([(2, False), (3, True), (7, True), (1, False), (5, True), (4, False)], 4, 5, ([(5, True), (4, False)], [(2, False), (3, True), (7, True), (1, False)])),
                          ([(2, False), (3, True), (7, True), (1, False), (5, True), (4, False)], 3, 5, ([(1, False), (5, True), (4, False)], [(2, False), (3, True), (7, True)])),
                          ([(2, False), (3, True), (7, True), (1, False), (5, True), (4, False)], 1, 3, ([(3, True), (7, True), (1, False)], [(2, False), (5, True), (4, False)])),
                          ([(2, False), (3, True), (7, True), (1, False), (5, True), (4, False)], 2, 3, ([(7, True), (1, False)], [(2, False), (3, True), (5, True), (4, False)])),
                          ([(2, False), (3, True), (7, True), (1, False), (5, True), (4, False)], 2, 4, ([(7, True), (1, False), (5, True)], [(2, False), (3, True), (4, False)]))])
def test_remove_from_middle(cards, start, end, expected):

    recreate_msg = helpers.gen_recreate_msg(MODULE, "remove_from_middle", cards, start, end,)

    try:
        c = copy.deepcopy(cards)
        actual = hw4.remove_from_middle(cards, start, end)

        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

        err_msg = helpers.check_list_unmodified("cards", c, cards, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


@pytest.mark.parametrize("cards, expected",
                         [([], 0),
                          ([(2, True)], 1),
                          ([(2, False)], 1),
                          ([(2, True), (8, True)], 2),
                          ([(2, False), (8, False)], 2),
                          ([(2, True), (8, False)], 1),
                          ([(2, False), (8, True)], 1),
                          ([(2, True), (3, True), (7, True), (1, True), (2, True)], 5),
                          ([(2, False), (3, False), (7, False), (1, False), (2, False)], 5),
                          ([(2, True), (3, True), (7, True), (1, True), (2, False)], 4),
                          ([(2, False), (3, True), (7, True), (1, True), (2, True)], 4),
                          ([(2, True), (3, True), (7, True), (1, False), (2, True)], 3),
                          ([(2, True), (3, False), (7, True), (1, True), (2, True)], 3),
                          ([(2, True), (3, True), (7, False), (1, True), (2, True)], 2),
                          ([(2, False), (3, True), (7, False), (1, True), (2, True)], 2),
                          ([(2, True), (3, False), (7, False), (1, True), (2, True)], 2),
                          ([(2, False), (3, True), (7, False), (1, False), (2, True)], 2),
                          ([(2, False), (3, True), (7, False), (1, True), (2, False)], 1),
                          ([(2, False), (3, False), (7, False), (1, True), (2, True)], 3),
                          ([(2, False), (3, True), (7, True), (1, False), (2, True)], 2),
                          ([(2, False), (3, True), (7, False), (1, False), (2, False), (6, False), (8, True)], 4),
                          ([(2, False), (3, False), (7, False), (1, True), (2, True), (6, True), (8, False)], 3)])
def test_count_longest_run(cards, expected):

    recreate_msg = helpers.gen_recreate_msg(MODULE, "count_longest_run", cards,)

    try:
        c = copy.deepcopy(cards)
        actual = hw4.count_longest_run(cards)

        err_msg = helpers.check_result(actual, expected, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

        err_msg = helpers.check_list_unmodified("cards", c, cards, recreate_msg)
        if err_msg is not None:
            pytest.fail(err_msg)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)