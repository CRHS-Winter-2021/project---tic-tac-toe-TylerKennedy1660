# Tic Tak Toe
# Tyler Kennedy 
# Feb 17th 2021

import sys

#constants
turn = 0
stop = 0
X_O_pos = []


def print_board():
  the_board = ('     |     |     \n  '+ X_O_pos[7] + '  |  '+ X_O_pos[8] + '  |  '+ X_O_pos[9] + '  \n_____|_____|_____\n     |     |     \n  '+ X_O_pos[4] + '  |  '+ X_O_pos[5] + '  |  '+ X_O_pos[6] + '  \n_____|_____|_____\n     |     |     \n  '+ X_O_pos[1] + '  |  '+ X_O_pos[2] + '  |  '+ X_O_pos[3] + '  \n     |     |     \n')
  print(the_board)

def check_win():

  if X_O_pos[1] == 'X' and X_O_pos[2] == 'X' and X_O_pos[3] == 'X'  or  X_O_pos[4] == 'X' and X_O_pos[5] == 'X' and X_O_pos[6] == 'X'  or  X_O_pos[7] == 'X' and X_O_pos[8] == 'X' and X_O_pos[9] == 'X'  or  X_O_pos[7] == 'X' and X_O_pos[4] == 'X' and X_O_pos[1] == 'X'  or  X_O_pos[8] == 'X' and X_O_pos[5] == 'X' and X_O_pos[2] == 'X'  or  X_O_pos[9] == 'X' and X_O_pos[6] == 'X' and X_O_pos[3] == 'X'  or  X_O_pos[7] == 'X' and X_O_pos[5] == 'X' and X_O_pos[3] == 'X'  or  X_O_pos[9] == 'X' and X_O_pos[5] == 'X' and X_O_pos[1] == 'X':
    
    print('X Wins!')
    sys.exit()
    
  if X_O_pos[1] == 'O' and X_O_pos[2] == 'O' and X_O_pos[3] == 'O'  or  X_O_pos[4] == 'O' and X_O_pos[5] == 'O' and X_O_pos[6] == 'O'  or  X_O_pos[7] == 'O' and X_O_pos[8] == 'O' and X_O_pos[9] == 'O'  or  X_O_pos[7] == 'O' and X_O_pos[4] == 'O' and X_O_pos[1] == 'O'  or  X_O_pos[8] == 'O' and X_O_pos[5] == 'O' and X_O_pos[2] == 'O'  or  X_O_pos[9] == 'O' and X_O_pos[6] == 'O' and X_O_pos[3] == 'o'  or  X_O_pos[7] == 'O' and X_O_pos[5] == 'O' and X_O_pos[3] == 'O'  or  X_O_pos[9] == 'O' and X_O_pos[5] == 'O' and X_O_pos[1] == 'O':
    print('O Wins!')
    sys.exit()

def check_draw():

  if X_O_pos.count(' ') == 0:
    stop = 1
    print('Draw!')
    sys.exit()

def play():
  global turn

  while stop == 0:
  
    if turn % 2 == 0:
      x_o = 'X'
      print("X's Turn")
    else:
      x_o = 'O'
      print("O's Turn")
  
  
    move = input('Where would you like to play ')

    while move not in ['1','2','3','4','5','6','7','8','9'] or X_O_pos[int(move)] != ' ':
      print('Invalid move')
      move = input('Where would you like to play ')

    X_O_pos[int(move)] = x_o

    print_board()

    check_win()

    check_draw()
    
    turn +=1

def setup(): 
  global X_O_pos
  global turn 

  print("Welcome to Tyler's Tic Tac Toe\nThe spaces are related to the numbers on the number pad")

  first_move = input("Player 1 would you like to be:\nX (1)\nO (2)\n")

  while first_move != '1' and first_move != '2': 
   print('You must pick 1 or 2')
   first_move = input("Player 1 would you like to be:\nX (1)\nO (2)\n")
  

  if first_move == '2':
    turn += 1

  X_O_pos = ['not a space',' ',' ',' ',' ',' ',' ',' ',' ',' ']


setup()
print_board()
play()
