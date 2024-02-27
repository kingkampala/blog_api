import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from routes.post import posts_bp
from routes.user import users_bp
from routes.like import like_bp

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

CORS(app)

app.register_blueprint(posts_bp)
app.register_blueprint(users_bp)
app.register_blueprint(like_bp)

url = os.getenv("DB_URL")

try:
    connection = psycopg2.connect(url)
    print("Successfully connected to the database!")
except psycopg2.Error as err:
    print("Error connecting to the database:", err)

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == '__main__':
    app.run(debug=True)