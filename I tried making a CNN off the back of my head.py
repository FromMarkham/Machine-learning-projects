import tensorflow as tf 
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt 

(train_images,train_labels),(test_images, test_labels)=datasets.cifar10.load_data()

train_images,test_images=train_images/255.0,test_images/255.0
#https://www.tensorflow.org/tutorials/images/cnn

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

cnn_model=models.Sequential()
cnn_model.add(layers.Conv2D())
cnn_model.add(layers.MaxPool2D())
cnn_model.add(layers.Conv2D)
cnn_model.add(layers.MaxPool2D())

cnn_model.add(layers.Flatten())
cnn_model.add(layers.Dense())
cnn_model.add(layers.Dense())
