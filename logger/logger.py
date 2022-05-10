import logging
import logging.config
import yaml

from constant.constant import Constant


with open(Constant.LOGGER_PATH.format(Constant.RESOURCE_PATH), "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger("access")
exc_logger = logging.getLogger("exception")
