from models.user import User
from models.follow import Follow
from flask import jsonify

def follow_user(follower_id, followed_id):
    follower = User.get_user(follower_id)
    followed = User.get_user(followed_id)

    if not follower:
        return jsonify({'error': 'Follower not found'}), 404
    if not followed:
        return jsonify({'error': 'User to follow not found'}), 404

    # Check if the follower is already following the user
    is_follow = Follow.is_following(follower.id, followed.id)

    if is_follow:
        # If already following, unfollow the user
        king = Follow(follower.id, followed.id)
        king.delete()
        return jsonify({'message': f'You({follower.username}) have unfollowed {followed.username}'}), 200
    else:
        # If not following, follow the user
        new_follow = Follow(follower_id=follower.id, followed_id=followed.id)
        new_follow.save()
        return jsonify({'message': f'You({follower.username}) are now following {followed.username}'}), 200
