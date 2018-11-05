import os.path

## Module to make reading from data files easier.
## create constant strings to store filepaths
CANADA_PATH = "data/TSP_Canada_4663.txt"
URUGUAY_PATH = "data/TSP_Uruguay_734.txt"
SAHARA_PATH = "data/TSP_WesternSahara_29.txt"

def read_pos_from_file(filepath):
    """
        Given a file path will read from file and parse position data
        into a list of tuples.
        args:
            string : the file path
        returns:
            list of tuples representing x, y coordinate
    """
    data = []
    if (os.path.isfile(filepath)):
        with open(filepath) as f:
            for line in f:
                split = line.split()
                data.append((float(split[1]), float(split[2])))
        return data
    else:
        print("ERROR: file at path '", filepath, "' could not be found.")
    
