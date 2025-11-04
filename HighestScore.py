List_Students =[
    {"name" : "Alice" , "score" : 85},
    {"name" : "Bob" , "score" : 92},
    {"name" : "Charlie" , "score" : 78},
    {"name" : "David" , "score" : 95},
    {"name" : "Eva" , "score" : 88}
]
highest_score = -1
top_student = None
for student in List_Students:
    if student["score"] > highest_score:
        highest_score = student["score"]
        top_student = student["name"]
print(f"The highest score is {highest_score}, achieved by {top_student}.")


