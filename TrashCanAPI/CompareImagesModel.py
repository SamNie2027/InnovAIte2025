import torch
import torchvision.models as models
import torch.nn as nn
from torchvision import datasets, transforms
from sklearn.metrics.pairwise import cosine_similarity

class CompareImagesModel():
    def __init__(self, base_model="resnet18"):

        # Load ResNet (without classification head)
        if base_model == "resnet18":
            self.model = models.resnet18(pretrained=True)
        elif base_model == "resnet34":
            self.model = models.resnet34(pretrained=True)
        elif base_model == "resnet50":
            self.model = models.resnet50(pretrained=True)
        else:
            raise ValueError("Invalid base model. Choose 'resnet18' or 'resnet34'.")

        self.model.eval()  # Set the model to evaluation mode

        # Define the image transformation pipeline
        self.transform = transforms.Compose([
            transforms.Resize(256),                # Resize the image
            transforms.CenterCrop(224),            # Crop to 224x224
            transforms.ToTensor(),                 # Convert to tensor
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # Normalize
        ])

    # Helper function to process the image
    def process_image(self, img):
        img = self.transform(img).unsqueeze(0)  # Add batch dimension
        return img

    # Helper function to extract the feature vector (embedding)
    def extract_features(self, img_tensor):
        with torch.no_grad():  # Disable gradient calculation
            features = self.model.conv1(img_tensor)  # Apply first layer
            features = self.model.bn1(features)
            features = self.model.relu(features)
            features = self.model.maxpool(features)

            # Pass through the ResNet layers until avgpool
            for layer in self.model.layer1:
                features = layer(features)
            for layer in self.model.layer2:
                features = layer(features)
            for layer in self.model.layer3:
                features = layer(features)
            for layer in self.model.layer4:
                features = layer(features)

            features = self.model.avgpool(features)
            features = features.view(features.size(0), -1)  # Flatten the feature map
        return features


    def predict(self, baseline_img, img):
        '''
        Predicts the Cosine Similarity of Resnet embeddings of two images.
        '''
        # Load the baseline image and extract its features
        baseline_img_tensor = self.process_image(baseline_img)
        baseline_features = self.extract_features(baseline_img_tensor)

        # Process the uploaded image
        img_tensor = self.process_image(img)
        # Extract features for the uploaded image
        uploaded_features = self.extract_features(img_tensor)
        # Compute the cosine similarity between the baseline and uploaded feature vectors
        similarity = cosine_similarity(baseline_features.numpy(), uploaded_features.numpy())[0][0]

        return similarity
    
    def getSimilarity(self, baseline_img, img):
        return self.predict(baseline_img, img)
    