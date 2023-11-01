import random
from arts import logo


def play(chance):

    for i in range(chance,1,-1):

        print(f"You have {i} chances more...")
        user=int(input("Enter the Guess: "))

        if choice==user:
            r=1
            print(f"{user} is Right Guess!!!")
            break
        elif user> choice:
            r=0
            print(f"{user} is Too high Guess!!!")
            print("Guess Again")

        elif user< choice:
            r=0
            
            print(f"{user} is Too Low Guess!!!")
            print("Guess Again")
    return r


print(logo)
print("Welcome to the Game!!!!!!")
print("Guess Number between 1 -100")
guess=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
choice=random.choice(guess)
print("Choose the difficulty level (easy/hard/medium)")
mode=input("Enter the mode: ").lower()






if mode=="hard":
    chance=5
    result=play(chance)
elif mode=="easy":
    chance=10
    result=play(chance)
elif mode=="medium":

    chance=7
    result=play(chance)
if result==1:
    print("You Won!!!!")
else:
    print("You Lose")