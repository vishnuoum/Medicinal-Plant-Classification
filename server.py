from flask import Flask, request
from controller import controller

app = Flask(__name__)

if __name__ == "__main__" :
    app.register_blueprint(controller)
    app.run(host = "0.0.0.0",port=3000)