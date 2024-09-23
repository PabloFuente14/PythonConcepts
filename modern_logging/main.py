import json
import logging.config
import logging.handlers
import pathlib


logger = logging.getLogger("myapp") #create logger,if not exists


def setup_logging():
    config_file = pathlib.Path(r'modern_logging\configs\config1.json')
    with open(config_file) as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config) #charge configuration defined in config file

def main():
    setup_logging() #se inicializa configuración del logging
    logger.debug("debug message", extra ={'x':'hello'})
    logger.info("info message", extra= {"1":"lpm"})
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")    
    try:
        1/0
    except ZeroDivisionError:
        logger.exception("exception message")


if __name__ == '__main__':
    main()