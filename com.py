from participant import Participant
import random
from time import sleep

class Computer(Participant):
    def __init__(self, name:str):
        super().__init__()
        self.score = 0
        self.name = name
    
    def choose_gesture(self):
        self.chosen_gesture = str(random.randint(0,4))
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        sleep(1)
        print(f"{self.name} has chosen {gesture_list[int(self.chosen_gesture)]}")
