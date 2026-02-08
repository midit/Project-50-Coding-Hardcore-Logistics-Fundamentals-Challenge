import os

def show_todo(file_path):
    if not os.path.exists(file_path):
        return "[!] Ваш список справ поки що порожній. Час щось додати!"
    
    with open(file_path, "r") as f:
        lines = f.readlines()

    if not lines:
        return "[!] Ваш список справ порожній."
    
    output = "\n--- Ваш список справ ---\n"

    for index, line in enumerate(lines, start=1):
        output += f"{index}. {line.strip()}\n"

    return output

def add_task(file_path, task):
    with open(file_path, "a") as f:
        f.write(f"{task} / Статус: Не виконано\n")

    return "[+] Нове завдання додано успішно!"

def mark_task(file_path, task_id):
    try:
        idx = int(task_id) - 1
        with open(file_path, "r") as f:
            lines = f.readlines()
        
        if 0 <= idx < len(lines):
            lines[idx] = lines[idx].replace("Статус: Не виконано", "Статус: Виконано")
            with open(file_path, "w") as f:
                f.writelines(lines)
            return "[+] Статус оновлено!"
        else:
            return "[!] Завдання з таким номером не існує."
    except ValueError:
        return "[!] Будь ласка, введіть число (номер завдання)."

def remove_task(file_path, task_id):
    try:
        idx = int(task_id) - 1
        with open(file_path, "r") as f:
            lines = f.readlines()
        
        if 0 <= idx < len(lines):
            lines.pop(idx)
            with open(file_path, "w") as f:
                f.writelines(lines)
            return "[+] Завдання видалено!"
        else:
            return "[!] Завдання з таким номером не існує."
    except ValueError:
        return "[!] Будь ласка, введіть число."

def todo_list():
    os.makedirs("Phase_2_Files_Data/other", exist_ok=True)
    file_location = "Phase_2_Files_Data/other/todo.txt"

    while True:
            print("""
Вибери опцію:
1. Показати список завдань
2. Додати завдання
3. Позначити завдання як виконане 
4. Видалити завдання
Щоб закінчити, напиши - 'exit'
                  """)
            
            option = input(">/ ").strip().lower()

            if option == "exit":
                print("Завершення роботи.. ;)")
                break
            
            if option == "1":
                print(show_todo(file_location))
            elif option == "2":
                task = input("[+] Що саме потрібно зробити?\n>/ ")
                if task:
                    print(add_task(file_location, task))
            elif option == "3":
                t_id = input("[?] Номер завдання для позначення виконаним:\n>/ ")
                print(mark_task(file_location, t_id))
            elif option == "4":
                t_id = input("[?] Номер завдання для видалення:\n>/ ")
                print(remove_task(file_location, t_id))
            else:
                print("[!] Невідома команда, спробуйте ще раз.")


if __name__ == "__main__":
    todo_list()