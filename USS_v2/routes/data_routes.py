from flask import Blueprint, request, jsonify
from services.encryption_service import encrypt, decrypt
from services.log_service import add_log
from services.anomaly_service import detect_anomaly

data_bp = Blueprint("data", __name__)

messages = []

@data_bp.route("/send", methods=["POST"])
def send():
    data = request.json["data"]
    secure = request.json["secure"]

    if detect_anomaly(data):
        add_log("Anomaly detected: " + data, "alert")

    if secure:
        enc = encrypt(data)
        dec = decrypt(enc)
        add_log(enc, "encrypted")
    else:
        enc = None
        dec = data
        add_log(data, "plain")

    # ✅ STORE MESSAGE
    msg = {
        "original": data,
        "encrypted": enc,
        "decrypted": dec
    }
    messages.append(msg)

    # ✅ RETURN AFTER STORING
    return jsonify({
        "status": "sent",
        "message": msg
    })

@data_bp.route("/get_messages", methods=["GET"])
def get_messages():
    return jsonify(messages)