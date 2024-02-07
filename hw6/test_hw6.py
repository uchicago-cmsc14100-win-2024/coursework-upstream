"""
CMSC 14100
Winter 2024
Test code for HW #6
"""
import hw6
import json
import copy
import os
import sys
import pytest
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw6"

# Exercise 1
sighting_to_string = json.load(open("tests/sighting_to_string.json", "r", encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("sighting, expected", sighting_to_string)
def test_sighting_to_string(sighting, expected):

    steps = [f"sighting = {sighting}",
             f"{MODULE}.sighting_to_string(sighting)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw6.sighting_to_string(sighting)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)



# Exercise 2
create_year_dict = json.load(open("tests/create_year_dict.json", "r", encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, sightings, expected", create_year_dict)
def test_create_year_dict(filename, sightings, expected):

    steps = [f"import data_helpers",
             f"sightings = data_helpers.load_csv_data('data/{filename}.csv')",
             f"{MODULE}.create_year_dict(sightings)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        c = copy.deepcopy(sightings)
        actual = hw6.create_year_dict(sightings)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


    err_msg = helpers.check_list_unmodified("sightings", c, sightings, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

    err_msg = helpers.check_dict_values(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


# Exercise 3
find_long_sightings = json.load(open("tests/find_long_sightings.json", "r", encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, sightings, min_length, expected", find_long_sightings)
def test_find_long_sightings(filename, sightings, min_length, expected):

    steps = [f"import data_helpers",
             f"sightings = data_helpers.load_csv_data('data/{filename}.csv')",
             f"{MODULE}.find_long_sightings(sightings, {min_length})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        c = copy.deepcopy(sightings)
        actual = hw6.find_long_sightings(sightings, min_length)
        actual.sort()
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


    err_msg = helpers.check_list_unmodified("sightings", c, sightings, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

    err_msg = helpers.check_1d_iterable(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


# Exercise 4
count_shapes = json.load(open("tests/count_shapes.json", "r", encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, sightings, expected", count_shapes)
def test_count_shapes(filename, sightings, expected):

    steps = [f"import data_helpers",
             f"sightings = data_helpers.load_csv_data('data/{filename}.csv')",
             f"{MODULE}.count_shapes(sightings)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        c = copy.deepcopy(sightings)
        actual = hw6.count_shapes(sightings)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


    err_msg = helpers.check_list_unmodified("sightings", c, sightings, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

    err_msg = helpers.check_dict_values(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)



# Exercise 5
most_common_shape = json.load(open("tests/most_common_shape.json", "r", encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, sightings, expected", most_common_shape)
def test_most_common_shape(filename, sightings, expected):

    steps = [f"import data_helpers",
             f"sightings = data_helpers.load_csv_data('data/{filename}.csv')",
             f"{MODULE}.most_common_shape(sightings)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        c = copy.deepcopy(sightings)
        expected = tuple(expected)
        actual = hw6.most_common_shape(sightings)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_list_unmodified("sightings", c, sightings, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

    err_msg = helpers.check_result(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)


# Exercise 6
sightings_by_year = json.load(open("tests/sightings_by_year.json", "r", encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, sightings, expected", sightings_by_year)
def test_sightings_by_year(filename, sightings, expected):

    steps = [f"import data_helpers",
             f"sightings = data_helpers.load_csv_data('data/{filename}.csv')",
             f"{MODULE}.sightings_by_year(sightings)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        c = copy.deepcopy(sightings)
        actual = hw6.sightings_by_year(sightings)

    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_list_unmodified("sightings", c, sightings, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

    err_msg = helpers.check_dict_values(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

# Exercise 7
close_sightings = json.load(open("tests/close_sightings.json", "r", encoding="utf-8"))
@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, sightings, max_distance, expected", close_sightings)
def test_close_sightings(filename, sightings, max_distance, expected):

    steps = [f"import data_helpers",
             f"sightings = data_helpers.load_csv_data('data/{filename}.csv')",
             f"{MODULE}.close_sightings(sightings, {max_distance})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        c = copy.deepcopy(sightings)
        for i, pair in enumerate(expected):
            expected[i] = tuple(pair)
        actual = hw6.close_sightings(sightings, max_distance)
        actual = [tuple(sorted(t)) for t in actual]
        actual.sort()
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_list_unmodified("sightings", c, sightings, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

    err_msg = helpers.check_1d_iterable(actual, expected, recreate_msg)
    if err_msg is not None:
        pytest.fail(err_msg)

