from app_container.repositories.database import createClient, create, get, fetch
from config.data_source_config import data_source_table
import pyodbc
import pandas as pd



class DataSourceService:
    def __init__(self):
        self.db = createClient()

    def create_data_source(self, data_source):
        return create(self.db, data_source_table, data_source)

    def get_data_source_by_id(self, data_source):
        return get(self.db, data_source_table, data_source)

    def fetch_data_source_by_parameter(self, data_source):
        return fetch(self.db, data_source_table, data_source)

    def get_data_source_details(self, data_source):
        dataSrc = self.get_data_source_by_id({"_id": data_source['_id']})
        username = dataSrc['username']
        password = dataSrc['password']
        server = dataSrc['server']
        
        result = {}
        conn = pyodbc.connect("Driver={SQL Server};"
                              f"Server={server};"
                              f"uid={username};"
                              f"pwd={password}")
        
        dbs = pd.read_sql("SET NOCOUNT ON;SELECT name FROM sys.databases", con = conn)['name'].values
        dbs = [i for i in dbs]
        print(dbs)
        for db in dbs:
            result[db] = {}
            tlbs_cols = pd.read_sql(f"SELECT TABLE_NAME, COLUMN_NAME FROM {db}.INFORMATION_SCHEMA.COLUMNS", con=conn)
            tlbs_cols = tlbs_cols.groupby('TABLE_NAME')
            for name, group in tlbs_cols:
                result[db][name] = [i for i in group['COLUMN_NAME'].values]

        return result