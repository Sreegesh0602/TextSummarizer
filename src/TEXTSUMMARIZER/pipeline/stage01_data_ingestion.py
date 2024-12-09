from TEXTSUMMARIZER.config.configurations import ConfigurationManager
from TEXTSUMMARIZER.components.data_ingestion import Dataingestion
from TEXTSUMMARIZER.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = Dataingestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip()