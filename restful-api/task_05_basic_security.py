# Import necessary libraries
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt_claims
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)

# Configure secret key for JWT
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to a secure key in production
jwt = JWTManager(app)

# Initialize HTTP Basic Authentication
auth = HTTPBasicAuth()

# User data stored in memory
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("adminpassword"), "role": "admin"}
}

# HTTP Basic Authentication
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username

# JWT Authentication endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', None)
    password = data.get('password', None)
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = users.get(username, None)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid username or password"}), 401

    # Generate JWT token
    access_token = create_access_token(identity=username, additional_claims={"role": user['role']})
    return jsonify(access_token=access_token), 200

# Basic Authentication protected route
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200

# JWT Authentication protected route
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

# Admin-only route
@app.route('/admin-only')
@jwt_required()
def admin_only():
    claims = get_jwt_claims()
    if claims['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted", 200

if __name__ == "__main__":
    app.run(debug=True)
    