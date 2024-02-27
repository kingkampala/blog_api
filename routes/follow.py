from flask import Blueprint
from controllers.follow import follow_user

# Create a Blueprint for the routes
follow_bp = Blueprint('follow', __name__)

@follow_bp.route('/follow/<int:follower_id>/<int:followed_id>', methods=['POST'])
def handle_follow_user(follower_id, followed_id):
    return follow_user(follower_id, followed_id)