import numpy as np

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_examples.models.pix2pix import pix2pix

from IPython.display import clear_output
import matplotlib.pyplot as plt
dataset, info = tfds.load('oxford_iiit_pet:3.*.*', with_info=True)

def UnetEncoder():
    x=layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3)
    x=layers.ZeroPadding2D()(x)
    x=layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3))(x)

    x=layers.ZeroPadding2D()(x)
    x=layers.MaxPool2D()(x)
    x=layers.MaxPool2D()(x)
    x=layers.Concatenate()(x)


def UnetDecoder():
    y=layers.Conv2DTranspose()

    
#https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/
#https://www.tensorflow.org/tutorials/images/segmentation
#https://medium.com/geekculture/u-net-implementation-from-scratch-using-tensorflow-b4342266e406
#tree.rocks/make-diffusion-model-from-scratch-easy-way-to-implement-quick-diffusion-model-e60d18fd0f2e
