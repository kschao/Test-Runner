from AI import AI
from Human import Human
from Player import Player #Do we need the above two import or would we just import in the parent? (Player)

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = AI()     #Look at above comment. Would this be self.ai and self.human or just self.player?

    def display_welcome(self):
     print(f"Welcome to the game of RPSLS")

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.single_or_multiplayer()


    
    def display_rules(self):
     rules = """Here are the rules to the game:,
    Rock crushes Scissors,
         Scissors cuts Paper,
         Paper covers Rock,
         Rock crushes Lizard,
         Lizard poisons Spock,
         Spock smashes Scissors,
         Scissors decapitates Lizard, 
         Lizard eats Paper,
         Paper disproves Spock,
         Spock vaporizes Rock"""
     print(rules)

       
       
    def single_or_multiplayer(self):
     player_choice = input("choose _single or _multiplayer:")
     if player_choice == "single":
        self.player1.choose_gesture()
        self.player2.choose_gesture()
        
     elif player_choice == "multiplayer":
      self.player1.choose_gesture()
      self.player1.choose_gesture()
    
         

      
      
      
      
      
      #  self.player1.choose_gesture()
    #  self.player2.choose_gesture()

        # print(self.player1.chosen_gesture)
        # self.display_welcome()
        # self.play() 
        # self.display_winnter()
        # self.display_welcome()
        # self.display_rules()
        # self.player1.choose_gesture()
        # print(self.player1.chosen_gesture)
        # self.display_winner()
        # self.play() #?
        

    # def display_welcome(self):
    #     print(f"Welcome to the game of RPSLS!")
       


    
    
   
   
   
   
   
   
   
   
   
   
   
    # # def play(self):
    # def type_of_player(self):
    #     player_choice = input("Enter 'single' for single player or 'multi' for multiple players: ")
    #     if player_choice == 'single':
    #         print("single player!")
    #     elif player_choice == 'multi':
    #         print("multi-player!")
    #     else:
    #         print("Please make a selection.")
            
# Where player will select single or multi player game
    # Will need to figure out this part
    # Where we keep track of scores?
  
    # def display_winner(self):
    #     if (self.human.score > self.ai.score):
    #         print("Human wins!")
    #     elif (self.human.score < self.ai.score):
    #         print("AI wins!")
    #     else:
    #         print("It's a tie. Play again!")
