import psycopg2
import os
from dotenv import load_dotenv

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

class Tag:
    def __init__(self, post_id=None, comment_id=None, tagged_username=None, id=None):
        self.post_id = post_id
        self.comment_id = comment_id
        self.tagged_username = tagged_username
        self.id = id

    def save(self):
        if self.post_id is not None:
            query = f"INSERT INTO tags (post_id, tagged_username) VALUES ({self.post_id}, '{self.tagged_username}')"
        elif self.comment_id is not None:
            query = f"INSERT INTO tags (comment_id, tagged_username) VALUES ({self.comment_id}, '{self.tagged_username}')"
        else:
            raise ValueError("Either post_id or comment_id must be provided for tagging")
        execute_query(query)

    @staticmethod
    def get_tags_for_post(post_id):
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        query = f"SELECT * FROM tags WHERE post_id = {post_id}"
        cursor.execute(query)
        tags = cursor.fetchall()
        cursor.close()
        connection.close()
        return tags

    @staticmethod
    def get_tags_for_comment(comment_id):
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        query = f"SELECT * FROM tags WHERE comment_id = {comment_id}"
        cursor.execute(query)
        tags = cursor.fetchall()
        cursor.close()
        connection.close()
        return tags
