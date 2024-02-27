import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

url = os.getenv("DB_URL")

# Define function to execute queries
def execute_query(query):
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

class Like:
    def __init__(self, user_id, post_id, timestamp=None):
        self.user_id = user_id
        self.post_id = post_id
        self.timestamp = timestamp if timestamp is not None else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def save(self):
        query = f"INSERT INTO likes (user_id, post_id, timestamp) VALUES ({self.user_id}, {self.post_id}, '{self.timestamp}')"
        execute_query(query)

    def delete(self):
        query = f"DELETE FROM likes WHERE user_id = {self.user_id} AND post_id = {self.post_id}"
        execute_query(query)

    @staticmethod
    def get_like_by_user_and_post(user_id, post_id):
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        query = f"SELECT * FROM likes WHERE user_id = {user_id} AND post_id = {post_id}"
        cursor.execute(query)
        like = cursor.fetchone()
        cursor.close()
        connection.close()
        return like
