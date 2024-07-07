import random


def get_choices():
  options = ['rock', 'paper', "scissors"]
  # indentation is very important
  player_choice = input('Enter your choice (rock, paper, scissors) -> ')
  if player_choice not in options:
    raise ValueError(f'invalid choice: {player_choice}')
  computer_choice = random.choice(options)
  choises_dict = {"player": player_choice, "computer": computer_choice}
  return choises_dict


choices = get_choices()


def check_win(p, c):
  print(f"you chose {p} computer chose {c}")

  if p == c:
    return 'draw'
  elif p == 'rock':
    return 'computer wins' if c == 'paper' else "player wins"
  elif p == 'paper':
    return 'computer wins' if c == 'scissors' else "player wins"
  elif p == 'scissors':
    return 'computer wins' if c == 'rock' else "player wins"


result = check_win(choices['player'], choices['computer'])

print(result)

