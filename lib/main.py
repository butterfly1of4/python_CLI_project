from peewee import *
from models import Contacts


print("My Contacts:")

on = True
while on == True:

    def intro():
        print("\nPlease choose from the following menu options: \n")
        print("1: For a list of All Contacts: Type 'all'; \n")
        print("2: To find One contact by first-name: Type the first name of the person you're looking for;\n ")
        print("3: To create a New contact: Type 'new'\n")
        print("4: To update a contact: Type 'update'\n")
        print("5: To delete a contact: Type 'delete'\n")
        print("6: To exit the program: Type 'exit\n")
    intro()
    menu = input("Type your choice: ")
# EXIT CHECK

    def checkExit():
        if menu == 'exit':
            on == False
            print("Goodbye")
        else:
            print('go on')
        checkExit()
# FIND ALL

    def findAll():
        all = Contacts.select()
        for entry in all:
            print(entry.first_name, entry.last_name, entry.number, entry.email)
    if menu == 'all':
        findAll()

        continue

# CREATE
    def createContact():

        first = input("First Name: ")
        last = input("Last Name: ")
        number = input("Phone Number: ")
        email = input("Email: ")
        Contacts.create(first_name=first, last_name=last,
                        number=number, email=email)
    if (menu == 'new'):
        createContact()

        continue


#UPDATE

    def updateContact():
        updateName = input("Type the first name of the contact you would like to update: ")
        person = Contacts.get(Contacts.first_name == updateName)
        findField = input("Enter the number of the field you would like to update:\n"
                          "1. First Name\n"
                          "2. Last Name\n"
                          "3. Phone Number\n"
                          "4. Email Address: ")
        if findField == "1":
                print(f"First Name:\n {person.first_name}") 
        elif findField == "2":
            print(f"Last Name:\n {person.first_name}: {person.last_name}")
        elif findField == "3":
            print(f"Phone Number:\n {person.first_name}: {person.number}: ")
        elif findField == "4": 
            print(f"Email Address:\n {person.first_name}: {person.email}")
        else:
            print("Select Again")
        newData = input("Please enter the new text of the field: ")
        print(newData)
        
        last = Contacts.get(Contacts.last_name == person.last_name)
        num = Contacts.get(Contacts.number == person.number)
        mail = Contacts.get(Contacts.email == person.email) 
        
        if findField == "1":
            person = Contacts.get(Contacts.first_name == updateName)
            person.first_name = newData
            person.save()
        
        elif findField == "2":
            last = Contacts.get(Contacts.last_name == person.last_name)
            last.last_name = newData
            last.save()
            # print(person.last_name, last.last_name, "three")
        elif findField == "3":
            num = Contacts.get(Contacts.number == person.number)
            num.number = newData
            num.save()
        elif findField == "4":
            mail = Contacts.get(Contacts.email == person.email) 
            mail.email = newData
            mail.save()
        print(person.first_name, last.last_name, num.number, mail.email)
        
    if menu == 'update':
        updateContact()
        continue  
        

#DELETE
    def deleteContact():
        deleteName = input("Type the name of the contact you wish to delete: ")
        deleteContact = Contacts.get(Contacts.first_name == deleteName)
        print(deleteContact.first_name, deleteContact.last_name, deleteContact.number, deleteContact.email)
        deleteContact.delete_instance()
        print("deleted")
        all = Contacts.select()
        for entry in all:
            print(entry.first_name, entry.last_name, entry.number, entry.email)
    if menu == 'delete':
        deleteContact()
        continue       
 
    
 # FIND ONE BY FIRST NAME
    def findName():
        person = Contacts.get(Contacts.first_name == menu)
        print(person.first_name, person.last_name, person.number, person.email)
    if menu == Contacts.first_name and menu != 'exit':
        findName()
        
        continue
    elif menu == 'exit':
        break
       
# EXIT
else:
    on == False
    menu == 'exit'
