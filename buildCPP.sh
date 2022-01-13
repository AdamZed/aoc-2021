#!/usr/bin/env bash

set -e

if [[ ! -f "bootstrap.sh" ]]; then
    cd ..
    if [[ ! -f "bootstrap.sh" ]]; then
        echo "Please run from within AoC directory"
    fi
fi

if [[ -z ${1} ]]; then
    echo 'Please supply the day'
    exit
fi

day="$1"
hday="$day"
if [[ "$day" -lt 10 ]]; then
    hday="0$day"
fi

cd "day$hday/" && c++ "day$day.cpp" -o "day$day.o" && "./day$day.o"