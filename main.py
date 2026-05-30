from src.projectDL_1.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.projectDL_1.pipeline.stage_02_data_validation import DataValidationPipeline
from src.projectDL_1 import logger




try:
    logger.info(f">>>>>>> Stage Data Ingestion started <<<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage Data Ingestion completed <<<<<<<<\n\nx==========x")

    logger.info(f">>>>>>> Stage Data Validation started <<<<<<<<")

    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>> Stage Data Validation completed <<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e