import numpy as np

from tqdm.auto import trange, tqdm
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow.keras import layers

#https://tree.rocks/make-diffusion-model-from-scratch-easy-way-to-implement-quick-diffusion-model-e60d18fd0f2e
#This is my first generative ML model

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.cifar10.load_data()
X_train = X_train[y_train.squeeze() == 1]
X_train = (X_train / 127.5) - 1.0

Image_size=32
Batch_size=128
Timesteps=16
Diffusion_schedule=np.linspace(0, 1.0, Timesteps + 1) #Linear variance scheldule 

def generate_ts(num):
    return np.random.randint(0, Timesteps, size=num)



t=generate_ts(25)
np.asarray(t)
t.astype(int)



def Forward_process(t,x):
    a=Diffusion_schedule[t]
    b=Diffusion_schedule[t+1]
    noise=np.random.normal(size=x.shape)
    
    a=a.reshape((-1,1,1,1))
    b=b.reshape((-1,1,1,1))

    Imagea=x*(1-a)+noise
    Imageb=x*(1-b)+noise*b

    return Imagea, Imageb
    

    

a, b = Forward_process(X_train[:25].astype(int), t)

def denoisingp1(noised_img1,noised_img2):
    img1layer=layers.Conv2D(32,32,kernel_size=3,padding='same')(noised_img1)
    img1layer=layers.Activation('relu')(img1layer)

    img2layer=layers.Dense(128)(noised_img2)
    img2layer=layers.Activation('relu')(img2layer)
    img2layer=layers.Reshape((1,1,128))(img2layer)
    
    img3layer=img2layer*img1layer

    img_out=layers.Conv2D(128,kernel_size=3,padding='same')(noised_img1)
    img_out=img_out+img1layer

    img_out=layers.LayerNormalization()(img_out)
    img_out=layers.Activation('relu')(img_out)
    
    return img_out


def mostofthemodel():
    x=

#def Forward_process(x,t);
