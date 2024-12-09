import os
from TEXTSUMMARIZER.entities import DataValidationConfig
from TEXTSUMMARIZER.logging import logger

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config


    def validate_all_files(self) -> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join('artifacts','data_ingestion',"samsum_dataset"))

            for file in all_files:
                if file in self.config.ALL_REQUIRED_FILE:
                    validation_status = True
                    with open(os.path.join(self.config.STATUS_FILE),'w') as file:
                        file.write(f"Validation Status: {validation_status}")
                else:
                    validation_status = False
                    with open(os.path.join(self.config.STATUS_FILE),'w') as file:
                        file.write(f"Validation Status: {validation_status}")
            return validation_status
        except Exception as e:
            raise e