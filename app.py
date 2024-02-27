import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from routes.post import posts_bp

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

CORS(app)

app.register_blueprint(posts_bp)

url = os.getenv("DB_URL")
connection = psycopg2.connect(url)

try:
    connection = psycopg2.connect(url)
    print("Successfully connected to the database!")
except psycopg2.Error as err:
    print("Error connecting to the database:", err)
