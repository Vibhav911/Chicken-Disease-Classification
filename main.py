# This program contains all the pipelines
from ChickenDisease import logger
from ChickenDisease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


# Data Ingestion
STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\n x========x')
except Exception as e:
    logger.exception(e)
    raise e