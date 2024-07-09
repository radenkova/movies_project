import sqlite3

DATABASE_NAME = 'movies.db'

def get_connection():
    """Establishes a connection to the SQLite database."""
    return sqlite3.connect(DATABASE_NAME)

def setup_database():
    # Connect to the database
    conn = get_connection()
    # Create a cursor object to execute SQL commands
    c = conn.cursor()
    
    # Create 'movies' table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        release_date TEXT,
        director TEXT,
        genre TEXT
    )''')

    # Create 'favorites' table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS favorites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER,
        FOREIGN KEY (movie_id) REFERENCES movies (id)
    )''')
    
    conn.commit()  # Commit the transaction
    conn.close()  # Close the connection

