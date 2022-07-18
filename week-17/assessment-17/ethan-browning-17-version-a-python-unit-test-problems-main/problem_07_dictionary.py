# DICTIONARY
#
# Write a function named "my_filter" that takes a dictionary as a parameter.
# Return another dictionary that consists of the key/value pairs from the
# argument where the value has a length less than or equal to 3. Use any
# construct you would like to implement "my_filter".
#
# Test data follows.

# WRITE YOUR CODE HERE
# Your code here
def my_filter(dct):
    new = {}
    for k, v in dct.items():
        if len(v) <= 3:
            new[k] = v
    return new
    # def filter_f(entry):
    #     if len(dct[entry]) <= 3:
    #         new[entry] = dct[entry]
    # filter(filter_f, dct)

    # # return new
    # return list(filter(lambda entry: len(dct[entry]) <= 3, dct))


# TEST DATA
print(my_filter({1: ".", 2: "..", 5: "....."}))   # > {1: ".", 2: ".."}
print(my_filter({}))                              # > {}
print(my_filter({1: ".....", 2: "....", 5: ""}))  # > {5: ""}
