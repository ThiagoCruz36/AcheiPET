import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, 'config.env'))

DBNAME = os.getenv("DB_NAME", "achei_pet")
USER = os.getenv("DB_USER", "postgre")
PASSWORD = os.getenv("DB_PASS", "123456")
HOST = os.getenv("DB_HOST", "localhost")
PORT = os.getenv("DB_PORT", "5432")