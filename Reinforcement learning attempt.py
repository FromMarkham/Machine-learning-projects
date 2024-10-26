#https://www.youtube.com/watch?v=cO5g5qLrLSo
import gym 
import tensorflow 
import keras 
import random
import numpy as np 

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy 
from rl.memory import SequentialMemory

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam 

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


    
def my_neural_network(states,actions):
    agent_cozmo=Sequential()

    agent_cozmo.add(Flatten(input_shape=(1,states)))
    agent_cozmo.add(Dense(125,activation='relu'))
    agent_cozmo.add(Dense(125,activation='sigmoid'))
    agent_cozmo.add(Dense(125,activation='relu'))
    agent_cozmo.add(Dense(125,activation='sigmoid'))
    agent_cozmo.add(Dense(actions,activation='linear'))

    return agent_cozmo
    
definetly_not_a_robot_player=my_neural_network(states,actions)
definetly_not_a_robot_player.summary()
