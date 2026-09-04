student_marks = int(input("Enter Your Marks:"))
if student_marks >= 90:
    print("Excellent")
elif student_marks > 70 and student_marks < 90:
    print("Good")
elif student_marks < 50 and student_marks > 20:
    print("Pass")
else:
    print("Fail")
