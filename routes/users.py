from flask import Blueprint, request, jsonify
from m import add_user, fetch_user

users_bp = Blueprint('users', __name__)

@users_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    add_user(name, email, password)
    return jsonify({"message": "User registered successfully!"}), 201

@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = fetch_user(email, password)
    print(user)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "Invalid credentials"}), 401
