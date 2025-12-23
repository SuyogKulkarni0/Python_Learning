#Taking user input for score and converting the string input to int to do Conditional check
grade_inp = int(input("Enter your Score to check the grade\n"))
if grade_inp >= 90 :
    print("Grade : A")
elif grade_inp < 90 and grade_inp >=80: 
    print("Grade : B")
elif grade_inp < 80 and grade_inp >=70:
    print("Grade : C")
elif grade_inp < 70 and grade_inp >=60:
    print("Grade : D")
else:
    print("Grade : F")

