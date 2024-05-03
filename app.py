# develop a rock-paper-scissors game 
# Create it for multiplayer and single player
# for single player the computer will randomly select rock, paper or scissors
# for multiplayer the players will input their selection
# all the interactions will be done through the terminal
# at the end of the game the players will be asked if they want to play again
# show player scores at the end of the game
# show the winner of the game
# show a message if the game is a tie
#rock beats scissors
#scissors beats paper
#paper beats rock

import random
import os 
import sys
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')    

def game():
    player1_score = 0
    player2_score = 0
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")
    while True:
        clear()
        print(f"Player 1: {player1} - {player1_score} points")
        print(f"Player 2: {player2} - {player2_score} points")
        player1_choice = input(f"{player1}, enter your choice (rock, paper, scissors): ")
        player2_choice = input(f"{player2}, enter your choice (rock, paper, scissors): ")
        if player1_choice == player2_choice:
            print("It's a tie!")
        elif player1_choice == "rock":
            if player2_choice == "scissors":
                print(f"{player1} wins!")
                player1_score += 1
            else:
                print(f"{player2} wins!")
                player2_score += 1
        elif player1_choice == "scissors":
            if player2_choice == "paper":
                print(f"{player1} wins!")
                player1_score += 1
            else:
                print(f"{player2} wins!")
                player2_score += 1
        elif player1_choice == "paper":
            if player2_choice == "rock":
                print(f"{player1} wins!")
                player1_score += 1
            else:
                print(f"{player2} wins!")
                player2_score += 1
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != "yes":
            break

def single_player_game():
    player_score = 0
    player = input("Player, enter your name: ")
    while True:
        clear()
        print(f"Player: {player} - {player_score} points")
        player_choice = input(f"{player}, enter your choice (rock, paper, scissors): ")
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer choice: {computer_choice}")
        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == "rock":
            if computer_choice == "scissors":
                print(f"{player} wins!")
                player_score += 1
            else:
                print("Computer wins!")
        elif player_choice == "scissors":
            if computer_choice == "paper":
                print(f"{player} wins!")
                player_score += 1
            else:
                print("Computer wins!")
        elif player_choice == "paper":
            if computer_choice == "rock":
                print(f"{player} wins!")
                player_score += 1
            else:
                print("Computer wins!")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != "yes":
            break

def main():
    while True:
        clear()
        print("Welcome to Rock-Paper-Scissors!")
        print("1. Single player")
        print("2. Multiplayer")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            single_player_game()
        elif choice == "2":
            game()
        elif choice == "3":
            sys.exit()
        else:
            print("Invalid choice!")
            time.sleep(1)

if __name__ == "__main__":
    main()

# Run the code
# python app.py





