import pygame

screen_width = 640
screen_height = 480

i = 1

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
screen.fill(white)
line_height = horizontal_center

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
	
	screen.fill(white)
	
	
	line_height += i											#increase the line by i
	if (line_height == 0) or (line_height == screen_height-1):	#if the line is at the edge of the screen...
		i = i * -.25											#flip its sign of what it's increased by and make it 75% slower
		
	line1 = pygame.draw.aaline(screen, blue, (0,line_height), (screen_width-1,line_height))	#draw the line
	
	
	pygame.display.flip()