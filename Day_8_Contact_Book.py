contacts = {}

def show_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Contact")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contacr {name} has added to contact book successfully")

def view_contacts():
    if contacts:
        print("\n--- Contacts ---")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
    else:
        print("Your contact book is empty")
    
def search_contact():
    name = input("Enter name: ")
    if name in contacts:
        print(f"\n--- Contact Details for {name} ---")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"Contact {name} not found")

def edit_contact():
    name = input("Enter name: ")
    if name in contacts:
        print(f"\n--- Edit Contact for {name} ---")
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email: ")
        contacts[name]['phone'] = phone
        contacts[name]['email'] = email
        print(f"Contact {name} has been edited successfully")
    else:
        print(f"Contact {name} not found")

def delate_contact():
    name = input("Enter name: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} has been deleted successfully")
    else:
        print(f"Contact {name} not found")

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        edit_contact()
    elif choice == '5':
        delate_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")