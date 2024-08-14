import os
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

class DataLoader:
    def __init__(self, dataset_path, image_size=(224, 224), batch_size=32):
        self.dataset_path = dataset_path
        self.image_size = image_size
        self.batch_size = batch_size

    def load_data(self):
        datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
        
        train_data = datagen.flow_from_directory(
            self.dataset_path,
            target_size=self.image_size,
            batch_size=self.batch_size,
            class_mode='binary',
            subset='training'
        )
        
        val_data = datagen.flow_from_directory(
            self.dataset_path,
            target_size=self.image_size,
            batch_size=self.batch_size,
            class_mode='binary',
            subset='validation'
        )
        
        return train_data, val_data
