
import sqlite3

conn = sqlite3.connect('movies.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS ratings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_id INTEGER,
    user_id INTEGER,
    rating INTEGER,
    timestamp TEXT,
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(user_id) REFERENCES users(id)
)
''')

# Insert sample data
c.executemany('INSERT INTO movies (title) VALUES (?)', [
    ('The Matrix',),
    ('Inception',),
    ('Interstellar',)
])
c.executemany('INSERT INTO users (name) VALUES (?)', [
    ('alice',),
    ('bob',),
    ('carol',)
])

conn.commit()
conn.close()
print("Database initialized.")
