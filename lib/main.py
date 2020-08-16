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
        print("5: To exit the program: Type 'exit\n")
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
            print(f"fLast Name:\n {person.first_name}: {person.last_name}")
        elif findField == "3":
            print(f"Phone Number:\n {person.first_name}: {person.number}: ")
        elif findField == "4": 
            print(f"Email Address:\n {person.first_name}: {person.email}")
        else:
            print("Select Again")
            # findField = input("Enter the number of the field you would like to update:\n"
            #               "1. First Name\n"
            #               "2. Last Name\n"
            #               "3. Phone Number\n"
            #               "4. Email Address: ")
        newData = input("Please enter the new text of the field: ")
        
    if menu == 'update':
        updateContact()
        continue  
  
        # print(f'{updateName} : {findField}')
        # last = Contacts.get(Contacts.last_name == (Contacts.last_name == findName))
        # for field in Contacts:
        #     if field == 1:
        #         Contacts.first_name == newData
        #         print(Contacts.first_name)
        #         print()

    #DELETE
    # def deleteContact():
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
    print("exiting")
    on == False
    menu == 'exit'
