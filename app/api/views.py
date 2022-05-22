import logging

from flask import Blueprint, request, jsonify

from app.posts.dao.posts_dao import PostsDAO
from app.posts.dao.comments_dao import CommentsDAO

api_blueprint = Blueprint('api_blueprint', __name__)

posts_dao = PostsDAO('data/posts.json')
comments_dao = CommentsDAO('data/comments.json')

logger = logging.getLogger('basic')


@api_blueprint.route('/api/posts/')
def post_all():
    logger.debug('Запрошены все посты через API')
    posts = posts_dao.get_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>/')
def post_one(post_id):
    return jsonify({'content': 'Страничка одного поста'})



