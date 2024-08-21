import numpy as np

from tqdm.auto import trange, tqdm
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow.keras import layers

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.cifar10.load_data()

print(X_train[:25].shape)

print(np.random.normal(8))


print(np.random.normal(X_train[:25].shape))


print(np.random.normal((4),(1),(5,5)))
