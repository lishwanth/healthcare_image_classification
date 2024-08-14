from data_pipeline.data_pipeline import DataPipeline
from models.training import ModelTraining
from database.mongodb import MongoDBClient
from utils.logger import Logger
from utils.config import Config

def main():
    logger = Logger('HealthcareClassification')

    # Data Pipeline
    logger.log("Starting Data Pipeline...")
    pipeline = DataPipeline(dataset_path='/path/to/dataset')
    train_data, val_data = pipeline.get_data()

    # Model Training
    logger.log("Training Model...")
    trainer = ModelTraining(input_shape=(224, 224, 3), num_classes=2)
    history = trainer.train_model(train_data, val_data, epochs=10)

    # Save results to MongoDB
    logger.log("Saving Results to MongoDB...")
    db_client = MongoDBClient(Config.MONGO_URI, Config.DATABASE_NAME)
    db_client.insert_record('training_results', {"history": history.history})

if __name__ == "__main__":
    main()
