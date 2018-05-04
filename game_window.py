import pygame

screen = pygame.display.set_mode([640, 480])

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
	screen.fill((255,255,255))
	pygame.display.flip()