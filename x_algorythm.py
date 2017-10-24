"""
    1. Win: If you have two in a row, play the third to get three in a row.

    2. Block: If the opponent has two in a row, play the third to block them.

    3. Fork: Create an opportunity where you can win in two ways.

    4. Block Opponent's Fork:

      Option 1: Create two in a row to force the opponent into defending, as long as it doesn't result in them creating a fork or winning.
      For example, if "X" has a corner, "O" has the center, and "X" has the opposite corner as well, "O" must not play a corner in order to win.
      (Playing a corner in this scenario creates a fork for "X" to win.)

      Option 2: If there is a configuration where the opponent can fork, block that fork.

    7. Center: Play the center.

    8. Opposite Corner: If the opponent is in the corner, play the opposite corner.

    9. Empty Corner: Play an empty corner.

    10.Empty Side: Play an empty side.

"""

import random

class X:
  def get_x(self, board):
    x = False
    if self.x_win(board):
      return 'x_win'
    elif self.o_win(board):
      return 'o_win'

    if "' '" in str(board):
      if self.x_can_win(board)[0]:
        # 1. Win: If you have two in a row, play the third to get three in a row.
        # print('x can win')
        x = self.x_can_win(board)[0]
      else:
        if self.o_can_win(board):
          # 2. Block: If the opponent has two in a row, play the third to block them.
          # print('block')
          x = self.o_can_win(board)
        else:
          if self.x_can_fork(board):
            x = self.x_can_fork(board)
          else:
            # 7. Center: Play the center.
            if ' ' in board [1][1]:
              # print('center')
              x = [1,1]
            else:
              if self.check_corners(board):
                # 8. Opposite Corner: If the opponent is in the corner, play the opposite corner.
                # print('opposite corner')
                x = self.check_corners(board)
              else:
               # 9. Empty Corner: Play an empty corner.
               for i in range(0, 4):
                 corner_x = random.randint(0,1)*2
                 corner_y = random.randint(0,1)*2
                 if ' ' in board[corner_x][corner_y]:
                   # print('empty corner')
                   x = [corner_x, corner_y]
                   # print(x)
                   return x
               # 10.Empty Side: Play an empty side.
               while True:
                 rand_side = random.randint(0, 4)
                 if rand_side == 1 and' ' in board[0][1]:
                   x = [0, 1]
                   break
                 elif rand_side == 2 and ' ' in board[1][0]:
                   x = [1, 0]
                   break
                 elif rand_side == 3 and ' ' in board[1][2]:
                   x = [1, 2]
                   break
                 elif rand_side == 4 and ' ' in board[2][1]:
                   x = [0, 1]
                   break
    return x

  def check_corners(self, board):
    if 'o' in board[0][0] and ' ' not in board[2][2]:
      x_corner = [2, 2]
    elif 'o' in board[0][2] and ' ' in board[2][0]:
      x_corner = [2, 0]
    elif 'o' in board[2][0] and ' ' in board[0][2]:
      x_corner = [0, 2]
    elif 'o' in board[2][2] and ' ' in board[0][0]:
      x_corner = [0, 0]
    else:
      x_corner = False
      
    return x_corner
    
  def x_win(self, board):
    # Check if X win horizontally
    for nr in range(0, 3):
      row = board[nr][0] + board[nr][1] + board[nr][2]
      if 'xxx' in row:
        return True
    
    # Check if X win vertically
    for nr in range(0, 3):
      column = board[0][nr] + board[1][nr] + board[2][nr]
      if 'xxx' in column:
        return True
      
    # Check if X win diagonally
    if 'x' in board[1][1]:
      if 'x' in board[0][0] and 'x' in board[2][2]:
        return True
      elif 'x' in board[0][2] and 'x' in board[2][0]:
        return True
    
    return False

  def x_can_win(self, board):
    x_win = []
    chances = 0
    # Check if x can win horizontally and return x_wub cords
    for nr in range(0, 3):
      row = board[nr][0] + board[nr][1] + board[nr][2]
      if 'xx ' in row:
        x_win = [nr, 2]
        chances += 1
      elif 'x x' in row:
        x_win = [nr, 1]
        chances += 1
      elif ' xx' in row:
        x_win = [nr, 0]
        chances += 1
  
    # Check if X can win vertically and return x cords
    for nr in range(0, 3):
      row = board[0][nr] + board[1][nr] + board[2][nr]
      if 'xx ' in row:
        x_win = [2, nr]
        chances += 1
      elif 'x x' in row:
        x_win = [1, nr]
        chances += 1
      elif ' xx' in row:
        x_win = [0, nr]
        chances += 1
  
    # Check if X can win by left diagonal and return x cords
    left_diagonal = board[0][0] + board [1][1] + board [2][2]
    if 'xx ' in left_diagonal:
      x_win = [2, 2]
      chances += 1
    elif 'x x' in left_diagonal:
      x_win = [1, 1]
      chances += 1
    elif ' xx' in left_diagonal:
      x_win = [0, 0]
      chances += 1

    # Check if X can win by right diagonal and return x cords
    right_diagonal = board[0][2] + board[1][1] + board[2][0]
    if 'xx ' in right_diagonal:
      x_win = [2, 0]
      chances += 1
    elif 'x x' in right_diagonal:
      x_win = [1, 1]
      chances += 1
    elif ' xx' in right_diagonal:
      x_win = [0, 2]
      chances += 1
      
    if chances < 1:
      x_win = False
    
    result =[x_win, chances]
    return result

  def o_can_win(self, board):
    global o
    o = False
    # Check if O can win horizontally and return o cords
    for nr in range(0, 3):
      row = board[nr][0] + board[nr][1] + board[nr][2]
      if 'oo ' in row:
        o = [nr, 2]
      elif 'o o' in row:
        o = [nr, 1]
      elif ' oo' in row:
        o = [nr, 0]
  
    # Check if O can win vertically and return o cords
    for nr in range(0, 3):
      row = board[0][nr] + board[1][nr] + board[2][nr]
      if 'oo ' in row:
        o = [2, nr]
      elif 'o o' in row:
        o = [1, nr]
      elif ' oo' in row:
        o = [0, nr]
  
    # Check if o can win by left diagonal and return o cords
    left_diagonal = board[0][0] + board[1][1] + board[2][2]
    if 'oo ' in left_diagonal:
      o = [2, 2]
    elif 'o o' in left_diagonal:
      o = [1, 1]
    elif ' oo' in left_diagonal:
      o = [2, 2]
  
    # Check if o can win by right diagonal and return o cords
    right_diagonal = board[0][2] + board[1][1] + board[2][0]
    if 'oo ' in right_diagonal:
      o = [2, 0]
    elif 'o o' in right_diagonal:
      o = [1, 1]
    elif ' oo' in right_diagonal:
      o = [0, 2]
  
    return o

  def x_can_fork(self, board):
    fork_x = False
    future_board = board
    for i in range(0, 3):
      for j in range(0,3):
        print('i: ' + str(i) + ' j: ' + str(j))
        if ' ' in future_board[i][j]:
          for line in future_board:
            print(line)
          print('Puste: ' + str(i) + ' ' + str(j))
          future_board[i][j] = 'x'
          if self.x_can_win(future_board)[1] > 1:
            fork_x = [i, j]
            future_board[i][j] = ' '
            print(str(fork_x) + ' xxx')
            return fork_x
          else:
            fork_x = False
            future_board[i][j] = ' '
    print(fork_x)
    return fork_x

  def o_win(self, board):
    # Check if O win horizontally
    for nr in range(0, 3):
      row = board[nr][0] + board[nr][1] + board[nr][2]
      if 'ooo' in row:
        return True
  
    # Check if O win vertically
    for nr in range(0, 3):
      column = board[0][nr] + board[1][nr] + board[2][nr]
      if 'ooo' in column:
        return True
  
    # Check if O win diagonally
    if 'o' in board[1][1]:
      if 'o' in board[0][0] and 'o' in board[2][2]:
        return True
      elif 'o' in board[0][2] and 'o' in board[2][0]:
        return True
      
    return False
