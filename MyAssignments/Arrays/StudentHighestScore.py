'''Question 15 
Create a program that takes an array of student names and a corresponding array of their test 
scores. Use parallel arrays and iteration to find and display the name of the student with the 
highest score.'''
# Question 15: Find student with highest score using parallel arrays
ArrayStudentName = ["Ria", "Maria", "Jessi", "Rincy"]
ArrayStudentScore = [90, 100, 70, 60]
StudentWithHighestScore = []
highest_score = float('-inf')  # Initialize to negative infinity

# Iterate over names and scores in parallel using zip
for name, score in zip(ArrayStudentName, ArrayStudentScore):
    if score > highest_score:
        StudentWithHighestScore = [name]  # Start new list with current name
        highest_score = score
    elif score == highest_score:
        StudentWithHighestScore.append(name)  # Add name to list

# Display result
if StudentWithHighestScore:
    print(f"Student(s) with the highest score ({highest_score}): {', '.join(StudentWithHighestScore)}")
else:
    print("No students found")