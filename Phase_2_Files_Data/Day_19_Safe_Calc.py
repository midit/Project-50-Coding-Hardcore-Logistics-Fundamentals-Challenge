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
            
            if operator == "+":
                print(f"Result: {num1+num2}")
            elif operator == "-":
                print(f"Result: {num1-num2}")
            elif operator == "/":
                print(f"Result: {num1/num2}")
            elif operator == "*":
                print(f"Result: {num1*num2}")

        except ValueError: print("Your calculator can't operate on strings.. that would be strange :/")
        except ZeroDivisionError: print("Bro.. stop it! You can't divide by zero.. :(")

if __name__ == "__main__":
    safe_calc()


    