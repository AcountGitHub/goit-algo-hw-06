'''Реалізація класів для управління адресною книгою'''

from collections import UserDict

class Field:
    '''Базовий клас для полів запису.'''
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)


class Name(Field):
    '''Клас для зберігання імені контакту.'''
    pass


class Phone(Field):
    '''Клас для зберігання номера телефону.'''
    def __init__(self, phone_number):
        # Валідація номера телефону, перевірка на 10 цифр
        if len(phone_number) == 10 and phone_number.isdigit():
            super().__init__(phone_number)
        else:
            raise ValueError("The phone number must contain only 10 digits.")


class Record:
    '''Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.'''
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone_number):
        '''Метод додавання номеру телефону'''
        if self.find_phone(phone_number) is None:
            self.phones.append(Phone(phone_number))


    def remove_phone(self, phone_number):
        '''Метод видалення номеру телефону'''
        self.phones = list(filter(lambda p: p.value != phone_number, self.phones))


    def edit_phone(self, old_number, new_number):
        '''Метод редагування номеру телефону'''
        old_phone = self.find_phone(old_number)
        if not old_phone is None:
            old_phone.value = Phone(new_number).value
        else:
            raise ValueError(f"Phone number {old_number} not found!")


    def find_phone(self, phone_number):
        '''Метод пошуку номеру телефону'''
        result = list(filter(lambda p: p.value == phone_number, self.phones))
        return result[0] if len(result) > 0 else None


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    '''Клас для зберігання та управління записами.'''
    def add_record(self, record):
        '''Метод додавання запису до адресної книги'''
        if self.find(record.name.value) is None:
            self.data[record.name.value] = record


    def find(self, name):
        '''Метод пошуку запису за ім'ям'''
        return self.data.get(name)


    def delete(self, name):
        '''Метод видалення запису за ім'ям'''
        self.data = {key: self.data[key] for key in self.data if key != name}


    def __str__(self):
        return f"{'\n'.join(self.data[k].__str__() for k in self.data)}"
