from seed import *
from seed import Contacts


# on = True
# def restart():
    # if on == False:
    #     welcome()
    # elif on==True:
    #     print('going')
    
    
def welcome():
    print("My Contacts:")
    print("Please choose from the following menu options: \n")
    print("For a list of All Contacts: Type 'all'; \n")
    print("To find One contact by first-name: Type the first name of the person you're looking for;\n ")
    print("To create a New contact: Type 'new'\n")
welcome()

menu = input("Type your choice: ")

def find_all():
    

def find_name():
        get_person = Contacts.get(Contacts.first_name == menu)
        print(get_person)
        
        
if menu == "Contacts.name.first_name":
    find_name()
    print(find_name)

#Create
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
    db="INSERT INTO contacts(first_name,last_name,number,email VALUE first, last, number, email )"
    print(createContact)
    print(db)
    # welcome()
    # on == False 
#create variable so while true, program is active
