def temperature_convertor():
    a=input("Enter your value in C: ")
            
    try:
        a = float(a)
        return(f"F: {(a*(9/5)+32):.2f}")
    except:
        return("Your input shoud be a Float number")

if __name__ == "__main__":
    print(temperature_convertor())
