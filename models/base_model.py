from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def build_model(self):
        pass

    @abstractmethod
    def train(self, train_data, val_data, epochs):
        pass

    @abstractmethod
    def evaluate(self, test_data):
        pass

    @abstractmethod
    def predict(self, image):
        pass
