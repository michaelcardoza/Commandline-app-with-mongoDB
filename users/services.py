import pymongo

clientdb = pymongo.MongoClient('mongodb://localhost:27017')
db = clientdb['escuela3d']
user_collection = db['users']


class UserService:

    def __init__(self):
        pass

    @staticmethod
    def create_user(user):
        user_collection.insert_one(user.to_dict())

    @staticmethod
    def delete_user(username):
        user_collection.delete_one({"username": username})

    @staticmethod
    def update_client(username, values):
        query = {
            "username": username
        }
        new_values = {
            "$set": {
                "fullname": values['fullname'],
                "email": values['email'],
                "phone": values['phone']
            }
        }

        user_collection.update_one(query, new_values)

    @staticmethod
    def list_users():
        return user_collection.find()
