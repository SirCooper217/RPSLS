class Participant:
    def  __init__(self, name):
        self.name = name
        self.score = 0
        self.chosen_gesture = ""
        pass

    def add_point(self):
        while self.score <= 2:
        pass