set -e

if [[ -f "bootstrap.sh" ]]; then
    echo "Please run from same directory"
fi

if [[ -z ${1} ]]; then
    echo 'Supply day'
    exit
fi

AOC_SESSION=$(cat .aoc_session)

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
    curl -s https://adventofcode.com/$year/day/$day/input \
        --cookie "session=$AOC_SESSION" \
        -o "$daydir/input.txt"
fi

touch "$daydir/sample.txt"

if [[ ! -f "$daydir/day$day.py" ]]; then
    cp template.py "$daydir/day$day.py"
fi