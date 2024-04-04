from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME = "Prepare base model"


class PrepareBaseModelTrainingPipeline :
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        Prepare_base_model_config = config.get_prepare_base_model_config()
        Prepare_base_model = PrepareBaseModel(config=Prepare_base_model_config)
        Prepare_base_model.get_base_model()
        Prepare_base_model.update_base_model()

if __name__ == 'main':
    try:
        logger.info(f"************************************")
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e
    