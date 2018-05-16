import pygame
line_y = 0
velocity = 5
running = 1
barheight = 500
color_height = int((barheight/2)+1)
gradient_intensity = int((255/barheight)*2)
screen = pygame.display.set_mode((800, 600));
 
barcolor = []
for i in range(1, color_height):
	barcolor.append((i*gradient_intensity, 255-i*gradient_intensity, 182 ))
for i in range(1, color_height):
    barcolor.append((i*gradient_intensity, 55, (255 - i*gradient_intensity) ))
for i in range(1, color_height):
    barcolor.append((i*gradient_intensity, (255 - i*gradient_intensity), i*gradient_intensity) )
for i in range(1, color_height):
    barcolor.append(((255 - i*gradient_intensity), 212, (255 - i*gradient_intensity) ))
	
 
while running:
	event = pygame.event.poll()
	
	if event.type == pygame.QUIT:
		running = 0

	screen.fill((0, 0, 0))
	for i in range(0, int(barheight*2)):
		pygame.draw.line(screen, barcolor[i], (0, line_y+i), (799, line_y+i))

	line_y += velocity
	if line_y + int(barheight) > 300+barheight:
		line_y = 0-barheight

	pygame.display.flip()
