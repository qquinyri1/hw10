import json 
from collections import UserDict

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.load_data()
    
    def load_data(self):
        try:
            with open('address_book.json','r') as fh:
                self.data = json.load(fh)
        except FileNotFoundError:
            self.data = {}
    
    def save_data(self):
        with open('address_book.json', 'w') as fh:
            json.dump(self.data, fh, indent=4)
    
    def add_record(self,record):
        self.data[record.name.value] = record.data
        self.save_data()

class Field:
    def __init__(self, value) -> None:
        self.value = value
    
class Name(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

class Record:
    def __init__(self, name) -> None:
        self.name = Name(name)
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def remove_phone(self,phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    @property
    def data(self):
        return {
            'name': self.name.value,
            'phones': [phone.value for phone in self.phones]
        }
