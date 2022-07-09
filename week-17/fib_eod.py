# def fib(num):
#     if num == 2:
#         return 1
#     elif num == 1:
#         return 0
#     else:
#         return fib(num - 1) + fib(num - 2)
# print(fib(5))
#  space o(n)
#  time  2^n


def fib(num, dic={1: 0, 2: 1}):
    if num in dic:
        return dic[num]
    else:
        dic[num] = fib(num - 1, dic) + fib(num - 2, dic)
        return dic[num]


# print(fib(45))
# super fast!
# space o(n)
#  time o(n)


# set1 = {1, 2, 3}
# set2 = {2, 4, 6}
# print(a - b)  # => {1, 3}
# print(b - a)  # => {4, 6}
# print(a ^ b)  # => {1, 3, 4, 6}

set1 = {1, "hello", 3, 4}
set2 = {"hello", 3, 6}
print(set1 - set2)
print(set1 ^ set2)
print(set2 & set1)
