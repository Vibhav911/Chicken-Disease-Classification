import os
import sys
import logging
from datetime import datetime

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s:]"
log_dir = "logs"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_filepath = os.path.join(log_dir,LOG_FILE)
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=log_filepath,
    level=logging.INFO, 
    format=logging_str
)

logger = logging.getLogger("ChickenDiseaseProject")


