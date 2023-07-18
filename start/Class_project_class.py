class Contact:
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
        self.__email = email

    def get_name(self, name):
        return self.__name

    def get_phone(self, phone):
        return self.__phone

    def get_email(self, email):
        return self.__email

    def __str__(self):
        return f'''Name: {self.__name}
Phone: {self.__phone}
Email: {self.__email}'''

# db = {'tony': contact.Contact("tony", "0208457762", "blair@gmail.con"), 'blair': contact.Contact("blair",
# "0591646302", "nation@gmail.com")
