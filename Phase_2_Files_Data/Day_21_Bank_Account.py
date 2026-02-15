class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Депозит: +{amount}$. Поточний баланс: {self._balance}$")
        else:
            print("Нуль баксів було додано на ваш рахунок, звертайтесь! :)")

    def withdraw(self, amount):
        if amount > self._balance:
            print(f"Недостатньо коштів! Баланс: {self._balance}$, це менше ніж: {amount}$")
        elif amount <= 0:
            print("Маєш нуль баксів, дивись не витрать усі :O")
        else:
            self._balance -= amount
            print(f"Зняття: -{amount}$. Залишок: {self._balance}$")

    def get_balance(self):
        return f"Рахунок {self.owner}: {self._balance}$"

if __name__ == "__main__":
    my_acc = BankAccount("Max", 100)
    
    print(my_acc.get_balance())
    my_acc.deposit(50)
    my_acc.withdraw(200)
    my_acc.withdraw(70)
    print(my_acc.get_balance())