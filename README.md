# python_CLI_project
# Contact book

main.py : 


# Contact Book
-Users should be able to create new contacts. 
-They should be able to see a list of contacts in their contact book. 
-They should be able to find a contact by the contact's first name.

https://github.com/Daniel-Edminster/python-contacts/blob/master/lib/contact.class.py


#FIND ALL 
def find_all():
    all = Contacts.select()
    for i in all:
        print(i.first_name, i.last_name,i.number,i.email)
    # on == True
        
if menu == 'all':       
    find_all()
    # on==False
    # restart()
    # print(find_all)

#FIND ONE     
# def find_name():
#     # on ==True
#     person = Contacts.get(Contacts.first_name == menu)
#     print(person.first_name, person.last_name, person.number, person.email)
#     # person = Contacts.select().where(Contacts.first_name == menu)
#     # print(name.first_name for name in person)
        
# if menu == Contacts.first_name:
#     find_name()
#     # on == False
#     # restart()
#     # welcome()
    
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
    # restart()
    # welcome()
    # on == False 




latest
   
print("My Contacts:")

#
on = False



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
if menu == 'all': #and on == True:       
    findAll()
    on==False
    # restart()
    welcome()
    
#CREATE 
def createContact():
    on == True
    first = input("First Name: ")
    last = input("Last Name: ")
    number = input("Phone Number: ")
    email = input("Email: ")
    c = Contacts.create(first_name = first, last_name =last, number = number, email=email)
    c.save()
    # createContact()
    on == False
if (menu == 'new'):
    createContact()
    # restart()
    welcome()



#FIND ONE     
def findName():
    on ==True
    person = Contacts.get(Contacts.first_name == menu)
    print(person.first_name, person.last_name, person.number, person.email)
    # findName()
if menu == Contacts.first_name:
    findName()
    on == False
    # restart()  
    welcome()

# def restart():
#     while on == False:
#         menu == menu
#     if  on==True:
#         print('stop')
# restart()  
   

    
# if menu == 'exit':
    # on == True;

