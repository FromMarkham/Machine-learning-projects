#https://www.youtube.com/watch?v=cO5g5qLrLSo
import gym 
import tensorflow 
import keras 
import random
import numpy as np 


environment=gym.make('CartPole-v1')

states=environment.observation_space.shape[0]
actions=environment.action_space.n

#states
#actions
#def the_model():

episodes=10

for i in range(episodes+1)

    currentState=environment.reset()

    while not done:
        environment.render()
        action=random.choice([0,1])
        currentState,reward,done,miscInfo=environment.step(action)
    done=False
    environment.step(action)
