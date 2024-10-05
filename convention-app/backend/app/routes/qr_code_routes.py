from flask import Blueprint, jsonify

qr_code_bp = Blueprint('qr_code', __name__)

@qr_code_bp.route('/qr_code/<email>', methods=['GET'])
def get_qr_code(email):
    qr_code_path = f"data/qr_codes/{email}.png"
    return jsonify({"qr_code_path": qr_code_path}), 200