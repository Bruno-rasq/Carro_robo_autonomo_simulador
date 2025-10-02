import os
import time

from core.board import Board
from core.robot import RobotCar
from sources.globals import TIMEOUT




# função auto follow inicia uma simulação simples, usando board simples(sem obstaculos), e um robo simples
# o carrinho robo inicial no ponto 0, 0 e segue a unica trilha até chegar ao final.
def auto_follow():
	
	BOARD 	= Board()
	ROBOT 	= RobotCar(0, 0)
	
	while True:

		board = BOARD.get_board()
		current_coordx, current_coordy = ROBOT.get_coord() 
		new_coordx, new_coordy = ROBOT.get_next_coord(board)
	
		if new_coordx == new_coordy == -1: break

		BOARD.clear_prev_robot_position(current_coordx, current_coordy)
		BOARD.set_robot_position(new_coordx, new_coordy)
	
		ROBOT.set_coord(new_coordx, new_coordy)
	
		Board.print_board_state(BOARD)
		
		print(f"curr coord: {new_coordx}:{new_coordy}")
		time.sleep(TIMEOUT)
		os.system("clear")
	


auto_follow()