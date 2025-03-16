from flask import Flask
from flask_cors import CORS
from blueprints.posts.views import posts
from blueprints.users.views import users
from dotenv import load_dotenv
from os import getenv


app = Flask(__name__)
CORS(app)
load_dotenv()
app.config["DEBUG"] = getenv("FLASK_DEBUG")
app.config["SECRET_KEY"] = getenv("FLASK_SECRET_KEY")
app.register_blueprint(posts)
app.register_blueprint(users)


if __name__ == "__main__":
    app.run()
