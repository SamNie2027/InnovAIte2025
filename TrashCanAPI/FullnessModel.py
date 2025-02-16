from sklearn.utils.class_weight import compute_class_weight
import numpy as np
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import ResNet50
from tensorflow.keras import layers, models
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.preprocessing import image
from PIL import Image

"""
Class used to train and predict if the trash can in the given image is full or empty
"""
class FullnessModel():
    """
    Initialization method.
    Pre-process data, build and train the model.
    """
    def __init__(self, load = True ,train_dir = '../Trash/Train', validate_dir = '../Trash/Validate'):
        self.train_dir = train_dir
        self.validate_dir = validate_dir
        self.model = None
        self.train_generator = None
        self.validate_generator = None
        if load is True:
            self._prepare_data()
            self.load_mode()
        else:
            self._build_model()
            self._train_model()

    """
    Data augmentation on training and validation 
    data to improve the model prediction.
   
    """
    def _prepare_data(self):
        # Data Augmentation
        train_datagen = ImageDataGenerator(
            rescale=1. / 255,
            rotation_range=30,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.3,
            horizontal_flip=True,
            fill_mode='nearest'
        )
        validate_datagen = ImageDataGenerator(rescale=1. / 255)

        # Load Data
        self.train_generator = train_datagen.flow_from_directory(
            self.train_dir,
            target_size=(224, 224),
            batch_size=32,
            class_mode='categorical'
        )

        self.validate_generator = validate_datagen.flow_from_directory(
            self.validate_dir,
            target_size=(224, 224),
            batch_size=32,
            class_mode='categorical'
        )

    """
    Build the model. Fit the data in a ResNet50 model.
    """
    def _build_model(self):
        # Handle Class Imbalance
        class_weights = compute_class_weight(
            class_weight='balanced',
            classes=np.unique(self.train_generator.classes),
            y=self.train_generator.classes
        )
        self.class_weights_dict = dict(enumerate(class_weights))

        # Load Pretrained ResNet50
        base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
        base_model.trainable = False  # Freeze base layers

        # Define Model
        self.model = models.Sequential([
            base_model,
            layers.GlobalAveragePooling2D(),
            layers.Dense(256, activation='relu'),
            layers.BatchNormalization(),
            layers.Dropout(0.5),
            layers.Dense(len(self.train_generator.class_indices), activation='softmax')
        ])

        # Compile Model
        optimizer = Adam(learning_rate=0.0001)
        self.model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

    def _train_model(self):
        early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

        self.model.fit(
            self.train_generator,
            epochs=50,
            validation_data=self.validate_generator,
            class_weight=self.class_weights_dict,
            callbacks=[early_stop]
        )

    def load_mode(self):
        # Path to the folder
        folder_path = "../"

        # Define the filename you're looking for
        filename = "Fullness_model.h5"

        # Search for the file in the directory
        file_path = os.path.join(folder_path, filename)

        if os.path.exists(file_path):
            print(f"File found at {file_path}")
            # Load the model or perform any operation
            self.model = load_model(file_path)
            print("Model loaded successfully!")
        else:
            print(f"File {filename} not found.")


    def predict(self, img):
        # If the input is a PIL image, convert it to the correct format
        if isinstance(img, Image.Image):
            img = img.resize((224, 224))  # Resize the image to (224, 224)
        else:
            # If it's a path, load the image using Keras' image loader
            img = image.load_img(img, target_size=(224, 224))

        # Convert image to numpy array
        img_array = image.img_to_array(img)

        # Add batch dimension (1 image)
        img_array = np.expand_dims(img_array, axis=0)

        # Normalize the image (same as in training)
        img_array = img_array / 255.0

        # Make a prediction
        prediction = self.model.predict(img_array)

        # Get class labels (Make sure train_generator is present and accessible)
        class_indices = self.train_generator.class_indices  # Get the class indices
        class_labels = list(class_indices.keys())  # Get the class labels

        # Get the class with the highest probability
        predicted_class = class_labels[np.argmax(prediction)]

        # Return the prediction
        return 1 if predicted_class == 'Full Trash' else 0

