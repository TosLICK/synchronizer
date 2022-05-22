import cmd_args_parser
import logger
import config_processor
import schedule
import time
import dirsync


is_sync_running: bool = False

def main():
    config_obj = cmd_args_parser.parse()
    logger.initialize_logger(config_obj.log_file)

    def synchronize():
        config_processor.validate(config_obj)
        global is_sync_running
        if not is_sync_running:
            is_sync_running = True
            try:
                logger.instance.info("Starting sync")
                dirsync.sync(config_obj.src_folder, config_obj.dstn_folder, "sync", verbose=True, purge=True, logger=logger.instance)
                logger.instance.info("Sync finished")
            except Exception:
                logger.instance.error("Sync failed")
            finally:
                is_sync_running = False

    schedule.every(config_obj.interval_sec).seconds.do(synchronize)

    while True:
        schedule.run_pending()
        time.sleep(1)
   
main()
