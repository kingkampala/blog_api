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

class Comment:
    def __init__(self, content, post_id, id=None):
        self.content = content
        self.post_id = post_id
        self.id = id

    def to_dict(self):
        return {
            'id': self.id,
            'post_id': self.post_id,
            'content': self.content
        }

    def save(self):
        if self.id is None:
            query = f"INSERT INTO comments (content, post_id) VALUES ('{self.content}', {self.post_id})"
        else:
            if isinstance(self.id, int):
                query = f"UPDATE comments SET content = '{self.content}', post_id = {self.post_id} WHERE id = {self.id}"
            else:
                raise ValueError(f"id must be an integer, but got {self.id} of type {type(self.id)}")
        execute_query(query)

    @staticmethod
    def get_comments_for_post(post_id):
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        query = f"SELECT * FROM comments WHERE post_id = {post_id}"
        cursor.execute(query)
        comments = cursor.fetchall()
        cursor.close()
        connection.close()
        return comments

    @staticmethod
    def get_comment(comment_id):
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        query = f"SELECT * FROM comments WHERE id = {comment_id}"
        cursor.execute(query)
        comment_data = cursor.fetchone()
        cursor.close()
        connection.close()
        if comment_data:
            return Comment(content=comment_data[1], post_id=comment_data[2], id=comment_data[0])
        else:
            return None
    
    def update(self, new_content):
        if isinstance(self.id, int):
            query = f"UPDATE comments SET content = '{new_content}' WHERE id = {self.id}"
            execute_query(query)
            self.content = new_content
        else:
            print(f"Error: id {self.id} is not an integer.")

    def delete(self):
        query = f"DELETE FROM comments WHERE id = {self.id}"
        execute_query(query)

    def __repr__(self):
        return f"Comment('{self.content}')"
