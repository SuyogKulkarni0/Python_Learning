The code in this problem has a basic usage of `input ` Function and `if .. elif ..else` statement.
In the first line we are getting user input converting it into int type carry out the conditional checks on the input 
If the input qualifies given range that for A , B, C, D, and F Grade the results are printed.


Else is the final condition if the user gives a wrong input or a score that does not match above if and elif conditions 
the final else statement will be executed.

```
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

```
