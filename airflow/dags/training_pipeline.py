# from asyncio import tasks
# import json
# from textwrap import dedent
# import pendulum
# import os
# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from dotenv import load_dotenv
# load_dotenv()

# with DAG(
#     'network_training_pipelinr',
#     default_args={'retries': 2},
#     description='Network security pipeline for training and syncing to S3',
#     schedule_interval="@weekly",
#     start_date=pendulum.datetime(2024,12,24, tz="UTC"),
#     catchup=False,
#     tags=['mlops'],
# ) as dag:

    
#     def training(**kwargs):
        
#         from networksecurity.pipeline.training_pipeline import TrainingPipeline
#         training_obj=TrainingPipeline()
#         training_obj.run_pipeline()
        
    
#     def sync_artifact_to_s3_bucket(**kwargs):
#         bucket_name = "networksecurity3"
#         os.system(f"aws s3 sync /app/Artifacts s3://{bucket_name}/artifact")
#         os.system(f"aws s3 sync /app/final_model s3://{bucket_name}/final_model")

#     training_pipeline  = PythonOperator(
#             task_id="train_pipeline",
#             python_callable=training

#     )

#     sync_data_to_s3 = PythonOperator(
#             task_id="sync_data_to_s3",
#             python_callable=sync_artifact_to_s3_bucket

#     )

#     training_pipeline >> sync_data_to_s3









