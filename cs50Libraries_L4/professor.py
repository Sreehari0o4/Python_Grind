# This program is a math quiz that asks the user to solve 10 addition problems.
# The user selects a difficulty level (1, 2, or 3), which determines the range of numbers used.
# For each problem, the user has up to 3 attempts to enter the correct answer.
# If the answer is incorrect or invalid, "EEE" is printed and the user can try again.
# If all attempts are used, the correct answer is displayed.
# At the end, the user's score (number of correct answers) is shown.

import random


def main():
    score = 0
    level = get_level()
    for i in range(1,11):
        a = generate_integer(level)
        b = generate_integer(level)
        tries = 3
        while tries:
            try:
                answer = int(input(f"{a} + {b} = "))
                if answer == a+b:
                    score+=1
                    break
                else:
                    print("EEE")
                    tries-=1
            except ValueError:
                print("EEE")
                tries-=1
                pass
        if tries == 0:
            print(f"{a} + {b} = {a+b}")
    print(f"Score: ",score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            try:
                if level in [1,2,3]:
                    return level
                else:
                    raise ValueError
            except ValueError:
                pass
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
    else:
        x = random.randint(100,999)
    return x


if __name__ == "__main__":
    main()