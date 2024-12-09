from TEXTSUMMARIZER.logging import logger
from TEXTSUMMARIZER.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f"Started {STAGE_NAME}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed with error: {e}")
    raise e