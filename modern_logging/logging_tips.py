import json
import logging.config
import logging.handlers
import pathlib


logger = logging.getLogger("myapp")


def setup_logging():
    config_file = pathlib.Path(r'modern_logging\config1.json')
    with open(config_file) as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)

def main():
    setup_logging()
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")    
    try:
        1/0
    except ZeroDivisionError:
        logger.exception("exception message")


if __name__ == '__main__':
    main()