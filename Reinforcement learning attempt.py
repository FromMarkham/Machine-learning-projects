#https://www.youtube.com/watch?v=cO5g5qLrLSo
import gym 
import tensorflow 
import keras 
import random
import numpy as np 

from tensorflow.keras.models import sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import adam 

environment=gym.make('CartPole-v1')

states=environment.observation_space.shape[0]
actions=environment.action_space.n

#states
#actions
#def the_model():

episodes=10

for i in range(episodes+1):
    score=0;
    currentState=environment.reset()
    done=False
    
    while not done:
        environment.render()
        action=random.choice([0,1])
        kkk,n_state,reward,done,info=environment.step(action)
        score+=reward


    print('i:{} score:{}',(i,score))


    
def my_neural_network():
    

    
