"""
CMSC 14100
Winter 2024
Homework #6

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
import csv
import math

RADIUS = 6371000.0


def sighting_to_string(sighting):
    """
    Create a string description of a UFO sighting in the form:
        Sighting [ID]: [shape] object, [duration] seconds

    Input:
        sighting [Dict]: a UFO sighting

    Returns [str]: A description of the sighting in the format above.
    """
    ### YOUR CODE HERE
    return None


def create_year_dict(sightings):
    """
    Given a list of UFO sightings, create a dictionary that maps each UFO 
        sighting ID to the year in which that sighting occurred.

    Inputs:
        sightings [List[Dict]]: list of UFO sightings

    Returns [Dict]: Dictionary that maps UFO sighting IDs to years.  
    """
    ### YOUR CODE HERE
    return None


def find_long_sightings(sightings, min_length):
    """
    Given a list of UFO sightings, create a list of sighting IDs for 
        sighting that lasted at least as long as some minimum number of seconds. 

    Inputs:
        sightings [List[Dict]]: list of UFO sightings
        min_length [int]: the minimum length of a sighting in seconds

    Returns [List[str]]: A list of sighting IDs that lasted at least as long
        as min_length.  
    """
    ### YOUR CODE HERE
    return None


def count_shapes(sightings):
    """
    Given a list of UFO sightings, create a dictionary that maps a UFO 
        sighting shape to the number of sightings of that shape. 

    Inputs:
        sightings [List[Dict]]: list of UFO sightings

    Returns [Dict]: Dictionary that maps UFO sighting shapes to the number of 
        sightings of that shape.  
    """
    ### YOUR CODE HERE
    return None


def most_common_shape(sightings):
    """
    Given a list of UFO sightings, determine the most commonly occurring 
        UFO sighting shape and the number of times it occurred. 
    
    Inputs:
        sightings [List[Dict]]: list of UFO sightings

    Returns [Tuple[str, int]]: The most commonly occuring shape and
        the number of times it occurred. 
    """
    ### YOUR CODE HERE
    return None


def sightings_by_year(sightings):
    """
    Given a list of UFO sightings, create a dictionary that maps a year 
        to a list of the UFO sighting dictionaries from that year.
    
    Inputs:
        sightings [List[Dict]]: list of UFO sightings

    Returns [Dict]: A dictionary that maps years to a list of UFO 
        sighting dictionaries.
    """
    ### YOUR CODE HERE
    return None

    
def close_sightings(sightings, max_distance):
    """
    Given a list of UFO sightings, find the sightings that occurred within 
        a given distance of each other. 

    Inputs:
        sightings [List[Dict]]: list of UFO sightings
        max_distance [float]: the maximum distance between two locations

    Returns [List[Tuple[str, str]]]: A list of UFO sighting ID tuples where
        the sightings are within max_distance of each other. 
    """
    ### YOUR CODE HERE
    return None
    