from seed import *
from seed import Contacts

def welcome():
    print("My Contacts:")
    print("Please choose from the following menu options: \n")
    print("For a list of All Contacts: Type 'all'; \n")
    print("To find One contact by first-name: Type the first name of the person you're looking for;\n ")
    print("To create a New contact: Type 'new'\n")
welcome()

menu = input("Type your choice: ")


if menu == "Contacts.name.first_name":
    
    print(Contacts.name.first_name, "main")
    
#Create
def createContact():
    on = True
    first = input("First Name: ")
    last = input("Last Name: ")
    number = input("Phone Number: ")
    email = input("Email: ")
    c = Contacts(first_name = first, last_name =last, number = number, email=email)
    c.save()


if menu == 'create contact':
    createContact()
    print(createContact,)
#create variable so while true, program is active
on = False 
def restart():
    if on == False:
        welcome()
    else:
        print('going')