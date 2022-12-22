from participant import Participant
from time import sleep

class User(Participant):
    def __init__(self, name:str):
        super().__init__(name)
        pass

    def choose_gesture(self):
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        conf_bool = True
        while conf_bool:
            user_input = input("\n What will you throw? \n0 for Rock \n1 for Paper \n2 for Scissors \n3 for Lizard \n4 for Spock\n")
            if user_input in ["0", "1", "2", "3", "4"]:
                self.chosen_gesture = int(user_input)
                conf_bool = False
        print(f"{self.name} has chosen {gesture_list[self.chosen_gesture]}")
        pass
