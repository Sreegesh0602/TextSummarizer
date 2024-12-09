from TEXTSUMMARIZER.config.configurations import ConfigurationManager
from TEXTSUMMARIZER.components.data_validation import DataValidation
from TEXTSUMMARIZER.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_files()
        