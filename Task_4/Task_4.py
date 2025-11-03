#function for parsing an user input
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#function to add a contact to a contact list
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

#function to change an existing contact phone
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name]=phone
        return "Contact updated"
    else:
        return "No contact with this name"

#function to show phone of a contact if exists
def show_phone(name, contacts):
    if name in contacts:
        return contacts[name]
    else:
        return "No contact with this name found"

#function to show all contacts
def show_all(contacts):
    return contacts

#main function of a bot
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command=="change":
            print(change_contact(args, contacts))
        elif command=="phone":
            print(show_phone(args[0], contacts))
        elif command=="all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
