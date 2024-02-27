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

class Post:
    def __init__(self, title, content, id):
        self.title = title
        self.content = content
        self.id = id

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }

    def save(self):
        schema_name = os.getenv("DB_NAME")
        if self.id is None:
            query = f"INSERT INTO posts (title, content) VALUES ('{self.title}', '{self.content}')"
        else:
            if isinstance(self.id, int):
                query = f"UPDATE posts SET title = '{self.title}', content = '{self.content}' WHERE id = {self.id}"
            else:
                raise ValueError(f"id must be an integer, but got {self.id} of type {type(self.id)}")
        execute_query(query)

    @staticmethod
    def get_all_posts():
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        schema_name = os.getenv("DB_NAME")
        query = "SELECT * FROM posts"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    
    def get_post(id):
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        schema_name = os.getenv("DB_NAME")
        query = f"SELECT * FROM posts WHERE id = {id}"
        cursor.execute(query)
        post_data = cursor.fetchone()
        cursor.close()
        connection.close()
        if post_data:
            return Post(post_data[1], post_data[2], post_data[0])
        else:
            return None
        
    def update(self, new_title, new_content):
        if isinstance(self.id, int):
            schema_name = os.getenv("DB_NAME")
            query = f"UPDATE posts SET title = '{new_title}', content = '{new_content}' WHERE id = {self.id}"
            execute_query(query)
            self.title = new_title
            self.content = new_content
        else:
            print(f"Error: id {self.id} is not an integer.")

    def delete(self):
        schema_name = os.getenv("DB_NAME")
        query = f"DELETE FROM posts WHERE id = {self.id}"
        execute_query(query)

    def __repr__(self):
        return f"Post('{self.title}')"
