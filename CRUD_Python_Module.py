# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username='aacuser', password='PASSWORD'): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database and the animals collection. 
        # 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
    def get_next_record_number(self):
        try:
            record = self.database.animals.find_one(sort=[("rec_num", -1)])
            if record is not None:
                return record["rec_num"] + 1
            return 1
        except Exception:
            return 1

    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None:
            try:
                if "rec_num" not in data:
                    data["rec_num"] = self.get_next_record_number()

                self.database.animals.insert_one(data)  # data should be dictionary
                return True
            except Exception:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, query):
        try:
            results = self.database.animals.find(query)
            return list(results)
        except Exception:
            return []

    # Update method to implement the U in CRUD.
    def update(self, query, data):
        if query is not None and data is not None:
            try:
                results = self.database.animals.update_many(query, data)
                return results.modified_count
            except Exception:
                return 0
        else:
            raise Exception("Nothing to update, because query or data parameter is empty")

    # Delete method to implement the D in CRUD.
    def delete(self, query):
        if query is not None:
            try:
                results = self.database.animals.delete_many(query)
                return results.deleted_count
            except Exception:
                return 0
        else:
            raise Exception("Nothing to delete, because query parameter is empty")