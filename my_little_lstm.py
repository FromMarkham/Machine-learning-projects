#https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html
#https://www.youtube.com/watch?v=RHGiXPuo_pI


da_numbers=torch.randn(19,13,10)

da_numbersp2=torch.randn(19,13,10)

da_numbersp3=torch.randn(19,13,10)

my_little_lstm=nn.LSTM(10,10,10)

out=my_little_lstm(da_numbers,(da_numbersp2,da_numbersp3))
