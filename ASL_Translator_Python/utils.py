from torchvision import transforms
import torch

# Match with how the model was trained
preprocess = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.CenterCrop(64),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

LABELS = [chr(i) for i in range(65, 91)] + ["del", "nothing", "space"] # A-Z

def preprocess_image(image):
    image = image.convert("RGB")
    return preprocess(image).unsqueeze(0)

def predict_sign(model, image):
    input_tensor = preprocess_image(image).to(next(model.parameters()).device)
    with torch.no_grad():
        outputs = model(input_tensor)
        _, preds = torch.max(outputs, 1)
        pred_index = preds.item()
        print(f"Predicted index: {pred_index}, Total labels: {len(LABELS)}")
        if pred_index >= len(LABELS):
            return "Unknown sign"
        return LABELS[pred_index]
