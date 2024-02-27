from flask import Blueprint
from controllers.like import like_post

# Create a Blueprint for the routes
like_bp = Blueprint('like', __name__)

@like_bp.route('/like/<int:user_id>/<int:post_id>', methods=['POST'])
def handle_like_post(user_id, post_id):
    return like_post(user_id, post_id)
