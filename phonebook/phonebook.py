from time import sleep

def main():
    phonebook = {}
    
    while True:
        display()

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_contact(phonebook)
            print("Successfully added a contact.")
        elif choice == '2':
            search_contact(phonebook)
        elif choice == '3':
            remove_contact(phonebook)
        elif choice == '4':
            list_contacts(phonebook)
        elif choice == '5':
            close()
            break
        else:
            print("Invalid choice. Try again!")


def display():
    print("===== PHONEBOOK MENU =====\n")
    print("1. Add a contact\n2. Search a contact\n3. Remove a contact\n4. List all contacts\n5. Close the phonebook\n")


def add_contact(dict):
    contact = input("\nEnter name: ").strip().title()
    number = int(input("Enter number: "))

    dict[contact] = number

    return dict


def search_contact(dict):
    contact = input("\nEnter name: ").strip().title()

    if contact in dict:
        print(f"\nName: {contact}\nContact: {dict[contact]}")
    else:
        print("Contact not found!")

    print()


def remove_contact(dict):
    contact = input("\nEnter name: ").strip().title()

    if contact in dict:
        del dict[contact]
        print(f"Successfully removed {contact}'s contact.")
    else:
        print("Contact not found!")

    print()


def list_contacts(dict):
    print()

    for key, value in dict.items():
        print(f"{key}: {value}")

    print()


def close():
    print("Closing the phonebook.")
    sleep(1.5)


if __name__ == "__main__":
    main()