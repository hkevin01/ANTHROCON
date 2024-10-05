import qrcode

def generate_qr_code(email):
    qr = qrcode.make(email)
    qr_path = f"data/qr_codes/{email}.png"
    qr.save(qr_path)
    return qr_path