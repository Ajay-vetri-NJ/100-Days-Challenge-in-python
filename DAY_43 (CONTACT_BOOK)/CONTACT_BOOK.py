class ContactBook:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, name, phone, email):
        self.contacts[name] = {"Phone": phone, "Email": email}
        print(f"Contact {name} added.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted.")
        else:
            print(f"Contact {name} not found.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}")
            print(f"Phone: {self.contacts[name]['Phone']}")
            print(f"Email: {self.contacts[name]['Email']}")
        else:
            print(f"Contact {name} not found.")
def main():
    book = ContactBook()
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            book.add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter name to delete: ")
            book.delete_contact(name)
        elif choice == '3':
            name = input("Enter name to search: ")
            book.search_contact(name)
        elif choice == '4':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
