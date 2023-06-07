from app.repositories.database import createClient, create, get, fetch
from config.data_source_config import data_source_table
import subprocess
import os


class DataSourceService():
    def __init__(self):
        self.db = createClient()

    def create_data_source(self, data_source):
        return create(self.db, data_source_table, data_source)

    def get_data_source_by_id(self, data_source):
        return get(self.db, data_source_table, data_source)

    def fetch_data_source_by_parameter(self, data_source):
        return get(self.db, data_source_table, data_source)
