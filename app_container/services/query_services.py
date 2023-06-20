from app_container.repositories.database import createClient, create, get, fetch
from config.query_config import query_actions, queries_table
from app_container.services.data_source_service import DataSourceService
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
        return fetch(self.db, queries_table, query)

    def execute_query(self, query):
        print("ser", query.keys())
        queries = query['queries']
        table = query['reference_table']
        reference_column = query['reference_column']
        database = query['database']
        username = query['username']
        password = query['password']
        server = query['server']

        conn = pyodbc.connect("Driver={SQL Server};"
                              f"Server={server};"
                              f"Database={database};"
                              f"uid={username};"
                              f"pwd={password}")

        query_string = f"SELECT * FROM {table} WHERE "
        for q in queries:
            column = [c for c in q.keys()][0]
            operation = [b for b in q[column].keys()][0]
            value = q[column][operation]

            query_string = query_string + \
                f'{column} {query_actions[operation]} {value}'

        df = pd.read_sql(query_string, con=conn)
        df = df.to_dict()
        return df
