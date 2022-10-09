#!/bin/bash

obs=$1
exp=$2

if ! cmp $obs $exp; then
    echo "Expected:"
    echo "------------------------------------"
    cat $exp
    echo "------------------------------------"
    echo
    echo "Observed:"
    echo "------------------------------------"
    cat $obs
    echo "------------------------------------"
    exit 2
fi

exit 0
