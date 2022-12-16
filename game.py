from user import User
from com import Computer
from time import sleep

class Game:
    def __init__(self):
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        pass
    
    def run_game(self):
        player_one = User("Player 1")
        self.display_welcome()
        player_two = User
        while player_two != Computer("Player 2"):
            player_two = input("\nWould you like to play against the AI, or against another player? \n 1 for single-player \n 2 for multiplayer")
            if player_two == "1":
                player_two = Computer("Player 2")
                print("You've been joined by {self.player_two}(AI)!")
            elif player_two == "2":
                player_two = User("Player 2")
                print("Let's have a nice, clean fight!")
            else:
                print("That was an invalid input. Please try again.")
                sleep(1.5)
        while player_one.score < 2 and player_two.score < 2:
            self.play_game("Player 1", "Player 2")
        
        pass

    def play_game(self, player_one, player_two):
        if player_one.chosen_gesture == player_two.chosen_gesture:
            print(f"Both players selected {player_one.chosen_gesture}. It's a tie!")
        elif player_one.chosen_gesture == "Rock":
            if player_two.chosen_gesture == "Scissors":
                print("Rock smashes scissors! Player 1 wins!")
            elif player_two.chosen_gesture == "Paper":
                print("Paper covers rock! Player 2 wins!")
        elif player_one.chosen_gesture == "Paper":
            if player_two.chosen_gesture == "Rock":
                print("Paper covers rock! Player 1 wins!")
            else:
                print("Scissors cuts paper! Player 2 wins!")
        elif player_one.chosen_gesture == "Scissors":
            if player_two.chosen_gesture == "Paper":
                print("Scissors cuts paper! Player 1 wins!")
            else:
                print("Rock smashes scissors! Player 2 wins!")
    pass

    def display_welcome(self):
        print("\n Welcome to RPSLS! \nEach game is a best of three! The rules are:")
        sleep(1)
        print("\nRock crushes Scissors \nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporizes Rock")
        sleep(2.5)
        pass

    def display_winner(self):
        pass