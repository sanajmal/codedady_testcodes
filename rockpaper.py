import random

min = 1
max = 3
score = 0
user1 = input("enter your name")
user2 = input("enter your name")

while True:


    roll = input("lets start the game y/n : ")
    if roll == "yes" or roll == "y" or roll == "Y":
        roll1 = random.randint(min, max)
        roll2 = random.randint(min, max)
        if roll1 == 1:
           roll1 = "stone"
        elif roll2 == 1:
            roll2 = "stone"
        elif roll1 == 2:
            roll1 = "paper"
        elif roll2 == 2:
            roll2 = "paper"
        elif roll1 == 3:
            roll1 = "scissor"
        elif roll2 == 3:
            roll2 = "scissor"
        print("user1 rolling", roll1)
        print("user2 rolling", roll2)
        if roll1 == "rock" and roll2 == "paper":
            print("roll2 win!!!!!!")
            score = score + 1
        if roll1 == "paper" and roll2 == "rock":
            print("roll1 win!!!!!!")
            score = score + 1
        if roll1 == "scissor" and roll2 == "paper":
            print("roll1 win!!!!!!")
            score = score + 1
        if roll1 == "paper" and roll2 == "paper":
            print("noo score!!!!!!")

        if roll1 == "rock" and roll2 == "rock":
            print("noo score!!!!!!")

        if roll1 == "scissor" and roll2 == "rock":
            print("roll2 win!!!!!!")
            score = score + 1
        if roll1 == "scissor" and roll2 == "scissor":
            print("noo score!!!!!!")

        if roll1 == "rock" and roll2 == "scissor":
            print("roll1 win!!!!!!")
            score = score + 1
        if roll1 == "scissor" and roll2 == "stone":
            print("roll2 win!!!!!!")
            score = score + 1