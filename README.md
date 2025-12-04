# AdventOfCode2025

## 2025/12/02
Here we go again with my attempt of remembering what developing looks like...

AoC in Python again this year - not enough spare time to learn a new programming language unfortunately.
Quite rubbish repo, I did not have the time to create proper helper functions.

| Day  | Puzzle name         | Part 1 ex. time (ms) | Part 1 complexity | Part 2 ex. time (ms) | Part 2 complexity | Notes                                     |
| ---- | ------------------- | -------------------- | ----------------- | -------------------- | ----------------- | ----------------------------------------- |
| 1    | Secret Entrance     | 0.9                  | O(n)              | 1.2                  | O(n)              | Simple loop, nothing fancy in my solution | 
| 2    | Gift Shop           | 1179                 | O(n*m)            | 6138                 | O(n*m)            | n = number of intervals, m = range of each interval. Can it be optimized?                      |
| 3    | Lobby               | 6.4                  | O(2n)             | 9.0                  | O(n^2)            | Nested loop for part 2                    | 
| 4    | Printing Department | 26 | O(n*2) | 815 | m*O(n^2) ~ O(n^3) | n = size of the square grid, m = number of iterations where we remove paper rolls (what is the upper bound?) |
