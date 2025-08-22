class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

# Take input from the console
name = input("Enter student's name: ")
roll_no = input("Enter student's roll number: ")
try:
    marks = float(input("Enter student's marks: "))
except ValueError:
    print("Invalid input for marks. Please enter a number.")
    marks = 0.0

student = Student(name, roll_no, marks)
student.display_details()

