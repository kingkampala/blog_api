from flask import Blueprint
from controllers.user import create_user, get_all_users, get_user, edit_user, delete_user

# Create a Blueprint for the routes
users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['POST'])
def handle_create_user():
    return create_user()

@users_bp.route('/users', methods=['GET'])
def handle_get_all_users():
    return get_all_users()

@users_bp.route('/users/<int:id>', methods=['GET'])
def handle_get_user(id):
    return get_user(id)

@users_bp.route('/users/<int:id>', methods=['PUT'])
def handle_edit_user(id):
    return edit_user(id)

@users_bp.route('/users/<int:id>', methods=['DELETE'])
def handle_delete_user(id):
    return delete_user(id)
