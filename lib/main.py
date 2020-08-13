from seed import *
from seed import Contacts

print("My Contacts:")
print("Please choose from the following menu options: \n")
menu = input("For a list of All Contacts: Type 'all'; \nTo find One contact by first-name: Type the first name of the person you're looking for;\n For all first names, Type: 'first names'\n")

#List All Contacts

if menu == "Contacts.name.first_name":
    
    print(Contacts.name.first_name, "main")
    
#Create
def createContact():
    first = input("First Name: ")
    last = input("Last Name: ")
    number = input("Phone Number: ")
    email = input("Email: ")
    # return(first, last, number, email)
    c = Contacts(first_name = first, last_name =last, number = number, email=email)
    c.save()

if menu == 'create contact':
    createContact()
    print(createContact,)
#create variable so while true, program is active