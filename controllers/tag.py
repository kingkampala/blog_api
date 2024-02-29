from flask import jsonify, request
from models.tag import Tag

def create_tag_for_post(post_id):
    data = request.json
    tagged_username = data.get('tagged_username')
    if not tagged_username:
        return jsonify({'error': 'Tagged username is required'}), 400
    if not tagged_username.startswith('@'):
        tagged_username = f'@{tagged_username}'
    new_tag = Tag(post_id=post_id, tagged_username=tagged_username)
    new_tag.save()
    return jsonify({'message': 'Tag created successfully'}), 201

def create_tag_for_comment(comment_id):
    data = request.json
    tagged_username = data.get('tagged_username')
    if not tagged_username:
        return jsonify({'error': 'Tagged username is required'}), 400
    if not tagged_username.startswith('@'):
        tagged_username = f'@{tagged_username}'
    new_tag = Tag(comment_id=comment_id, tagged_username=tagged_username)
    new_tag.save()
    return jsonify({'message': 'Tag created successfully'}), 201
