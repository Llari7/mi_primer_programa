from contacts_package import contacts_ui
from contacts_package import contacts

GUI_DIARY = 1
LINE_COMMANDS_DIARY = 2
ACTON_EXIT = 3
MAIN_MENU_OPTIONS = [GUI_DIARY, LINE_COMMANDS_DIARY, ACTON_EXIT]


def ask_until_option_expected(options):
    selected_action = ""
    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Qué opción deseas? ")
    return int(selected_action)


def main():
    print("Bienvenido a su agenda personal:")
    print("1- Agenda con interfaz gráfica.")
    print("2- Agenda por línea de comandos")
    print("3- Salir")

    option = ask_until_option_expected(MAIN_MENU_OPTIONS)
    if option == GUI_DIARY:
        contacts_ui.contacts_ui_main()
    elif option == LINE_COMMANDS_DIARY:
        contacts.line_commands_main()


if __name__ == "__main__":
    main()
