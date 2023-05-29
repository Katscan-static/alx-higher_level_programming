#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, str):
            if value.isdigit():
                value = int(value)
        print("{:d}".format(value))
        return True
    except ValueError:
        False
