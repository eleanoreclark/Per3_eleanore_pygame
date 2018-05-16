import pygame
line_y = 0
velocity = .1
running = 1
barheight = 124
color_height = int((barheight/2)+1)
screen = pygame.display.set_mode((800, 600));
 
barcolor = []
for i in range(1, color_height):
	barcolor.append((0, 0, (i*4) ))
for i in range(1, color_height):
    barcolor.append((0, 0, (255 - i*4) ))
	
 
while running:
	event = pygame.event.poll()
	
	if event.type == pygame.QUIT:
		running = 0

	screen.fill((0, 0, 0))
	for i in range(0, int(barheight)):
		pygame.draw.line(screen, barcolor[i], (0, line_y+i), (799, line_y+i))

	line_y += velocity
	if line_y + int(barheight) > 599+barheight:
		line_y = 0-barheight

	pygame.display.flip()
