from objectClassifier import logger

#logger.info("welocme to my custom log")

from objectClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from objectClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from objectClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from objectClassifier.pipeline.stage_04_evaluation import EvaluationPipeline



# 01-data-ingestion

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


# 02-prepare-base-model

STAGE_NAME = "prepare base model stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e




# 03- we dont need to create a callback pipeline, we only needed it for our training

#04- training
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
        


#05- evaluation
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
            