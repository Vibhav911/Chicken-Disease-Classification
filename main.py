# This program contains all the pipelines
from ChickenDisease import logger
from ChickenDisease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ChickenDisease.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from ChickenDisease.pipeline.stage_03_training import ModelTrainingPipeline
from ChickenDisease.pipeline.stage_04_evaluation import EvaluationPipeline


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


# Training
STAGE_NAME = "Training"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


# Evaluation
STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e