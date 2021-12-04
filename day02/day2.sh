depth=0; pos=0;
while read line; do
  entry=($line)
  dir=${entry[0]}
  dis=${entry[1]}
  case $dir in
    forward) ((pos+=dis));;
    up) ((depth-=dis));;
    down) ((depth+=dis));;
  esac
done < input.txt
echo "Part 1: $((depth*pos))"

aim=0; depth=0; pos=0
while read line; do
  entry=($line)
  dir=${entry[0]}
  dis=${entry[1]}
  case $dir in
    forward)
      ((pos+=dis))
      ((depth+=aim*dis))
    ;;
    up) ((aim-=dis)) ;;
    down) ((aim+=dis)) ;;
  esac
done < input.txt
echo "Part 2: $((depth*pos))"
