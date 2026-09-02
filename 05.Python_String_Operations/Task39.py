# Task 39 — Sentence Analyzer
# Take a sentence from the user.

# Your program should display:

# The original sentence.
# Number of characters.
# Number of words.
# First character.
# Last character.
# Sentence in uppercase.
# Sentence in lowercase.
# Sentence in title case.
# Whether "Python" exists in the sentence.
# Number of times a chosen character occurs.

user_input= str(input("Enter a sentence:"))
print("original sentence:",user_input)
print("Number of characters:",len(user_input))
print("Number Of Words:", len(user_input.split()))
print("First Character", user_input[0])
print("Last Character",user_input[-1])
print("Sentence in uppercase:", user_input.upper())
print("Sentence in lower", user_input.lower())
print("Sentence in title",user_input.title())
print("Is the word Pythong present in the sentence:", "Python" in user_input)
user_ask=("Enter the letter you want to find how many times it occured:") 
print("")

