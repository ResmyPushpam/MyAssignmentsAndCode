try:
    student = {'name' : 'Alice', 'age' : 23, 'courses' : ['Math', 'CompScience']}
    print("Student Name:", student['name'])
    print("Student Age:",student['age'])
    print("Student Courses:",student['courses'])
except KeyError as ke:
    print("An error occurred:", ke)




    