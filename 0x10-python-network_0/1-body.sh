#!/bin/bash
# return body of 200
url="$1"; response=$(curl -s -o /dev/null -w "%{http_code}" "$url"); [ "$response" -eq 200 ] && curl -s "$url"
