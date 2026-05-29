from src.projectDL_1.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.projectDL_1 import logger



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e