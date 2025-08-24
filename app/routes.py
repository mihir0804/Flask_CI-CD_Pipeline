from flask import Blueprint, jsonify

bp = Blueprint('routes', __name__)

@bp.route('/hello')
def hello():
    return jsonify({"message": "Hello, World!"})
