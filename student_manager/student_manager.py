from time import sleep

class Student:
    def __init__(self, name, marks, students):
        self.name = name
        self.marks = marks
        self.students = students


    def add_student(self, name, marks):
        self.students[name] = marks
        print("\nSuccessfully added a student.")


    def search_student(self, name):
        if name in self.students:
            print(f"\nName: {name}\nMarks: {self.students[name]}")
        else:
            print("Student not found!")

    
    def update_marks(self, name, marks):
        if name in self.students:
            self.students[name] = marks
            print("\nSuccessfully updated the marks.")
        else:
            print("Student not found!")


    def delete_student(self, name):
        if name in self.students:
            del self.students[name]
            print("\nSuccessfully deleted the student.")
        else:
            print("Student not found!")


    def display_all_students(self):
        print()
        SN = 1

        for name, marks in self.students.items():
            print(f"{SN}. Name: {name}\tMarks: {marks}\n")
            SN += 1


def main():
    student = Student("", 0, {})

    while True:
        display()

        choice = input("\nEnter your choice: ")

        if choice == '1':
            name = input("\nEnter name: ").strip().title()
            marks = int(input("Enter marks: "))

            student.add_student(name, marks)
        elif choice == '2':
            name = input("\nEnter name: ").strip().title()

            student.search_student(name)
        elif choice == '3':
            name = input("\nEnter name: ").strip().title()
            marks = int(input("Enter new marks: "))

            student.update_marks(name, marks)
        elif choice == '4':
            name = input("\nEnter name: ").strip().title()

            student.delete_student(name)
        elif choice == '5':
            student.display_all_students()
        elif choice == '6':
            print("\nExiting the program!")
            sleep(1.5)
            break


def display():
    print("\n===== STUDENT MANAGER =====")
    print("1. Add student\n2. Search student\n3. Update marks\n4. Delete student\n5. Show all students\n6. Quit the program")


if __name__ == "__main__":
    main()