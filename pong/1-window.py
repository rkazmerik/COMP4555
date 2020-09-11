import pygame, sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

# Game Loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	pygame.display.flip()
	clock.tick(60) #redraws the screen every 0.6ms