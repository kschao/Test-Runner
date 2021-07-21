from _typeshed import Self
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
      self.display_welcome()
      self.display_rules()
      self.player1.choose_gesture()
      print(self.player1.chosen_gesture)
      self.display_winner()
                # self.play() #?
            

    # def display_welcome(self):
    #     print(f"Welcome to the game of RPSLS!")
       


    
    def display_rules(self):
        print("Here are the rules to the game:")
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard") 
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")

   
   
   
   
   
   
   
   
   
   
   
    # def play(self):
    def type_of_player(self):
        player_choice = input("Enter 'single' for single player or 'multi' for multiple players: ")
        if player_choice == 'single':
            print("single player!")
        elif player_choice == 'multi':
            print("multi-player!")
        else:
            print("Please make a selection.")
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







 # def play(): # We will need to add in 'l' = lizard and 's' = spock. Since there are 2 with 's', this might confuse the code. could we number them instead? 
    #     user = input("What is your choice? 'r' = rock, 'p' = paper, 's' = scissor, 'l' = lizard, or 'v' = spock???")
    #     user = user.lower()

    #     computer = random.choice(['r', 'p', 's', 'l', 'v'])

    #     if user == computer:
    #         return (0, user, computer)

        
    #     if the_winner(user, computer):
    #         return (1, user, computer)

    #     return (-1, user, computer)


    # def the_winner(player, opponent):
    #         if (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r') or (player == 'r' and opponent == 'l') or (player == 'l' and opponent == 'v') or (player == 'v' and opponent == 's' or (player == 's' and opponent == 'l') or (player == 'l' and opponent == 'p') or (player == 'p' and opponent == 'v') or (player == 'v' and opponent == 'r') or (player == 'r' and opponent == 's')) :
    #             return True

    #         return False

        
#   def best_winner =(Self):
#       player_wins = 0
#       comp_wins = 0
#       play_ties = 0
        
#     while player_wins < play_ties and comp_wins < play_ties:
#             result, user, computer = play()
#   if result == 0:
#       print('Its a tie!! you and the opponent chosen {}. \n'.format(user))
#   elif result == 1:
#       player_wins +=1
#       print('You choosen {} and the opponent chose{}. You are the winner!!: \n'.format(user, computer))
#   else: comp_wins +=1
#       print('You chose {} and the opponent chose {} You LOST!! \n'.format(user, computer))
#   if  player_wins > comp_wins:
#       print('You have won the game! with the best of {}'.format(n))
#   else:
#       print('Oh NO!, the opponent has won with the best of {} Good luck next time!'.format(n))

#   if __name__ == '__main__':
#     best_winner(3)


