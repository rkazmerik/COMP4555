import pygame
import sys

# Pygame Variables
pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

# Create background image
bg_surface = pygame.image.load('./assets/background-day.png').convert() #import the bg image and convert
bg_surface = pygame.transform.scale2x(bg_surface) #scale up the bg image x2

# Create moving floor
floor_surface = pygame.image.load('./assets/base.png') #import the floor surface
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

def draw_floor();
  screen.blit(floor_surface, (floor_x_pos,900)) #draw the floor on the screen
  screen.blit(floor_surface, (floor_x_pos + 576 ,900)) #draw a second floor

# Game Loop
while True:

  # Events Loop
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  # Surfaces
  screen.blit(bg_surface, (0,0)) #draw the surface on the screen
  
  floor_x_pos -= 1 #animate the floor to move
  draw_floor()

  if floor_x_pos <= -576: #redraw the floor if it reaches the edge
    floor_x_pos = 0
  
  # Updating Display
  pygame.display.update()
  clock.tick(120)