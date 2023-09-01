#!/usr/bin/python3
""" posts email to url """
import urllib
import sys


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.parse.Request(sys.argv[1], data)

    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode("utf-8"))
        print(content)
