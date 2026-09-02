# Task 30 — User Input
# Take a name from the user using input().

# Assume the user may accidentally enter spaces before or after the name.

# Remove the extra surrounding spaces and display the cleaned name.

a = str(input("Enter Your Name:"))
b = a.strip()
print(b)