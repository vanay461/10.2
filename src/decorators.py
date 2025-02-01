import functools
import logging

def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            handler = logging.FileHandler(filename) if filename else logging.StreamHandler()
            handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
            logger.addHandler(handler)

            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")
                raise
            finally:
                logger.removeHandler(handler)
                handler.close()  # Закрываем файл!

        return wrapper
    return decorator