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
ENEMY_LIST = [ENEMY_POS]




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

def drop_enemies(ENEMY_LIST):

	# add enemies 

	if len(ENEMY_LIST) < 10:
		x_pos = random.randint(0, WIDTH-ENEMY_SIZE)
		y_pos = 0
		ENEMY_LIST.append([x_pos, y_pos])

def draw_enemies(ENEMY_LIST):
	for ENEMY_POS in ENEMY_LIST:
		pygame.draw.rect(SCREEN, BLUE, (ENEMY_POS[0], ENEMY_POS[1], ENEMY_SIZE,ENEMY_SIZE))



def update_falling_positions(ENEMY_LIST):

	for idx,ENEMY_POS in enumerate(ENEMY_LIST):
		if ENEMY_POS[1] >=0 and ENEMY_POS[1] < HEIGHT:
		# Update on refresh
			ENEMY_POS[1] += SPEED
			# move the enemy block downward
		else: 
			ENEMY_LIST.pop(idx)


def collision_check(ENEMY_LIST, PLAYER_POS):
	for ENEMY_POS in ENEMY_LIST:
		if detect_collision(ENEMY_POS,PLAYER_POS):
			return True
	return False



def detect_collision(PLAYER_POS, ENEMY_POS):
	
	# Determining collision between enemy blocks and player block

	p_x = PLAYER_POS[0]
	p_y = PLAYER_POS[1]

	e_x = ENEMY_POS[0]
	e_y = ENEMY_POS[1]

	if (e_x >= p_x and e_x < (p_x + PLAYER_SIZE)) or (p_x >= e_x and p_x < (e_x + ENEMY_SIZE)):
		# The ways in which the X coordinate can overlap
		if (e_y >= p_y and e_y < (p_y + PLAYER_SIZE)) or (p_y >= e_y and p_y < (e_y + ENEMY_SIZE)):
			# The ways in which the Y coordinate can overlap
			return True	
	return False



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
	

	if detect_collision(PLAYER_POS, ENEMY_POS):
		game_over = True
		break
		
		# Less overlap (eliminates one update cycle)
	
	drop_enemies(ENEMY_LIST)

	update_falling_positions(ENEMY_LIST)

	if collision_check(ENEMY_LIST, PLAYER_POS):
		game_over = True
		break

	draw_enemies(ENEMY_LIST)
	
	pygame.draw.rect(SCREEN, RED, (PLAYER_POS[0], PLAYER_POS[1], PLAYER_SIZE, PLAYER_SIZE))
	# takes in surface, color, rectangle dimensions

	clock.tick(30)

	pygame.display.update()
	# refresh the screen
