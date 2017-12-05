#!/bin/bash
function run {
    echo day$1
    cd $1 && python3 "day$1.py" < "input.txt" && cd ..
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
    
