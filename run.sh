#!/bin/bash
function run {
    echo day$1
    python3 "$1/day$1.py" < "$1/input.txt"
}
if [ -z "$1" ]
then
    for f in **/*.py; do
        nr=${f%/*}
        run $nr
        echo ""
    done
else
    run $1
fi
    
