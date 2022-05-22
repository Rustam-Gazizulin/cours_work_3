from flask import Blueprint, render_template, request
from app.posts.dao.posts_dao import PostsDAO

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
posts_dao = PostsDAO('data/posts.json')

@posts_blueprint.route('/')
def post_all():
    try:
        posts = posts_dao.get_all()
        return render_template('index.html', posts=posts)
    except:
        return "Что пошло не так"


@posts_blueprint.route('/posts/<int:post_pk>/')
def post_one(post_pk):

    try:
        post = posts_dao.get_by_pk(post_pk)
        return render_template('post.html', post=post)
    except:
        return "Произошло ошибка при получении поста"

    return "Страничка одного поста"


@posts_blueprint.route('/search/')
def posts_search():
    return "Поиск по постам"


@posts_blueprint.route('/users/<username>/')
def posts_by_user(username):
    return f"Поиск по имени пользователя {username}"
