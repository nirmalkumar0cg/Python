# Task 40 — Student Information
# Create a program that takes the following information from the user:

# First name
# Last name
# City
# Course
# Age
# The program should:

# Remove unnecessary spaces from text inputs.
# Create the full name.
# Display the full name in title case.
# Display the full name in uppercase.
# Display the full name in lowercase.
# Display the length of the full name.
# Display the first character of the full name.
# Display the last character of the full name.
# Display the city and course.
# Display the age using an f-string.
# Check whether the course contains "Python".
# Replace one word in the course name with another word.
# Display the number of words in the course name.
 
first_name = input("Enter Your First Name:")
last_name = input("Enter Your Last Name:")
user_city =input("Enter Your City:")
user_course = "Python  HTML"
user_age = int(input("Enter Your Age:"))
full_name = first_name + last_name
strip = first_name.strip(),last_name.strip(),user_city.strip()
print(full_name.capitalize(),full_name.upper(),full_name.lower(),len(full_name),full_name[0],full_name[-1],user_city,user_course, f"User Age is {user_age}")
print(user_course.count("Python"))
replace_string = user_course.replace("Python", "CSS")
print(replace_string)

