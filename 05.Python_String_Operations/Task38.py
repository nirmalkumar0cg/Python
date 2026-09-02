# Task 38 — Name Processor
# Create a program that takes a user's full name as input.

# Your program should:

# Remove extra spaces from the beginning and end.
# Display the original input.
# Display the cleaned name.
# Display the name in uppercase.
# Display the name in lowercase.
# Display the name in title case.
# Display the length of the name.
# Display the first character.
# Display the last character.
# Check whether the name contains a particular character.

user_name = str(input("Enter your full name: "))
print("Remove extra spaces from the beginning and end",user_name.strip())
print("Original Input:" ,user_name)
print("Name in uppercase:",user_name.upper())
print("Name in lowercase",user_name.lower())
print("Name in title",user_name.title())
print("Length of the name:",len(user_name))
print("First character:",user_name[0])
print("Last Character:",user_name[-1])
print("Searching for a in your name",user_name.find(user_name))

