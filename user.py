from participant import Participant
from time import sleep

class User(Participant):
    def __init__(self, name:str):
        super().__init__()
        self.score = 0
        self.name = name

    def choose_gesture(self, user_input):
        self.chosen_gesture = user_input
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        user_input = 
        print(f"{self.name} has chosen {gesture_list[int(self.chosen_gesture)]}")
