import argparse
import importlib
from datetime import datetime
from pytz import timezone

parser = argparse.ArgumentParser()
parser.add_argument("--day", help="Day's solution to run", default=datetime.now(tz=timezone("US/Eastern")).day, type=str)#, choices=range(1,26))
parser.add_argument("--year", help="Year's solution to run", default=datetime.now(tz=timezone("US/Eastern")).year, type=str)
args = parser.parse_args()
_part = ""
if len(args.day) > 6:
    _part = args.day[6:]
    args.day = args.day[:6]
args.day = int(args.day.strip("day_"))
args.year = int(args.year.replace("/",".").replace("\\",".").split(".")[-1])
importlib.import_module(f"solutions.{args.year}.day_{'0'+str(args.day) if args.day < 10 else args.day}" + _part, ".")
