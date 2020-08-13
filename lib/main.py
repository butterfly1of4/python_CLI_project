from seed import Contacts


print("My Contacts:")
menu = input("Please choose from the following menu options: ")

#List All Contacts
if menu == "all":
    all_contacts = Contacts.select(aimee, judy)
    print(all_contacts)
elif menu == "Aimee":
    contact_aimee = Contacts.get(aimee)