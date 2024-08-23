import logging

logger = logging.getLogger(__name__)

def research(dividend: int | float, devider: int | float):
    logger.debug('Log DEBUG')
    logger.info('Log INFO')
    logger.warning('Log WARNING')
    logger.error('Log ERROR')
    logger.critical('Log CRITICAL')

    try:
        num = dividend / devider
        return num
    except ZeroDivisionError:
        logger.exception('Division by 0')