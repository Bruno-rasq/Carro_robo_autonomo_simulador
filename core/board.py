import random
from typing import List
from sources.boards import EXAMPLE_BOARDS
from sources.globals import board_cells_config


# classe Board gerencia os estados do board e suas peças(celulas) suas 
# estados:
#   1 -> célula acessível
#   2 -> posição do robô
#   3 -> célula já visitada (marcada como vazia na exibição) 
#   0 -> célula não acessível.
class Board:
    def __init__(self):
        self.board = self.get_random_board()

    def get_random_board(self) -> List[List[int]]:
        size = len(EXAMPLE_BOARDS)
        idx = random.randint(0, 60) % size
        return EXAMPLE_BOARDS[idx]

    def get_board(self) -> List[List[int]]:
        return self.board

    def set_robot_position(self, coord_x: int, coord_y: int) -> None:
        self.board[coord_x][coord_y] = 2

    def clear_prev_robot_position(self, coord_x: int, coord_y: int) -> None:
        self.board[coord_x][coord_y] = 3

    def define_cell(self, cell: int) -> str:
        return board_cells_config[cell]

    def print_board_state(self):
        for row in self.board:
            for cell in row:
                print(self.define_cell(cell), end="")
            print()