
# Healthcare Image Classification Project

## Overview

This project is a comprehensive, modular neural network-based image classification system tailored for healthcare applications. It employs a wide range of open-source tools and technologies to create a scalable, maintainable, and efficient architecture. The primary goal is to classify medical images to aid in diagnosing conditions such as pneumonia and skin cancer.

## Project Structure and Tools

### 1. **data_pipeline/**
This directory contains modules responsible for data loading, preprocessing, and augmentation.

- **data_loader.py**: Utilizes TensorFlow's `ImageDataGenerator` to load and split the dataset into training and validation sets.
- **preprocessing.py**: Contains image preprocessing logic, including resizing, normalization, and augmentation.
- **data_pipeline.py**: Combines data loading and preprocessing into a streamlined pipeline for easy integration with the model.

### 2. **models/**
This directory defines the architecture and training logic of the neural networks used in the project.

- **base_model.py**: An abstract base class that outlines the structure of the model, including methods for building, training, evaluating, and predicting.
- **cnn_model.py**: Implements a Convolutional Neural Network (CNN) using TensorFlow/Keras, tailored for image classification tasks.
- **training.py**: Handles the model training process, including parameter tuning and logging.

### 3. **database/**
Manages interactions with the MongoDB database, used to store training results and metadata.

- **mongodb.py**: Contains the `MongoDBClient` class for connecting to MongoDB, inserting records, and retrieving data.

### 4. **airflow_dags/**
This directory contains the Apache Airflow DAG for automating the data pipeline and model training processes.

- **classification_dag.py**: Defines a DAG that schedules the data pipeline and model training tasks, ensuring that the workflow runs automatically on a set schedule.

### 5. **docker/**
Contains Docker-related files to containerize the application, making it easy to deploy across different environments.

- **Dockerfile**: Defines the environment setup for running the application, including installing dependencies and setting the working directory.
- **docker-compose.yml**: Configures multiple services (application and MongoDB) to run in isolated containers, making the setup process seamless.

### 6. **utils/**
Houses utility scripts that support logging and configuration management.

- **logger.py**: Implements a logging system to track the application's progress and debug information.
- **config.py**: Stores configuration settings, including database connection strings and other environment-specific variables.

### 7. **datasets/**
A directory placeholder for storing datasets used in the project.

- **chest_xray/**: Directory to store the Chest X-Ray Images (Pneumonia) dataset.
- **isic/**: Directory to store the ISIC Skin Cancer Detection dataset.

### 8. **main.py**
The main script to orchestrate the entire process, from data loading to model training and saving results in MongoDB.

### 9. **requirements.txt**
Lists all the Python dependencies required to run the project.

### 10. **LICENSE**
The MIT license under which this project is distributed.

### 11. **README.md**
Provides a detailed overview of the project, instructions for setup, and guidelines for contribution.

## Getting Started

### Prerequisites

- **Python 3.9+**: The programming language used for this project.
- **Docker and Docker Compose**: For containerizing and orchestrating the application.
- **MongoDB**: A NoSQL database used to store training results, accessible via Docker.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/healthcare_image_classification.git
    cd healthcare_image_classification
    ```

2. **Install dependencies:**

    If you are running the project locally without Docker:

    ```bash
    pip install -r requirements.txt
    ```

3. **Build and run Docker containers:**

    ```bash
    docker-compose up --build
    ```

4. **Download Datasets:**

    The project uses the following datasets:

    - [Chest X-Ray Images (Pneumonia) Dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)
    - [ISIC Skin Cancer Detection Dataset](https://www.isic-archive.com/)

    After downloading, place the datasets in the `datasets/` directory:

    ```
    healthcare_image_classification/
    └── datasets/
        ├── chest_xray/
        └── isic/
    ```

5. **Run the main script:**

    ```bash
    python main.py
    ```

## Usage

### Data Pipeline

The `DataPipeline` class in `data_pipeline/data_pipeline.py` is designed to handle all aspects of data loading and preprocessing. Modify the `dataset_path` in `main.py` to point to your datasets.

### Model Training

The `ModelTraining` class in `models/training.py` encapsulates the training process. The architecture is based on a Convolutional Neural Network (CNN), and the model's hyperparameters can be adjusted in `models/cnn_model.py`.

### Database

Results from training sessions, including accuracy and loss metrics, are stored in MongoDB. Configuration details are provided in `utils/config.py`.

### Automation with Airflow

The DAG defined in `airflow_dags/classification_dag.py` automates the entire workflow. Apache Airflow ensures that your data pipeline and model training are executed on a schedule, making the process fully automated.

## Deployment

The application is containerized using Docker, enabling easy deployment across different environments. The Docker setup ensures that all dependencies are installed and configured correctly, simplifying the deployment process.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
