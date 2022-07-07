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


print(fib(45))
# super fast!
# space o(n)
#  time o(n)
