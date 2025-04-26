from Student_Processor import Process_Student

def main():
    # List of students
    students_info = [
        ("Alex", [85, 90, 78]),
        ("Taylor", [92, 88, 95]),
        ("Jordan", [76, 82, 79]),
    ]

    # Create and display students
    print("Welcome to the Student Grade Calculator")
    for name, scores in students_info:
        Process_Student(name, scores).display()

if __name__ == "__main__":
    main()