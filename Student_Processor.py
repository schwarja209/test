class Process_Student:
    grade_thresholds = [
        (90, "A"),
        (80, "B"),
        (70, "C"),
        (60, "D")
    ]

    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.total = sum(scores)
        self.average = self.total / len(scores)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        for threshold, grade in Process_Student.grade_thresholds:
            if self.average >= threshold:
                return grade
        return "F"

    def display(self):
        print(f"\nStudent: {self.name}")
        print(f"Scores: {', '.join(map(str, self.scores))}")
        print(f"Average: {self.average:.2f}")
        print(f"Grade: {self.grade}")