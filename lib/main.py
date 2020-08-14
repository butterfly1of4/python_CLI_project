from seed import *
from seed import Contacts


on = False
def restart():
    if on == False:
        welcome()
    elif on==True:
        print('going')
    
    
def welcome():
    print("My Contacts:")
    print("Please choose from the following menu options: \n")
    print("For a list of All Contacts: Type 'all'; \n")
    print("To find One contact by first-name: Type the first name of the person you're looking for;\n ")
    print("To create a New contact: Type 'new'\n")
welcome()

menu = input("Type your choice: ")
# print(menu)

#FIND ALL 
def find_all():
    all = Contacts.select()
    for i in all:
        print(i.first_name, i.last_name,i.number,i.email)
        
if menu == 'all':       
    find_all()
    # print(find_all)

#FIND ONE    

 
def find_name():
    person = Contacts.get(Contacts.first_name == menu)
    print(person.first_name, person.last_name, person.number, person.email, "first name")
    # person = Contacts.select().where(Contacts.first_name == menu)
    # print(name.first_name for name in person)
        
if menu == Contacts.first_name:
    find_name()
    # print(find_name)
    print("print person")
    
#CREATE 
def createContact():
    # on == True
    first = input("First Name: ")
    last = input("Last Name: ")
    number = input("Phone Number: ")
    email = input("Email: ")
    c = Contacts(first_name = first, last_name =last, number = number, email=email)
    c.save()


if menu == 'create contact' or menu == 'new':
    createContact()
    print(createContact)
    # print(db)
    # welcome()
    # on == False 
#create variable so while true, program is active
