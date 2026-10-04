import random 

options = ("Rock", "Paper", "Scissor")
options_str = ", ".join(options)
running = True

while running:

    computer = random.choice(options)
    player = input(f"Enter your choice ({options_str}) : ")

    while player not in options:
        player = input(f"Invalid choice! Enter ({options_str}) : ")
    
    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("It's a tie! Well played! 🤝✨")
    elif player == "Rock" and computer == "Scissor":
        print("Victory! You beat the bot! 🤖💥")
    elif player == "Paper" and computer == "Rock":
        print("You won! 🏆🎉")
    elif player == "Scissor" and computer == "Paper":
        print("Victory! You beat the bot! 🤖💥")
    else:
        print("Game over! The bot got this round! 🤖👑")

    # Call .lower() on the output of input(), not inside it
    if input("Do you wanna play again?(y/n): ").lower() != "y":
        running = False

print("Thanks for playing!!")