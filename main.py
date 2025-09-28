import os
import time

from core.board import Board
from core.robot import Robot
from core.pathfinder import get_next_coord


BOARD 	= Board.get_random_board()
ROBOT 	= Robot(0, 1, "D")
TIMEOUT = 0.6


def auto_follow():
	while True:
		os.system("clear")
		
		Rx, Ry = ROBOT.get_coord() 
		x, y = get_next_coord(BOARD, Rx, Ry)
	
		if x == y == -1: break
	
		BOARD[Rx][Ry] = 3
		BOARD[x][y] = 2
	
		ROBOT.set_coord(x, y)
	
		Board.print_board_state(BOARD)
		print(f"curr coord: {x}:{y}")
		time.sleep(TIMEOUT)
	


auto_follow()