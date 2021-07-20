from AI import AI
# from human import Human
from Player import Player #Do we need the above two import or would we just import in the parent? (Player)

class Game:
    def __init__(self):
        self.player1 = AI()
        self.player2 = None     #Look at above comment. Would this be self.ai and self.human or just self.player?

    def run_game(self):
        self.player1.choose_gesture()
        print(self.player1.chosen_gesture)
        # self.display_welcome()
        # self.play() #?
        # self.display_winnter()

    # def play(self):
    #     # Will need to figure out this part

    # def display_winner(sel):
    #     if (self.human.score > self.ai.score):
    #         print "Human wins!"
    #     elif (self.human.score < self.ai.score):
    #         print "AI wins!"
    #     else
    #         print "It's a tie. Play again!"
