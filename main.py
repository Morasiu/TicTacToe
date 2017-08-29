import random

class Tic:
	i = 1
	w = 0
	def print_board(self):
		print(' ' + board[0][0] + '|' + board[0][1] + '|' + board[0][2] + '\n',
		      '-----\n',
		      board[1][0] + '|' + board[1][1] + '|' + board[1][2] + '\n',
		      '-----\n',
		      board[2][0] + '|' + board[2][1] + '|' + board[2][2] + '\n\n',
		      '\/\/\/\/\/\/\n')

	def rand(self):
		rand = random.randint(0, 2)
		return rand

	def o(self):
		while True:
			row = self.rand()
			col = self.rand()
			if board[row][col] == ' ':
				board[row][col] = 'o'
				position = 0
				if row == 0 and col == 0:
					position = 1
				elif row == 0 and col == 1:
					position = 2
				elif row == 0 and col == 2:
					position = 3
				elif row == 1 and col == 0:
					position = 4
				elif row == 1 and col == 1:
					position = 5
				elif row == 1 and col == 2:
					position = 6
				elif row == 2 and col == 0:
					position = 7
				elif row == 2 and col == 1:
					position = 8
				elif row == 2 and col == 2:
					position = 9

				o_list.append(position)
				print("Step " + str(self.i) + '\n')
				self.print_board()
				self.i += 1
				break


	def win(self):
		self.w += 1
		self.print_board()
		print("X WIN!!!")

	def draw(self):
		self.print_board()
		print("DRAW (-_-)")

	def score(self):
		print('Win: ' + str(self.w))

if __name__ == '__main__':
	tic = Tic()
	def play():
		global board
		global o_list
		board = [[" ", " ", " "],
		         [" ", " ", " "],
		         [" ", " ", " "]]
		# who_start = random.randint(0,1)
		who_start = 1
		tic.print_board()
		o_list = []
		if who_start:
			x = board[1][1] = 'X'
			tic.o()
			if 8 not in o_list and 2 not in o_list:
				print()
				board[0][1] = 'X'
				tic.o()
				if not 8 in o_list:
					board[2][1] = 'X'
					tic.win()
					# WIN
				else:
					if 1 in o_list:
						board[2][0] = 'X'
						tic.o()
						if 3 not in o_list:
							board[0][2] = 'X'
							tic.win()
							# WIN
						else:
							board[1][2] = 'X'
							tic.o()
							if 4 not in o_list:
								board[1][0] = 'X'
								tic.win()
								# WIN
							else:
								board[2][2] = 'X'
								tic.draw()
								# DRAW
					elif 3 in o_list:
						board[2][2] = 'X'
						tic.o()
						if 1 not in o_list:
							board[0][2] = 'X'
							tic.win()
							# WIN
						else:
							board[1][0] = 'X'
							tic.o()
							if 6 not in o_list:
								board[1][2] = 'X'
								tic.win()
								# WIN
							else:
								board[2][0] = 'X'
								tic.draw()
								# DRAW
					elif 4 in o_list:
						board[2][0] = 'X'
						tic.o()
						if 3 not in o_list:
							board[0][2] = 'X'
							tic.win()
							# WIN
						else:
							board[2][2] = 'X'
							tic.o()
							if 1 not in o_list:
								board[0][0] = 'X'
								tic.win()
								# WIN
							else:
								board[1][2] = 'X'
								tic.draw()
								# DRAW
					elif 6 in o_list:
						board[2][2] = 'X'
						tic.o()
						if 1 not in o_list:
							board[0][0] = 'X'
							tic.win()
							# WIN
						else:
							board[2][2] = 'X'
							tic.o()
							if 3 not in o_list:
								board[0][2] = 'X'
								tic.win()
								# WIN
							else:
								board[1][0] = 'X'
								tic.draw()
								# DRAW
					elif 7 in o_list:
						board[2][2] = 'X'
						tic.o()
						if 1 not in o_list:
							board[0][0] = 'X'
							tic.win()
							# WIN
						else:
							board[1][0] = 'X'
							tic.o()
							if 6 not in o_list:
								board[1][2] = 'X'
								tic.win()
								# WIN
							else:
								board[0][2] = 'X'
								tic.draw()
								# DRAW
					elif 9 in o_list:
						board[2][0] = 'X'
						tic.o()
						if not 3 in o_list:
							board[0][2] = 'X'
							tic.win()
							# WIN
						else:
							board[1][2] = 'X'
							tic.o()
							if  4 not in o_list:
								board[1][0] = 'X'
								tic.win()
								# WIN
							else:
								board[0][0] = 'X'
								tic.draw()
								# DRAW
			else:
				board[0][0] = 'X'
				tic.o()
				if 9 not in o_list:
					board[2][2] = 'X'
					tic.win()
					# WIN
				else:
					board[2][0] = 'X'
					tic.o()
					if 4 not in o_list:
						board[1][0] = 'X'
						tic.win()
						# WIN
					else:
						board[0][2] = 'X'
						tic.win()
						# WIN
		else:
			tic.o()
			board[1][0] = 'X'

	play()
