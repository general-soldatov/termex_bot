import logging
from .reg import research

logger = logging.getLogger(__name__)

def prod():
    a, b = 12, 2
    c, d = 4, 0

    logger.debug('Log DEBUG')
    logger.info('Log INFO')
    logger.warning('Log WARNING')
    logger.error('Log ERROR')
    logger.critical('Log CRITICAL')

    print(research(a, b))
    print(research(c, d))