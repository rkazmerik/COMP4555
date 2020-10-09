import random

ball_speeds = list(range(5,30,5)) # start the game with a variable ball speed in steps of 5

def get_ball_speed():

  speed = ball_speeds[random.randint(0, 4)] * random.choice((1,-1))

  return speed