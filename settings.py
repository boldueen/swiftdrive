# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

LOGIN = os.environ.get("LOGIN")
PASSWORD = os.environ.get("PASSWORD")

DOWNLOAD_PATH  = os.environ.get("PWD") + os.environ.get("DOWNLOAD_PATH")
FILEPATH = os.environ.get("PWD") + os.environ.get("DOWNLOAD_PATH") + os.environ.get("FILENAME")
BASE_DOWNLOAD_PATH = DOWNLOAD_PATH + os.environ.get("BASE") 
PROJ_DOWNLOAD_PATH = DOWNLOAD_PATH + os.environ.get("PROJ") 
FILENAME = os.environ.get("FILENAME")

MAIL_EMAIL=os.environ.get("MAIL_EMAIL")
MAIL_PASS=os.environ.get("MAIL_PASS")

PWD = os.environ.get("PWD")
HOME = os.environ.get("HOME")
