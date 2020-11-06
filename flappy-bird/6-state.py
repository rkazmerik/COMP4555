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
game_active = True #create a game state variable

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
bird_rect = bird_surface.get_rect(center = (100,512))

# Pipes
pipe_surface = pygame.image.load('./assets/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface) 
pipe_list = []

SPAWNPIPE = pygame.USEREVENT 
pygame.time.set_timer(SPAWNPIPE, 1200) 
pipe_height = [400,600,800]


def draw_floor():
  screen.blit(floor_surface, (floor_x_pos,900))
  screen.blit(floor_surface, (floor_x_pos + 576 ,900)) 

def create_pipe(): 
  randome_pipe_pos = random.choice(pipe_height) 
  bottom_pipe = pipe_surface.get_rect(midtop = (700, randome_pipe_pos))
  top_pipe = pipe_surface.get_rect(midbottom = (700, randome_pipe_pos-300))
  
  return top_pipe, bottom_pipe

def move_pipes(pipes):
  
  for pipe in pipes:
    pipe.centerx -= 5
  
  return pipes

def draw_pipes(pipes): 
  
  for pipe in pipes:  
    if pipe.bottom > 1024: 
      screen.blit(pipe_surface, pipe)
    else: 
      flip_pipe = pygame.transform.flip(pipe_surface, False, True)
      screen.blit(flip_pipe, pipe)

def check_collision(pipes):

  for pipe in pipes:
    if bird_rect.colliderect(pipe):
      return False #end the game state

  if bird_rect.top <= -100 or bird_rect.bottom >= 900:
    return False #end the game state

  return True #continue the game state

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

      if event.key == pygame.K_SPACE and game_active == False: #detect if the game is over
        game_active = True
        pipe_list.clear() #clear out the pipes
        bird_rect.center = (100, 512) #reposition the bird
        bird_movement = 0 #reset the bird movement


    if event.type == SPAWNPIPE: 
      pipe_list.extend(create_pipe())

  # Surfaces
  screen.blit(bg_surface, (0,0))

  # Floor Movement
  floor_x_pos -= 1
  draw_floor()

  if game_active: #check for game state
    # Bird Movement
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)
    game_active = check_collision(pipe_list) #check the game state

    # Pipe Movement
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

  if floor_x_pos <= -576:
    floor_x_pos = 0
  
  # Updating Display
  pygame.display.update()
  clock.tick(120)