import torch 
import torch.nn as nn 
import torch.nn.functional as F
from torch.optim.adam import Adam 

import lightning as L 
from torch.utils.Data import TensorDataset, DataLoader 
#https://www.youtube.com/@statquest/videos
#https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html
#https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html
#https://www.youtube.com/watch?v=RHGiXPuo_pI
my_words_lmao={}

my_embeddings=nn.Embedding(2,5)

class my_little_lstm_aww(L.LightningModule):
    mean=torch.tensor(0.5)
    standarddeviation=torch.tensor(1.0)
    
    def __init__(self):

        super().__init__()
        
        #parameters of the model 
        self.weight=nn.Parameter(torch.normal(mean=mean,std=standarddeviation),requires_grad=True)
        self.weight2=nn.Parameter(torch.normal(mean=mean,std=standarddeviation),requires_grad=True)
        self.bias=nn.Parameter(torch.tensor(0),requires_grad=True)

        self.weigh3=nn.Parameter(torch.normal(mean=mean,std=standarddeviation),requires_grad=True)
        self.weight4=nn.Parameter(torch.normal(mean=mean,std=standarddeviation),requires_grad=True)
        self.bias1=nn.Parameter(torch.tensor(0),requires_grad=True)

        self.weight5=nn.Parameter(torch.normal(mean=mean,std=standarddeviation),requires_grad=True)
        self.weight6=nn.Parameter(torch.normal(mean=mean,std=standarddeviation),requires_grad=True)
        self.bias2=nn.Parameter(torch.tensor(0),requires_grad=True)

        self.weight7=nn.Parameter(torch.normal(mean=mean,std=standarddeviation),requires_grad=True)
        self.weight8=nn.Parameter(torch.normal(mean=mean,std=standarddeviation),requires_grad=True)
        self.bias3=nn.Parameter(torch.tensor(0),requires_grad=True)
        
    def this_is_where_it_lives(self):

    def optimise_lstm(self):

    def train_network(self):
        
    def the_lstm_in_action(self,inputs,longmemory,shortmemory):
        longterm_memory_percentage=torch.sigmoid()
        shortterm_memory_percentage=torch.()
