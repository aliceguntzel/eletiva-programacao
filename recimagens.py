import torch
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image

# Carregar o modelo pré-treinado
model = models.mobilenet_v2(pretrained=True)
model.eval()

# Transformações para pré-processamento das imagens
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Carregar as classes do modelo
with open('imagenet_classes.txt', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Função para prever as classes da imagem
def predict_image(image_path):
    # Carregar e pré-processar a imagem
    image = Image.open(image_path)
    image_tensor = preprocess(image)
    image_tensor = torch.unsqueeze(image_tensor, 0)

    # Fazer a predição
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted_idx = torch.max(outputs, 1)
        predicted_label = classes[predicted_idx.item()]

    return predicted_label

# Caminho da imagem de teste
image_path = 'test_image.jpg'

# Fazer a predição na imagem de teste
predicted_label = predict_image(image_path)
print(f"Objeto identificado: {predicted_label}")
