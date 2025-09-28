from typing import Tuple


class Robot:
	def __init__(self, x: int, y: int, direction: str):
		self.coord_x = x
		self.coord_y = y
		self.direction = direction

	def get_coord(self) -> Tuple[int, int]: 
		return (self.coord_x, self.coord_y)
		
	def get_direction(self) -> str: 
		return self.direction

	def set_direction(self, direction: str) -> None: 
		self.direction = direction
		
	def set_coord(self, x: int, y: int) -> None:
		self.coord_x = x
		self.coord_y = y

	
	