from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

USER_SERVICE_URL = 'http://localhost:5000'  # Assuming User Service runs on port 5000

@app.route('/create_order', methods=['POST'])
def create_order():
    data = request.get_json()
    username = data['username']
    # Call User Service to validate user (example)
    try:
        response = requests.post(f'{USER_SERVICE_URL}/login', json={'username': username, 'password': data.get('password', 'default_password')})
        if response.status_code == 200:
            return jsonify({'message': f'Order created for user {username}'}), 201
        else:
            return jsonify({'message': 'User authentication failed'}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'message': f'Error connecting to User Service: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
