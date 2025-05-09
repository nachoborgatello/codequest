# En src/core/players.py
import sqlite3

class PlayerManager:
    def __init__(self, db_path="data/players.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT,
            score INTEGER
        )
        """)
    
    def add_score(self, name, score):
        self.cursor.execute("INSERT INTO players (name, score) VALUES (?, ?)", (name, score))
        self.conn.commit()