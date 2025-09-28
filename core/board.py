import random
from sources.boards import BOARDS
from typing import List



class Board:

	@staticmethod
	def get_random_board() -> List[List[int]]:
		size = len(BOARDS)
		idx = random.randint(0, 60) % size
		return BOARDS[idx]

# estados:
# 	1 -> celula acessivel
#	2 -> posicao do robo
#	3 -> celula já visitada (marcada como vazia na exibição) 
#	0 -> celula não acessivel.
	@staticmethod
	def set_cell(cell: int) -> str:
		if cell == 2: return "X"
		if cell == 3: return "_"
		return "#" if cell == 0 else "_"

	@staticmethod
	def print_board_state(board):
		for line in board:
			for cell in line: 
				print(Board.set_cell(cell), end="")
			print("\n")
		