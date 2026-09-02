# Task 37
# Run each piece of code separately.

# Identify the error produced by each.

# A
# text = "Python"
# print(text[20])
# B
# text = "Python"
# text[0] = "J"
# C
# age = 20
# print("Age: " + age)
# D
# text = "Python"
# print(text.index("Java"))
# For each:

# Identify the error.
# Explain why it occurred.
# Write the corrected version where possible.


# text = "Python"
# print(text[20])
#IndexError.
#It Occurred Because the index specified in the print function is 20.
# There are only 0,1,2,3,4,5 in python so dont take more than 5.


# text = "Python"
# text[0] = "J"
# TypeError
# String is immutable so we cant change string sub's string data.
# text = "Python"
# print(text.replace("P","J"))


# age = 20
# print("Age: " + age)
# TypeError
# Because we cannot merge str and int data types


# age = 20
# print("Age:",str(age))
# text = "Python"
# print(text.index("Java"))
# ValueError
# Because the index value we are trying to find doesn't exists
