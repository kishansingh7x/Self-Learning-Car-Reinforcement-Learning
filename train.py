import random
import numpy as np
import pygame
from environment import CarEnv
from dqn_model import build_model

env = CarEnv()

state_size = 2
action_size = 3

model = build_model(state_size, action_size)

epsilon = 1.0
epsilon_min = 0.01
epsilon_decay = 0.995
gamma = 0.95

episodes = 200

for episode in range(episodes):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    total_reward = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if random.random() < epsilon:
            action = random.randint(0, action_size - 1)
        else:
            action = np.argmax(model.predict(state, verbose=0))

        next_state, reward, done = env.step(action)
        next_state = np.reshape(next_state, [1, state_size])

        target = reward
        if not done:
            target += gamma * np.max(
                model.predict(next_state, verbose=0)
            )

        target_f = model.predict(state, verbose=0)
        target_f[0][action] = target

        model.fit(state, target_f, epochs=1, verbose=0)

        state = next_state
        total_reward += reward

        env.render()

        if done:
            break

    epsilon = max(epsilon_min, epsilon * epsilon_decay)
    print(f"Episode {episode} | Reward: {total_reward}")
