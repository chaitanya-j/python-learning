import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "first_log.log",
                    level = logging.WARNING,
                    format = LOG_FORMAT,
                    )

logger = logging.getLogger()

logger.debug("First Message.")
logger.info("Second Message.")
logger.warning("Third Message.")
logger.error("Fourtho Message.")

print(logger.level)
