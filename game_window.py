import pygame

screen = pygame.display.set_mode([640, 480])
screen = pygame.display.set_mode([500, 50])
running = True

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = False