#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    result = {i: a_dictionary[i] for i in keys}
    for j in result:
        print("{} : {}".format(j, result[j]))
