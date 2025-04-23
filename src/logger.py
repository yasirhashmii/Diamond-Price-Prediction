import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime("%m_%d_%Y_%H_%S")}.log"

logs_dir = os.path.join(os.getcwd(),"logs")
os.makedirs(logs_dir,exist_ok=True)

LOG_PATH_FILE = os.path.join(logs_dir,LOG_FILE)

logging.basicConfig(
    filename=LOG_PATH_FILE,
    format="[%(asctime)s]"
)