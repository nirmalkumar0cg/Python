user_age=int(input("Enter Your age"))
user_marks=float(input("Enter Your Marks:"))
has_id = bool(input("Do You Have A Id?(True/False)"))

if user_age>=18 and user_marks>=60 and has_id==True:
    print("Eligible")
else:
    print("Not Eligible")