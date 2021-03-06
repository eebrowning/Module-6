# WHILE LOOP
#
# In this problem, write a function named "my_while_map" that accepts an
# iterable of strings as a parameter and returns a new list with strings from
# the original list that are all transformed to upper case. The function must
# use a while loop in its implementation.
#
# The str object in Python has a method on it named "upper".
#
# There are two sample data calls for you to use.

# WRITE YOUR FUNCTION HERE
def my_while_map(iter):
    lst = []
    i = 0
    while i < len(iter):
        lst.append(iter[i].upper())
        i += 1
    return lst
# Your code here

# TEST DATA


test = ["plop", "", "drop", "zop", "stop"]
print(my_while_map(test))  # > ["PLOP", "", "DROP", "ZOP", "STOP"]

test = []
print(my_while_map(test))  # > []
