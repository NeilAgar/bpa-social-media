import os
from pymongo import MongoClient

mongo = MongoClient(os.getenv("MONGODB_URL"))
db = mongo[os.getenv("DATABASE_NAME")]
