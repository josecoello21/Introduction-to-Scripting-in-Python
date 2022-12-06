# Practice Project: Rock-Paper-Scissors-Lizard-Spock

**NOTE:** The practice project functions can be executed in  [CodeSkulptor3/Rock-Paper-Scissors-Lizard-Spock](https://py3.codeskulptor.org/#user307_01NkeiV0qw_1.py)

```{python}
"""
Week 4 practice project template for Python Programming Essentials
Rock-paper-scissors-lizard-Spock
"""

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
    
def name_to_number(name):
    """
    Given string name, return integer 0, 1, 2, 3, or 4 
    corresponding to numbering in video
    """
  
    # convert name to number using if/elif/else
    
    msj_one = 'name argument must be a string'
    msj_two = 'invalid name argument'
    
    if not isinstance(name, str):
        return msj_one
    
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return msj_two
    
def number_to_name(number):
    """
    Given integer number (0, 1, 2, 3, or 4)
    corresponding name from video
    """
    
    # convert number to a name using if/elif/else
    
    msj_one = 'name argument must be a int'
    msj_two = 'invalid integer argument'
    
    if not isinstance(number, int):
        return msj_one
    
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return msj_two

def rpsls(player_choice):
    """
    Given string player_choice, play a game of RPSLS 
    and print results to console
    """
    
    # print a blank line to separate consecutive games
    print('')
    # print out the message for the player's choice
    print('Player chooses', player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    if player_number in ('name argument must be a string', 'invalid name argument'):
        print(player_number)
        return player_number

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 4)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out message for computer's choice
    print('Computer chooses', comp_choice)

    # compute difference of player_number and comp_number modulo five
    play_diff = (player_number - comp_number) % 5

    # use if/elif/else to determine winner and print winner message
    if play_diff in (1,2):
        print('Player wins!')
        return 'Player wins!'
    else:
        print('Computer wins!')
        return 'Computer wins!'

    
# test your code
rpsls('rock')
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
```

    Player chooses rock
    Computer chooses Spock
    Computer wins!

    Player chooses Spock
    Computer chooses Spock
    Computer wins!

    Player chooses paper
    Computer chooses Spock
    Player wins!

    Player chooses lizard
    Computer chooses lizard
    Computer wins!

    Player chooses scissors
    Computer chooses paper
    Player wins!
