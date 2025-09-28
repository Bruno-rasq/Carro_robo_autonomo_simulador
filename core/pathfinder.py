from typing import List, Tuple


DELTA_MOVE = [(0, -1), (0, 1), (-1, 0), (1, 0)]


# a função in_bound é responsavel por verificar se uma coordenada
# x, y é válida, estando dentro dos limites do board em questão.
def in_bound(board: List[List[int]], nx: int, ny: int) -> bool:
	return 0 <= nx < len(board) and 0 <= ny < len(board[0])


#get adj state é o metodo que verifica as quatro celulas adjacentes
#no board dada uma coordenada x, y.  o retorno é uma string com uma
#sinalização para o saber se a celula em questão é válida para pro-
#seguir (0 = acessivel, 1= inacessivel).
def get_adj_state(board: List[List[int]], x: int, y: int) -> str:
	
	adj_state = ""
	for dx, dy in DELTA_MOVE:
		nx, ny = dx + x, dy + y 

		verify = in_bound(board, nx, ny) and board[nx][ny] == 1
		adj_state += "0" if verify else "1"

	return adj_state


#get next coord retorna a unica coordenada valida para proseguir
#o caminho, retorna (-1, -1) quando não for possivel seguir.
def get_next_coord(board: List[List[int]], x: int, y: int) -> Tuple[int, int]:

	for dx, dy in DELTA_MOVE:
		nx, ny = dx + x, dy + y

		if in_bound(board, nx, ny) and board[nx][ny] == 1:
			return (nx, ny)
			
	return (-1, -1)