from seed import *
from seed import Contacts


on = False
def restart():
    if on == True:
        welcome()
        menu = input("")
    elif on==False:
        print('stop')
    
    
print("My Contacts:")
def welcome():
    print("Please choose from the following menu options: \n")
    print("For a list of All Contacts: Type 'all'; \n")
    print("To find One contact by first-name: Type the first name of the person you're looking for;\n ")
    print("To create a New contact: Type 'new'\n")
welcome()

menu = input("Type your choice: ")
# print(menu)


    
def findAll():
    on == True 
    all = Contacts.select()
    for entry in all:
        print(entry.first_name, entry.last_name,entry.number,entry.email)
    # findAll()
    on==False
    # restart()
    # print(find_all)

#FIND ONE     
def findName():
    on ==True
    person = Contacts.get(Contacts.first_name == menu)
    print(person.first_name, person.last_name, person.number, person.email)
    # person = Contacts.select().where(Contacts.first_name == menu)
    # print(name.first_name for name in person)
    # findName()
        
    on == False
#     # restart()
#     # welcome()
    
#CREATE 
def createContact():
    on == True
    first = input("First Name: ")
    last = input("Last Name: ")
    number = input("Phone Number: ")
    email = input("Email: ")
    c = Contacts(first_name = first, last_name =last, number = number, email=email)
    c.save()
    # createContact()
    on == False
    # print(createContact)

if menu == 'all': #and on == True:       
    findAll()
    restart()
elif menu == Contacts.first_name:
    findName()
    restart()  
elif menu == 'create contact' or menu == 'create' or menu == 'new':
    createContact()
    restart()

    # welcome()
    # on == False 
