player1_score = 0
player2_score = 0

options = ['rock' ,'paper', 'scissors']

def get_choice(player):
    while True:
      players_choice = input(f'{player} what is your pick : ')
      if players_choice in options:
          return players_choice
        
def check_score(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        print('draw')
        return 0

    score = {
      ('paper', 'rock'): 1,
      ('rock', 'scissors'): 1,
      ('scissors', 'paper'): 1,
    }

    return score.get((player1_choice, player2_choice), -1) 


while player1_score != 3 and player2_score != 3:
    player1_choice = get_choice('Player 1')
    player2_choice = get_choice('Player 2')
    score = check_score(player1_choice, player2_choice)
    
    if score == 1:
        print('Player 1 wins')
        player1_score += 1
    elif score == -1:
        print('Player 2 wins')
        player2_score += 1    

if player1_score > player2_score:
  print('Player 1 won the game')
else:
  print('Player 2 won the game')