import os
from datetime import datetime

DATABASE_NAME = "US_VISA"

COLLECTION_NAME = "visa_date"

MONGODB_URL_KEY = "mongodb+srv://ajaygopireddy216:ajaygopireddy216@cluster0.7lfy2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

PIPELINE_NAME: str = "us_visa"
ARTIFACT_DIR: str = "artifact"

FILE_NAME: str = "usvisa.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
MODEL_FILE_NAME = "model.pkl"

"""
Data Ingestion related constant start with DATA_INGESTION Var name
"""

DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2


