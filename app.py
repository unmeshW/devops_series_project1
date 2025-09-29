from flask import Flask
import datetime

app = Flask(__name__)  # <-- Must be defined before @app.route

@app.route('/')
def home():
    return """
    <html>
    <head><title>My WebApp</title></head>
    <body>
    <h1>Hello all, Welcome to my WebApp..!!!</h1>
    <p>Check <a href="/health">Health Status</a> or <a href="/users">Users List</a></p>
    </body>
    </html>
    """

@app.route('/health')
def health_check():
    return """
    <html>
    <body>
    <h2>Status: All Healthy</h2>
    <p>Timestamp: {}</p>
    </body>
    </html>
    """.format(datetime.datetime.utcnow())

@app.route('/users')
def get_users():
    return """
    <html>
    <body>
    <h2>Users List</h2>
    <ul>
      <li>Unmesh - Cloud support engineer</li>
      <li>Tony - Site reliability engineer</li>
    </ul>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
