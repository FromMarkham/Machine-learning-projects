
import torch 
import numpy
#https://www.youtube.com/shorts/1KmTc0VuMms

training=datasets.MNIST()

testing=datasets.MNIST()

dataloadertrain=DataLoader(dataset=training)
dataloadertest=DataLoader(dataset=testing)


class my_neural_network(nn.Module)
      def __init__(self):
          self.layer1=nn.Linear(100,100)
          self.layer2=nn.ReLU()
          self.layer3=nn.Linear(100,100)
          self.layer4=nn.sigmoid()
          self.layer5wutdahelllohmygawdddddddd=nn.Linear(100,100)

      def my_neural_networkpart2(x):
            output=self.layer1(x)
            output=self.layer2(output)
            output=self.layer3(output)
            output=self.layer4(output)
            output=self.layer5wutdahelllohmygawdddddddd(output)
            
            return output 

scitechbois_model=my_neural_network()

loss_function=nn.CrossEntropyLoss()

optimisergradientdescent=torch.optim.Adam()
