#!/usr/bin/python3
""" posts email to url """
import urllib
import sys


data = {'email': sys.argv[2]}
data = urllib.parse.urlopen(data).encode('utf-8')

with urllib.request.urlopen(sys.argv[1], data=data) as response:
    content = response.read().decode('utf-8')
    print(content)
