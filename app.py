from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the URL shortener app'}), 200

if __name__ == "__main__":
    app.run(debug=True)