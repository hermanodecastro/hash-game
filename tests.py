import unittest
from game import Game 
from player import Player 

class GameTest(unittest.TestCase):

	def test_player_win_first_row(self):
		player = Player('Player', 'X')
		board = [
			['X', 'X', 'X'],
			['O', 'O', 'X'],
			['X', 'O', 'O']
		]
		game = Game(board)
		self.assertEqual(True, game.check_win(player), 'Win first row fail')

	def test_player_win_second_row(self):
		player = Player('Player', 'X')
		board = [
			['X', 'O', 'O'],
			['X', 'X', 'X'],
			['O', 'X', 'O']
		]
		game = Game(board)
		self.assertEqual(True, game.check_win(player), 'Win second row fail')

	def test_player_win_third_row(self):
		player = Player('Player', 'X')
		board = [
			['O', 'O', 'X'],
			['X', 'O', 'O'],
			['X', 'X', 'X']
		]
		game = Game(board)
		self.assertEqual(True, game.check_win(player), 'Win third row fail')

	def test_player_win_first_col(self):
		player = Player('Player', 'X')
		board = [
			['X', 'O', 'X'],
			['X', 'O', 'O'],
			['X', 'X', 'O']
		]
		game = Game(board)
		self.assertEqual(True, game.check_win(player), 'Win first col fail')

	def test_player_win_second_col(self):
		player = Player('Player', 'X')
		board = [
			['O', 'X', 'X'],
			['X', 'X', 'O'],
			['O', 'X', 'O']
		]
		game = Game(board)
		self.assertEqual(True, game.check_win(player), 'Win second col fail')

	def test_player_win_third_col(self):
		player = Player('Player', 'X')
		board = [
			['X', 'O', 'X'],
			['O', 'O', 'X'],
			['O', 'X', 'X']
		]
		game = Game(board)
		self.assertEqual(True, game.check_win(player), 'Win third col fail')

	def test_player_win_principal_diagonal(self):
		player = Player('Player', 'X')
		board = [
			['X', 'O', 'X'],
			['O', 'X', 'O'],
			['O', 'O', 'X']
		]
		game = Game(board)
		self.assertEqual(True, game.check_win(player), 'Win principal diagonal fail')

	def test_player_win_secondary_diagonal(self):
		player = Player('Player', 'X')
		board = [
			['X', 'O', 'X'],
			['O', 'X', 'O'],
			['X', 'X', 'O']
		]
		game = Game(board)
		self.assertEqual(True, game.check_win(player), 'Win secondary diagonal fail')

	def test_player_not_win(self):
		player = Player('Player', 'X')
		board = [
			['X', 'O', 'X'],
			['X', 'X', 'O'],
			['O', 'X', 'O']
		]
		game = Game(board)
		self.assertEqual(False, game.check_win(player), 'Not Win fail')


if __name__ == '__main__':
	unittest.main()