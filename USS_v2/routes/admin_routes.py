from flask import Blueprint, render_template, session

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/dashboard")
def dashboard():
    if "user" not in session:
        return "Login first"
    return render_template("dashboard.html")