from flask import jsonify, request
from models.post import Post
from models.tag import Tag
from models.user import User

def create_post():
    data = request.json
    title = data.get('title')
    content = data.get('content')
    if not title or not content:
        return jsonify({'error': 'Title and content are required'}), 400
    
    tagged_usernames = extract_tagged_username(content)

    new_post = Post(title=title, content=content)
    new_post.save()

    if tagged_usernames:
        for username in tagged_usernames:
        #if not tagged_username.startswith('@'):
        #    tagged_username = f'@{tagged_username}'  # Add "@" if not present
            new_tag = Tag(post_id=new_post.id, tagged_username=username)
            new_tag.save()

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



def extract_tagged_username(content):
    # Find all occurrences of "@"
    at_indices = [i for i, char in enumerate(content) if char == '@']

    tagged_usernames = []
    # Iterate over the indices of "@" symbols
    for index in at_indices:
        # Find the next space or end of string after the "@" symbol
        end_index = content.find(' ', index)
        if end_index == -1:
            end_index = len(content)

        # Extract the username substring after the "@" symbol
        username = content[index+1:end_index]

        # Check if the extracted username exists in the database
        user = User.get_user_by_username(username)
        if user:
            tagged_usernames.append(username)
        else:
            # If the username doesn't exist, raise an error
            raise ValueError(f"User '{username}' doesn't exist")

    return ' '.join(tagged_usernames)
    