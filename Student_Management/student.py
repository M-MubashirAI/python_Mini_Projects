import json  # Importing JSON module for file handling

class Student:
    """
    Represents a Student with attributes: ID, Name, Course, and Marks.
    """
    def __init__(self, student_id, name, course, marks):
        self.student_id = student_id  # Unique Student ID
        self.name = name  # Student Name
        self.course = course  # Course Enrolled
        self.marks = marks  # Marks obtained

    def to_dict(self):
        """Converts student object to dictionary for JSON storage"""
        return {
            "ID": self.student_id,
            "Name": self.name,
            "Course": self.course,
            "Marks": self.marks
        }

class StudentManager:
    """
    Manages the student records: Add, Update, Delete, Search, and Display.
    """
    FILE_NAME = "students.json"  # File to store student records

    def __init__(self):
        self.students = []  # List to hold student objects
        self.load_students()  # Load existing students from file

    def load_students(self):
        """Loads student records from the JSON file."""
        try:
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)
                self.students = [Student(**student) for student in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.students = []  # If file not found, initialize an empty list

    def save_students(self):
        """Saves student records to the JSON file."""
        with open(self.FILE_NAME, "w") as file:
            json.dump([student.to_dict() for student in self.students], file, indent=4)

    def add_student(self, student_id, name, course, marks):
        """Adds a new student record."""
        if any(student.student_id == student_id for student in self.students):
            print("Student ID already exists! Choose a unique ID.")
            return
        student = Student(student_id, name, course, marks)
        self.students.append(student)
        self.save_students()
        print("Student added successfully!")

    def update_student(self, student_id, name=None, course=None, marks=None):
        """Updates an existing student record."""
        for student in self.students:
            if student.student_id == student_id:
                if name:
                    student.name = name
                if course:
                    student.course = course
                if marks is not None:
                    student.marks = marks
                self.save_students()
                print("Student updated successfully!")
                return
        print("Student not found!")

    def delete_student(self, student_id):
        """Deletes a student record by ID."""
        self.students = [student for student in self.students if student.student_id != student_id]
        self.save_students()
        print("Student deleted successfully!")

    def search_student(self, student_id):
        """Searches for a student by ID and displays details."""
        for student in self.students:
            if student.student_id == student_id:
                print(f"Student Found: {student.to_dict()}")
                return
        print("Student not found!")

    def display_students(self):
        """Displays all student records in a structured format."""
        if not self.students:
            print("No students found!")
            return
        print("\n=== Student Records ===")
        for student in self.students:
            print(student.to_dict())
        print("========================")

# Main program to interact with user
def main():
    manager = StudentManager()
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Display All Students")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            course = input("Enter Course: ")
            marks = float(input("Enter Marks: "))
            manager.add_student(student_id, name, course, marks)
        
        elif choice == "2":
            student_id = input("Enter Student ID to update: ")
            name = input("Enter new name (leave blank to skip): ") or None
            course = input("Enter new course (leave blank to skip): ") or None
            marks = input("Enter new marks (leave blank to skip): ")
            marks = float(marks) if marks else None
            manager.update_student(student_id, name, course, marks)
        
        elif choice == "3":
            student_id = input("Enter Student ID to delete: ")
            manager.delete_student(student_id)
        
        elif choice == "4":
            student_id = input("Enter Student ID to search: ")
            manager.search_student(student_id)
        
        elif choice == "5":
            manager.display_students()
        
        elif choice == "6":
            print("Exiting the Student Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
