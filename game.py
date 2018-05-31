import pygame
import time
pygame.init()

screen_height = 400
screen_width = 500
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
drawn = False

#make the player:
player_height = 30
jump_height = 300


surf = pygame.Surface((10, player_height))
surf.fill((255, 255, 255))
surf.set_colorkey((255,0,0))


screen.fill((40, 40, 40))


def jump():
	current_coord = screen_height - player_height
	velocity = .2
	
	screen.blit(surf, (int(screen_width/2), current_coord) ) 
	

	for i in range(1,3000,1):
		screen.fill((40, 40, 40))
		
		velocity = (velocity*.999)
		current_coord -= velocity
		screen.blit(surf, ( int(screen_width/2), current_coord ))
	
		pygame.display.flip()
		
		
	for i in range(1,3000,1):
		screen.fill((40, 40, 40))
		
		velocity = (velocity*1.001)
		current_coord += velocity	
		screen.blit(surf, ( int(screen_width/2), current_coord ))
	
		pygame.display.flip()
		
	

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = False
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_SPACE]:
		print("jump!")
		jump()
	
	screen.blit(surf, ( (screen_width/2) , screen_height))

	pygame.display.flip()
	