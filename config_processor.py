from cmd_args_parser import Config
import os
import logger


def __is_folder(path: str) -> bool:
    return os.path.isdir(path)

def __try_create_folder(path: str) -> bool:
    try:
        os.mkdir(path)
        return True
    except OSError:
        return False

def __is_src_path_valid(path: str) -> bool:
    if __is_folder(path):
        return True
    else:
        logger.instance.error("Source path '%s' does not exist", path)
        return False

def __is_dstn_path_valid(src_path: str, dstn_path: str) -> bool:
    if __is_folder(dstn_path) and os.path.abspath(src_path) != os.path.abspath(dstn_path) or __try_create_folder(dstn_path):
        return True
    elif os.path.abspath(src_path) == os.path.abspath(dstn_path):
        logger.instance.error("Destination folder is the same as the source folder")
    else:
        logger.instance.error("Destination folder '%s' does not exist and could not be created", dstn_path)
    return False

def __is_interval_sec_valid(interval: int) -> bool:
    if interval > 0:
        return True
    else:
        logger.instance.error("Interval '%d' must be greater than zero", interval)
        return False


def validate(config_obj: Config) -> None:
    if not __is_src_path_valid(config_obj.src_folder) or not __is_dstn_path_valid(config_obj.src_folder
    , config_obj.dstn_folder) or not __is_interval_sec_valid(config_obj.interval_sec):
        raise ValueError("Invalid input")