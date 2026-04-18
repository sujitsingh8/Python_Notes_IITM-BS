''' Attributes and Methods '''

class Student:
    count = 0   # class attribute

    def __init__(self, a, b):
        self.roll_no = a
        self.name = b
        Student.count += 1   # automatically increment

    def display(self):       # method inside class
        print(self.roll_no, self.name)


s0 = Student(0, 'Sujit')
s0.display()
# 0 Sujit

s1 = Student(1, 'Harshit')
s1.display()
# 1 Harshit

print(Student.count)
# 2

''' Count is a variable inside a class Student and therefore belongs to he whole class. It is a class attribute. '''