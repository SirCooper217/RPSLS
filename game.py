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
        print("\nPlayer 1, your turn: \n")
        player_one.choose_gesture
        if player_two == Computer("Player 2"):
            player_two.choose_gesture
        else:
           print("\nPlayer 2, your turn: \n") 
           player_two.choose_gesture
        if player_one.chosen_gesture == player_two.chosen_gesture:
            print(f"Both players selected {player_one.chosen_gesture}. It's a tie!\n")
            # Tie Results
        elif player_one.chosen_gesture == "Rock":
            if player_two.chosen_gesture == "Scissors":
                print("Rock smashes Scissors!\n")
                sleep(1)
                print("Player 1 wins!\n")
                player_one.add_point
                sleep(1)
            elif player_two.chosen_gesture == "Lizard":
                print("Rock crushes Lizard!\n")
                sleep(1)
                print("Player 1 wins!\n")
                player_one.add_point
                sleep(1)
            elif player_two.chosen_gesture == "Spock":
                print("Spock vaporizes Rock!\n")
                sleep(1)
                print("Player 2 wins!\n")
                player_two.add_point
                sleep(1)
            elif player_two.chosen_gesture == "Paper":
                print("Paper covers rock!\n")
                sleep(1)
                print("Player 2 wins!\n")
                player_two.add_point
                sleep(1)
            else: 
                print("I'm sorry, that input is ivalid. Please try again.\n")
                sleep(1)
                # Player 1 Chooses Rock results
        elif player_one.chosen_gesture == "Paper":
            if player_two.chosen_gesture == "Rock":
                print("Paper covers rock!\n")
                sleep(1)
                print("Player 1 wins!\n")
                player_one.add_point
                sleep(1)
            elif player_two.chosen_gesture == "Scissors":
                print("Scissors cuts paper!\n")
                sleep(1)
                print("Player 2 wins!\n")
                player_two.add_point
                sleep(1)
            elif player_two.chosen_gesture == "Spock":
                print("Paper disproves Spock!\n")
                sleep(1)
                print("Player 1 wins!\n")
                player_one.add_point
                sleep(1)
            elif player_two.chosen_gesture == "Lizard":
                print("Lizard eats Paper!\n")
                sleep(1)
                print("Player 2 wins!\n")
                player_two.add_point
                sleep(1)
            else: 
                print("I'm sorry, that input is ivalid. Please try again.\n")
                # Player 1 chooses Paper results
        elif player_one.chosen_gesture == "Scissors":
            if player_two.chosen_gesture == "Paper":
                print("Scissors cuts paper!\n")
                sleep(1)
                print("Player 1 wins!\n")
                player_one.add_point
                sleep(1)
            elif player_two.chosen_gesture == "Rock":
                print("Rock smashes scissors!\n")
                sleep(1)
                print("Player 2 wins!\n")
                player_two.add_point
                sleep(1)
            elif player_two.chosen_gesture == "Lizard":
                print("Scissors decapitates Lizard!\n")
                sleep(1)
                print("Player 1 wins!\n")
                player_one.add_point
                sleep(1)
            elif player_two.chosen_gesture == "Spock":
                print("Spock smashes Scissors!\n")
                sleep(1)
                print("Player 2 wins!\n")
                player_two.add_point
                sleep(1)
            else: 
                print("I'm sorry, that input is ivalid. Please try again.\n")
                sleep(1)
                #Player 1 chooses Scissors results
        elif player_one.chosen_gesture == "Lizard":
            if player_two.chosen_gesture == "Scissors":
               print("Scissors decapitates Lizard!\n")
               sleep(1)
               print("Player 2 wins!\n")
               player_two.add_point
               sleep(1)
            elif player_two.chosen_gesture == "Spock":
                print("Lizard poisons Spock!\n")
                sleep(1)
                print("Player 1 wins!\n")
                player_one.add_point
                sleep(1)
            elif player_two.chosen_gesture == "Rock":
                print("Rock crushes Lizard!\n")
                sleep(1)
                print("Player 2 wins!\n")
                player_two.add_point
                sleep(1)
            elif player_two.chosen_gesture == "Paper":
                print("Lizard eats Paper!\n")
                sleep(1)
                print("Player 1 wins!\n")
                player_one.add_point
                sleep(1)
            else: 
                print("I'm sorry, that input is ivalid. Please try again.\n")
                sleep(1)
                #Player 1 chooses Lizard reults
        elif player_one.chosen_gesture == "Spock":
            if player_two.chosen_gesture == "Scissors":
                print("Spock smashes Scissors!\n")
                sleep(1)
                print("Player 1 wins!\n")
                player_one.add_point
                sleep(1)
            elif player_two.chosen_gesture == "Lizard":
                print("Lizard poisons Spock!\n")
                sleep(1)
                print("Player 2 wins!\n")
                player_two.add_point
                sleep(1)
            elif player_two.chosen_gesture == "Paper":
                print("Paper disproves Spock!\n")
                sleep(1)
                print("Player 2 wins!\n")
                player_two.add_point
                sleep(1)
            elif player_two.chosen_gesture == "Rock":
                print("Spock vaporizes Rock!\n")
                sleep(1)
                print("Player 1 wins!\n")
                player_one.add_point
                sleep(1)
            else:
                print("I'm sorry, that input is ivalid. Please try again.\n")
                sleep(1)
                #Player 1 chooses Spock results
        else: 
            print("I'm sorry, that input is ivalid. Please try again.\n")
            sleep(1)
    pass

    def display_welcome(self):
        print("\n Welcome to RPSLS! \nEach game is a best of three! The rules are:")
        sleep(1)
        print("\nRock crushes Scissors \nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporizes Rock")
        sleep(2.5)
        pass

    def display_winner(self):
        pass