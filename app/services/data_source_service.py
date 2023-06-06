from app.repositories.database import createClient, create, get, fetch
from config.data_source_config import data_source_table
import subprocess
import os


class DataSourceService():
    def __init__(self):
        self.db = createClient()

    def create_data_source(self, data_source):
        """
        Add code to load the csv file
        Save the csv file as file.csv in the scripts folder
        """
        os.chdir('app/scripts')
        latestCommit = subprocess.run(
            ['bash', 'dvc_upload.sh'], capture_output=True, text=True)
        data_source['hash'] = latestCommit
        return create(self.db, data_source_table, data_source)

    def get_data_source_by_id(self, data_source):
        return get(self.db, data_source_table, data_source)

    def fetch_data_source_by_parameter(self, data_source):
        return get(self.db, data_source_table, data_source)
