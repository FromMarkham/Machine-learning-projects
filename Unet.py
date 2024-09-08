import numpy as np

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_examples.models.pix2pix import pix2pix

from IPython.display import clear_output
import matplotlib.pyplot as plt
dataset, info = tfds.load('oxford_iiit_pet:3.*.*', with_info=True)

Unet=models.Sequential()
x=layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3)
x=layers.ZeroPadding2D(x)
Unet.add(layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3))

Unet.add(layers.ZeroPadding2D)
Unet.add(layers.MaxPool2D)
Unet.add(layers.MaxPool2D)
Unet.add(layers.Concatenate())
Unet.add(layers.UpSampling2D)

#https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/
#https://www.tensorflow.org/tutorials/images/segmentation
#https://tree.rocks/make-diffusion-model-from-scratch-easy-way-to-implement-quick-diffusion-model-e60d18fd0f2e#:~:text=%23%20%2D%2D%2D%2D%2D%20right%20(%20up%20)%20%2D%2D%2D%2D%2D%0A%20%20%20%20x%20%3D%20layers.Concatenate()(%5Bx%2C%20x4%5D)%0A%20%20%20%20x%20%3D%20block,x16%5D)%0A%20%20%20%20x%20%3D%20block(x%2C%20x_ts)%0A%20%20%20%20x%20%3D%20layers.UpSampling2D(2)(x)
