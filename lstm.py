import tensorflow as tf 

xtrain=
ytrain=
xtest=
ytest=

mylstm=tf.keras.layers.Sequential[tf.keras.Layers.lstm(),tf.keras.layers.dense()]
mylstm.compile(optimizer='Lion',Loss='BinaryCrossentropy',Metrics=['Accuracy','BinaryAccuracy'])


#https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM
#https://pieriantraining.com/tensorflow-lstm-example-a-beginners-guide/