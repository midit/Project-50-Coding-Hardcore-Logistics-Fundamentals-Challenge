import json

class Book:
    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available
    
    def to_dict(self):
        return {"title": self.title, "author": self.author, "is_available": self.is_available}

class Library:
    def __init__(self, file_path):
        self.file_path = file_path
        self.books = self.load_data()
        
    def load_data(self):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                return data
            
        except FileNotFoundError:
            return []
        
    def display_books(self):
        print(f"{'№':<3} | {'Назва':<20} | {'Автор':<30} | {'Статус':<5}")
        print("--------------------------------------------------------------------------")
        for index, book in enumerate(self.books):
            status = "Вільна" if book['is_available'] else "Зайнята"
            print(f"{index:<3} | {book['title']:<20} | {book['author']:<30} | {status:<8}")
    
    def add_book(self, title, author):
        book = Book(title=title, author=author)
        
        self.books.append(book.to_dict())
        self.save_data()
    
    def toggle_status(self, index):
        if 0 <= index < len(self.books):
            are_you_sure = input(f"Ви впевнені що хочете змінити статус книги {self.books[index]['title']} на {"Вільна" if not self.books[index]['is_available'] else "Зайнята"}? [ТАК/НІ]: ")
            if are_you_sure.lower() == "так":
                self.books[index]['is_available'] = not self.books[index]['is_available']
                self.save_data()
            elif are_you_sure.lower() == "ні":
                print("Ну то нащо ти голову морочиш?\n")     
        else:
            print("Немає книги з таким ID!") 
    
    def delete_book(self, index):
        if 0 <= index < len(self.books):
            are_you_sure = input(f"Ви впевнені що хочете видалити книгу {self.books[index]['title']} від автора {self.books[index]['author']}? [ТАК/НІ]: ")
            if are_you_sure.lower() == "так":
                self.books.pop(index)
                self.save_data()
            elif are_you_sure.lower() == "ні":
                print("Ну то нащо ти голову морочиш?\n")
        else:
            print("Немає книги з таким ID!") 
    
    def save_data(self):
        with open(self.file_path, "w") as f:
            json.dump(self.books, f, indent=4, ensure_ascii=False)

def library():
    file_location = "Phase_2_Files_Data/other/Day_22/library.json"

    my_library = Library(file_path=file_location)

    while True:
            print("""
Вибери опцію:
1. Список книг
2. Додати книгу
3. Змінити статус
4. Видалити книгу
Щоб закінчити, напиши - 'exit'
                  """)
            
            option = input(">/ ").strip().lower()

            if option == "exit":
                print("Завершення роботи.. ;)")
                break
            
            if option == "1":
                my_library.display_books()
            elif option == "2":
                my_library.add_book(input("Назва книги: "), input("Автор: "))
            elif option == "3":
                try:
                    book_to_toggle = int(input("Напиши ID книги якій хочеш змінити статус: "))
                except:
                    print("ID має бути числом!")
                    continue
                my_library.toggle_status(book_to_toggle)
            elif option == "4":
                try:
                    book_to_delete = int(input("Напиши ID книги яку хочеш видалити: "))
                except:
                    print("ID має бути числом!")
                    continue
                my_library.delete_book(book_to_delete)
            else:
                print("[!] Невідома команда, спробуйте ще раз.")

if __name__ == "__main__":
    library()