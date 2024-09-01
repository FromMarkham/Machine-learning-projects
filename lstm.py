import tensorflow as tf 

xtrain=[1,2,3,4,5]
ytrain=['q','w','e','r','t']
xtest=[]
ytest=[]

mylstm=tf.keras.layers.Sequential[tf.keras.Layers.LSTM(64,input_shape=(5,1)),tf.keras.layers.dense(1)]
mylstm.compile(optimizer='Lion',Loss='BinaryCrossentropy',Metrics=['Accuracy','BinaryAccuracy'])

mylstm.fit(xtrain,ytrain,epochs=4)
#https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM
#https://pieriantraining.com/tensorflow-lstm-example-a-beginners-guide/
