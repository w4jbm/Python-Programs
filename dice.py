#!/usr/bin/python3
#
# Dice Problem Solution in Python
# by Jim McClanahan, W4JBM
# February/March 2023
#
# I found that this puzzle is actually the same as one in The Time
# called Teaser 2598.

import math

# This function tests an argument and returns True if it is a prime number
# and False if it is not.
def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

# Checks that a 3 digit number could really appear with a roll of 3 dice
# No digits in the number below 1 and no numbers above 6
def is_dice3(n):
    for i in range(0,3):
        if ((n % 10) < 1) or ((n % 10) > 6):
            return False
        n = int(n / 10)
    return True

# Reverses a 3 digit number that could really appear with a roll of 3 dice
def rev_dice3(n):
    rev_n = 0
    position_n = 100
    for i in range(0,3):
        rev_n = rev_n + (position_n * (n %10))
        n = int(n / 10)
        position_n = position_n / 10
    return(int(rev_n))

# Return how many members are shared between two lists.
def common_member_count(a, b):
    a_set = set(a)
    b_set = set(b)
    return(len(a_set & b_set))

# Check that three digits could really be part of a real dice by
# 1) Making sure the numbers for each die are different and,
# 2) Making sure the opposit sides add to seven.
def check_dice3(d1, d2, d3):
    for i in range(0,3):
        dice_side1 = (d1 % 10)
        dice_side2 = (d2 % 10)
        dice_side3 = (d3 % 10)
        if (dice_side1 == dice_side2) or (dice_side1 == dice_side3)\
         or (dice_side2 == dice_side3):
            return(False)
        if (dice_side2 + dice_side3) != 7:
            return(False)
        d1 = int(d1 / 10)
        d2 = int(d2 / 10)
        d3 = int(d3 / 10)
    return(True)

# Without the following, you get six possible answers:
#
# [144, 441, 421, 653]
# [144, 441, 461, 613]
# [163, 361, 251, 625]
# [361, 163, 625, 251]
# [441, 144, 613, 461]
# [441, 144, 653, 421]
#
# But the question narrows this down by saying the number of pips shown
# is an odd number. We know the first die is the 'top', so the values
# there and the value on the bottom (which is not showing) will sum to
# 7. There are 21 pips total on a normal die which means we have 63 pips
# minus (7 - top value) for each of the three die.
#
# With some thinking, we can see that for the exposed pips to sum to
# an odd number, the number of pips "hidden" on the bottom of the three
# dice must be an even number.
#
# This function checks to see if the three opposite sides of the value
# given would be even (return True) or odd (return False).
def check_even3(n):
    total_hid = 0
    for i in range(0,3):
        total_hid = total_hid + (n % 10)
        n = int(n / 10)
    if (total_hid % 2) == 0:
        return(True)
    return(False)

print('Katy places three identical standard dice in a row on a table-top,')
print('leaving just eleven faces and an odd number of pips visible.')
print('')
print('Taking each face as a digit (with the number of pips representing')
print('the number), from the front Katy can read a three-digit number along')
print('the vertical faces of the dice and another three-digit number along')
print('the top. If Katy goes to the opposite side of the table, she can read')
print('a three-digit number along the vertical faces and another three-digit')
print('number along the top.')
print('')
print('Of the four three-digit numbers Katy read, two are primes and two are')
print('different perfect squares.')
print('')
print('What four three-digit numbers does Katy see? (Two from the front and')
print('two from the back.)')
print('')

# Hint: The digits on the top will be seen as "reversed" when viewed from
# different sides, so we need to find a number that is either a prime or a
# square when read forward or backwards.
#
# Constraint: Obviously, the digits represented by each face of a die must
# only appear once. (That is, a dice cannot be showing a '2' on one face and
# a '2' on another face.)
#
# Constraint: Obviously since we are using digits from a die, only the
# digits 1 through 6 can appear in any number in the solution.
#
# Constraint: Opposite sides of a die total to a value of 7.
#
# Constraint: For an odd number of pips to be visible, an even number of
# pips must be "invisible" on the bottom of the dice.


# Build list of 3 digit prime numbers with only digits between 1 and 6 as
# you would find on the face of a die.

Debug = False

primes = []

for i in range(111,667):
    if is_prime(i):
        if is_dice3(i) or Debug:
            primes.append(i)
print('Primes for 3 Dice:')
print(primes)
print('')

squares = []

for i in range(int(math.sqrt(111)), int(math.sqrt(666))+1):
    if is_dice3(i*i) or Debug:
        squares.append(i*i)
print('Squares for 3 Dice:')
print(squares)
print('')

#Loop through all dice and
print('Order is Dice 1-3 read on top from the front, Dice 3-1 read on the top')
print('from the back, Dice 1-3 read from the front, and Dice 3-1 read from')
print('the back. Possible combinations are:')
for face1 in range(111,666):
    if is_dice3(face1) == False:
        continue
    for face2 in range(111,666):
        if is_dice3(face2) == False:
            continue
        for face3 in range(111,666):
            if is_dice3(face3) == False:
                continue
            if check_dice3(face1, face2, rev_dice3(face3)) == False:
                continue
            if check_even3(face1) == False:
                continue
            dice_list = [face1, rev_dice3(face1), face2, face3]
            if common_member_count(dice_list, primes) ==2 and\
               common_member_count(dice_list, squares)==2:
                print(dice_list)
