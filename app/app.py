import os

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "ok", "service": "hardened-microservice"}

if __name__ == "__main__":
    app_host = os.getenv("APP_HOST", "127.0.0.1")
    app_port = int(os.getenv("APP_PORT", "8080"))
    app.run(host=app_host, port=app_port)
