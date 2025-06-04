
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import datetime

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('movies.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/rate', methods=['POST'])
def rate_movie():
    data = request.get_json()
    movie_id = data.get('movie_id')
    user_id = data.get('user_id')
    rating = data.get('rating')
    timestamp = datetime.datetime.utcnow().isoformat()

    conn = get_db_connection()
    conn.execute('INSERT INTO ratings (movie_id, user_id, rating, timestamp) VALUES (?, ?, ?, ?)',
                 (movie_id, user_id, rating, timestamp))
    conn.commit()
    conn.close()

    return jsonify({
        'movie_id': movie_id,
        'user_id': user_id,
        'rating': rating,
        'timestamp': timestamp
    })

@app.route('/movies', methods=['GET'])
def get_movies():
    conn = get_db_connection()
    movies = conn.execute('SELECT * FROM movies').fetchall()
    conn.close()
    return jsonify([dict(m) for m in movies])

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return jsonify([dict(u) for u in users])

if __name__ == '__main__':
    app.run(debug=True)
