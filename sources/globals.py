# controlador de time
TIMEOUT = 0.6

# Definindo as cores ANSI
RESET = "\033[0m"
LIGHT_BLUE = "\033[94m"
DARK_BLUE = "\033[34m"
YELLOW = "\033[93m"


board_cells_config = {
	0: f"{LIGHT_BLUE}{'#'}{RESET}",
	1: f"{DARK_BLUE}{'.'}{RESET}",
	2: f"{YELLOW}{'X'}{RESET}",
	3: f"{DARK_BLUE}{'.'}{RESET}",
}

#deslocamentos grid: esquerda, direita, cima, baixo
DELTA_MOVE = [(0, -1), (0, 1), (-1, 0), (1, 0)]