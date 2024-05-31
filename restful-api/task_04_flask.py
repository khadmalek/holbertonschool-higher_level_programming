from flask import Flask, jsonify, request

# Create a Flask application
app = Flask(__name__)

# Dictionary to store users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Route for the root of the API
@app.route('/')
def home():
    """Endpoint for the root URL."""
    return "Welcome to the Flask API!"

# Route to return a list of all usernames
@app.route('/data')
def get_data():
    """Endpoint to return a list of all usernames."""
    return jsonify(list(users.keys()))

# Route to check the status of the API
@app.route('/status')
def get_status():
    """Endpoint to check the status of the API."""
    return "OK"

# Route to get details of a specific user
@app.route('/users/<username>')
def get_user(username):
    """Endpoint to return the details of a specific user."""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

# Route to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    """Endpoint to add a new user."""
    data = request.get_json()
    username = data.get('username')
    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    else:
        users[username] = data
        return jsonify({"message": "User added", "user": data}), 201

if __name__ == '__main__':
    app.run(debug=True)
    