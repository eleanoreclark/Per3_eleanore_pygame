import pygame
line_y = 0
velocity = .1
running = 1
barheight = 124
color_height = int((barheight/2)+1)
screen = pygame.display.set_mode((800, 600));
gradient_intensity = 4

 
barcolor = []
for i in range(1, color_height):
	barcolor.append((255*gradient_intensity, 255*gradient_intensity, (i*gradient_intensity) ))
for i in range(1, color_height):
    barcolor.append((255*gradient_intensity, 255*gradient_intensity, (255 - i*gradient_intensity) ))
	
 
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
