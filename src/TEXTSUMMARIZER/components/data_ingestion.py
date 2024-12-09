import os,urllib.request as request
import zipfile
from TEXTSUMMARIZER.logging import logger
from TEXTSUMMARIZER.entities import DataIngestionConfig
from TEXTSUMMARIZER.utils.common import get_size


class Dataingestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,header = request.urlretrieve(self.config.source_url,self.config.local_data_file)
            logger.info(f"{filename} download! with following info :\n {header}")
        else:
            logger.info(f"File already exists at {self.config.local_data_file}\n size: {get_size(self.config.local_data_file)}")

    def extract_zip(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
