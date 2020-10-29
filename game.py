from player import Player #only to use as type hint in check function
from error import OccupiedPositionError

class Game(Exception):

	def __init__(self, board=None):
		self.board = board or [
			[' ', ' ', ' '],
			[' ', ' ', ' '],
			[' ', ' ', ' ']
		]

	def move(self, row: int, col: int , player: Player) -> None:
		if self.board[row][col] != ' ':
			raise OccupiedPositionError()
		else:
			if player.get_symbol() == 'O':
				self.board[row][col] = 'O'
			else:
				self.board[row][col] = 'X'

	def check_win(self, player: Player) -> bool:
		symbol = player.get_symbol()
		primary_diagonal = 0
		secondary_diagonal = 0
		for i in range(0, 3):
			row = 0
			col = 0
			for j in range(0, 3):
				if self.board[i][j] == symbol:
					row += 1
				if self.board[j][i] == symbol:
					col += 1
				if i == j and self.board[i][j] == symbol:
					primary_diagonal += 1
				if j == (2 - i) and self.board[i][j] == symbol:
					secondary_diagonal += 1
			if row == 3 or col == 3 or primary_diagonal == 3 or secondary_diagonal == 3:
				return True
		return False

	def display(self) -> None:
		print('\n')
		list(map(print,self.board))
		print('\n')
		


