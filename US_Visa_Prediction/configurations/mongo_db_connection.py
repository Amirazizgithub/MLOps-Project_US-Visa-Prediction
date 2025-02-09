
import sys
from pymongo import MongoClient
from US_Visa_Prediction.constants import DATABASE_NAME, MONGODB_URI
from US_Visa_Prediction.logger import logging
from US_Visa_Prediction.exceptions import USvisaException
import certifi

ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = MONGODB_URI
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URI} is not set.")
                MongoDBClient.client = MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")
        except Exception as e:
            raise USvisaException(e,sys)
        
    def mongodb_collections(self):
        return self.database.list_collection_names()

# MongoDBClient().mongodb_collections()