#!/bin/bash
# get body size of a request
url="$1"
response=$(curl -sI "$url" | grep -i "Content-Length" | cut -d' ' -f2)
echo "$response"
