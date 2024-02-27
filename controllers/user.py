from flask import jsonify, request
from models.user import User
import bcrypt

def create_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    existing_user = User.get_user_by_username(username)
    existing_email = User.get_user_by_email(email)
    if existing_user:
        return jsonify({'error': 'Username already exists'}), 400
    elif existing_email:
        return jsonify({'error': 'Email already exists'}), 400

    if not username or not email or not password:
        return jsonify({'error': 'Username, email, and password are required'}), 400
    hash_pwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    new_user = User(username=username, email=email, password=hash_pwd)
    new_user.save()
    return jsonify({'message': 'User created successfully', 'new_user': {'username': new_user.username, 'email': new_user.email, 'password': new_user.password}}), 201

def get_all_users():
    users = User.get_all_users()
    user_data = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify(user_data), 200

def get_user(id):
    user = User.get_user(id)
    user_data = [{'id': user.id, 'username': user.username, 'email': user.email}]
    if user:
        return jsonify(user_data), 200 #.to_dict()
    else:
        return jsonify({'error': 'User not found'}), 404
    
def edit_user(id):
    try:
        id = int(id)
    except ValueError:
        return jsonify({'error': 'Invalid id'}), 400
    
    data = request.json
    new_username = data.get('username')
    new_email = data.get('email')
    new_password = data.get('password')
    if not new_username or not new_email or not new_password:
        return jsonify({'error': 'Username, email, and password are required'}), 400
    hash_pwd = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    user = User.get_user(id)
    if user:
        user.update(new_username, new_email, hash_pwd)
        return jsonify({'message': 'User updated successfully', 'updated_user': {'username': user.username, 'email': user.email, 'password': user.password}}), 200
    else:
        return jsonify({'error': 'User not found'}), 404
    
def delete_user(id):
    user = User.get_user(id)
    if user:
        user.delete()
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404
