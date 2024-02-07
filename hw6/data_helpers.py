"""
CMSC 14100
Winter 2024

Functions for reading from a CSV file. 
"""
import csv
import os

def load_csv_data(filename):
    """
    Load CSV data from a file.

    Input:
        filename [str]: name of the CSV file

    Returns [List[Dict]]: A list of dictionaries, where each row
        in the CSV file is stored in a dictionary.
    """
    assert filename.endswith(".csv")

    try:
        f = os.path.exists(filename)
    except OSError:
        print(f"Cannot open {filename}")
        sys.exit(1)

    f = open(filename)
    reader = csv.DictReader(f)
    data = []
    for row in reader:
        data.append(row)
    f.close()

    for sighting in data:
        sighting["Duration"] = int(sighting["Duration"])
        sighting["Latitude"] = float(sighting["Latitude"])
        sighting["Longitude"] = float(sighting["Longitude"])

    return data