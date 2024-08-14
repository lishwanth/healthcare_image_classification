from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np

class Preprocessor:
    def __init__(self, image_size=(224, 224)):
        self.image_size = image_size

    def preprocess_image(self, image_path):
        image = load_img(image_path, target_size=self.image_size)
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        image /= 255.0
        return image
