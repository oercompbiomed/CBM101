
#pip install ipykernel ipython jupyter_client jupyter_core traitlets ipython_genutils

import numpy as np

representation_size = 2
input_size = 4
n_samples = 2000
batch_size = 5
n_samples_per_batch = n_samples//input_size

y = np.array([i for i in range(input_size)  for _ in range(n_samples_per_batch)])

d = np.identity(input_size)
x = np.array([d[i] for i in y], dtype=np.float32)

import torch
from torch import nn
from torch.autograd import Variable
class VAE(nn.Module):
    def __init__(self):
        super(VAE, self).__init__()
        self.en1 = nn.Linear(in_features = input_size, out_features = 200)
        self.en_mu = nn.Linear(in_features = 200, out_features = representation_size)
        self.en_std = nn.Linear(in_features = 200, out_features = representation_size)
        self.de1 = nn.Linear(in_features = representation_size, out_features = 200)
        self.de2 = nn.Linear(in_features = 200, out_features = input_size)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
        
    def encode(self, x):
        """Encode a batch of samples, and return posterior parameters for each point."""
        h1 = self.relu(self.en1(x))
        return self.en_mu(h1), self.en_std(h1)
    
    def decode(self, z):
        """Decode a batch of latent variables"""
        
        h2 = self.relu(self.de1(z))
        return self.sigmoid(self.de2(h2))
    
    def reparam(self, mu, logvar):
        """Reparameterisation trick to sample z values. 
        This is stochastic during training,  and returns the mode during evaluation."""
        
        if self.training:
            print("Logarithm of the variance is")
            print(logvar)
            std = logvar.mul(0.5).exp_()
            eps = Variable(std.data.new(std.size()).normal_()) # sample as
            print("THe size of the standard deviation is")
            print(std.size())
            print("The sampled data under STD has size")
            print(eps.size())
            sampled_values_from_normal = eps.mul(std).add_(mu)
            print(sampled_values_from_normal)
            #print(sampled_values_from_normal.shape)
            return sampled_values_from_normal
        else:
            return mu
            
    def forward(self, x):
        """Takes a batch of samples, encodes them, and then decodes them again to compare."""
        mu, logvar = self.encode(x.view(-1, input_size))
        z = self.reparam(mu, logvar)
        return self.decode(z), mu, logvar
    
    def loss(self, reconstruction, x, mu, logvar):
        """ELBO assuming entries of x are binary variables, with closed form KLD."""
        bce = torch.nn.functional.binary_cross_entropy(reconstruction, x.view(-1, input_size))
        KLD = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
        # Normalise by same number of elements as in reconstruction
        KLD /= x.view(-1, input_size).data.shape[0] * input_size

        return bce + KLD
    
    def get_z(self, x):
        """Encode a batch of data points, x, into their z representations."""
        mu, logvar = self.encode(x.view(-1, input_size))
        return self.reparam(mu, logvar)
