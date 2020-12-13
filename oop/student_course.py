class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0-100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student("Aditya", 21, 9.69)
s2 = Student("Sanan", 23, 8.24)
s3 = Student("Saransh", 25, 6.30)

science = Course("Science", 2)
science.add_student(s1)
science.add_student(s2)
print(science.add_student(s3))

print(science.get_avg_grade())
