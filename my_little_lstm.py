import torch 
import torch.nn as nn 
import torch.nn.functional as F
from torch.optim.adam import Adam 

import lightning as L 
from torch.utils.Data import TensorDataset, DataLoader 

class my_little_lstm_aww(L.LightningModule):
    mean=torch.tensor(0.5)
    standarddeviation=torch.tensor(1.0)
    
    def __init__(self):
        self.weight=nn.Parameter()
        
    def this_is_where_it_lives(self):

    def optimise_lstm(self):

    def train_network(self):
        
    
