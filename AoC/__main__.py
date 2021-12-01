import argparse
import importlib
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-day", help="Day's solution to run", default=datetime.now().day, type=int, choices=range(1,26))
args = parser.parse_args()

importlib.import_module(f"AoC.solutions.day_{'0'+str(args.day) if args.day < 10 else args.day}", ".")
