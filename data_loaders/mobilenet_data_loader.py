from __future__ import print_function
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import Dataset,DataLoader
from PIL import Image as PILImage
import torchvision.transforms as transforms
from time import time

def get_file_index_list(path):
    return  [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

  
classes = ["LargeQuadcopters", "SmallQuadcopters", "WingedDrones", "FlyingBirds"]
class TrainImageDataset(Dataset): 
    

    def __init__(self, root_dir,  transform=None):
        """
        Args:
            csv_file (string): Path to the csv file with annotations.
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.root_dir = root_dir
        self.transform = transform
        self.file_index_list = {}
        
        for class_id,cls in enumerate(classes):
            self.file_index_list[class_id] = get_file_index_list(self.root_dir + "/" +  cls)


    def __len__(self):
        return 8000

    def __getitem__(self, idx):
      
        class_id = int(idx/2000)
        file_id = idx - class_id*2000
        #print("idx=", idx, " class_id=",  class_id, " file_id: ",file_id)
        #print("file_index_list: ",file_id)
        indx_list =  self.file_index_list[class_id]
        valid = False
        
        while not valid:
            img = None
        
            try:
                img = PILImage.open(self.root_dir + "/" + classes[class_id] + "/" + indx_list[file_id])
            except:
                #print("Train Excetpion caught while opening file:" + classes[class_id] + "/" + indx_list[file_id])
                pass
            
            if img is not None:        
                if self.transform is not None:
                    img = self.transform(img)
                    #print(" img shape: ", img.shape)
                
            if img is None or img.shape[0] != 3 or img.shape[1] != 224 or img.shape[2] != 224:
                #print(classes[class_id] + "/" + indx_list[file_id] + " is not good")
                file_id = (file_id + 1) % 2000 
            else: 
                valid = True
        
  
        
        return {"X" : img, "Y": class_id}


class TestImageDataset(Dataset): 
    

    def __init__(self, root_dir,transform=None):
        """
        Args:
            csv_file (string): Path to the csv file with annotations.
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.root_dir = root_dir
        self.transform = transform
        self.file_index_list = {}
        
        for class_id,cls in enumerate(classes):
            self.file_index_list[class_id] = get_file_index_list(self.root_dir + "/" +  cls)


    def __len__(self):
        return 2000 

    def __getitem__(self, idx):
        class_id = int(idx/500)
        file_id = idx - class_id*500
        #print("idx=", idx, " class_id=",  class_id, " file_id: ",file_id)
        #print("file_index_list: ",file_id)
        indx_list =  self.file_index_list[class_id]
        valid = False
        while not valid:
            img = None
        
            try:
                img = PILImage.open(self.root_dir + "/" + classes[class_id] + "/" + indx_list[file_id])
            except:
                #print("Test Excetpion caught while opening file:" + classes[class_id] + "/" + indx_list[file_id])
                pass
            
            if img is not None:        
                if self.transform is not None:
                    img = self.transform(img)
                    #print(" img shape: ", img.shape)
                
            if img is None or img.shape[0] != 3 or img.shape[1] != 224 or img.shape[2] != 224:
                #print(classes[class_id] + "/" + indx_list[file_id] + " is not good")
                file_id = (file_id + 1) % 500  
            else: 
                valid = True
  
        
        return {"X" : img, "Y": class_id}


