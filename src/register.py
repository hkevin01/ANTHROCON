from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)

# Mock database
users_db = {}

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    email = data['email']
    password = data['password']
    if email in users_db:
        return jsonify({'message': 'User already exists'}), 400
    hashed_password = generate_password_hash(password, method='sha256')
    user_id = str(uuid.uuid4())
    users_db[email] = {
        'user_id': user_id,
        'email': email,
        'password': hashed_password,
        'qr_code': f"https://yourapp.com/user/{user_id}"
    }
    return jsonify({'message': 'User registered successfully', 'user_id': user_id}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']
    user = users_db.get(email)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'message': 'Invalid credentials'}), 401
    return jsonify({'message': 'Login successful', 'user_id': user['user_id']}), 200

if __name__ == '__main__':
    app.run(debug=True)