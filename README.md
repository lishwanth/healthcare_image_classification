
# Healthcare Image Classification Project

## Overview

This project is an end-to-end, modular neural network-based image classification system designed specifically for healthcare applications. It leverages open-source tools such as TensorFlow, Docker, MongoDB, and Apache Airflow to create a scalable and maintainable architecture. The primary objective is to classify medical images to assist in diagnosing conditions like pneumonia and skin cancer.

## Project Structure

```
healthcare_image_classification/
│
├── data_pipeline/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   └── data_pipeline.py
│
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── cnn_model.py
│   └── training.py
│
├── database/
│   ├── __init__.py
│   ├── mongodb.py
│
├── airflow_dags/
│   ├── __init__.py
│   └── classification_dag.py
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   └── config.py
│
├── datasets/
│   ├── chest_xray/
│   └── isic/
│
├── main.py
├── requirements.txt
├── LICENSE
└── README.md
```

### Modules

- **data_pipeline/**: Handles the loading, preprocessing, and data augmentation of images.
- **models/**: Contains model architecture (CNN) and training logic using TensorFlow/Keras.
- **database/**: Manages database operations with MongoDB for storing training results.
- **airflow_dags/**: Contains the Airflow DAG for automating the data pipeline and model training.
- **docker/**: Docker configuration files to containerize the application for easy deployment.
- **utils/**: Utility scripts including logging and configuration management.
- **datasets/**: Directory to store datasets.

## Getting Started

### Prerequisites

- Python 3.9+
- Docker and Docker Compose
- MongoDB (included in Docker setup)

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

    After downloading, place the datasets in the `datasets/` directory.

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

The `DataPipeline` class loads and preprocesses the image data. You can customize the `dataset_path` in the `main.py` script to point to your datasets.

### Model Training

The `ModelTraining` class trains a Convolutional Neural Network (CNN) on the preprocessed data. You can adjust the model architecture and training parameters in `models/cnn_model.py`.

### Database

Training results are stored in a MongoDB database, which is managed by the `MongoDBClient` class. The database URI and name can be configured in `utils/config.py`.

### Automation with Airflow

The project includes an Apache Airflow DAG to automate the data pipeline and model training. To use Airflow, ensure it is installed and configure the DAG in `airflow_dags/classification_dag.py`.

## Deployment

The application is containerized using Docker, which simplifies deployment. You can run the entire application using Docker Compose, which will start the app and MongoDB services.

## Contribution

Feel free to contribute to this project by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
