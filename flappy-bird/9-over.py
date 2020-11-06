import pygame
import sys
import random

# Pygame Variables
pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()
game_font = pygame.font.Font('./fonts/04B_19.ttf', 40)

# Game Variables
gravity = 0.25 
bird_movement = 0
game_active = True
score = 0
high_score = 0 

# Background
bg_surface = pygame.image.load('./assets/background-day.png').convert() 
bg_surface = pygame.transform.scale2x(bg_surface)

# Floor
floor_surface = pygame.image.load('./assets/base.png')
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

# Bird
bird_surface = pygame.image.load('./assets/bluebird-midflap.png').convert_alpha()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,512))

# Pipes
pipe_surface = pygame.image.load('./assets/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface) 
pipe_list = []

SPAWNPIPE = pygame.USEREVENT 
pygame.time.set_timer(SPAWNPIPE, 1200) 
pipe_height = [400,600,800]

game_over_surface = pygame.transform.scale2x(pygame.image.load('./assets/message.png').convert_alpha()) #load the game over image
game_over_rect = game_over_surface.get_rect(center = (288, 512)) #convert to a rect

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
      return False 

  if bird_rect.top <= -100 or bird_rect.bottom >= 900:
    return False

  return True


def rotate_bird(bird):

  new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)

  return new_bird


def score_display(game_state): 
  if game_state == "main_game":
    score_surface = game_font.render(str(int(score)), True, (255,255,255))
    score_rect = score_surface.get_rect(center=(288, 100)) 
    screen.blit(score_surface, score_rect) 
  
  if game_state == "game_over":
    score_surface = game_font.render(f"Score: {int(score)}", True, (255,255,255))
    score_rect = score_surface.get_rect(center=(288, 100)) 
    screen.blit(score_surface, score_rect) 

    high_score_surface = game_font.render(f"High Score: {int(high_score)}", True, (255,255,255)) 
    high_score_rect = high_score_surface.get_rect(center=(288, 850)) 
    screen.blit(high_score_surface, high_score_rect)


def update_score(score, high_score):
  
  if score > high_score:
    high_score = score
  
  return high_score

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

      if event.key == pygame.K_SPACE and game_active == False: 
        game_active = True
        pipe_list.clear() 
        bird_rect.center = (100, 512) 
        bird_movement = 0 
        score = 0 


    if event.type == SPAWNPIPE: 
      pipe_list.extend(create_pipe())

  # Surfaces
  screen.blit(bg_surface, (0,0))

  # Floor Movement
  floor_x_pos -= 1
  draw_floor()

  if game_active: 

    # Bird Movement
    bird_movement += gravity
    rotated_bird = rotate_bird(bird_surface)
    bird_rect.centery += bird_movement
    screen.blit(rotated_bird, bird_rect)
    game_active = check_collision(pipe_list) 

    # Pipe Movement
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # Scoreboard
    score += 0.01 
    score_display("main_game") 

  else:
    screen.blit(game_over_surface, game_over_rect) #draw the game over on the screen
    high_score = update_score(score, high_score) 
    score_display("game_over") 

  if floor_x_pos <= -576:
    floor_x_pos = 0
  
  # Updating Display
  pygame.display.update()
  clock.tick(120)