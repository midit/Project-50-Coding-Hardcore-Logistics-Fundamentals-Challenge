def calculate(num1, num2, operator):
    if operator == "+": return num1 + num2
    if operator == "-": return num1 - num2
    if operator == "*": return num1 * num2
    if operator == "/":
        if num2 == 0: raise ZeroDivisionError
        return num1 / num2
    raise ValueError("Invalid operator")

def safe_calc():
    while True:
        try:
            print("\nTo stop, enter 'Exit'")
            val = input("First number: ")
            if val.lower() == "exit": break

            num1 = int(val)
            num2 = int(input("Second number: "))

            operators = ["+", "-", "/", "*"]
            operator = input("Choose an operation [+-/*]: ")
            if operator not in operators:
                continue
            
            print(f"Result: {calculate(num1, num2, operator)}")

        except ValueError: print("Your calculator can't operate on strings.. that would be strange :/")
        except ZeroDivisionError: print("Bro.. stop it! You can't divide by zero.. :(")

if __name__ == "__main__":
    safe_calc()