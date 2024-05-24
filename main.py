# This program contains all the pipelines
from ChickenDisease import logger
from ChickenDisease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ChickenDisease.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


# Data Ingestion
STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\n x========x')
except Exception as e:
    logger.exception(e)
    raise e

# Prepare Base Model
STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>> {STAGE_NAME} Completed <<<<<<<<\n\n x=========x")
except Exception as e:
    logger.exception(e)
    raise e