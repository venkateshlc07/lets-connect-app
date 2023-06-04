import os
from pathlib import Path
from dotenv import load_dotenv

# set path to env file
env_path = Path('.')/ '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    """ Set Flask configuration vars from .env file."""

    # Load environment variables
    TESTING = os.getenv('TESTING')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SERVER = os.getenv('SERVER')
