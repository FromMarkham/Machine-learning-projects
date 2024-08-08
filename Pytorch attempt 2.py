import numpy as np 
import torch
import torch.nn as nn
import torch.optim as optim 

dataset=np.loadtxt('pima-indians-diabetes.data.csv', delimiter=',')

X=dataset[:,0:8]
Y=dataset[:,8]

X=torch.tensor(X,dtype=torch.float32)
Y=torch.tensor(Y,dtype=torch.float32).reshape(-1,1)

model2=nn.Sequential(nn.Linear(8,12),nn.ReLU(),nn.Linear(12,8),nn.ReLU(),nn.Linear(8,1),nn.Sigmoid())

loss=nn.BCELoss()
optimizer=optim.Adam(model2.parameters(),lr=0.001)

epochs=5
batches=100

for x in range(epochs):
    for y in range(0,len(X),batches):
        Xbatch = X[y:y+batches]
        y_pred = model2(Xbatch)
        ybatch = Y[y:y+batches]
        loss2 = loss(y_pred, ybatch)
        optimizer.zero_grad()
        loss2.backward()
        optimizer.step()
        
    print(f'Finished epoch {epochs}, latest loss {loss2}')
