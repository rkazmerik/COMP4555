import pygame
import sys

# Pygame Variables
pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

# Game Variables
gravity = 0.25 #specify how much gravity to apply to the bird
bird_movement = 0

# Background
bg_surface = pygame.image.load('./assets/background-day.png').convert() 
bg_surface = pygame.transform.scale2x(bg_surface)

# Floor
floor_surface = pygame.image.load('./assets/base.png')
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

# Bird
bird_surface = pygame.image.load('./assets/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,512)) #add a rect object for the bird


def draw_floor():
  screen.blit(floor_surface, (floor_x_pos,900))
  screen.blit(floor_surface, (floor_x_pos + 576 ,900)) 

# Game Loop
while True:

  # Events Loop
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN: #detect space bar press
      if event.key == pygame.K_SPACE:
        bird_movement == 0 #make the bird jump on space
        bird_movement -= 12

  # Surfaces
  screen.blit(bg_surface, (0,0))

  bird_movement += gravity #animate the bird downward
  bird_rect.centery += bird_movement #assign the center to the new value

  screen.blit(bird_surface, bird_rect) #draw the bird rect

  floor_x_pos -= 1
  draw_floor()

  if floor_x_pos <= -576:
    floor_x_pos = 0
  
  # Updating Display
  pygame.display.update()
  clock.tick(120)