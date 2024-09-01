import tensorflow as tf 
import tensorflow as tf
import keras
from keras import layers

import numpy as np 
xtrain=np.ndarray([])
ytrain=np.ndarray([]) 

my_rnn=models.Sequential()
my_rnn.add(tf.keras.layers.SimpleRNN(128))


#https://www.tensorflow.org/guide/keras/working_with_rnns
