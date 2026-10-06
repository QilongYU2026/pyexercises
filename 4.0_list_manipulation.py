"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A list of monthly order quantities.
# 2. Process:Display the list, select one item, sort the list, and calculate the total.
# 3. Out:The original list, one selected item, the sorted list, and the total number of orders.
# 4. What my list is about, and what I computed from it:My list is about monthly order quantities. I computed the total because it shows the overall number of orders during the period.


# Your code below

num1 =2 
num2 = 3
num3 = 4

numbers = [5,6,7,8,1,2,3,4,5,6,7]

print(num1)
print(num2)
print(num3)

# show all in the list
print("The original list is:", numbers)

# show a item in the list
print("The third item of the list is:", numbers[2])

# list before sort
print("The list is not sorted", numbers)

# 自动对列表排序
numbers.sort()
print("The sorted list is:", numbers)

# sum of the list
total = sum(numbers)
print("The sum of the list", total)

# removing the last item from the list 删掉最后一个元素
numbers.pop()

#print the list after removing the last number
print("The list after removing the last:", numbers)