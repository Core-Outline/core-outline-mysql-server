from dotenv import load_dotenv
from pathlib import Path
import os
from pymongo import MongoClient


env_path = Path('..', '.env')
load_dotenv(dotenv_path=env_path)

env_var = os.getenv('.env')


db_username = env_var['MONGODB_USERNAME']
db_password = env_var['MONGODB_PASSWORD']
db_database = env_var['MONGODB_DATABASE']
