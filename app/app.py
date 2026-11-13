import os

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "ok", "service": "hardened-microservice"}

if __name__ == "__main__":
    app.run(host=os.getenv("APP_HOST", "127.0.0.1"), port=8080)
