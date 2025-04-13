import logging

class Log_Maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\logs\\ebs.log",format='%(asctime)s:%(levelname)s:%(message)s', datefmt="%Y-%m-%d_%H-%M-%S",force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger