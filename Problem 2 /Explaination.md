This Program has one pre-defined Dictionary which can have various operations that can be done on this dictionary 
Primarily we are using `update ` function of the `dictionary` to update and make new addition to the existing dictionary 
along with this we are using key to index find and update the record of existing student.
Rest of the explaination is available in the code as a comments.

```
student_and_grades = {
    'Virat': 'A',
    'Rohit': 'A',
    'Hardik': 'B',
    'Shubhman' : 'B',
    'KL Rahul':'B',
    'Shardul':'C'
}

#Adding new Student and Grade to the Dictionary
def add_new_student(name,grade):
    student_and_grades.update({name:grade})


#Updating the record of existing student by asking user for name of student 
def update_existing_student():
    stud_name = input("Enter name of student to update the grade\n")
    updated_grade = input("Enter upgraded grade you want to update\n")
    student_and_grades[stud_name] = updated_grade


def print_grades():
    print(student_and_grades)


#Printing students and grades with print_grade()
print_grades()

#Calling update function to update a student record 
update_existing_student()
print_grades()

#Adding new student by calling function defined above
stud_name = input("Enter name of new student to be added \n")
grade = input("Enter grade for new student\n")
add_new_student(stud_name,grade)
print_grades()

```
