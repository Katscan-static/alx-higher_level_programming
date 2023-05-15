#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_list = []
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        new_list = my_list.copy()
        new_list[idx] = element
    return new_list
