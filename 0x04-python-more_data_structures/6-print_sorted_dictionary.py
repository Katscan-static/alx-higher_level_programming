#!/usr/bin/pythom3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = {k: a_dictionary[k] for k in sorted(a_dictionary.keys())}
    print(sorted_dict)
