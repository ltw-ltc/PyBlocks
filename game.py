# install pygame via pip install pygame in cmd
# use the internet for help - Keith Galli on Youtube

import pygame
import sys
import random

pygame.init()
# called when an object is created from a class and
# it allows the class to initialize the attributes
# of the class

WIDTH = 800 
HEIGHT = 600
# Size of window

PLAYER_SIZE = 50
PLAYER_POS = (WIDTH/2, HEIGHT-2*PLAYER_SIZE)
# Player block initialization

ENEMY_SIZE = 50
ENEMY_POS = [random.randint(0, WIDTH-ENEMY_SIZE),0]




RED = (255,0,0)
BLUE = (0,0,255)
BACKGROUND_COLOR = (0,0,0)


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) 
# in pixels

game_over = False 

clock = pygame.time.Clock()
# frames/sec
SPEED = 10
# speed of enemy block

def detect_collision(PLAYER_POS, ENEMY_POS):
	
	p_x = PLAYER_POS[0]
	p_y = PLAYER_POS[1]

	e_x = ENEMY_POS[0]
	e_y = ENEMY_POS[1]

while not game_over:

	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			sys.exit()
			# allows us to quit properly

		if event.type == pygame.KEYDOWN:

			x = PLAYER_POS[0]
			y = PLAYER_POS[1]

			if event.key == pygame.K_LEFT:
				x -= PLAYER_SIZE
				# move X coordinate left
			elif event.key == pygame.K_RIGHT:
				x += PLAYER_SIZE
				# move X coordinate right

			PLAYER_POS = [x,y]
			# update coordinates

	SCREEN.fill((BACKGROUND_COLOR[0], BACKGROUND_COLOR[1], BACKGROUND_COLOR[2]))
	
	if ENEMY_POS[1] >= 0 and ENEMY_POS[1] <= HEIGHT:
		ENEMY_POS[1] += SPEED
		# move the enemy block downward
	else:
		ENEMY_POS[0] = random.randint(0, WIDTH-ENEMY_SIZE)
		# is off screen, move it back to zero
		ENEMY_POS[1] = 1

	pygame.draw.rect(SCREEN, BLUE, (ENEMY_POS[0], ENEMY_POS[1], ENEMY_SIZE,ENEMY_SIZE))
	
	pygame.draw.rect(SCREEN, RED, (PLAYER_POS[0], PLAYER_POS[1], PLAYER_SIZE, PLAYER_SIZE))
	# takes in surface, color, rectangle dimensions

	clock.tick(30)
	#

	pygame.display.update()
	# refresh the screen


