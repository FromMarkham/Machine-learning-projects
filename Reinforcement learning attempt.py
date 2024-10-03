#https://www.youtube.com/watch?v=cO5g5qLrLSo
import gym 
import tensorflow 
import keras 
import random
import numpy as np 

score=0
environment=gym.make('CartPole-v1')

states=environment.observation_space.shape[0]
actions=environment.action_space.n

states
actions

environment.reset()


def model():
    pass

for episode in range(1,11):

    action=random.choice([0,1])
    states=environment.reset()
    environment.render()
    score=0
    done=False
    environment.step(action)
