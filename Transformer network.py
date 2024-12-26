import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import math
import copy

import numpy as np
import tensorflow as tf 
#Yayyyy all da shit will import 
#https://medium.com/@hunter-j-phillips/positional-encoding-7a93db4109e6
#https://discuss.pytorch.org/t/positional-encoding/175953
#https://www.datacamp.com/tutorial/building-a-transformer-with-py-torch
#https://medium.com/@lovelyndavid/self-attention-a-step-by-step-guide-to-calculating-the-context-vector-3d4622600aac
#https://www.youtube.com/watch?v=U0s0f995w14
#https://www.datacamp.com/tutorial/fine-tuning-large-language-models
#https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html


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

centralwordvector=torch.cat(hello,i,am,a,robot)

#https://machinelearningmastery.com/a-gentle-introduction-to-positional-encoding-in-transformer-models-part-1/

def my_positional_encoding(sentence_length=6,vector_length=6,n=10000):
    positionalEncodingVector=np.zeros(sentence_length,vector_length)

    for kVectorposition in range(sentence_length):
        for i in np.arange(int(vector_length/2)):
            denominator=np.power
            positionalEncodingVector[kVectorpositon,2*i]=np.sin
            positionalEncodingVector[kVectorposition,2*i+1]=np.sin
           
            
    
def my_positional_encoding(sentence_length,vector_length,n=10000):
    positionalEncodingVector=np.zeros((sentence_length,vector_length))

    for kVectorposition in range(sentence_length):
        for i in np.arange(int(vector_length/2)):
            denominator=np.power(n,2*i/sentence_length)
            positionalEncodingVector[kVectorposition]=np.sin(kVectorposition/denominator)
            positionalEncodingVector[kVectorposition]=np.sin(kVectorposition/denominator)
           
    return positionalEncodingVector

positionvectors=my_positional_encoding(sentence_length=6,vector_length=6,n=10000)
print(positionvectors)
    

wordsplusposition=torch.cat(positionvectors,centralwordvector)

class MultiHeadAttention(nn.Module):
    def __init__(self,model_dimension,head_count):
         super(MultiHeadAttention, self).__init__() #im inheriting from the multi headed attention class lol

         assert model_dimenion%head_count==0 #making sure that Model dimension should be divisble by head count
         multi_headed_attention=torch.nn.MultiheadAttention(64,8)


        query=nn.Linear(model_dimension)
        key=nn.Linear(model_dimension)
        value=nn.Linear(model_dimension)
        output=nn.Linear(model_dimension)


    def calculate_attention_scores(self,q,k,v):
        attention_scores=torch.matmul(q,k)/math.sqrt()

        attention_probabilities=torch.softmax(attention_scores)




    
