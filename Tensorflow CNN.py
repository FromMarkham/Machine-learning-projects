import tensorflow as tf 
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt 

(train_images,train_labels),(test_images, test_labels)=datasets.cifar10.load_data()

train_images,test_images=train_images/255.0,test_images/255.0
#https://www.tensorflow.org/tutorials/images/cnn

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

#plt.figure(figsize=(10,10))✅
#for i in range(25):
#    plt.subplot(5,5,i+1)
#    plt.xticks([])
#    plt.yticks([])
#    plt.grid(False)
#    plt.imshow(train_images[i])
    # The CIFAR labels happen to be arrays, 
    # which is why you need the extra index
#    plt.xlabel(class_names[train_labels[i][0]])
#plt.show()

bobscnn=models.Sequential()
bobscnn.add(layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3)))
bobscnn.add(layers.MaxPooling2D((2,2)))
bobscnn.add(layers.Conv2D(64,(3,3),activation='relu'))
bobscnn.add(layers.MaxPooling2D((2,2)))
bobscnn.add(layers.Conv2D(64, (3, 3), activation='relu'))

#bobscnn.summary()✅

bobscnn.add(layers.Flatten())
bobscnn.add(layers.Dense(64,activation='relu'))
bobscnn.add(layers.Dense(10))

bobscnn.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['Accuracy'])

kotsopoulos=bobscnn.fit(train_images,train_labels,epochs=10,validation_data=(test_images,test_labels))
