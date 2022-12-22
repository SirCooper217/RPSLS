from user import User
from com import Computer
from time import sleep

class Game:
    def __init__(self):
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        pass
    
    def run_game(self):
        player_one = User("Player 1")
        keep_playing = True
        while keep_playing:
            self.display_welcome()
            player_two = input("\nWould you like to play against the AI, or against another player? \n 1 for single-player \n 2 for multiplayer\n")
            sleep(0.5)
            if player_two == "1":
                    player_two = Computer("Player 2")
                    print("You've been joined by Player 2(AI)!")
                    sleep(0.5)
            elif player_two == "2":
                    player_two = User("Player 2")
                    print("Let's have a nice, clean fight!")
                    sleep(0.5)
            else:
                    print("That was an invalid input. Please try again.")
                    sleep(1.5)
            while player_one.score < 2 and player_two.score < 2:
                self.play_game(player_one, player_two)
            sleep(0.5)
            self.display_winner(player_one)
            pa_input= input("\nWould you like to play again? Y/N")
            if pa_input.upper() == "N":
                keep_playing = False
                print("\nThanks for playing! :)")
            else:
                print("\n Let's go again!")
                player_one.score = 0
                player_two.score = 0
        pass

    def play_game(self, player_one, player_two):
        print("\nPlayer 1, your turn: \n")
        player_one.choose_gesture()
        sleep(0.75)
        print("\nPlayer 2, your turn: \n") 
        player_two.choose_gesture()
        sleep(0.75)
        if player_one.chosen_gesture == player_two.chosen_gesture:
            print(f"Both players selected the same gesture! \nIt's a tie!\n")
            sleep(1)
            # Tie Results
        elif player_one.chosen_gesture == 0:
            if player_two.chosen_gesture == 2:
                print("Rock smashes Scissors!\n")
                sleep(1)
                print("Player 1 scores!\n")
                player_one.add_point()
                sleep(1)
            elif player_two.chosen_gesture == 3:
                print("Rock crushes Lizard!\n")
                sleep(1)
                print("Player 1 scores!\n")
                player_one.add_point()
                sleep(1)
            elif player_two.chosen_gesture == 4:
                print("Spock vaporizes Rock!\n")
                sleep(1)
                print("Player 2 scores!\n")
                player_two.add_point()
                sleep(1)
            elif player_two.chosen_gesture == 1:
                print("Paper covers rock!\n")
                sleep(1)
                print("Player 2 scores!\n")
                player_two.add_point()
                sleep(1)
            else: 
                print("I'm sorry, that input is invalid. Please try again.\n")
                sleep(1)
                # Player 1 Chooses Rock results
        elif player_one.chosen_gesture == 1:
            if player_two.chosen_gesture == 0:
                print("Paper covers rock!\n")
                sleep(1)
                print("Player 1 scores!\n")
                player_one.add_point()
                sleep(1)
            elif player_two.chosen_gesture == 2:
                print("Scissors cuts paper!\n")
                sleep(1)
                print("Player 2 scores!\n")
                player_two.add_point()
                sleep(1)
            elif player_two.chosen_gesture == 4:
                print("Paper disproves Spock!\n")
                sleep(1)
                print("Player 1 scores!\n")
                player_one.add_point()
                sleep(1)
            elif player_two.chosen_gesture == 3:
                print("Lizard eats Paper!\n")
                sleep(1)
                print("Player 2 scores!\n")
                player_two.add_point()
                sleep(1)
            else: 
                print("I'm sorry, that input is invalid. Please try again.\n")
                # Player 1 chooses Paper results
        elif player_one.chosen_gesture == 2:
            if player_two.chosen_gesture == 1:
                print("Scissors cuts paper!\n")
                sleep(1)
                print("Player 1 scores!\n")
                player_one.add_point()
                sleep(1)
            elif player_two.chosen_gesture == 0:
                print("Rock smashes scissors!\n")
                sleep(1)
                print("Player 2 scores!\n")
                player_two.add_point()
                sleep(1)
            elif player_two.chosen_gesture == 3:
                print("Scissors decapitates Lizard!\n")
                sleep(1)
                print("Player 1 scores!\n")
                player_one.add_point()
                sleep(1)
            elif player_two.chosen_gesture == 4:
                print("Spock smashes Scissors!\n")
                sleep(1)
                print("Player 2 scores!\n")
                player_two.add_point()
                sleep(1)
            else: 
                print("I'm sorry, that input is invalid. Please try again.\n")
                sleep(1)
                #Player 1 chooses Scissors results
        elif player_one.chosen_gesture == 3:
            if player_two.chosen_gesture == 2:
               print("Scissors decapitates Lizard!\n")
               sleep(1)
               print("Player 2 scores!\n")
               player_two.add_point()
               sleep(1)
            elif player_two.chosen_gesture == 4:
                print("Lizard poisons Spock!\n")
                sleep(1)
                print("Player 1 scores!\n")
                player_one.add_point()
                sleep(1)
            elif player_two.chosen_gesture == 0:
                print("Rock crushes Lizard!\n")
                sleep(1)
                print("Player 2 scores!\n")
                player_two.add_point()
                sleep(1)
            elif player_two.chosen_gesture == 1:
                print("Lizard eats Paper!\n")
                sleep(1)
                print("Player 1 scores!\n")
                player_one.add_point()
                sleep(1)
            else: 
                print("I'm sorry, that input is invalid. Please try again.\n")
                sleep(1)
                #Player 1 chooses Lizard reults
        elif player_one.chosen_gesture == 4:
            if player_two.chosen_gesture == 2:
                print("Spock smashes Scissors!\n")
                sleep(1)
                print("Player 1 scores!\n")
                player_one.add_point()
                sleep(1)
            elif player_two.chosen_gesture == 3:
                print("Lizard poisons Spock!\n")
                sleep(1)
                print("Player 2 scores!\n")
                player_two.add_point()
                sleep(1)
            elif player_two.chosen_gesture == 1:
                print("Paper disproves Spock!\n")
                sleep(1)
                print("Player 2 scores!\n")
                player_two.add_point()
                sleep(1)
            elif player_two.chosen_gesture == 0:
                print("Spock vaporizes Rock!\n")
                sleep(1)
                print("Player 1 scores!\n")
                player_one.add_point()
                sleep(1)
            else:
                print("I'm sorry, that input is invalid. Please try again.\n")
                sleep(1)
                #Player 1 chooses Spock results
        else: 
            print("I'm sorry, that input is invalid. Please try again.\n")
            sleep(1)
    pass

    def display_welcome(self):
        print("\nWelcome to RPSLS! \nEach game is a best of three! The rules are:\n")
        sleep(1)
        print("\nRock crushes Scissors \nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporizes Rock")
        sleep(2.5)
        pass

    def display_winner(self, player_one):
        if player_one.score >= 2:
            print("\nPlayer 1 won!! Have a cookie!\n")
            sleep(0.5)
        else:
            print("\nPlayer 2 won!! Have a sweetroll!\n")
            sleep(0.5)
        pass

