from participant import Participant
import random
from time import sleep

class Computer(Participant):
    def __init__(self, name:str):
        super().__init__(name)
        pass
    
    def choose_gesture(self):
        self.chosen_gesture = random.randint(0,4)
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        sleep(1)
        print(f"{self.name} has chosen {gesture_list[self.chosen_gesture]}")
        pass
