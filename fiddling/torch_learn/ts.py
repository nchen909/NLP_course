import tsensor
import torch
nhidden = 256
n = 200
d = 764
Whh_ = torch.eye(nhidden, nhidden)
Uxh_ = torch.randn(nhidden, d)# corrected definition
bh_ = torch.zeros(nhidden, 1)
h = torch.randn(nhidden, 1)# fake previous hidden state h
r = torch.randn(nhidden, 1) # fake this computation
X = torch.rand(n,d) # fake input
tsensor.astviz("h_ = torch.tanh(Whh_ @ (r*h) + Uxh_ @ X.T + bh_)")
