from participant import Participant
import random
from time import sleep

class Computer(Participant):
    def __init__(self, name:str):
        super().__init__(name)
        pass
    
    def choose_gesture(self):
        self.chosen_gesture = random.randint(0,4)
        #AI chooses random integer between 0 and 4, which refers to a position in the gesture list
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        sleep(1)
        print(f"{self.name} has chosen {gesture_list[self.chosen_gesture]}")
        #Displays AI choice
        pass
