import random
from Player import Player

class AI(Player):
    def __init__(self):
        super().__init__('AI')

    def choose_gesture(self): #I know this is wrong but something like that?
        self.chosen_gesture = random.choice(self.gestures_list)

