import pygame
line_y = 0
velocity = .25
running = 1
barheight = 1000
screen = pygame.display.set_mode((800, 600));
 
barcolor = []
for i in range(1, int(barheight/2)+1):
	barcolor.append((0, 0, i*4))
for i in range(1, int(barheight/2)+1):
    barcolor.append((0, 0, 255 - i*4))
	

 
while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0

	screen.fill((0, 0, 0))
	for i in range(0, int(barheight/2)):
		pygame.draw.line(screen, barcolor[i], (0, line_y+i), (799, line_y+i))

	line_y += velocity
	if line_y + int(barheight/2) > 599 or line_y < 0-int(barheight/2):
		velocity *= -1

	pygame.display.flip()
