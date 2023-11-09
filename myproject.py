from flask import Flask, request
from index import dash_app

server = Flask(__name__)

@server.route("/dashboard")
def dashboard():
    return dash_app.layout()

@server.route('/')
def home():
    return "<h1 style='color:blue'>Hello There!</h1"

if __name__ == "__main__":
    server.run(host='0.0.0.0')
