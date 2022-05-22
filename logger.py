import logging


instance: logging.Logger = None

def initialize_logger(log_file: str) -> None:
    # create logger
    my_logger = logging.getLogger('synchronizer')
    my_logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch2 = logging.FileHandler(log_file)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)
    ch2.setFormatter(formatter)

    # add ch to logger
    my_logger.addHandler(ch)
    my_logger.addHandler(ch2)

    global instance
    instance = my_logger
