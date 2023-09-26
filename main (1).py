class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the student list in descending order of CGPA
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
students1 = [
    Student("Alice", "A101", 3.8),
    Student("Bob", "B102", 3.5),
    Student("Charlie", "C103", 4.0),
    Student("David", "D104", 3.9),
]

students2 = [
    Student("Eve", "E105", 3.2),
    Student("Frank", "F106", 3.7),
    Student("Grace", "G107", 3.6),
    Student("Helen", "H108", 3.3),
]

sorted_students1 = sort_students(students1)
sorted_students2 = sort_students(students2)

print("Sorted Students 1:")
for student in sorted_students1:
    print(f"{student.name} ({student.roll_number}): {student.cgpa}")

print("\nSorted Students 2:")
for student in sorted_students2:
    print(f"{student.name} ({student.roll_number}): {student.cgpa}")