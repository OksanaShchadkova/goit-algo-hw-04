def parse_input(user_input: str):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage: add <username> <phone>"
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added with phone number '{phone}'."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Usage: change <username> <phone>"
    name, phone = args
    if name not in contacts:
        return f"Contact '{name}' not found."
    contacts[name] = phone
    return f"Contact '{name}' updated with new phone number '{phone}'."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Usage: phone <username>"
    name = args[0]
    return contacts.get(name, f"Contact '{name}' not found.")


def show_all(_, contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{n}: {p}" for n, p in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Available commands: hello, add <username> <phone>, change <username> <phone>, phone <username>, all, exit, close")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("exit", "close"):
            print("Good bye!")
            break
        if command == "hello":
            print("How can I help you?")
            continue

        handler = {
            "add": add_contact,
            "change": change_contact,
            "phone": show_phone,
            "all": show_all,
        }.get(command, lambda args, contacts: "Invalid command. Please try again.")

        print(handler(args, contacts))


if __name__ == "__main__":
    main()
