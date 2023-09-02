#!/usr/bin/python3
""" posts email to url """
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data).encode('utf-8')

    with urllib.request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode("utf-8"))
