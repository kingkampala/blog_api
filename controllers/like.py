from models.like import Like
from flask import jsonify

def like_post(user_id, post_id):
    like = Like.get_like_by_user_and_post(user_id, post_id)
    if like:
        kampala = Like(user_id=user_id, post_id=post_id)
        kampala.delete()
        return jsonify({'message': 'Post unliked successfully'}), 200
    else:
        new_like = Like(user_id=user_id, post_id=post_id)
        new_like.save()
        return jsonify({'message': 'Post liked successfully'}), 200
