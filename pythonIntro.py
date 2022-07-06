# def get_average(num1, num2):
#     average = (num1 + num2) / 2
#     print(average)
#     if True:
#         print("hello")
#     return average


# print(get_average(4, 6))

# name = input("What is your name?")
# print("Hi," + name + ".")
# print("Hi, %s" % name)
# print("Hi, {0}.".format(name))
# print(f"Hi, {name}.")

# a = "a"
# b = "b"
# an = "an"
# print(b + an + an + a)


# for character in "aabbccaaa":
#     print(character)

# total = 0
# for num in range(101):
#     total += num
# print(total)


# print("My name is")
# for i in range(5):
#     print("Carlita Cinco (" + str(i) + ")")

# a = True
# try:
#     print(len(a))
# except:
#     print(f"{a} aint have no lenth")

# lambda
toUpper = lambda str: str.upper()
# works like "let toUpper=(str)=>{str.toUpperCase()}"
# print(toUpper("string"))

# return a function from a function
# def greeting_maker(salutation):
#     def greeting(name):
#         return f"{salutation} {name}"

#     return greeting

# hello = greeting_maker("Hello")
# hiya = greeting_maker("Hiya")
# print(hello("Ethan"))
# print(hiya("Ethan"))


# def lunch(food):
#     if food == "nothing":
#         print(f"{food} is my favorite food")
#     elif food == "something":
#         print(f"i guess i should eat {food}")
#     else:
#         print(f"{food} is just okay")


# lunch("something")


# def first_before_second(string, letter1, letter2):
#     letter1_last_index = string.rindex(letter1)
#     letter2_first_index = string.index(letter2)
#     return letter1_last_index < letter2_first_index

# print(first_before_second("a rabbit jumps joyfully", "a", "j"))
