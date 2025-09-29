from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    html = """
    <html>
        <head>
            <title>My WebApp</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #f4f4f9; text-align: center; padding: 50px; }
                h1 { color: #333; }
                p { color: #555; font-size: 18px; }
                a { text-decoration: none; color: #007bff; }
            </style>
        </head>
        <body>
            <h1>Welcome to My WebApp!</h1>
            <p>Hello all, enjoy exploring my website. 🚀</p>
            <p>Check <a href="/health">Health Status</a> or <a href="/users">Users List</a></p>
        </body>
    </html>
    """
    return render_template_string(html)

# Health page
@app.route('/health')
def health_check():
    html = f"""
    <html>
        <head>
            <title>Health Check</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #e0f7fa; text-align: center; padding: 50px; }}
                h2 {{ color: green; }}
                p {{ font-size: 18px; color: #333; }}
            </style>
        </head>
        <body>
            <h2>Status: All Healthy ✅</h2>
            <p>Timestamp (UTC): {datetime.datetime.utcnow()}</p>
            <p><a href="/">Back to Home</a></p>
        </body>
    </html>
    """
    return render_template_string(html)

# Users page
@app.route('/users')
def get_users():
    users = [
        {"id": 101, "name": "Unmesh", "role": "Cloud Support Engineer"},
        {"id": 102, "name": "Tony", "role": "Site Reliability Engineer"}
    ]
    
    html = """
    <html>
        <head>
            <title>Users List</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #fff3e0; padding: 50px; }
                table { width: 50%; margin: auto; border-collapse: collapse; }
                th, td { border: 1px solid #ddd; padding: 10px; text-align: center; }
                th { background-color: #007bff; color: white; }
                tr:nth-child(even) { background-color: #f2f2f2; }
                h2 { text-align: center; }
                a { display: block; text-align: center; margin-top: 20px; color: #007bff; }
            </style>
        </head>
        <body>
            <h2>Users List</h2>
            <table>
                <tr><th>ID</th><th>Name</th><th>Role</th></tr>
                {% for user in users %}
                    <tr>
                        <td>{{ user.id }}</td>
                        <td>{{ user.name }}</td>
                        <td>{{ user.role }}</td>
                    </tr>
                {% endfor %}
            </table>
            <a href="/">Back to Home</a>
        </body>
    </html>
    """
    
    return render_template_string(html, users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
