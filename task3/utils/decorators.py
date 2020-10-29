from functools import wraps
from loguru import logger


def tracing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.success(f'Start {func.__name__}')
        result = func(*args, **kwargs)
        logger.success(f'Finish {func.__name__}')
        return result

    return wrapper
