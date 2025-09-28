from flask import Flask

app = Flask(__name__)

@app.route("/intro")
def myintro():
    return "I'm Unmesh, actively looking for cloud/devops roles"

@app.route("/info")
def info():
    return "This is the 1st prpject from the Devops-series"

app.run(host="0.0.0.0")
