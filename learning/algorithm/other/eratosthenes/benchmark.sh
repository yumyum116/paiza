#!/bin/bash

N=10000000
PYTHON=python3

FILES=(
    "eratosthenes.py"
    "eratosthenes_odd.py"
    "eratosthenes_bytearray.py"
    "eratosthenes_fast.py"
)

echo "Benchmark n=${N}"
echo "=========================="

for file in "${FILES[@]}"
do
    echo ""
    echo ">>> ${file}"
    time ${PYTHON} ${file} ${N}
done
