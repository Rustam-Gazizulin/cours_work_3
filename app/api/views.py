from flask import Blueprint, request, jsonify

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts/')
def post_all():
    return jsonify({'content': 'Все посты тут'})


@api_blueprint.route('/api/posts/<int:post_id>/')
def post_one(post_id):
    return jsonify({'content': 'Страничка одного поста'})



