import json
from Contacts import *

def menuContacts():
    print("Welcome to Contacts 1.0.0.")
    print("A - Add a new contact")
    print("D - Delete a contact")
    print("S - Search for a contact")
    print("P - Print all contacts")
    print("X - Exit")
    userSelection = input("Select your option: ")
    return userSelection

def addContact(contacts):
    userName = input("Contact's Name: ")
    userTel = input("Contact's Tel: ")
    contact = contacts.append({"name": userName, "tel": userTel})
    print("Added.")
    writeContact(contact, DATA_FILE)

def writeContact(contact, DATA_FILE):
    with open(DATA_FILE, "r+") as file:
        existingData = json.load(file)
        existingData["contact_details"].append(contact)
        file.seek(0)
        json.dump(existingData, file, indent = 4)

def printContacts(DATA_FILE, contacts):
    with open(DATA_FILE) as file:
        json.load(file)
    print("contact_details")

