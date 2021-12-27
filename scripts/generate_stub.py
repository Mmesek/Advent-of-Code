import argparse, os, json
from datetime import datetime
from pytz import timezone

parser = argparse.ArgumentParser()
parser.add_argument(
    "day",
    help="Day's stub to generate",
    default=datetime.now(tz=timezone("US/Eastern")).day,
    type=int,
    choices=range(1, 26),
)
parser.add_argument("language", help="Language to generate stub for", default="python", type=str)
parser.add_argument("year", help="Year's stub to generate", type=str)
args = parser.parse_args()
if args.year == "Current":
    args.year = datetime.now(tz=timezone("US/Eastern")).year

with open("scripts/stubs.json", "r", newline="", encoding="utf-8") as file:
    languages = json.load(file)

SOLUTIONS_PATH = "solutions"
YEAR_PATH = SOLUTIONS_PATH + f"/{args.year}"
DAY_PATH = (
    YEAR_PATH
    + f"/day_{'0'+str(args.day) if int(args.day) < 10 else args.day}.{languages.get(args.language, {}).get('extension', '')}"
)

if not os.path.exists(DAY_PATH):
    if not os.path.exists(SOLUTIONS_PATH):
        os.mkdir(SOLUTIONS_PATH)
    if not os.path.exists(YEAR_PATH):
        os.mkdir(YEAR_PATH)
    with open(DAY_PATH, "w", encoding="utf-8") as file:
        file.write(languages.get(args.language, {}).get("content", "").format(day=args.day, year=args.year))
else:
    print("File already exists! Skipping...")
