from .data_loader import DataLoader
from .preprocessing import Preprocessor

class DataPipeline:
    def __init__(self, dataset_path, image_size=(224, 224), batch_size=32):
        self.loader = DataLoader(dataset_path, image_size, batch_size)
        self.preprocessor = Preprocessor(image_size)

    def get_data(self):
        return self.loader.load_data()
    
    def preprocess_single_image(self, image_path):
        return self.preprocessor.preprocess_image(image_path)
