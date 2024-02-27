from flask import Blueprint
from controllers.post import create_post, get_all_posts, get_post, edit_post, delete_post

# Create a Blueprint for the routes
posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/posts', methods=['POST'])
def handle_create_post():
    return create_post()

@posts_bp.route('/posts', methods=['GET'])
def handle_get_all_posts():
    return get_all_posts()

@posts_bp.route('/posts/<int:id>', methods=['GET'])
def handle_get_post(id):
    return get_post(id)

@posts_bp.route('/posts/<int:id>', methods=['PUT'])
def handle_edit_post(id):
    return edit_post(id)

@posts_bp.route('/posts/<int:id>', methods=['DELETE'])
def handle_delete_post(id):
    return delete_post(id)
