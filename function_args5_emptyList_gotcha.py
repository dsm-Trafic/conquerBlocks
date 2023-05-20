def createStudent(name, age, grades=None):
  if grades is None:
    grades = []
  return {
    'name': name,
    'age': age,
    'grades': grades
  }
 
def addGrade(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])

#Now if we create our students again and add grades to them:

chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)
 
addGrade(chrisley, 90)
addGrade(dallas, 100)

'''
We would get our expected result:

[90]
[100]
'''