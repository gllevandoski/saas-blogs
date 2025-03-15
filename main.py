from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os


app = Flask(__name__)
CORS(app)
load_dotenv()
app.config["DEBUG"] = os.getenv("FLASK_DEBUG")


@app.get("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
