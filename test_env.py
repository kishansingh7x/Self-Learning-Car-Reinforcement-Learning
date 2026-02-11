from environment import CarEnv
import random
import pygame

env = CarEnv()
state = env.reset()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    action = random.randint(0, 2)
    state, reward, done = env.step(action)
    env.render()

    if done:
        state = env.reset()
