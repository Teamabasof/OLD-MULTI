import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

STAT_STICK = os.environ.get("STAT_STICK", "CAACAgUAAxkBAAIMMmJ_Y17NRUpBJgLhsqUTTRNilYxAAAKeBAACf7TwVxZUQiDRe7p1HgQ")

PICS = os.environ.get("PICS", "https://telegra.ph/file/34fd203eb89fd747ffb57.jpg").split()

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMIN', '900873119').split()]

DB_URL = os.environ.get("DB_URL", "")

DELAY = int(os.environ.get("DELAY", "1"))

FORCE_SUB = os.environ.get("FORCE_SUB", None)           

HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")

LOG = int(os.environ.get("LOG_CHANNEL", -100))
