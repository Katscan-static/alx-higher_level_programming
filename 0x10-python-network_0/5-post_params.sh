#!/bin/bash
#send data via post
curl -s -d "email:test@gmail.com&subject:I will always be here for PLD" "$1"
