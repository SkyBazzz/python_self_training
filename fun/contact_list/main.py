import json

from fun.contact_list.models import Contact, UnknownContact


def add_contact_info():
    contact = form_contact_to_add()

    contact_to_add = {contact.full_name(): json.dumps(contact)}
    update_contacts_list(contact_to_add)


def form_contact_to_add():
    name = input("Input name: ").strip().title()
    surname = input("Input surname: ").strip().title()
    phone_number = input("Input phone number: ")
    contact = Contact(name, surname, phone_number)
    return contact


def update_contacts_list(data):
    try:
        with open("contact_list.json", mode="r", encoding="UTF-8") as contacts:
            contacts_info: dict = json.load(contacts)
    except FileNotFoundError:
        with open("contact_list.json", mode="w", encoding="UTF-8") as contacts:
            json.dump(data, contacts, indent=2)
    else:
        with open("contact_list.json", mode="w", encoding="UTF-8") as contacts:
            contacts_info.update(data)
            json.dump(contacts_info, contacts, indent=2)


def show_contact_info(full_name: str):
    try:
        with open("contact_list.json", mode="r", encoding="UTF-8") as contacts:
            contacts_info: dict = json.load(contacts)
    except FileNotFoundError:
        print("Contact list doesn't exist, add contact first")
    else:
        return f"{Contact(**contacts_info.get(full_name, UnknownContact().__dict__))!s}"


print(show_contact_info("Oleksandr Balkashyn"))
