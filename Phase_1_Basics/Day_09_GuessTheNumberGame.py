import random

def guess_the_number():

    attempts = 0
    number = random.randint(1,100)

    while True:
        try: 
            attempts += 1
            guess = int(input("Take a guess: "))
            if guess > number:
                print("Lower..\n")
            elif guess < number:
                print("Higher..\n")
            else:
                print(f"YOU WON! NUMBER IS {number}. Attempts: {attempts}")
                return
        except:
            print("[!] Enter a number.")
            continue
        
if __name__ == "__main__":
    guess_the_number()