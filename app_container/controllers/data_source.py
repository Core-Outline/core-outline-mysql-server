from flask import Blueprint, request, jsonify
from app_container.models.data_source import DataSource

data_source_controller = Blueprint('data_source', __name__)
dataSource = DataSource()


@data_source_controller.route('/', methods=['GET'])
def fetch_data_sources():
    params = dict(request.args)
    print(params)
    obj = dataSource.fetch(params)
    obj = [{**item, "_id": str(item['_id'])} for item in obj]
    return jsonify(obj)


@data_source_controller.route('/create-data-source', methods=['POST'])
def create_data_source():
    print(request.data)
    req = request.get_json()
    print(req)
    req['type'] = 'mysql'
    return jsonify(dataSource.create(req))


@data_source_controller.route('/get-data-source', methods=['GET'])
def get_data_source():
    params = dict(request.args)
    obj = dataSource.get(params)
    obj['_id'] = str(obj['_id'])
    return jsonify(obj)

@data_source_controller.route('/get-db-columns-tables', methods=['GET'])
def get_data_source_details():
    params = dict(request.args)
    obj = dataSource.get_details(params)
    print(obj)
    return jsonify(obj)