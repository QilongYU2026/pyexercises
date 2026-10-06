"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: My original list of monthly order quantities.
# 2. Process: Display the list in four different orders without changing the original list.
# 3. Out: Four different orders of the list and the original list at the end.
# 4. My four orders, and which ones modify the original:My four orders are original, ascending, descending, and reversed. sorted() and reversed() create new results. sort() modifies a list in place, so I use sort() only on a copy of the original list.


# Your code below

# 排序会生成新列表：sorted()；修改原列表的排序sort()；倒叙排列reverse=True; 生成新列表的倒叙reversed

numbers = [5,6,7,8,1,2,3,4,5,6,7]

print("The orignial list is: ", numbers)

# 生成新列表的排序
new_numbers = sorted(numbers)
print("Ascending ", new_numbers)

# 修改原列表的重新排序
copy_numbers = numbers.copy()
copy_numbers.sort()
print("Sorted: ", copy_numbers)

# 降序排列
print("Descending: ",sorted(numbers, reverse=True))

# 生成新列表的降序排列
backlist = list(reversed(numbers))
print("Reversing: ", backlist)  

print("The orignial list has not changed: ", numbers)