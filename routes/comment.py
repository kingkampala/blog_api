from flask import Blueprint
from controllers.comment import create_comment, get_comments_for_post, get_comment, edit_comment, delete_comment

# Create a Blueprint for the routes
comments_bp = Blueprint('comments', __name__)

@comments_bp.route('/comments/<int:post_id>', methods=['POST'])
def handle_create_comment(post_id):
    return create_comment(post_id)

@comments_bp.route('/comment/<int:post_id>/comments', methods=['GET'])
def handle_get_comments_for_post(post_id):
    return get_comments_for_post(post_id)

@comments_bp.route('/comments/<int:comment_id>', methods=['GET'])
def handle_get_comment(comment_id):
    return get_comment(comment_id)

@comments_bp.route('/comments/<int:comment_id>', methods=['PUT'])
def handle_edit_comment(comment_id):
    return edit_comment(comment_id)

@comments_bp.route('/comments/<int:comment_id>', methods=['DELETE'])
def handle_delete_comment(comment_id):
    return delete_comment(comment_id)
