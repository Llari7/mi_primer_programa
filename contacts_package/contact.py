class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def print_contact(self):
        print("Nombre: {} ; Email: {} ; Phone: {} ".format(self.name, self.email, self.phone))
