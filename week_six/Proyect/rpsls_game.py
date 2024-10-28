import random
import time

chooses = {
  1: 'Rock✊',
  2: 'Paper✋',
  3: 'Scissors✌️',
  4: 'Lizard🦎',
  5: 'Spock🖖'
}

win_conditions = {
  'Rock✊': ['Scissors✌️', 'Lizard🦎'],
  'Paper✋': ['Rock✊', 'Spock🖖'],
  'Scissors✌️': ['Paper✋', 'Lizard🦎'],
  'Lizard🦎': ['Spock🖖', 'Paper✋'],
  'Spock🖖': ['Scissors✌️', 'Rock✊']
}

scores = {'tie': 0, 'win': 0, 'lose': 0}

scores_for_game = {'tie': 0, 'win': 0, 'lose': 0}

rock = chooses[1]
paper = chooses[2]
scissors = chooses[3]
lizard = chooses[4]
spock = chooses[5]

def typewriter(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def play_game():
  typewriter(f'Welcome to RPSLS Game\n({rock}, {paper}, {scissors} , {lizard}, {spock})!\n\n')
  rules = display_rules()
  typewriter(rules)
  play = ''
  choice = ''
  output = ''

  while True:
    while play != 'n' and play != 'y':
      typewriter('\nDo you want to play? (y/n): ')
      play = input().lower()

      if play != 'n' and play != 'y':
        typewriter('NOT VALID\n')
      elif play == 'n':
        typewriter('YOU ARE DIE!\n')
        return False
    
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    
    if player_choice not in chooses.values():
      typewriter(player_choice)
    else:
      typewriter(f'You chose {player_choice}')
      time.sleep(1)
      typewriter(f'\nPC chose {chooses[computer_choice]}', 0.1)
      time.sleep(1)
      typewriter(f'\nYou {result}\n', 0.1)

      score = update_score(result)
      typewriter(score)

    if scores['win'] > scores['lose']:
      output = 'win'
    elif scores['win'] < scores['lose']:
      output = 'lose'

    
    if scores_for_game['win'] == 3 or scores_for_game['lose'] == 3:
      display_statistics()
      while choice.lower() != 'y' and choice.lower() != 'n':
        typewriter(f'\nDo you want to continue {output}? (y/n): ')
        choice = input()
        if choice.lower()!= 'y' and choice.lower()!= 'n':
          typewriter('NOT VALID\n')

      if choice == 'n':
        typewriter(f'Thanks for {output}!')
        break
      elif choice == 'y':
        reset_scores_for_game()
        typewriter(f'Let\'s continue {output}\n')
        choice = ''

def get_player_choice():
    try:
      typewriter('\nChoose or DIE: ')
      choice = int(input())
      if choice < 1 or choice > 5:
        return 'YOU CHOSE DIE\n'
      else:
        return chooses[choice]
    except ValueError:
      return 'YOU CHOSE DIE\n'

def get_computer_choice():
  return random.randint(1, 5)

def determine_winner(player_choice, computer_choice):
  computer_choice = chooses[computer_choice]
  try:
    if player_choice not in chooses.values():
      return 'YOU CHOSE DIE'
    elif player_choice == computer_choice:
      return 'tie'
    elif computer_choice in win_conditions[player_choice]:
      return 'win'
    else:
      return 'lose'
  except ValueError:
    return 'YOU CHOSE DIE'
  
def display_rules():
  return f'RULES\n{scissors}  cut {paper}\n{paper} covers {rock}\n{rock} crushes {lizard}\n{lizard} poisons {spock}\n{spock} smashes {scissors}\n{scissors}  decapitate {lizard}\n{lizard} eats {paper}\n{paper} disproves {spock}\n{spock} vaporizes {rock}\nAnd as always, {rock} crushes {scissors}.\n\n1: {rock}\n2: {paper}\n3: {scissors}\n4: {lizard}\n5: {spock}\n'

def update_score(result):
  scores[result] += 1
  scores_for_game[result] += 1
  return f'Score:\nWins {scores["win"]} | Losses {scores["lose"]} | Ties {scores["tie"]}\n'

def reset_scores_for_game():
  scores_for_game['tie'] = 0
  scores_for_game['win'] = 0
  scores_for_game['lose'] = 0  

def display_statistics():
    total_games = scores['win'] + scores['lose'] + scores['tie']
    
    if total_games == 0:
        win_percentage = 0
        lose_percentage = 0
        tie_percentage = 0
    else:
        win_percentage = (scores['win'] / total_games) * 100
        lose_percentage = (scores['lose'] / total_games) * 100
        tie_percentage = (scores['tie'] / total_games) * 100

    print('\n------------------------------')
    typewriter(f'Total Games Played: {total_games}\n')
    typewriter(f'\nGame Statistics:\n')
    typewriter(f'Wins: {scores["win"]} ({win_percentage:.2f}%)\n')
    typewriter(f'Losses: {scores["lose"]} ({lose_percentage:.2f}%)\n')
    typewriter(f'Ties: {scores["tie"]} ({tie_percentage:.2f}%)\n')
    print('------------------------------')

if __name__ == '__main__':
  play_game() 