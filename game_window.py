import pygame

screen_width = 640
screen_height = 480

upper_left = (0,0)
lower_left = (0, screen_height)
lower_right = (screen_width,screen_height)
upper_right = (screen_width,0)


screen = pygame.display.set_mode([screen_width, screen_height])



while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
	
	screen.fill((255,230,240))
	pygame.draw.line(screen, (255, 0, 0), (upper_left), (lower_right))
	pygame.draw.aaline(screen, (100, 100, 200), (upper_right), (lower_left))
	
	
	pygame.display.flip()