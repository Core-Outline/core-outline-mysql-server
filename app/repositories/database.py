from pymongo import MongoClient
from bson.objectid import ObjectId

from config.database_config import db_username, db_password, db_database


def createClient():
    client = MongoClient(
        f'mongodb+srv://{db_username}:{db_password}@cluster0.rfams.mongodb.net')

    return client[db_database]


def create(db, collection, document):
    return db[collection].insert_one(document)


def get(db, collection, condition):
    return db[collection].find_one({'_id': ObjectId(condition._id)})


def fetch(db, collection, array_of_conditions):
    docs = db[collection].find({'$and': array_of_conditions})
    return [doc for doc in docs]
