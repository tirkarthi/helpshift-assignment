
from __future__ import print_function
import re

def store_contact(name, names):
    '''
    @param name   - Name to be stored
    @param names  - List of names already present
    @return names - List with the new name
    '''
    names.append(name)
    return names

def search_contact(contact, contacts):
    '''
    @param contact  - Contact to search
    @param contacts - List of contacts to be searched
    @return results - Sorted list of Contacts with the following assumptions

    Assumptions : 
    1. Matching is case sensitive
    2. If there is more than one exact match then they are sorted by the index of the first character
    3. If there are partial matches they are displayed after exact matches and they are also sorted by the index of the first character
    

    '''
    bounded_regex = re.compile(r"\b{}\b".format(contact))
    unbounded_regex = re.compile(r"{}".format(contact))
    names = filter(lambda y: y[1] is not None, map(lambda x: (x, unbounded_regex.search(x)), contacts))

    def sort_by_exact_index(name, match):
        bounded_match = bounded_regex.search(name)
        if bounded_match:
            return 0, bounded_match.start()
        else:
            return 1, match.start()

    return list(map(lambda x: x[0], sorted(names, key = lambda x: sort_by_exact_index(x[0], x[1]))))

def is_valid_name(name):
    '''
    @param name  - Input name from the user
    @return bool - Return if the name matches the following rules

    Rules : 

    1. Maximum length of the names is 50
    2. Starts with one or more letters(startname) followed by an optional series of one or more characters(lastname) separated by a single space
    '''
    return bool(len(name) <= 50 and re.match("^[A-Za-z]+(\s?[A-Za-z]+)?$", name))

def format_result(result):
    '''
    @param result            - A list of matched names
    @return formatted_result - A string with names joined by \n if present or else an error message
    '''
    if result:
        formatted_result = "\n".join(result)
    else:
        formatted_result = "No match found"
    return formatted_result

def get_exit_message():
    '''
    return the exit message
    '''
    return "Happy searching"

def get_input(prompt):
    '''
    @param prompt - Prompt string for the user inpu
    @param data   - User input
    Loop through with the prompt message until there is an input 
    '''
    data = ''
    while not data:
        data = input(prompt)
    return data
