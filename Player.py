class Player:
    def __init__(self, name):
        self.name = name
        self.gestures_list = ['rock', 'scissor', 'paper', 'lizard', 'spock']
        self.score = 0
        self.chosen_gesture = None


    def choose_gesture(self):
        pass
    



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

        
    # def best_winner =(n):
    #     player_wins = 0
    #     comp_wins = 0
    #     play_ties = 0
        
    #     while player_wins < play_ties and comp_wins < play_ties:
    #         result, user, computer = play()
    #         if result == 0:
    #             print('Its a tie!! you and the opponent chosen {}. \n'.format(user))
    #         elif result == 1:
    #             player_wins +=1
    #             print('You choosen {} and the opponent chose{}. You are the winner!!: \n'.format(user, computer))
    #         else: comp_wins +=1
    #             print('You chose {} and the opponent chose {} You LOST!! \n'.format(user, computer))
    #         if player_wins > comp_wins:
    #             print('You have won the game! with the best of {}'.format(n))
    #         else:
    #             print('Oh NO!, the opponent has won with the best of {} Good luck next time!'.format(n))

    #     if __name__ == '__main__':
    #         best_winner(3)


