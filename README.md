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
