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
    def is_correct_number(self):
        '''Валідація номера телефону, перевірка на 10 цифр'''
        return len(self.value) == 10 and self.value.isdigit()


class Record:
    '''Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.'''
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone_number):
        '''Метод додавання номеру телефону'''
        phone = Phone(phone_number)
        if phone.is_correct_number() and self.find_phone(phone_number) is None:
            self.phones.append(phone)


    def remove_phone(self, phone_number):
        '''Метод видалення номеру телефону'''
        self.phones = list(filter(lambda p: p.value != phone_number, self.phones))


    def edit_phone(self, old_number, new_number):
        '''Метод редагування номеру телефону'''
        new_phone = Phone(new_number)
        if new_phone.is_correct_number():
            old_phone = self.find_phone(old_number)
            if not old_phone is None:
                old_phone.value = new_number
            else:
                raise ValueError(f"Phone number {old_number} not found!")
        else:
            raise ValueError("The new phone number must contain 10 digits.")


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
