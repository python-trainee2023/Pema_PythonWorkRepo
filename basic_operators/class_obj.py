# Class & Object
class Student:
    def __int__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def introduce(self):
            return f"Hi, i'm {self.name}, and my id is {self.student_id}."


student1 = Student(101, "A", "first")
student2 = Student(101, "A", "first")

print(student1.introduce())
print(student2.introduce())

