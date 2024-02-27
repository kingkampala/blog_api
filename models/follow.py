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

class Follow:
    def __init__(self, follower_id, followed_id, timestamp=None):
        self.follower_id = follower_id
        self.followed_id = followed_id
        self.timestamp = timestamp if timestamp is not None else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def save(self):
        query = f"INSERT INTO follows (follower_id, followed_id, timestamp) VALUES ({self.follower_id}, {self.followed_id}, '{self.timestamp}')"
        execute_query(query)

    def delete(self):
        query = f"DELETE FROM follows WHERE follower_id = {self.follower_id} AND followed_id = {self.followed_id}"
        execute_query(query)

    @staticmethod
    def is_following(follower_id, followed_id):
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        query = f"SELECT * FROM follows WHERE follower_id = {follower_id} AND followed_id = {followed_id}"
        cursor.execute(query)
        follow_data = cursor.fetchone()
        cursor.close()
        connection.close()
        return follow_data is not None
