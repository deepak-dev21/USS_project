from flask import Blueprint, render_template, request, redirect, session
from services.auth_service import register_user, login_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def home():
    return render_template("login.html")

@auth_bp.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        register_user(request.form["username"], request.form["password"])
        return redirect("/")
    return render_template("register.html")

@auth_bp.route("/login", methods=["POST"])
def login():
    user = login_user(request.form["username"], request.form["password"])
    if user:
        session["user"] = user[1]
        return redirect("/dashboard")
    return "Invalid login"