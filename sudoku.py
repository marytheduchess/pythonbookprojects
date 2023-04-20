import pygame
pygame.font.init()
Window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("SUDOKU GAME")
x = 0
z =0
diff = 500 / 9
value = 0
defaultgrid = [
        [0, 0, 4, 0, 6, 0, 0, 0, 5],
        [7, 8, 0, 4, 0, 0, 0, 2, 0],
        [0, 0, 2, 6, 0, 1, 0, 7, 8],
        [6, 1, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 7, 5, 4, 0, 0, 6, 1],
        [0, 0, 1, 7, 5, 0, 9, 3, 0],
        [0, 7, 0, 3, 0, 0, 0, 1, 0],
        [0, 4, 0, 2, 0, 6, 0, 0, 7],
        [0, 2, 0, 0, 0, 7, 4, 0, 0],
        
     ]
     
font = pygame.font.SysFont("timesnewroman", 40)
font1 = pygame.font.SysFont("timesnewroman", 20)

	def cord(pos):
		global x
		x = pos[0]//diff
		global z
		z = pos[1]//diff
		
	def highlightbox():		#highlights cell selected by the user
		for k in range(2):
			pygame.draw.line(Window, (0, 0, 0), (x * diff-3, (z + k)*diff),
	(x * diff + diff + 3, (z + k)*diff), 7) 
			pygame.draw.line(Window, (0, 0, 0), ( (x + k)*diff, z * diff), ((x + k) *
	diff, z * diff), ((x + k) * diff, z * diff + diff), 7)
	
	#function for drawing lines for making sudoku grid
	def drawlines():
		for i in range (9):
			for j in range (9):
				if defaultgrid[i][j]!= 0:
					pygame.draw.rect(Window, (255, 255, 0), 
			(i * diff, j * diff, diff, + 1, diff + 1))
					text1 = font.render(str(defaultgrid[i][j])), 1, (0, 0, 0))
					Window.blit(text1, (i * diff + 15, j * diff + 15))
		for 1 in range(10):
			if 1 % 3 == 0:
				thick = 7
			else:
				thick = 1 
