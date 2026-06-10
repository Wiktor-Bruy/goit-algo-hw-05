from functools import wraps

comands = ['"hello" - to start',
          '"exit" or "close" - to close programm',
          '"help" - return valid comands',
          '"add [name] [phone]" - to add contacts',
          '"change [name] [phone]" - to change contact',
          '"phone [name]" - to get phone',
          '"all" - to get all contacts']

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid command. Use the 'help' command to get valid commands."
        except IndexError:
            return "Invalid command. Use the 'help' command to get valid commands."
        except KeyError:
            return "Contact not found"
        except:
            return "Invalid command. Use the 'help' command to get valid commands."

    return inner

def parse_comand(user_input: str):
    if not user_input:
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.lower()
    return cmd, args


@input_error
def add_contact(args: list, contacts: dict):
    name, phone = args
    contacts[name] = phone
    return "Caontact added."

@input_error
def change_contact(args: list, contacts: dict):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed"
    return "Contact not found"
    
@input_error
def get_phone(args: list, contacts: dict):
    name = args[0]
    return f"Name: {name}; Phone: {contacts[name]}"

def get_all(contacts: list):
    if len(contacts) > 0:
        return contacts
    else:
        return "Your contacts is empty..."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_inp = input("Enter a command: ").strip()
        comand, list_arg = parse_comand(user_inp)

        if comand in ["exit", "close"]:
            print("Good bye!")
            break
        elif comand == "hello":
            print("How can I help you?")
        elif comand == "help":
            for comand in comands:
                print(comand)
        elif comand == "all":
            print(get_all(contacts))
        elif comand == "add":
            print(add_contact(list_arg, contacts))
        elif comand == "phone":
            print(get_phone(list_arg, contacts))
        elif comand == "change":
            print(change_contact(list_arg, contacts))
        else:
            print("Invalid command. Use the 'help' command to get valid commands.")

if __name__ == "__main__":
    main()