#!/usr/bin/python3
#
# sudoku_solve.py
#
# Jim McClanahan (W4JBM)
#
# Solve a sudoku puzzle. Nothing fancy and you have to enter
# the puzzle as part of the program.
#
# Bits an pieces from various sources and example, but started
# with this:
#
# https://see.stanford.edu/materials/icspacs106b/H19-RecBacktrackExamples.pdf
#
# Originally found that with a 6502 assembly langague example at:
#
# https://github.com/MoleskiCoder/6502_sudoku
#
# (Still working on the 6502 version in 64tass...)
#
# Puzzle from:
#
# http://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html

puzzle = [
    [ 8, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 3, 6, 0, 0, 0, 0, 0],
    [ 0, 7, 0, 0, 9, 0, 2, 0, 0],
    [ 0, 5, 0, 0, 0, 7, 0, 0, 0],
    [ 0, 0, 0, 0, 4, 5, 7, 0, 0],
    [ 0, 0, 0, 1, 0, 0, 0, 3, 0],
    [ 0, 0, 1, 0, 0, 0, 0, 6, 8],
    [ 0, 0, 8, 5, 0, 0, 0, 1, 0],
    [ 0, 9, 0, 0, 0, 0, 4, 0, 0]
]

# Solve the puzzle
def solve(pz):
    find = find_empty(pz)    # look for an empty spot in the puzzle
    if not find:             # if it is full, we've solved it
        return True
    else:                    # otherwise, let's try to fill this spot
        row, col = find

    for i in range(1,10):               # let's look at possible values
        if valid(pz, i, (row, col)):    # and see if one works
            pz[row][col] = i
            if solve(pz):               # recursion == magic
                return True
            pz[row][col] = 0 # if it didn't work, back things out

    return False


# Find the next empty cell in the puzzle
def find_empty(pz):
    for i in range(len(pz)):
        for j in range(len(pz[0])):
            if pz[i][j] == 0: # a zero indicates empty
                return (i, j)  # row, col
    return None


# See if num(ber) is valid for pos(ition)
def valid(pz, num, pos):
    for i in range(len(pz[0])):    # check row
        if pz[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(pz)):       # check column
        if pz[i][pos[1]] == num and pos[0] != i:
            return False

    # check 3x3 box (from upper left corner)
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if pz[i][j] == num and (i,j) != pos:
                return False

    return True


# print the puzzle
def print_puzzle(pz):
    for i in range(len(pz)):
        if i % 3 == 0 and i != 0:
            print("- - - + - - - + - - -")

        for j in range(len(pz[0])):
            if j % 3 == 0 and j != 0:
                print("! ", end="")

            if j == 8:
                print(pz[i][j])
            else:
                print(str(pz[i][j]) + " ", end="")


# Now that we've defined all the functions we need,
# let's see if we can solve the puzzle!
print("Original Puzzle:")
print_puzzle(puzzle)
if solve(puzzle):
    print("\nSolved Puzzle:")
    print_puzzle(puzzle)
else:
    print("\nThis does not seem to be a valid puzzle!")

