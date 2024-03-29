from flask import Flask
from flask_cors import CORS
from app_container.controllers.data_source import data_source_controller
from app_container.controllers.query import query_controller
import os
app = Flask(__name__)
CORS(app)


app.register_blueprint(data_source_controller, url_prefix='/data-source')
app.register_blueprint(query_controller, url_prefix='/query')


if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=6001)
