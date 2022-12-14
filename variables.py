import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

STAT_STICK = os.environ.get("STAT_STICK", "CAACAgUAAxkBAAIMMmJ_Y17NRUpBJgLhsqUTTRNilYxAAAKeBAACf7TwVxZUQiDRe7p1HgQ")

PICS = os.environ.get("PICS", "https://telegra.ph/file/34fd203eb89fd747ffb57.jpg").split()

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '900873119').split()]

DB_URL = os.environ.get("DB_URL", "")

DELAY = int(os.environ.get("DELAY", "1"))

FORCE_SUB = os.environ.get("FORCE_SUB", None)           

HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")
 
log_channel = environ.get("LOG_CHANNEL")

LOG_CHANNEL = int(log_channel) if log_channel and id_pattern.search(log_channel) else None

LOG_TEXT = """<i><u>ποΈβπ¨οΈUSER DETAILS</u>

β ID : <code>{id}</code>
β DC : <code>{dc_id}</code>
β First Name : <code>{first_name}<code>
β UserName : @{username}

By = {bot}</i>"""


B_TEXT = """π ΚΚα΄α΄α΄α΄α΄κ±α΄ κ±α΄α΄Κα΄α΄α΄ π 
β­ββββββββββββββββββ£
β£βͺΌπ― α΄α΄α΄α΄Κ - <code>{tot}</code>
β£βͺΌβοΈ α΄α΄Ι΄α΄ - <code>{success}</code>
β£βͺΌβοΈ κ°α΄ΙͺΚα΄α΄ - <code>{failed}</code>
β°ββββββββββββββββββ£ """









