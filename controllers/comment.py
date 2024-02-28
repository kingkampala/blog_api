from flask import jsonify, request
from models.comment import Comment

def create_comment(post_id):
    data = request.json
    content = data.get('content')
    if not content:
        return jsonify({'error': 'Content is required'}), 400
    new_comment = Comment(post_id=post_id, content=content)
    new_comment.save()
    return jsonify({'message': 'Comment created successfully', 'new_comment': {'post_id': new_comment.post_id, 'content': new_comment.content}}), 201

def get_comments_for_post(post_id):
    comments = Comment.get_comments_for_post(post_id)
    return jsonify(comments), 200

def get_comment(comment_id):
    comment = Comment.get_comment(comment_id)
    if comment:
        return jsonify(comment.to_dict()), 200
    else:
        return jsonify({'error': 'Comment not found'}), 404

def edit_comment(comment_id):
    try:
        comment_id = int(comment_id)
    except ValueError:
        return jsonify({'error': 'Invalid comment id'}), 400
    
    data = request.json
    new_content = data.get('content')
    if not new_content:
        return jsonify({'error': 'Content is required'}), 400
    comment = Comment.get_comment(comment_id)
    if comment:
        comment.update(new_content)
        return jsonify({'message': 'Comment updated successfully', 'updated_comment': {'content': comment.content}}), 200
    else:
        return jsonify({'error': 'Comment not found'}), 404

def delete_comment(comment_id):
    comment = Comment.get_comment(comment_id)
    if comment:
        comment.delete()
        return jsonify({'message': 'Comment deleted successfully'}), 200
    else:
        return jsonify({'error': 'Comment not found'}), 404
