import random

def rock_paper_scissors():

    score = 0

    win_logic = {
        1: 3,
        2: 1,
        3: 2
    }

    choices = {
        1: "Rock",
        2: "Paper",
        3: "Scissors",
        4: "Exit",
    }

    while True:
        bot_choice = random.randint(1,3)
        try:
            user_choice = int(input("Choose [Rock (1), Paper (2) or Scissors (3). Or Exit (4)]"))
            
            if user_choice == 4:
                print(f"Your score: {score}. Goodbye!")
                return
            elif user_choice not in choices:
                print("[!] Enter a number between 1 and 4!")
                continue
            elif bot_choice == user_choice: 
                print("It's a Tie!")
            elif (win_logic[user_choice] == bot_choice):
                print(f"You won! Bot had: {choices[bot_choice]}")
                score += 1
            else:
                print(f"You lose! Bot chosed: {choices[bot_choice]}")
                score -= 1
            
            print(f"Your score: {score}. Wanna play again?")

        except:
            print("[!] Enter a number.")
            continue

if __name__ == "__main__":
    rock_paper_scissors()