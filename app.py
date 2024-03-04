import random

def play_game():
    options = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Enter your choice (rock/paper/scissors): ").lower()

        if player_choice not in options:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)

        print(f"Player chooses: {player_choice}")
        print(f"Computer chooses: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

play_game()
