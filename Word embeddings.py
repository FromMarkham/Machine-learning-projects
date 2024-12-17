import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import math
import copy


torch.manual_seed(1)
words={"hello":0,"everyone":1,"i":2,"am":3,"a":4,"robot":5}
embeddings=nn.Embedding(6,6)

hellotensor= torch.tensor(words["hello"], dtype=torch.long)
everyonetensor= torch.tensor(words["everyone"], dtype=torch.long)
itensor= torch.tensor(words["i"], dtype=torch.long)
amtensor= torch.tensor(words["am"], dtype=torch.long)
atensor= torch.tensor(words["a"], dtype=torch.long)
robottensor= torch.tensor(words["robot"], dtype=torch.long)

hello=embeddings(hellotensor)
everyone=embeddings(everyonetensor)
i=embeddings(itensor)
am=embeddings(amtensor)
a=embeddings(atensor)
robot=embeddings(robottensor)

print(hello)
print(everyone)
print(i)
print(am)
print(a)
print(robot)
