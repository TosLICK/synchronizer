from argparse import ArgumentParser


class Config:
    def __init__(self, src_folder, dstn_folder, log_file, interval_sec):
        self.src_folder = src_folder
        self.dstn_folder = dstn_folder
        self.log_file = log_file
        self.interval_sec = interval_sec


parser = ArgumentParser()
parser.add_argument("src_folder", type=str, help="path to the source folder")
parser.add_argument("dstn_folder", type=str, help="path to the destination folder")
parser.add_argument("interval_sec", type=int, help="period of synchronization, secs")
parser.add_argument("log_file", type=str, help="path to the log file")

args = parser.parse_args()

def parse():
    return Config(args.src_folder, args.dstn_folder, args.log_file, args.interval_sec)