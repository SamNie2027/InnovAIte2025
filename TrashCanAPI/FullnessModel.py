from sklearn.utils.class_weight import compute_class_weight

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import ResNet50
from tensorflow.keras import layers, models
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

"""
Class used to train and predict if the trash can in the given image is full or empty
"""
class FullnessModel:
    """
    Initialization method.
    Pre-process data, build and train the model.
    """
    def __init__(self, train_dir, validate_dir):
        self.train_dir = train_dir
        self.validate_dir = validate_dir
        self.model = None
        self.train_generator = None
        self.validate_generator = None
        self._prepare_data()
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

    def predict(self, image):
        if self.model is None:
            raise ValueError("Model is not trained yet.")

        result = self.model.predict(image)
        class_indices = self.train_generator.class_indices
        class_labels = list(class_indices.keys())

        predicted_class = class_labels[np.argmax(result)]

        return 1 if predicted_class == 'Full trash' else 0
