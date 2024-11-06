#https://docs.kanaries.net/topics/Python/nn-linear#:~:text=The%20nn.Linear,is%20out_features.
#https://stackoverflow.com/questions/55348647/weight-matrix-dimension-intuition-in-a-neural-network
#https://www.youtube.com/watch?v=pDdP0TFzsoQ

class my_cnn(nn.module):
      self.my_cnn_layer=nn.Conv2d(4,4,4)
      self.my_pooling_layer=nn.MaxPool2d()

      self.a_percetron_later=nn.Linear
