"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user's answer.
# 2. Process: Keep asking the user to type yes until the answer is yes or 3 attempts are reached.
# 3. Out: The result and the total number of attempts.
# 4. My stop condition, my attempt limit, my summary: The program stops when the user answers yes or after 3 attempts. It accepts different capitalizations and extra spaces. The summary shows whether the user answered yes and how many attempts were made.


# Your code below

attempts = 0
answer = "no"

while answer != "yes" and attempts < 3:
    answer = input ("Type yes to stop").strip().lower()
    attempts = attempts + 1

if answer == "yes":
    print("Your answer is yes after", attempts, " times")
else:
    print("Maximum attempts reached")
    print("Total attempts: ", attempts)