from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
from hashids import Hashids

# Hashids is a small open-source library that generates short, unique, non-sequential ids from numbers. It converts numbers like 347 into strings like “yr8”
# alternative to Hashids would be bycrypt

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'your secret key'

hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the URL shortener app'}), 200

if __name__ == "__main__":
    app.run(debug=True)