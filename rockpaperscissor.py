import random

user_score = int(0)
pc_score = int(0)
score_limit = 5


while user_score != score_limit or pc_score != score_limit:

    user_guess: str = input(str("pls enter your guess, rock/paper/scissors:")).lower()

    my_list = "rock", "paper", "scissors"
    pc_guess = random.choice(my_list)
    print("the computer chose", pc_guess)

    if pc_guess == "rock" and user_guess == "rock":
        print ( "Tie!!" )

    if pc_guess == "paper" and user_guess == "paper":
        print("Tie!!")

    if pc_guess == "scissors" and user_guess == "scissors":
        print("Tie!!")

    if pc_guess == "paper" and user_guess == "rock":
        print("the computer scores")

        pc_score = pc_score + 1
        print("the pc score is:", pc_score)

    if pc_guess == "rock" and user_guess == "paper":
        print("yay u scored")

        user_score = user_score + 1
        print("the user score is:", user_score)

    if pc_guess == "rock" and user_guess == "scissors":
        print("the computer scored")

        pc_score = int(pc_score) + 1
        print("the pc score is:", pc_score)

    if pc_guess == "scissors" and user_guess == "rock":
        print("yay u scored")

        user_score = user_score + 1
        print("the user score is:", user_score)

    if pc_guess == "paper" and user_guess == "scissors":
        print("yay u scored")


        user_score = user_score + 1
        print("the user score is:", user_score)

    if pc_guess == "scissors" and user_guess == "paper":
        print("the computer scored")

        pc_score = int(pc_score) + 1
        print("the pc score is:", pc_score)

        pc_guess = random.choice(my_list)

    if user_score == score_limit:
        print("yay congrats u won")

    elif pc_score == score_limit:
        print("oopsies, the computer won, better luck next time")

        break