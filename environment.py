import pygame
import numpy as np


class CarEnv:
    def __init__(self):
        pygame.init()

        # Window settings
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Self Driving Car - Reinforcement Learning")

        self.clock = pygame.time.Clock()

        # Car settings
        self.car_width = 40
        self.car_height = 60
        self.speed = 10

        self.reset()

    # Reset environment at the start of every episode
    def reset(self):
        self.car_x = self.width // 2
        self.car_y = self.height - 80
        self.done = False
        return self.get_state()

    # State given to the neural network
    def get_state(self):
        return np.array([
            self.car_x / self.width,   # normalized x position
            self.car_y / self.height   # normalized y position
        ])

    # Apply action and return new state, reward, done
    def step(self, action):

        # Actions:
        # 0 -> move left
        # 1 -> move right
        # 2 -> move forward

        if action == 0:
            self.car_x -= self.speed
        elif action == 1:
            self.car_x += self.speed
        elif action == 2:
            self.car_y -= self.speed

        # Default reward for staying alive
        reward = 0.5

        # Penalize going close to road edges
        if self.car_x < 50 or self.car_x > self.width - 50:
            reward = -1

        # Crash condition
        if self.car_x < 0 or self.car_x > self.width:
            reward = -100
            self.done = True

        return self.get_state(), reward, self.done

    # Draw everything on the screen
    def render(self):
        self.screen.fill((25, 25, 25))  # dark background

        # Road boundaries
        pygame.draw.line(self.screen, (255, 255, 255), (50, 0), (50, self.height), 2)
        pygame.draw.line(self.screen, (255, 255, 255),
                         (self.width - 50, 0), (self.width - 50, self.height), 2)

        # Car
        pygame.draw.rect(
            self.screen,
            (0, 255, 0),
            (self.car_x, self.car_y, self.car_width, self.car_height)
        )

        pygame.display.update()
        self.clock.tick(60)
