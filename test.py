import gym
from make_env import *

# env = gym.make()
env = make_env('simple_tag')
for i_episode in range(20):
    observation = env.reset()
    for t in range(10000):
        env.render()
        print(observation)
        #action = env.action_space.sample()
        #env.step(observation)

env.close()
