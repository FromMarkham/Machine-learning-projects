import tensorflow as tf 

xtrain=[1,2,3,4,5]
ytrain=['q','w','e','r','t']
xtest=[]
ytest=[]

mylstm=tf.keras.layers.Sequential[tf.keras.Layers.lstm(),tf.keras.layers.dense()]
mylstm.compile(optimizer='Lion',Loss='BinaryCrossentropy',Metrics=['Accuracy','BinaryAccuracy'])

mylstm.fit(xtrain,ytrain,epochs=4)
#https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM
#https://pieriantraining.com/tensorflow-lstm-example-a-beginners-guide/