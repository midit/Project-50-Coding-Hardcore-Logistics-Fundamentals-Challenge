from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, wage):
        self.name = name
        if not isinstance(wage, (int, float)):
            raise ValueError(f"[!] Помилка: Зарплата {name} має бути числом")
        if wage < 0:
            raise ValueError(f"[!] Помилка: Зарплата {name} не може бути від'ємною")
        self._wage = wage

    @abstractmethod
    def calculate_salary(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__:<10} | {self.name:<10}"

class Manager(Employee):
    def __init__(self, name, wage, bonus):
        super().__init__(name, wage)
        if not isinstance(bonus, (int, float)):
            raise ValueError(f"[!] Помилка: Бонус для {name} має бути числом")
        self._bonus = bonus

    def calculate_salary(self):
        return self._wage + self._bonus

class Developer(Employee):
    def __init__(self, name, wage, multiplier):
        super().__init__(name, wage)
        if not isinstance(multiplier, (int, float)):
            raise ValueError(f"[!] Помилка: Множник для {name} має бути числом")
        self._multiplier = multiplier
    
    def calculate_salary(self):
        return self._wage * self._multiplier

def inheritance():
    raw_data = [
        ("Manager", "Олег", 3000, 500),
        ("Developer", "Віталій", "error_string", 1.5),
        ("Developer", "Андрій", 2000, "error_string")
    ]

    staff = []
    print("--- Процес створення штату ---")
    for role, name, wage, extra in raw_data:
        try:
            if role == "Manager":
                staff.append(Manager(name, wage, extra))
            else:
                staff.append(Developer(name, wage, extra))
        except ValueError as e:
            print(e)

    print("\n--- Фінальна відомість ---")
    for person in staff:
        print(f"{person} | До виплати: {person.calculate_salary():.2f}$")

if __name__ == "__main__":
    inheritance()