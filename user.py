from participant import Participant
from time import sleep

class User(Participant):
    def __init__(self, name:str):
        super().__init__()
        pass

    def choose_gesture(self):
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        user_input = input("\n What will you throw? \n0 for Rock \n1 for Paper \n2 for Scissors \n3 for Lizard \n4 for Spock")
        self.chosen_gesture = int(user_input)
        print(f"{self.name} has chosen {gesture_list[self.chosen_gesture]}")
        pass
