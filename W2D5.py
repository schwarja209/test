def calculate (score1, score2, score3):
    total = score1 + score2 + score3
    average = total / 3

    grade = ""
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    
    return [total, average, grade]

# This program calculates grades for different students
# Notice how similar code is copied and pasted multiple times
print("Welcome to the Student Grade Calculator")

student1_name = "Alex"
student1_score1 = 85
student1_score2 = 90
student1_score3 = 78

print(f"\nStudent: {student1_name}")
print(f"Scores: {student1_score1}, {student1_score2}, {student1_score3}")
print("Average: ", calculate(student1_score1, student1_score2, student1_score3)[1])
print("Grade: ", calculate(student1_score1, student1_score2, student1_score3)[2])

student2_name = "Taylor"
student2_score1 = 92
student2_score2 = 88
student2_score3 = 95

print(f"\nStudent: {student2_name}")
print(f"Scores: {student2_score1}, {student2_score2}, {student2_score3}")
print("Average: ", calculate(student2_score1, student2_score2, student2_score3)[1])
print("Grade: ", calculate(student2_score1, student2_score2, student2_score3)[2])

student3_name = "Jordan"
student3_score1 = 76
student3_score2 = 82
student3_score3 = 79

print(f"\nStudent: {student3_name}")
print(f"Scores: {student3_score1}, {student3_score2}, {student3_score3}")
print("Average: ", calculate(student3_score1, student3_score2, student3_score3)[1])
print("Grade: ", calculate(student3_score1, student3_score2, student3_score3)[2])
