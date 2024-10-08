import tensorflow as tf 
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt 

(train_images,train_labels),(test_images, test_labels)=datasets.cifar10.load_data()

train_images,test_images=train_images/255.0,test_images/255.0
#https://www.tensorflow.org/tutorials/images/cnn

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

#Conv2D.__init__() missing 2 required positional arguments: 'filters' and 'kernel_size'
cnn_model=models.Sequential()
cnn_model.add(layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3)))
cnn_model.add(layers.MaxPool2D())
cnn_model.add(layers.Conv2D(1,1))
cnn_model.add(layers.MaxPool2D())

cnn_model.add(layers.Flatten())
cnn_model.add(layers.Dense(64, activation='relu'))
cnn_model.add(layers.Dense(10))

cnn_model.compile(optimizer='Lion',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['Accuracy','BinaryAccuracy'])

train_cnn=cnn_model.fit(train_images,train_labels,epochs=10,validation_data=(test_images,test_labels))

cnn_model.summary()

#https://www.tensorflow.org/tutorials/images/cnn
