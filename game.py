import pygame
import time
pygame.init()

screen_height = 400
screen_width = 500
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
drawn = False

#make the player:
surf = pygame.Surface((10, 50))
surf.fill((255, 255, 255))
surf.set_colorkey((255,0,0))


screen.fill((40, 40, 40))


def jump():
	ycoord = screen_height - 50
	
	for i in range(1,2500,1):
		screen.fill((40, 40, 40))
		ycoord = (ycoord**0.9997)
		screen.blit(surf, (200,(ycoord)))
		
		print(ycoord)
		pygame.display.flip()
		
	for i in range(1,2500,1):
		screen.fill((40, 40, 40))
		ycoord = (ycoord**1.0003)		
		screen.blit(surf, (200,(ycoord)))
		
		print(ycoord)
		pygame.display.flip()
		
	



while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = False
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_SPACE]:
		print("jump!")
		jump()
	
	blitted_player = screen.blit(surf, ( (screen_width/2) , screen_height))
	
	#jump()

		


	pygame.display.flip()
	