import json
import os
import qrcode

USER_DB = 'data/users.json'

def load_users():
    if not os.path.exists(USER_DB):
        return {}
    with open(USER_DB, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USER_DB, 'w') as f:
        json.dump(users, f)

def register_user(email, password):
    users = load_users()
    if email in users:
        raise ValueError("User already exists.")
    users[email] = {"password": password, "qr_code": generate_qr_code(email)}
    save_users(users)

def generate_qr_code(email):
    qr = qrcode.make(email)
    qr_path = f"data/qr_codes/{email}.png"
    qr.save(qr_path)
    return qr_path

def login_user(email, password):
    users = load_users()
    if email not in users or users[email]["password"] != password:
        raise ValueError("Invalid credentials.")
    return users[email]