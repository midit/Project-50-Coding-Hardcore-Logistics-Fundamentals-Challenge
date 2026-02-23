import json
import os
import datetime

class TodoManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def save(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, indent=4, ensure_ascii=False)

    def show_tasks(self):
        if not self.tasks:
            return "[!] Список порожній."
        output = "\n--- Список справ ---\n"
        for i, t in enumerate(self.tasks, 1):
            status = "✅" if t['status'] == "Виконано" else "❌"
            output += f"{i}. {t['task']} [{status}] ({t['createdAt']})\n"
        return output

    def add(self, task_text):
        new_task = {
            "id": len(self.tasks) + 1,
            "task": task_text,
            "status": "Не виконано",
            "createdAt": datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        }
        self.tasks.append(new_task)
        self.save()
        return "[+] Додано!"

    def mark_done(self, idx):
        if 0 < idx <= len(self.tasks):
            self.tasks[idx-1]['status'] = "Виконано"
            self.save()
            return "[+] Оновлено!"
        return "[!] Невірний номер."

    def remove(self, idx):
        if 0 < idx <= len(self.tasks):
            self.tasks.pop(idx-1)
            self.save()
            return "[+] Видалено!"
        return "[!] Невірний номер."

def main():
    manager = TodoManager("Phase_3_OOP/other/Day_29/todo.json")
    
    while True:
        print("\n1. Список | 2. Додати | 3. Виконано | 4. Видалити | exit")
        choice = input(">/ ").strip().lower()

        if choice == "exit": break
        if choice == "1": print(manager.show_tasks())
        elif choice == "2":
            text = input("Що зробити?: ")
            print(manager.add(text))
        elif choice == "3":
            num = int(input("Номер: "))
            print(manager.mark_done(num))
        elif choice == "4":
            num = int(input("Номер: "))
            print(manager.remove(num))

if __name__ == "__main__":
    main()