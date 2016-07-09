
from __future__ import print_function
import sys

try:
    from contacts import *
except ImportError as e:
    # ImportError when ran as a script. Hence append the path for correct imports
    from os.path import dirname, join
    PROJECT_PATH = dirname(dirname(__file__))
    sys.path.append(join(PROJECT_PATH, "contacts"))
    from contacts import *

def main():
    contacts = []
    prompt_name = "Enter name: "
    while True:
        choice = get_input("1) Add contact 2) Search 3) Exit\n").strip()
        if choice == "1":
            valid = False
            while not valid:
                name = get_input(prompt_name)
                if is_valid_name(name):
                    contacts = store_contact(name, contacts)
                    valid = True
                else:
                    print("Invalid name")
        elif choice == "2":
            name = get_input(prompt_name)
            result = search_contact(name, contacts)
            print(format_result(result))
        elif choice == "3":
            print(get_exit_message())
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
