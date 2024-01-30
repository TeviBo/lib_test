import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('../logs/'),
                    log.StreamHandler()
                ])


def log_data(logger, log_message: str) -> None:
    try:
        logger.error(log_message)
    except Exception as e:
        logger.error(f'Error: {e}')
