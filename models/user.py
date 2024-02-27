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

class User:
    def __init__(self, username, email, password, id=None):
        self.username = username
        self.email = email
        self.password = password
        self.id = id

    '''
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }
    '''

    def save(self):
        schema_name = os.getenv("DB_NAME")
        if self.id is None:
            query = f"INSERT INTO users (username, email, password) VALUES ('{self.username}', '{self.email}', '{self.password}')"
        else:
            if isinstance(self.id, int):
                query = f"UPDATE users SET username = '{self.username}', email = '{self.email}', password = '{self.password}' WHERE id = {self.id}"
            else:
                raise ValueError(f"id must be an integer, but got {self.id} of type {type(self.id)}")
        execute_query(query)

    @staticmethod
    def get_user_by_username(username):
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        query = f"SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user_data = cursor.fetchone()
        cursor.close()
        connection.close()
        if user_data:
            return User(user_data[0], user_data[1], user_data[2])
        else:
            return None

    @staticmethod
    def get_user_by_email(email):
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        query = f"SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        user_data = cursor.fetchone()
        cursor.close()
        connection.close()
        if user_data:
            return User(user_data[0], user_data[1], user_data[2])
        else:
            return None

    @staticmethod
    def get_all_users():
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        schema_name = os.getenv("DB_NAME")
        query = "SELECT * FROM users"
        cursor.execute(query)
        users = []
        for user_data in cursor.fetchall():
            user = User(username=user_data[1], email=user_data[2], password=user_data[3], id=user_data[0])
            users.append(user)
        cursor.close()
        connection.close()
        return users
    
    @staticmethod
    def get_user(id):
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        schema_name = os.getenv("DB_NAME")
        query = f"SELECT * FROM users WHERE id = {id}"
        cursor.execute(query)
        user_data = cursor.fetchone()
        cursor.close()
        connection.close()
        if user_data:
            return User(user_data[1], user_data[2], user_data[3], user_data[0])
        else:
            return None
    
    def update(self, new_username, new_email, new_password):
        if isinstance(self.id, int):
            schema_name = os.getenv("DB_NAME")
            query = f"UPDATE users SET username = '{new_username}', email = '{new_email}', password = '{new_password}' WHERE id = {self.id}"
            execute_query(query)
            self.username = new_username
            self.email = new_email
            self.password = new_password
        else:
            print(f"Error: id {self.id} is not an integer.")

    def delete(self):
        schema_name = os.getenv("DB_NAME")
        query = f"DELETE FROM users WHERE id = {self.id}"
        execute_query(query)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
