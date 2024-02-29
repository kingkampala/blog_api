from flask import Blueprint
from controllers.tag import create_tag_for_post, create_tag_for_comment

# Create a Blueprint for the routes
tag_bp = Blueprint('tags', __name__)

@tag_bp.route('/posts/<int:post_id>/tags', methods=['POST'])
def handle_create_tag_for_post(post_id):
    return create_tag_for_post(post_id)

@tag_bp.route('/comments/<int:comment_id>/tags', methods=['POST'])
def handle_create_tag_for_comment(comment_id):
    return create_tag_for_comment(comment_id)
