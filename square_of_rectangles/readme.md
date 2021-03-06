# Square of rectangles

The [`rectangles.py`](https://github.com/tylerneylon/puzzles/blob/master/square_of_rectangles/rectangles.py)
script solves a physical puzzle given to my friend John Bohannon.
I'm not sure of the original author of the puzzle.
It consists of 12 rectangles, each marked clearly with a pair of integer dimensions.
The goal is to combine all the pieces into a gapless partition of a larger
rectangle.

This script finds a solution in about 2.5 seconds.

```
$ time python rectangles.py 56 56
Found a solution!
+---------------------------------------------------------------+-------------------+---------------------------+
|32x11                                                          |10x32              |14x21                      |
|                                                               |                   |                           |
|                                                               |                   |                           |
|                                                               |                   |                           |
|                                                               |                   |                           |
|                                                               |                   |                           |
|                                                               |                   |                           |
|                                                               |                   |                           |
|                                                               |                   |                           |
|                                                               |                   |                           |
+---------------------------+-----------------------------------|                   |                           |
|14x17                      |18x21                              |                   |                           |
|                           |                                   |                   |                           |
|                           |                                   |                   |                           |
|                           |                                   |                   |                           |
|                           |                                   |                   |                           |
|                           |                                   |                   |                           |
|                           |                                   |                   |                           |
|                           |                                   |                   |                           |
|                           |                                   |                   |                           |
|                           |                                   |                   +---------------------------+
|                           |                                   |                   |14x21                      |
|                           |                                   |                   |                           |
|                           |                                   |                   |                           |
|                           |                                   |                   |                           |
|                           |                                   |                   |                           |
|                           |                                   |                   |                           |
+-------------+-------------|                                   |                   |                           |
|7x28         |7x10         |                                   |                   |                           |
|             |             |                                   |                   |                           |
|             |             |                                   |                   |                           |
|             |             +-----------------------------------+-------------------|                           |
|             |             |28x6                                                   |                           |
|             |             |                                                       |                           |
|             |             |                                                       |                           |
|             |             |                                                       |                           |
|             |             |                                                       |                           |
|             +-------------+---------------------------+---------------------------|                           |
|             |21x18                                    |14x4                       |                           |
|             |                                         |                           |                           |
|             |                                         |                           |                           |
|             |                                         +---------------------------+---------------------------+
|             |                                         |28x14                                                  |
|             |                                         |                                                       |
|             |                                         |                                                       |
|             |                                         |                                                       |
|             |                                         |                                                       |
|             |                                         |                                                       |
|             |                                         |                                                       |
|             |                                         |                                                       |
|             |                                         |                                                       |
|             |                                         |                                                       |
|             |                                         |                                                       |
|             |                                         |                                                       |
|             |                                         |                                                       |
+-------------+-----------------------------------------+-------------------------------------------------------+

real	0m2.485s
```
