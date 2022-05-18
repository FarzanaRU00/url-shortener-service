from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from werkzeug import exceptions
from controllers import urls

# Hashids is a small open-source library that generates short, unique, non-sequential ids from numbers. It converts numbers like 347 into strings like “yr8”
# alternative to Hashids would be bycrypt

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the URL shortener app'})

@app.route('/urls', methods=['GET', 'POST'])
def urls_handler():
    fns = {
        'GET': urls.index,
        'POST': urls.create
    }
    response, code = fns[request.method](request)
    return jsonify(response), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)