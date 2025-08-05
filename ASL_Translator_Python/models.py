import torch
from torchvision import models
import torch.nn as nn
import os

NUM_CLASSES = 29  # Or however many signs you're classifying

def load_model():
    model = models.resnet50(pretrained=False)
    model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)
    model_path = os.path.join("models", "asl_model_epoch5.pth")
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model
