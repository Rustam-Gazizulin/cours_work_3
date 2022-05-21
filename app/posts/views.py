from flask import Blueprint, render_template, request

posts_blueprint=Blueprint('posts_blueprint', __name__, template_folder='templates')

@posts_blueprint.route('/')
def post_all():
    return "Все посты тут"


@posts_blueprint.route('/posts/<int:post_id>/')
def post_one(post_id):
    return "Страничка одного поста"


@posts_blueprint.route('/')
def posts_search('/search/'):
    return "Поиск по постам"