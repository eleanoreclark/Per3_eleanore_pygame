import pygame

screen = pygame.display.set_mode([640, 480])



while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
	
	screen.fill((255,230,240))
	pygame.draw.line(screen, (255, 0, 0), (0, 0), (639, 479))
	pygame.draw.aaline(screen, (100, 100, 200), (639, 0), (0, 479))
	
	
	pygame.display.flip()