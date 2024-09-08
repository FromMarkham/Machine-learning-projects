import numpy as np

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_examples.models.pix2pix import pix2pix

from IPython.display import clear_output
import matplotlib.pyplot as plt
dataset, info = tfds.load('oxford_iiit_pet:3.*.*', with_info=True)

Unet=models.Sequential()
Unet.add(layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3))
Unet.add(layers.ZeroPadding2D)
Unet.add(layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3))

Unet.add(layers.ZeroPadding2D)
Unet.add(layers.MaxPool2D)
Unet.add(layers.MaxPool2D)
Unet.add(layers.Concatenate())
Unet.add(layers.UpSampling2D)

#https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/
#https://www.tensorflow.org/tutorials/images/segmentation
