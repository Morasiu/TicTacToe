import random

from x_algorythm import X


class Tic:
  def print_board(self):
    print(' ' + board[0][0] + '|' + board[0][1] + '|' + board[0][2] + '\n',
          '-----\n',
          board[1][0] + '|' + board[1][1] + '|' + board[1][2] + '\n',
          '-----\n',
          board[2][0] + '|' + board[2][1] + '|' + board[2][2] + '\n\n',
          '~~~~~\n')
    # pass

  def coin_flip(self):
    rand = random.randint(0, 2)
    return rand
  
  def o_win(self):
    # Check if o win horizontally
    for nr in range(0, 3):
      row = board[nr][0] + board[nr][1] + board[nr][2]
      if 'ooo' in row:
        return True
  
    # Check if o win vertically
    for nr in range(0, 3):
      column = board[0][nr] + board[1][nr] + board[2][nr]
      if 'ooo' in column:
        return True
  
    # Check if o win diagonally
    if 'o' in board[1][1]:
      if 'o' in board[0][0] and 'o' in board[2][2]:
        return True
      elif 'o' in board[0][2] and 'o' in board[2][0]:
        return True
    
    return False
  
  def get_rand_o(self, board):
    o = [0, 0]
    if not self.o_win():
      while True:
        o[0] = random.randint(0, 2)
        o[1] = random.randint(0, 2)
        
        if(board[o[0]][o[1]]) == " ":
          break
        elif "' '" not in str(board):
          o = False
          break
    else:
      o = True
    return o
    
if __name__ == '__main__':
  tic = Tic()
  x = X()
  print()
  
  who_start = 0
  x_win = 0
  o_win = 0
  draw = 0
  
  for z in range(0, 1):
    # who_start = tic.coin_flip() # if 1, them X has first move
    who_start = 0
    
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    
    if who_start:
      # print("X starts\n")
      while True:
        x_cords = x.get_x(board) #1st is X, 2nd is Y
        if x_cords == 'x_win':
          # print('!!!X WIN!!!')
          x_win += 1
          break
        elif not x_cords:
          # tic.print_board()
          # print("←X DRAW→")
          draw += 1
          break
        elif x_cords == 'o_win':
          o_win += 1
          tic.print_board()
          break
        else:
          board[x_cords[0]][x_cords[1]] = "x"
          o_cords = tic.get_rand_o(board)  # 1st is X, 2nd is Y
          if o_cords == True:
            tic.print_board()
            print('O WIN :(')
            o_win += 1
            break
          elif not o_cords:
            # tic.print_board()
            # print('←O DRAW→')
            draw += 1
            break
          board[o_cords[0]][o_cords[1]] = "o"
        
        # tic.print_board()
    else:
      print("O starts\n")
      while True:
        o_cords = tic.get_rand_o(board)  # 1st is X, 2nd is Y
        if o_cords == True:
          # print('!!!O WIN!!!')
          tic.print_board()
          o_win += 1
          break
        elif not o_cords:
          tic.print_board()
          draw += 1
          # print("←O DRAW→")
          break
        else:
          board[o_cords[0]][o_cords[1]] = "o"
          x_cords = x.get_x(board)  # 1st is X, 2nd is Y
          if x_cords == 'x_win':
            x_win += 1
            print('X WIN :)')
            break
          elif not x_cords:
            tic.print_board()
            print('←X DRAW→')
            draw += 1
            break
          elif x_cords == 'o_win':
            print('O WIN :(')
            o_win += 1
            tic.print_board()
            break
          board[x_cords[0]][x_cords[1]] = "x"
          tic.print_board()
        
  print('\nx win: ' + str(x_win))
  print('o win: ' + str(o_win))
  print('draw:  ' + str(draw))

  # else:
  #   print("O starts")

