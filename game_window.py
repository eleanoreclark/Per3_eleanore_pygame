import pygame

screen_width = 640
screen_height = 480

upper_left = (0,0)
lower_left = (0, screen_height)
lower_right = (screen_width,screen_height)
upper_right = (screen_width,0)

vertical_center = (screen_width/2)
horizontal_center = (screen_height/2)


red = (255, 0, 0)
blue = (100, 100, 200)
black = (0,0,0)
white = (255,255,255)


####################################################################

screen = pygame.display.set_mode([screen_width, screen_height])

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
	
	screen.fill(white)
	pygame.draw.line(screen, red, upper_left, lower_right)
	pygame.draw.aaline(screen, blue, upper_right, lower_left)
	
	
	pygame.draw.line(screen,black,(vertical_center,0),(vertical_center,screen_height))
	
	
	pygame.display.flip()