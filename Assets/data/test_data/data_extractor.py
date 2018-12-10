
from pathlib import Path
import os
import sys
import json

def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

def write_file(filename, data_dict):
    with open(filename, 'w') as f:
        for key in data_dict:
            f.write(key + '\n')
            f.write(data_dict[key])
            f.write('\n\n')

if __name__ == '__main__':

    pathlist = Path(os.getcwd()).glob('**/*.json')
    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)
        
        filename = path_in_str

        ## Fix poor formatting in data file.
        data = read_file(filename)
        format_data = data.replace('}{', '}!{').split('!')

        ## build dictionary of dicts thanks to json lib
        dict_list = []
        for d in format_data:
            dict_list.append(json.loads(d))

        ## extract needed data into seperate strings
        data_dict = {
            "time" : "",
            "generation" : "",
            "best_fitness" : "",
            "avg_fitness" : ""
        }
        for d in dict_list:
            data_dict["time"] += str(d["elapsed_time"].split(":")[2]) + ","
            data_dict["generation"] += str(d["generation"]) + ","
            data_dict["best_fitness"] += str(d["best_fitness"]) + ","
            data_dict["avg_fitness"] += str(d["avg_fitness"]) + ","

        write_file(filename + "_results.txt", data_dict)

        print("Data saved to file ", filename + "_results.txt")


    