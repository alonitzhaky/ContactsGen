"""
Method List:
    Menu
# Load
# Add
# Print
# Delete
# Search
"""
from helper import *
contacts = []
DATA_FILE = "contacts.json"
# Implemented parameters

def main(): 
    userSelection = menuContacts()
    while userSelection != "x":
        if userSelection == "a":
            addContact(contacts)
        if userSelection == "p":
            printContacts(contacts)
        if userSelection == "d":
            deleteContact()
        if userSelection == "s":
            searchContact()
        userSelection = menuContacts()
    # saveInfo("THIS IS A TEST.")


if __name__ == "__main__":
    main()