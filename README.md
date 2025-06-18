## sudoku-solver-generator
### My sudoku solver/generator that stemmed from a short Python exercise
During the pythonic block of the infoshare Academy *Data Science* course we were asked to write a simple Python program that would show a text-based representation of a 9x9 sudoku board to the player, enable insertion and modification of the digits in the cells (those that were orignally empty) and - finally - verify the filled board for correctness.
I figured: why not try and write a **sudoku generator** in Python?
It quickly turned out a sensible intermediate waypoint would be to write a **sudoku solver** function as well.

<ins>I decided to have some fun and set out the following goals:</ins>\
:white_check_mark: Write the text-based interface and solution verification function I was originally asked for;\
:white_check_mark: Write a "simple solver" function that would fill a cell when it only has one possible candidate digit;\
:white_medium_square: Write a "brute solver" function to solve harder sudokus and count the number of possible solutions (I guess only one possible solution should be expected of a good suodku);\
:white_medium_square: Move on to generating sudokus by stripping down random solved (valid) diagrams until a puzzle is obtained (with one unique solution);\
:white_medium_square: Add export to HTML / export to PDF functionality, producing printable puzzles one may enjoy unplugged :writing_hand:
