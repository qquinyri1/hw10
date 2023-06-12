from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

class Record:
    def __init__(self, name, *fields):
        self.name = name
        self.fields = list(fields)

    def add_field(self, field):
        self.fields.append(field)

    def delete_fields(self, field):
        if field in self.fields:
            self.fields.remove(field)

    def edit_fields(self, old_field, new_field):
        if old_field in self.fields:
            index = self.fields.index(old_field)
            self.fields[index] = new_field

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass


if __name__ == "__main__":
    # main()
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].fields, list)
    assert isinstance(ab['Bill'].fields[0], Phone)
    assert ab['Bill'].fields[0].value == '1234567890'
    print('All Ok)')