import torch 
import torch.nn as nn 
import torch.nn.functional as F
from torch.optim.adam import Adam 

import lightning as l

#https://www.youtube.com/@statquest/videos
#https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html
#https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html
#https://www.youtube.com/watch?v=RHGiXPuo_pI
my_words_lmao={}
mynumbers=[1,8,27,64,125,216,343,512,729,1000,1331,1728] #nth term=n^3
labels=[1,2,3,4,5,6,7,8,9,10,11,12]
my_embeddings=nn.Embedding(2,5)

#I tried to make an lstm in pytorch but i failed. The code doesn't work.

class my_little_lstm_aww(l.LightningModule):

    
    def __init__(self):

        super().__init__()
        mean=torch.tensor(0.5)
        standarddeviation=torch.tensor(1.0)
        #parameters of the model 
        self.weight=nn.Parameter(torch.normal(mean=mean,std=standarddeviation),requires_grad=True)
        self.weight2=nn.Parameter(torch.normal(mean=mean,std=standarddeviation),requires_grad=True)
        self.bias=nn.Parameter(torch.tensor(0.0),requires_grad=True)

        self.weight3=nn.Parameter(torch.normal(mean=mean,std=standarddeviation),requires_grad=True)
        self.weight4=nn.Parameter(torch.normal(mean=mean,std=standarddeviation),requires_grad=True)
        self.bias1=nn.Parameter(torch.tensor(0.0),requires_grad=True)

        self.weight5=nn.Parameter(torch.normal(mean=mean,std=standarddeviation),requires_grad=True)
        self.weight6=nn.Parameter(torch.normal(mean=mean,std=standarddeviation),requires_grad=True)
        self.bias2=nn.Parameter(torch.tensor(0.0),requires_grad=True)

        self.weight7=nn.Parameter(torch.normal(mean=mean,std=standarddeviation),requires_grad=True)
        self.weight8=nn.Parameter(torch.normal(mean=mean,std=standarddeviation),requires_grad=True)
        self.bias3=nn.Parameter(torch.tensor(0.0),requires_grad=True)
        
    def the_lstm_in_action(self,inputs,longmemory,shortmemory):
        percent_long_term_to_remember=torch.sigmoid((shortmemory*self.weight)+(inputs*self.weight2)+self.bias)
        potential_memory_to_remember=torch.sigmoid((shortmemory*self.weight3)+(inputs*self.weight4)+self.bias1)
        potential_longterm_memery=torch.tanh((shortmemory*self.weight3)+(inputs*self.weight4)+self.bias2)
        percent_output=torch.sigmoid((shortmemory*self.weight4)+(inputs*self.weight5)+self.bias3)
        update_long_memeory=torch.tanh(potential_longterm_memery)*percent_output #i assume u did not initialise update long memeory
        return  update_long_memeory
        return percent_output
    #u was forgetting a return statement bruh
        
    


    def optimise_lstm(self):
        
        return Adam(self.Parameters())

    def forward(self, input):
        firstnumber=mynumbers[0]
        second=mynumbers[1]
        third=mynumbers[2]
        fourth=mynumbers[3]
        fitch=mynumbers[4]
        sixth=mynumbers[5]
        seventh=mynumbers[6]

        longterm_memory=0
        shortterm_memory=0 

        longterm_memory,shortterm_memory=self.the_lstm_in_action(firstnumber,longterm_memory,shortterm_memory)
        longterm_memory,shortterm_memory=self.the_lstm_in_action(second,longterm_memory,shortterm_memory)
        longterm_memory,shortterm_memory=self.the_lstm_in_action(third,longterm_memory,shortterm_memory)
        longterm_memory,shortterm_memory=self.the_lstm_in_action(fourth,longterm_memory,shortterm_memory)
        longterm_memory,shortterm_memory=self.the_lstm_in_action(fitch,longterm_memory,shortterm_memory)
        longterm_memory,shortterm_memory=self.the_lstm_in_action(sixth,longterm_memory,shortterm_memory)
        longterm_memory,shortterm_memory=self.the_lstm_in_action(seventh,longterm_memory,shortterm_memory)

        return shortterm_memory
         
    def train_network(self,labels,digits):
        output=self.forward_pass(labels[0])
        loss=(digits-output)**2

        self.log("Loss",loss)

        return loss 

my_model=my_little_lstm_aww()

print("Output",my_model(torch.tensor([1,8,27,64,125,216,343,512,729,1000,1331,1728])).detach())