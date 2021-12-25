import argparse
import importlib
from datetime import datetime
from pytz import timezone

parser = argparse.ArgumentParser()
parser.add_argument("-day", help="Day's solution to run", default=datetime.now(tz=timezone("US/Eastern")).day, type=int, choices=range(1,26))
args = parser.parse_args()

importlib.import_module(f"AoC.solutions.day_{'0'+str(args.day) if args.day < 10 else args.day}", ".")
