import pygame
import sys

# Pygame Variables
pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

# Game Loop
while True:

  # Events Loop
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  # Updating Display
  pygame.display.update()
  clock.tick(120)