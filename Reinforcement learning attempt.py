#https://www.youtube.com/watch?v=cO5g5qLrLSo
import gym 
import tensorflow 
import keras 
import random

environment=gym.make('CartPole-v1')

states=environment.observation_space.shape[0]
actions=environment.action_space.n

states
actions

environment.reset()
environment.render()
