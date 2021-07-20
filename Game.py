from ai import AI
from human import Human
from player import Player #Do we need the above two import or would we just import in the parent? (Player)

Class Game:
    def __init__(self):
        self.player = Player() #Look at above comment. Would this be self.ai and self.human or just self.player?

    def run_game(self):
        self.display_welcome()
        self.play() #?
        self.display_winnter()

    def play(self):
        # Will need to figure out this part

    def display_winner(sel):
        if (self.human.score > self.ai.score):
            print "Human wins!"
        elif (self.human.score < self.ai.score):
            print "AI wins!"
        else
            print "It's a tie. Play again!"
