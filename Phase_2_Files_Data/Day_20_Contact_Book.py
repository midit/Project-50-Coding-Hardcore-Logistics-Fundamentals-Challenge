import json

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def to_dict(self):
        return {"name": self.name, "phone": self.phone}

class ContactBook:
    def __init__(self, file_path):
        self.file_path = file_path
        self.contacts = self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                return data
            
        except FileNotFoundError:
            return []
        
    def display_contacts(self):
        print(f"{'№':<3} | {'Ім\'я':<20} | {'Телефон':<15}")
        print("--------------------------------------------")
        for index, contact in enumerate(self.contacts):
            print(f"{index:<3} | {contact['name']:<20} | {contact['phone']:<15}")

    def add_contact(self, name, phone):
        contact = Contact(name=name, phone=phone)
        
        self.contacts.append(contact.to_dict())
    
    def search(self, name):
        for contact in self.contacts:
            if name.lower() in contact['name'].lower():
                return [contact['phone'], contact['name']]
            
    def delete(self, name):
        target = self.search(name)
        if target:
            self.contacts = [c for c in self.contacts if c['name'].lower() != name.lower()]
            return target
        return None
        
    def save_data(self):
        with open(self.file_path, "w") as f:
            json.dump(self.contacts, f, indent=4, ensure_ascii=False)

def contact_book():
    file_location = "Phase_2_Files_Data/other/Day_20/contacts.json"

    my_book = ContactBook(file_path=file_location)

    while True:
            print("""
Вибери опцію:
1. Показати список контактів
2. Додати контакт
3. Знайти контакт 
4. Видалити контакт
Щоб закінчити, напиши - 'exit'
                  """)
            
            option = input(">/ ").strip().lower()

            if option == "exit":
                print("Завершення роботи.. ;)")
                break
            
            if option == "1":
                my_book.display_contacts()
            elif option == "2":
                my_book.add_contact(input("Ім'я: "), input("Телефон: "))
                my_book.save_data()
            elif option == "3":
                search_term = input("Кого шукаємо?: ")
                result = my_book.search(search_term)
                if result == None:
                    print(f"Нікого з ім'ям {search_term} не знайдено, точно правильно написано?")
                    continue
                print(f"Знайдено! Ім'я: {result[1]} Телефон: {result[0]}")
            elif option == "4":
                name_to_delete = input("Введіть ПОВНЕ ім'я для видалення: ")
                are_you_sure = input(f"Ви впевнені що хочете видалити користувача на ім'я {name_to_delete}? [ТАК/НІ]: ")
                if are_you_sure.lower() == "так":
                    result = my_book.delete(name_to_delete)
                    print(f"Видалено! Ім'я: {result[1]} Телефон: {result[0]}")
                    my_book.save_data()
                elif are_you_sure.lower() == "ні":
                    print("Ну то нащо ти голову морочиш?\n")
            else:
                print("[!] Невідома команда, спробуйте ще раз.")

if __name__ == "__main__":
    contact_book()