from flask import Blueprint, request, jsonify
from app_container.models.query import Query

query_controller = Blueprint('query', __name__)
query = Query()


@query_controller.route('/', methods=['GET'])
def fetch_queries():
    print(request.args)
    params = dict(request.args)
    obj = query.fetch(params)
    print(obj)
    obj = [{**item, "_id": str(item['_id'])} for item in obj]
    return jsonify(obj)


@query_controller.route('/create-query', methods=['POST'])
def create_query():
    req = request.get_json()
    return jsonify(str(query.create(req)))


@query_controller.route('/get-query', methods=['GET'])
def get_query():
    params = dict(request.args)
    obj = query.get(params)
    obj['_id'] = str(obj['_id'])
    return jsonify(obj)


@query_controller.route('/execute', methods=['POST'])
def execute_query():
    req = request.get_json()
    return jsonify(query.execute(req))
