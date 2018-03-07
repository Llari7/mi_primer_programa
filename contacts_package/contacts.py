import pickle

from time import sleep
from contacts_package.contact import Contact
from contacts_package.main import ask_until_option_expected

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

SAVE_FILE_NAME = "contactsDB.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]


def show_menu():
    print("Acciones disponinbles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar un contacto")
    print("4 - Exportar contactos a un CSV")
    print("5 - Salir")
    return ask_until_option_expected(MENU_OPTIONS)


def add_contact(contacts):
    print("\n\nAñadir contacto\n")
    name = input("Nombre: ")
    email = input("Email: ")
    phone = input("Teléfono: ")
    contact = Contact(name, email, phone)
    contacts.append(contact)
    print("Se ha añadido el contacto {} correctamente\n".format(contact.name))
    sleep(2)


def remove_contact(contacts):
    print("Se procederá al borrado de un usuario de la agenda.")
    searched_contact = searching_contact(contacts)
    counter = 0
    contact_index = 0
    for contact in contacts:
        if searched_contact == contact:
            contact_index = counter
        else:
            counter += 1
    print("El usuario {} ha sido eliminado de la agenda.".format(contacts[contact_index].name))
    del contacts[contact_index]
    sleep(2)


def find_contact(contacts):
    contact = searching_contact(contacts)
    if contact is not None:
        contact.print_contact()
    sleep(2)


def searching_contact(contacts):
    while True:
        print("\n\nBuscar contacto\n")
        search_term = input("Introducir el nombre del contacto/email o parte de él: ")
        found_contacts = []

        print("He encontrado los siguientes contactos:")
        contact_indexes = []
        contact_counter = 0

        for contact in contacts:
            if (contact.name.find(search_term) >= 0) or (contact.email.find(search_term) >= 0):
                found_contacts.append(contact)
                print("{} - {}".format(contact_counter, contact.name))
                contact_indexes.append(contact_counter)
                contact_counter += 1

        if len(contact_indexes) > 1:
            contact_index = ask_until_option_expected(contact_indexes)
            return found_contacts[contact_index]
        elif len(contact_indexes) == 0:
            print("No se ha encontrado ninguno.")
            if input("¿Desea seguir buscando? (S/N) ").upper() == "N":
                return None
        else:
            contact_index = 0
            return found_contacts[contact_index]


def export_contacts():
    pass


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []
    except EOFError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
        print("Datos guardados correctamente.")


def line_commands_main():
    contacts = load_contacts()
    action = show_menu()

    while action != ACTION_EXIT:
        if action == ACTION_ADD_CONTACT:
            add_contact(contacts)
        elif action == ACTION_REMOVE_CONTACT:
            remove_contact(contacts)
        elif action == ACTION_FIND_CONTACT:
            find_contact(contacts)
        elif action == ACTION_EXPORT_CONTACT:
            export_contacts()

        action = show_menu()

    save_contacts(contacts)
    print("¡Adiós!")
