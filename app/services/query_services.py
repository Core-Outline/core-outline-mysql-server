from app.repositories.database import createClient, create, get, fetch
from config.query_config import query_actions, queries_table
from app.services.data_source_service import DataSourceService
import pandas as pd
import subprocess
import pyodbc


class QueryService():
    def __init__(self):
        self.db = createClient()

    def create_query(self, query):
        return create(self.db, queries_table, query)

    def get_query(self, query):
        return get(self.db, queries_table, query)

    def fetch_queries(self, query):
        return get(self.db, queries_table, query)

    def execute_query(self, query):
        dataSourceService = DataSourceService()
        dataSource = dataSourceService.get_data_source_by_id(
            {'_id': query['data_source_id']})
        queries = query.queries
        table = query.reference_table
        reference_columns = query.reference_columns
        database = query.database
        username = dataSource.user_name
        password = dataSource.password
        server = dataSource.server

        conn = pyodbc.connect("Driver={SQL Server};"
                              f"Server={server};"
                              f"Database={database};"
                              f"uid={username};"
                              f"pwd={password}")

        query_string = f"SELECT {','.join(reference_columns)} WHERE"
        for q in queries:
            column = q.keys[0]
            operation = q[column].keys[0]
            value = q[column][operation]

            query_string = query_string + \
                f'{column} {query_actions[operation]} value'

        df = pd.read_sql(query_string, con=conn)
        return df
