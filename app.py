from flask import Flask, jsonify
import random, datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello all, Welcome to my WebApp..!!!"
    })

@app.route('/health')
def health_check():
    return jsonify({"status": "All Healthy", "timestamp": str(datetime.datetime.utcnow())})

@app.route('/api/users')
def get_users():
    users = [
        {"id": 101, "name": "Unmesh", "role": "Cloud support engineer"},
        {"id": 102, "name": "Tony", "role": "Site reliability engineer"}
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
