import pymongo


class UserService:

    def __init__(self, database):
        self.__db_client = pymongo.MongoClient(database['db_client'])
        self.__db_name = self.__db_client[database['db_name']]
        self.__user_collection = self.__db_name['users']

    def create_user(self, user):
        self.__user_collection.insert_one(user.to_dict())

    def delete_user(self, username):
        self.__user_collection.delete_one({"username": username})

    def update_client(self, username, values):
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

        self.__user_collection.update_one(query, new_values)

    def list_users(self):
        return self.__user_collection.find()

    def search_users(self, key, value):
        query = {
            key: value
        }

        return self.__user_collection.find(query)
