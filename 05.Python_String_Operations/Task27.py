# Task 27 — Limited Replacement
# Using the same string, replace only the first "apple".

# Use the third argument of replace().

# Task 28 — Check Immutability
# Create:

# text = "Python"
# Call:

# text.upper()
# Then print text.

# Observe whether the original string changed.

# Then store the result back into text and print it again.
text = "apple apple apple"
newtext= text.replace("apple", "mango", 1)
print(newtext)

