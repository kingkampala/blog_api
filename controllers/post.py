from flask import jsonify, request
from models.post import Post

def create_post():
    data = request.json
    title = data.get('title')
    content = data.get('content')
    if not title or not content:
        return jsonify({'error': 'Title and content are required'}), 400
    new_post = Post(title=title, content=content)
    new_post.save()
    return jsonify({'message': 'Post created successfully', 'new_post': {'title': new_post.title, 'content': new_post.content}}), 201

def get_all_posts():
    posts = Post.get_all_posts()
    return jsonify(posts), 200

def get_post(id):
    post = Post.get_post(id)
    if post:
        return jsonify(post.to_dict()), 200
    else:
        return jsonify({'error': 'Post not found'}), 404
    
def edit_post(id):
    try:
        id = int(id)
    except ValueError:
        return jsonify({'error': 'Invalid id'}), 400
    
    data = request.json
    new_title = data.get('title')
    new_content = data.get('content')
    if not new_title or not new_content:
        return jsonify({'error': 'Title and content are required'}), 400
    post = Post.get_post(id)
    if post:
        post.update(new_title, new_content)
        return jsonify({'message': 'Post updated successfully', 'updated_post': {'title': post.title, 'content': post.content}}), 200
    else:
        return jsonify({'error': 'Post not found'}), 404
    
def delete_post(id):
    post = Post.get_post(id)
    if post:
        post.delete()
        return jsonify({'message': 'Post deleted successfully'}), 200
    else:
        return jsonify({'error': 'Post not found'}), 404
    