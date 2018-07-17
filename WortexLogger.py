import logging
import config

logging.basicConfig(filename=config.settings['LOG_LOCATION'], level=logging.INFO)
logging.info('Started')
