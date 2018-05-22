import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
running = True
drawn = False

up_velo = 1
y_coordinate = 400

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = False



	screen.fill((40, 40, 40))
	
	
	player = pygame.Surface((10, 50))
	player.fill((255, 255, 255))
	player.set_colorkey((255,0,0))
	
	blitted_player = screen.blit(player, (200,y_coordinate))
	
	'''for i in range(1, 100):
		i += i*.01
		up_velo = (100 - (i*i) )
		y_coordinate = y_coordinate + up_velo'''

	pygame.display.flip()
	