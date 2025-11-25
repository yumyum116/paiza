#!/bin/bash

INPUT=input.txt

echo "### submit.py ###"
time python3 submit.py < $INPUT > /dev/null

echo -e "\n### fast_approach.py ###"
time python3 fast_approach.py < $INPUT > /dev/null

echo -e "\n### cache.py ###"
time python3 cache.py < $INPUT > /dev/null
