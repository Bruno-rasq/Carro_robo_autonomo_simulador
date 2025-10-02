from typing import Tuple, List
from sources.globals import DELTA_MOVE


# Classe RobotCar funciona geranciando coordenadas
#	 - cada instancia inicia em uma coordenada X, Y
class RobotCar:
	def __init__(self, coordX: int, coordY: int):
		self.coord_x = coordX
		self.coord_y = coordY

	def get_coord(self) -> Tuple[int, int]: 
		return (self.coord_x, self.coord_y)

	def set_coord(self, x: int, y: int) -> None:
		self.coord_x = x
		self.coord_y = y

	def get_next_coord(self, board: List[List[int]]) -> Tuple[int, int]:
		
		for dx, dy in DELTA_MOVE:
			nx, ny = dx + self.coord_x, dy + self.coord_y

			if 0 <= nx < len(board) and 0 <= ny < len(board[0]) \
			and board[nx][ny] == 1:
				return (nx, ny)

		return (-1, -1)


# classe robot car with direction herda da classe robot car
# com a diferença da limitação do carro (comandos) e seu sentido
# 	= carro só pode se mover para frente, ou girar 90 graus.
# 	= sentido / direcao indica para qual lado ele vai se deslocar
# 	ao andar para frente.

class RobotCarWithDirection (RobotCar): 
	def __init__(self, x: int, y: int, direction: str):
		self.coord_x = x
		self.coord_y = y
		self.direction = direction
	
	def get_direction(self) -> str: 
		return self.direction

	def set_direction(self, direction: str) -> None: 
		self.direction = direction