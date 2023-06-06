from flask import Blueprint, request, jsonify
from app.models.data_source import DataSource

data_source_controller = Blueprint('data_source', __name__)
dataSource = DataSource()


@data_source_controller.route('/data-source', methods=['GET'])
def fetch_data_sources():
    params = dict(request.args)
    return jsonify(dataSource.get(params))


@data_source_controller.route('/create-data-source', methods=['POST'])
def create_data_source():
    req = request.get_json()
    return jsonify(dataSource.create(req))


@data_source_controller.route('/get-data-source', methods=['GET'])
def get_data_source():
    params = dict(request.args)
    return jsonify(dataSource.get(params))
