from flask import Flask
from routes.auth_routes import auth_bp
from routes.data_routes import data_bp
from routes.admin_routes import admin_bp
from routes.log_routes import log_bp
from services.db_service import init_db
app = Flask(__name__)
app.secret_key = "supersecretkey"

app.register_blueprint(auth_bp)
app.register_blueprint(data_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(log_bp)
init_db()
if __name__ == "__main__":
    app.run(debug=True)