# Game 3 : Flappy Bird
* How is the screen motion different in this game?
* What is the challenge in Flappy Bird?

## 1-window.py
* initialize pygame
* create the main screen
* create the game loop

## 2-surfaces.py
? How can we create the illusion of a moving floor ?
* create background & floor surfaces
* animate floor surface
* recycle floor surface

## 3-bird.py
? What pygame events will we listen for on the bird ?
* create bird rect
* add gravity factor
* add bird jumping

## 4-pipes.py
* draw & animate pipes
* spawn new pipes
* flip pipes

## 5-collisions.py
? What types of collisions do we need to consider?
* detect bird collision with pipe
* detect bird collision with screen boundaries
* add collision detection to our game loop

## 6-state.py
* end game on pipe collision
* end game on boundary collision
* allow user to restart the game

## 7-rotation.py
* import bird on a surface
* rotate bird on another surface
* blit the rotated bird surface

## 8-score.py
* create a font
* add current score
* add high score

## 9-over.py
* create game over surface
* create game over rect
* draw game over on screen

## 10-sound.py
* load game sounds
* initialize the pygame mixer
* trigger sounds in loop