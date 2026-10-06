"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A positive integer entered by the user.
# 2. Process: Check every number from 1 to the user's number and determine if it is odd or even.
# 3. Out: "odd" or "even" for every number from 1 to the user's number.
# 4. What happens on 0, on a negative number, on a very large number: If the number is 0 or negative, the program displays a message asking for a positive number. If the number is greater than 100, it displays a message saying that the number is too large.

# Your code below
num = int(input("Enter a number:"))

for num in range (1,num+1):     #range左边包含右边不包含，所以要num+1
    result = num % 2
    if result != 0:
        print("odd!")
    else:
        print("even!!")