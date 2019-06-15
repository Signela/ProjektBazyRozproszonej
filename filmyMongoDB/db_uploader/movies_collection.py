import pymongo


class MovieDbUploader:

    def __init__(self):
        self.myClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.myDb = self.myClient["SBD4_Filmy"]

    # INSERT
    def insert_documents_into_collection(self, collection_name, inserted_documents_list):
        collection = self.myDb[collection_name]
        collection.insert_many(inserted_documents_list)