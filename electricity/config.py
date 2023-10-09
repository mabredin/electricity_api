import os

from dotenv import load_dotenv


load_dotenv()

# Settings
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG')
LOCAL_HOST = os.getenv('LOCAL_HOST')
SERVER_HOST = os.getenv('SERVER_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER_NAME = os.getenv('DB_USER_NAME')
DB_USER_PASSWORD = os.getenv('DB_USER_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
SESSION_COOKIE_AGE = os.getenv('SESSION_COOKIE_AGE', 1209600)
