from game import Game 
from player import Player 
import os
import platform
from error import OccupiedPositionError

if __name__ == '__main__':

	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')

	player1_name = input('Player 1: ')
	player2_name = input('Player 2: ')

	player1 = Player(player1_name, 'O')
	player2 = Player(player2_name, 'X')

	game = Game()

	finish = False
	turn = 1

	while(not finish):
		if turn: #player 1 turn
			try:
				print('\n{} make your move'.format(player1.get_name())) 
				row = int(input('Row: '))
				col = int(input('Col: '))
				game.move(row, col, player1)
				game.display()
				win = game.check_win(player1)
				if win:
					print(player1.get_name(), ' Win!!')
					finish = True
				turn = not turn
			except ValueError:
				print('\n[Row and Col must be a integer.]')
				print('[Play again.]')
			except IndexError:
				print('\n[Valid indexes (0,1,2).]')
				print('[Play again.]')
			except OccupiedPositionError:
				print('\n[Position is already occupied.]')
				print('[Play again.]')

		else: #player 2 turn
			try:
				print('\n{} make your move'.format(player2.get_name()))
				row = int(input('Row: '))
				col = int(input('Col: '))
				game.move(row, col, player2)
				game.display()
				win = game.check_win(player2)
				if win:
					print(player2.get_name(), ' Win!!')
					finish = True
				turn = not turn
			except ValueError:
				print('\n[Row and Col must be a integer.]')
				print('[Play again]')
			except IndexError:
				print('\n[Valid indexes (0,1,2).]')
				print('[Play again]')
			except OccupiedPositionError:
				print('\n[Position is already occupied.]')
				print('[Play again.]')


