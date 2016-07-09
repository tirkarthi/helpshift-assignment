## Contacts [![Build Status](https://travis-ci.org/tirkarthi/helpshift-assignment.svg?branch=master)](https://travis-ci.org/tirkarthi/helpshift-assignment)

A simple command line application to store and search contacts in-memory. The contacts are not persisted and are only available for the session.

### Usage without installation : 

1. Clone the repository with `git clone https://github.com/tirkarthi/helpshift-assignment.git`
2. Go to the folder helpshift-assignment. 
3. Run the program with `python scripts/contacts`
4. Use one of the following options:
    1. Add contact - Add a contact name
    2. Search      - Search for a contact by name
    3. Exit        - Exit the program

### System wide installation :

1. Install virtualenv from https://virtualenv.pypa.io/en/stable/installation/
2. Initialize a virtualenv with `virtualenv helpshift-env`
3. Activate the virtualenv with `source helpshift-env/bin/activate`
4. Go to the cloned repository in the same terminal and run `python setup.py install`
5. The script is accessible system wide with the name `contact-search`
6. Run `contact-search` from the terminal to use the program with above mentioned options
