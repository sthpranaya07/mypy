from time import sleep

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def add_student(self, name, marks, my_dictionary):
        my_dictionary[name] = marks
        print("\nSuccessfully added a student.")


    def search_student(self, name, my_dictionary):
        if name in my_dictionary:
            print(f"\nName: {name}\nMarks: {my_dictionary[name]}")
        else:
            print("Student not found!")

    
    def update_marks(self, name, marks, my_dictionary):
        if name in my_dictionary:
            my_dictionary[name] = marks
            print("\nSuccessfully updated the marks.")
        else:
            print("Student not found!")


    def delete_student(self, name, my_dictionary):
        if name in my_dictionary:
            del my_dictionary[name]
            print("\nSuccessfully deleted the student.")
        else:
            print("Student not found!")


    def display_all_students(self, my_dictionary):
        print()
        SN = 1

        for name, marks in my_dictionary.items():
            print(f"{SN}. Name: {name}\tMarks: {marks}\n")
            SN += 1


def main():
    students = {}
    student = Student("", 0)

    while True:
        display()

        choice = input("\nEnter your choice: ")

        if choice == '1':
            name = input("\nEnter name: ").strip().title()
            marks = int(input("Enter marks: "))

            student.add_student(name, marks, students)
        elif choice == '2':
            name = input("\nEnter name: ").strip().title()

            student.search_student(name, students)
        elif choice == '3':
            name = input("\nEnter name: ").strip().title()
            marks = int(input("Enter new marks: "))

            student.update_marks(name, marks, students)
        elif choice == '4':
            name = input("\nEnter name: ").strip().title()

            student.delete_student(name, students)
        elif choice == '5':
            student.display_all_students(students)
        elif choice == '6':
            print("\nExiting the program!")
            sleep(1.5)
            break


def display():
    print("\n===== STUDENT MANAGER =====")
    print("1. Add student\n2. Search student\n3. Update marks\n4. Delete student\n5. Show all students\n6. Quit the program")


if __name__ == "__main__":
    main()