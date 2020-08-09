import torch.nn as nn
import torchvision.models as models
import torch

def get_model(pretrained=False):
    #model = models.mobilenet_v2()
    model = torch.hub.load('pytorch/vision', 'mobilenet_v2', pretrained=pretrained)
    for param in model.parameters():
        param.requires_grad = False
    model.classifier[1] = nn.Linear(1280, 4)
    for param in model.classifier[1].parameters():
        param.requires_grad = True
    return model
