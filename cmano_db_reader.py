# Python environment cmano

import sqlalchemy
import os
from dotenv import load_dotenv
load_dotenv()

class CmanoDB:
    '''
    Functions to read from the CMANO SQLite database
    '''

    def __init__(self):
        self.db_path = os.getenv("CMANO_DB")
        self.cmano_db_engine = sqlalchemy.create_engine('sqlite:///' + self.db_path) 
        self.cmano_db_cx = self.cmano_db_engine.connect()
        print("Connection to CMANO database established")

    def db_query(self, query):
        '''
        Function to query CMANO database using SQLAlchemy connection. Function creates a 
        query cursor object, executes the query, and then closes the cursor connection.
        query: SQL query text to query CMANO database
        '''
        query_results = self.cmano_db_cx.execute(query)
        return query_results

    def db_close(self):
        '''
        Function to dispose of the engine and close the connection to the CMANO database.
        '''
        self.cmano_db_cx.close()
        self.cmano_db_engine.dispose()
        print("Connection to CMANO database closed")