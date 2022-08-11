from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/phi")
def null_api():
    return "<p>Hello, Phi!</p>"
