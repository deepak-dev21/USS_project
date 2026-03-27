from flask import Blueprint, jsonify
from services.log_service import get_logs

log_bp = Blueprint("log", __name__)

@log_bp.route("/logs")
def logs():
    return jsonify(get_logs())