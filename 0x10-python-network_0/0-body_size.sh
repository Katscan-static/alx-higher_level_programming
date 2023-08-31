#!/bin/bash
#get body size of a request
url="$1"
curl -sI "$url" | grep -i "Content-Length" | cut -d' ' -f2
