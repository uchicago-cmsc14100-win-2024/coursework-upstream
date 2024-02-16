"""
CMSC 14100
Winter 2023

Functions for reading and writing images in PPM P3 format.
"""

import json
import os
import sys
import hw7

def get_image_from_file(filename):
    """
    Get Image object from PPM file
    """

    tuples = load_image(filename)

    pixels = []

    for tuple_row in tuples:
        pixel_row = []
        for r, g, b in tuple_row:
            color = hw7.Color(r, g, b)
            pixel_row.append(color)
        pixels.append(pixel_row)

    image = hw7.Image(pixels)

    return image

def load_grid(filename):
    """
    Load an image or a mask from a file.

    Input:
        filename (str): the name of the file containing the grid
          The filename must end in .ppm or .json

    Returns [List[List[Tuple(int, int, int))] | List[List[bool]]]: returns either an image
      or a mask depending on the file loaded.
    """
    assert filename.endswith(".ppm") or filename.endswith(".json"), \
        "The filename must end with .ppm (image file) ) or .json (mask)."

    if filename.endswith(".ppm"):
        return load_image(filename)
    else:
        return load_mask(filename)


def load_image(filename):
    """
    Load a file that is formatted using PPM P3 format.

    Input:
        filename (string): the name of the file containing the image

    Returns: list of lists of colors
    """
    try:
        f = os.path.exists(filename)
    except OSError:
        print(f"Cannot open {filename}")
        sys.exit(1)

    f = open(filename, "r")

    ppm_type = f.readline().strip()
    if ppm_type != "P3":
        print("Wrong file type. This function only loads P3 PPMs\n",
              file=sys.stderr)
        sys.exit(1)

    width, height = (int(x) for x in f.readline().strip().split())
    # We have no use for the max color
    _ = int(f.readline())

    rgbs = [int(x) for x in f.read().split()]
    assert len(rgbs) == height*width*3

    img = []
    rgbs_index = 0
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(tuple(rgbs[rgbs_index:rgbs_index + 3]))
            rgbs_index += 3
        img.append(row)

    f.close()
    return img

def write_image_to_file(filename, image):
    """
    Write an Image object to a file
    """

    tuples = []

    for pixel_row in image.pixels:
        tuple_row = []
        for pixel in pixel_row:
            r = pixel._Color__r
            g = pixel._Color__g
            b = pixel._Color__b

            tuple_row.append((r, g, b))
        tuples.append(tuple_row)

    write_image(filename, tuples)

def write_image(filename, img):
    """
    Write an image to a file in P3 PPM format

    Input:
        filename (string): the name of the file to write
        image (list of lists of colors): the image to write to the file
    """
    try:
        f = open(filename, "w")
    except OSError:
        print(f"Cannot open {filename}")
        sys.exit(1)

    print("P3", file=f)
    # output width height
    print(f"{len(img[0])} {len(img)}", file=f)
    print("255", file=f)
    for row in img:
        flatten = []
        for color in row:
            flatten.extend([str(c) for c in color])
        print(" ".join(flatten), file=f)
    f.close()


    
def load_mask(filename):
    """
    Load a mask file that is formatted using json

    Input:
        filename (string): the name of the file containing the image

    Returns [List[List[bool]]: a mask
    """
    try:
        f = os.path.exists(filename)
    except OSError:
        print(f"Cannot open {filename}")
        sys.exit(1)

    with open(filename, "r") as f: 
        return json.load(f)


def write_mask(filename, mask):
    """
    Write a mask to a JSON file.

    Inputs:
        filename [str]: the name of the file to write
        mask [List[List[bool]]]: the mask to write
    """

    try:
        json.dump(mask, open(filename, "w"))
    except OSError:
        print(f"Cannot write to {filename}")
        sys.exit(1)
    
