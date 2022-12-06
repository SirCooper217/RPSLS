from user import User
from com import Computer
from time import sleep

class Game:
    def __init__(self):
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        pass
    
    def run_game(self, participant):
        player_one = User("User")
        print("\n Welcome to RPSLS! \nEach game is a best of three! The rules are:")
        sleep(1)
        print("\nRock crushes Scissors \nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporizes Rock")
        sleep(2.5)
        input("Would you like to play against the AI, or against another player?")
        
        pass

    def display_winner(self):
        pass