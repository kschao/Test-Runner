from AI import AI
from Human import Human
from Player import Player #Do we need the above two import or would we just import in the parent? (Player)

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = AI()     #Look at above comment. Would this be self.ai and self.human or just self.player?

    def run_game(self):
      print(f"Welcome to the game of RPSLS")
      self.player1.choose_gesture()
      self.player2.choose_gesture()

    # def single_or_multiplayer(self):
    #  player_choice = input("choose single of multiplayer")
    #  if player_choice == "single":
    #      self.player1.choose_gesture()
    #      self.player2.choose_gesture()
    #      print("you have chosen single player")

    #  elif player_choice == "multiplayer":
    #      self.player1.choose_gesture()
    #      self.player1.choose_gesture()
    #      print("you have chosen multiplayer")
         

    
        # print(self.player1.chosen_gesture)
        # self.display_welcome()
        # self.play() 
        # self.display_winnter()

    # def display_welcome(self):
    #     print(f"Welcome to the game of RPSLS!")
       



   
   
   
   
   
   
   
   
   
   
   
    # def play(self):
    #     # Will need to figure out this part

    # def display_winner(sel):
    #     if (self.human.score > self.ai.score):
    #         print "Human wins!"
    #     elif (self.human.score < self.ai.score):
    #         print "AI wins!"
    #     else
    #         print "It's a tie. Play again!"
