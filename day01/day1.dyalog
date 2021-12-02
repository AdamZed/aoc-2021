⍝ input is preloaded

⍝ my first attempts
Part1←{+/1↓⍵>¯1⌽⍵}
Part2←Part1 {¯2↓(⍵)+(1⌽⍵)+(2⌽⍵)}

⍝ my first attempt at making (at least part1) tacit
Part1←+/1↓⊢>¯1∘⌽

⍝ and now I have found out about using num,func,reduce for sliding window
Part1←+/2</⊢
Part2←Part1 3+/⊢

'Part 1: ', Part1 input
'Part 2: ', Part2 input