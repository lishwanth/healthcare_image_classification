from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from data_pipeline.data_pipeline import DataPipeline
from models.training import ModelTraining

def run_pipeline():
    pipeline = DataPipeline(dataset_path='/path/to/dataset')
    train_data, val_data = pipeline.get_data()
    
    trainer = ModelTraining(input_shape=(224, 224, 3), num_classes=2)
    trainer.train_model(train_data, val_data, epochs=10)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 15),
    'retries': 1
}

dag = DAG('classification_dag', default_args=default_args, schedule_interval='@daily')

run_pipeline_task = PythonOperator(task_id='run_pipeline', python_callable=run_pipeline, dag=dag)
