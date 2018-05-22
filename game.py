import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
running = True
drawn = False

up_velo = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = False



	screen.fill((40, 40, 40))
	
	
	surf = pygame.Surface((10, 50))
	surf.fill((255, 255, 255))
	surf.set_colorkey((255,0,0))
	
	blitted_player = screen.blit(surf, (200,up_velo))
	
	for i in range (1,10):
		up_velo = (100 - (i*i) )
		if up_velo > 360:
			up_velo = 0

	pygame.display.flip()
	