import pygame
import sys
import random

# Pygame Variables
pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

# Game Variables
gravity = 0.25 
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

# Pipes
pipe_surface = pygame.image.load('./assets/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface) #draw the pipe on the bird surface
pipe_list = []

SPAWNPIPE = pygame.USEREVENT #create a new event for adding a pipe
pygame.time.set_timer(SPAWNPIPE, 1200) #create a timer for 1.2s
pipe_height = [400,600,800]


def draw_floor():
  screen.blit(floor_surface, (floor_x_pos,900))
  screen.blit(floor_surface, (floor_x_pos + 576 ,900)) 

def create_pipe(): #create a new pipe
  randome_pipe_pos = random.choice(pipe_height) #choose a random pipe height
  bottom_pipe = pipe_surface.get_rect(midtop = (700, randome_pipe_pos))
  top_pipe = pipe_surface.get_rect(midbottom = (700, randome_pipe_pos-300))
  
  return top_pipe, bottom_pipe #return the tuple of both pipes

def move_pipes(pipes):
  
  for pipe in pipes: #move each pipe to the left by 5px
    pipe.centerx -= 5
  
  return pipes

def draw_pipes(pipes): #draw each pipe on the screen
  
  for pipe in pipes:
    
    if pipe.bottom > 1024: 
      screen.blit(pipe_surface, pipe)
    else: #flip the pipe image
      flip_pipe = pygame.transform.flip(pipe_surface, False, True)
      screen.blit(flip_pipe, pipe)

      
# Game Loop
while True:

  # Events Loop
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        bird_movement == 0
        bird_movement -= 12

    if event.type == SPAWNPIPE: #detect new pipe event
      pipe_list.extend(create_pipe())

  # Surfaces
  screen.blit(bg_surface, (0,0))

  # Floor Movement
  floor_x_pos -= 1
  draw_floor()

  # Bird Movement
  bird_movement += gravity
  bird_rect.centery += bird_movement
  screen.blit(bird_surface, bird_rect)

  # Pipe Movement
  pipe_list = move_pipes(pipe_list)
  draw_pipes(pipe_list)

  if floor_x_pos <= -576:
    floor_x_pos = 0
  
  # Updating Display
  pygame.display.update()
  clock.tick(120)