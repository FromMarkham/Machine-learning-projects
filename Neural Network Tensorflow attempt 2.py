import tensorflow as tf
mnist = tf.keras.datasets.mnist
#https://www.tensorflow.org/tutorials/quickstart/beginner
#https://www.analyticsvidhya.com/blog/2022/08/dropout-regularization-in-deep-learning/#:~:text=your%20neural%20network.-,Training%20with%20Drop%2DOut%20Layers,compared%20to%20the%20preceding%20layer.
#https://stackoverflow.com/questions/48618879/whats-the-dimensionality-of-the-output-space-in-tensorflows-docs
(xtrain,ytrain),(xtest,ytest)=mnist.load_data()

xtrain,xtest=xtrain/255.0,xtest/255.0


bobsmodel=tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28, 28)),tf.keras.layers.Dense(70,activation="relu"),tf.keras.layers.Dense(70,activation="sigmoid"),tf.keras.layers.Dense(70,activation="sigmoid"),tf.keras.layers.Dense(70,activation="sigmoid"),tf.keras.layers.Dense(70,activation="sigmoid"),tf.keras.layers.Dropout(0.1),tf.keras.layers.Dense(10)])

bobspredictions=bobsmodel(xtrain[:1]).numpy()

bobspredictions2=tf.nn.softmax(bobspredictions).numpy()

lossfunction=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

lossfunction(ytrain[:1], bobspredictions2).numpy()

bobsmodel.compile(optimizer='adam',loss=lossfunction,metrics=['accuracy'])

bobsmodel.fit(xtrain,ytrain,epochs=10)

bobsmodel.evaluate(xtest,ytest)
