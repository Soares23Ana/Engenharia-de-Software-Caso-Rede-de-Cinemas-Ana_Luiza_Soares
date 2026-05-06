import sqlite3

class MovieRepository:
    def __init__(self, db_path="cinema.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT, duration INTEGER, director TEXT)"""
        self.conn.execute(query)

    def save(self, movie):
        query = "INSERT INTO movies (title, duration, director) VALUES (?, ?, ?)"
        self.conn.execute(query, (movie.title, movie.duration, movie.director))
        self.conn.commit()