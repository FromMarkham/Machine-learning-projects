import tensorflow as tf 
from tensorflow.keras import datasets, layers, models
#oof gotta use an array instead next time lol 
xtrain=[1,2,3,4,5]
ytrain=['q','w','e','r','t']
xtest=[]
ytest=[]

mylstm=tf.keras.Sequential([tf.keras.layers.LSTM(64,input_shape=(5,1)),tf.keras.layers.Dense(1)])
mylstm.compile(optimizer='Lion',loss='BinaryCrossentropy',metrics=['Accuracy','BinaryAccuracy'])

mylstm.fit(xtrain,ytrain,epochs=4)
#https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM
#https://pieriantraining.com/tensorflow-lstm-example-a-beginners-guide/
