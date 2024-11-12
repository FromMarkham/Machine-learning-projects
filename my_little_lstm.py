import torch 
import torch.nn as nn 
import torch.nn.functional as F
from torch.optim.adam import Adam 

import lightning as L 
from torch.utils.Data import TensorDataset, DataLoader 
#https://www.youtube.com/@statquest/videos
#https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html

my_embeddings=nn.Embedding()

class my_little_lstm_aww(L.LightningModule):
    mean=torch.tensor(0.5)
    standarddeviation=torch.tensor(1.0)
    
    def __init__(self):

        super().__init__()
        
        self.weight=nn.Parameter(torch.normal(),requires_grad=True)
        
    def this_is_where_it_lives(self):

    def optimise_lstm(self):

    def train_network(self):
        
    
