import random

user_wins = 0
comp_wins = 0
options = ["rock", "paper", "sissor"]

while True:
    user_inp = (input("Choose Rock, Paper or Sissor OR q to quit: ")).lower()
    if user_inp == "q":
        print("Thanks for playing!")
        break
    
    if user_inp not in options:
        print("Choose correctly!")
        continue

    rand_num = random.randint(0,2)
    comp_inp = options[rand_num]

    if user_inp == "rock" and comp_inp == "sissor":
        print("You won!")
        user_wins += 1
    elif user_inp == "paper" and comp_inp == "rock":
        print("You won!")
        user_wins += 1
    elif user_inp == "sissor" and comp_inp == "paper":
        print("You won!")
        user_wins += 1
    elif user_inp == comp_inp :
        print("Tie!")
    else:
        print("System won!")
        comp_wins += 1

print("You won", user_wins, "times.")
print("System won", comp_wins, "times.")
