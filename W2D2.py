class student:
    def __init__ (self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.gpa = 0.0

    def honor_roll(self):
        return self.gpa >= 3.5
    
    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

student1 = student("jacob", "000000")

print(f"{student1.name} was born with the following parameters...")
print(f"name: {student1.name}, student_id: {student1.student_id}, gpa: {student1.gpa}\n")

student1.update_gpa(3.8)
student1.student_id = 123456

print(f"{student1.name} grew up to have these new parameters...")
print(f"name: {student1.name}, student_id: {student1.student_id}, gpa: {student1.gpa}\n")

if student1.honor_roll():
    print(f"{student1.name} is awesome\n")
else:
    print(f"{student1.name} is less than awesome\n")