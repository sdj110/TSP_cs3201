

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
def format_string(data):
    pass

if __name__ == '__main__':

    filename = "sahara/500p_2t.json"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    ## Fix poor formatting in data file.
    data = read_file(filename)
    format_data = data.replace('}{', '}!{').split('!')

    ## build dictionary of dicts thanks to json lib
    dict_list = []
    for d in format_data:
        dict_list.append(json.loads(d))

    ## extract needed into into seperate lists
    data_dict = {
        "time" : "",
        "generation" : "",
        "best_fitness" : "",
        "avg_fitness" : ""
    }
    for d in dict_list:
        data_dict["time"] += str(d["elapsed_time"]) + ","
        data_dict["generation"] += str(d["generation"]) + ","
        data_dict["best_fitness"] += str(d["best_fitness"]) + ","
        data_dict["avg_fitness"] += str(d["avg_fitness"]) + ","

    write_file(filename + "_results.txt", data_dict)
