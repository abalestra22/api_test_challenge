import logging
import coloredlogs

# Create and configure logger
logger = logging.getLogger("WorldSys API")
logger.setLevel(logging.DEBUG)

# Format: level | name | message
coloredlogs.install(
    level='DEBUG',
    logger=logger,
    fmt='%(asctime)s [%(levelname)s] %(name)s - %(message)s',
    datefmt='%H:%M:%S'
)
