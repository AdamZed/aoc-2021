set -e

source ./.aoc_session.sh

if [[ -z ${1} ]]; then
    echo 'Supply day'
    exit
fi

year="2021"
day="$1"
hday="$day"
if [[ "$day" -lt 10 ]]; then
    hday="0$day"
fi

daydir="day$hday"
if [[ ! -d "$daydir" ]]; then
    mkdir $daydir
fi

if [[ ! -f "$daydir/input.txt" ]]; then
    curl https://adventofcode.com/$year/day/$day/input \
        --cookie "session=$AOC_SESSION" \
        -o "$daydir/input.txt"
fi

touch "$daydir/sample.txt"
cp template.py "$daydir/day$day.py"