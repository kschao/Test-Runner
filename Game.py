from AI import AI
from Human import Human
from Player import Player #Do we need the above two import or would we just import in the parent? (Player)

class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None     #Look at above comment. Would this be self.ai and self.human or just self.player?

    def run_game(self):
        self.display_welcom()
        self.display_rules()
        self.player1.choose_gesture()
        print(self.player1.chosen_gesture)
        self.display_winner()
        # self.play() #?
        

    def display_welcome(self):
        print(f"Welcome to the game of RPSLS!")

    
    def display_rules(self):
        print("Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock")

    # def play(self):
    # Where player will select single or multi player game
    # Will need to figure out this part
    # Where we keep track of scores?


    def display_winner(self):
        if (self.human.score > self.ai.score):
            print("Human wins!")
        elif (self.human.score < self.ai.score):
            print("AI wins!")
        else:
            print("It's a tie. Play again!")
