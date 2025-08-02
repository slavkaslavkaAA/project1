import random

options = ["Rock", "Paper", "Scissors"]

player_score = 0
bot_score = 0

while True:
    player_choice = input("Choose: Rock, Paper or Scissors: ")

    if(player_choice not in options):
        print("Incorrect! Choose again")
        continue
    computer_choice = random.choice(options)
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("Draw")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or (player_choice == "Paper" and computer_choice == "Rock") or (player_choice == "Scissors" and computer_choice == "Paper"):
        print("You won")
        player_score += 1
    else:
        print("Computer won")
        bot_score += 1
    print(f"Your score: {player_score}", f"Computer's score is: {bot_score}")
        
    play_again = input("Wanna play again? y/n")
    if play_again != "y":
        print("Thank you for your playing")
        break
