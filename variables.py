import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

STAT_STICK = os.environ.get("STAT_STICK", "CAACAgUAAxkBAAIMMmJ_Y17NRUpBJgLhsqUTTRNilYxAAAKeBAACf7TwVxZUQiDRe7p1HgQ")

PICS = os.environ.get("PICS", "https://telegra.ph/file/34fd203eb89fd747ffb57.jpg").split()

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMIN', '').split()]

DB_URL = os.environ.get("DB_URL","")
