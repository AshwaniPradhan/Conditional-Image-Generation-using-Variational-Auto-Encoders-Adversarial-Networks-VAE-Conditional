import torch
import torchvision
import torch.nn as nn
from torchvision.transforms import ToTensor, Compose, Normalize
from torch.utils.data import dataloader

def Dataloader(batch_size,root_dir):
    root = root_dir
    transform = Compose([ToTensor(),Normalize((0.5),(0.5))])
    dataset = torchvision.datasets.MNIST(root=root,train=True, download= True, transform = transform)
    data_loader = dataloader.DataLoader(dataset,batch_size=batch_size,shuffle=True)
    return data_loader