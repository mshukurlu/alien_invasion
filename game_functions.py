import sys

import pygame 


def check_events(ship):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
	
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
			#	ship.rect.centerx +=1
				ship.moving_right = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False			
def update_screen(ai_settings,screen,ship):
	"""Update images on the screen and flip to the new scree."""
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	pygame.display.flip()		
		
