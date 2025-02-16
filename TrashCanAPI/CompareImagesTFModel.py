import tensorflow as tf
import numpy as np
from tensorflow.keras.applications import ResNet50, ResNet101, ResNet152
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
from sklearn.metrics.pairwise import cosine_similarity

# This is tensorflow version of model.

class CompareImagesModel():
    def __init__(self, base_model="resnet50"):
        # Load ResNet model without classification head
        if base_model == "resnet50":
            self.model = ResNet50(weights='imagenet', include_top=False, pooling='avg')
        elif base_model == "resnet101":
            self.model = ResNet101(weights='imagenet', include_top=False, pooling='avg')
        elif base_model == "resnet152":
            self.model = ResNet152(weights='imagenet', include_top=False, pooling='avg')
        else:
            raise ValueError("Invalid base model. Choose 'resnet50', 'resnet101', or 'resnet152'.")
        
    # Helper function to process the image
    def process_image(self, img):
        img = img.resize((224, 224))  # Resize to match model input size
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array = preprocess_input(img_array)  # Normalize
        return img_array

    # Helper function to extract feature embeddings
    def extract_features(self, img_array):
        features = self.model.predict(img_array)
        return features

    def predict(self, baseline_img, img):
        '''
        Predicts the Cosine Similarity of ResNet embeddings of two images.
        '''
        # Process and extract features
        baseline_features = self.extract_features(self.process_image(baseline_img))
        uploaded_features = self.extract_features(self.process_image(img))
        
        # Compute cosine similarity
        similarity = cosine_similarity(baseline_features, uploaded_features)[0][0]
        
        return similarity
    
    def getSimilarity(self, baseline_img, img):
        return self.predict(baseline_img, img)
