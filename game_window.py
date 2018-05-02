import pygame

screen = pygame.display.set_mode((500, 500))
running = True

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = False