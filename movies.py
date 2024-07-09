from db_setup import get_connection

def list_movies():
    """Lists all movies stored in the database."""
    conn = get_connection()
    c = conn.cursor()
    
    # Execute SQL query to select all movies
    c.execute('SELECT * FROM movies')
    movies = c.fetchall()
    
    if movies:
        # Print details of each movie if there are movies in the result
        for movie in movies:
            print(f"ID: {movie[0]}, Title: {movie[1]}, Description: {movie[2]}, Release Date: {movie[3]}, Director: {movie[4]}, Genre: {movie[5]}")
    else:
        print("No movies found.")
    
    conn.close()

def movie_details(movie_id):
    """Displays details of a specific movie identified by its ID."""
    conn = get_connection()
    c = conn.cursor()
    
    # Execute SQL query to select movie by ID
    c.execute('SELECT * FROM movies WHERE id = ?', (movie_id,))
    movie = c.fetchone()
    
    if movie:
        # Print details of the movie if found
        print(f"ID: {movie[0]}, Title: {movie[1]}, Description: {movie[2]}, Release Date: {movie[3]}, Director: {movie[4]}, Genre: {movie[5]}")
    else:
        print("Movie not found.")
    
    conn.close()

def search_movies(query):
    """Searches movies based on the provided query string."""
    conn = get_connection()
    c = conn.cursor()
    
    # Execute SQL query to search movies by title
    c.execute('SELECT * FROM movies WHERE title LIKE ?', ('%' + query + '%',))
    movies = c.fetchall()
    
    if movies:
        # Print details of each movie found
        for movie in movies:
            print(f"ID: {movie[0]}, Title: {movie[1]}, Description: {movie[2]}, Release Date: {movie[3]}, Director: {movie[4]}, Genre: {movie[5]}")
    else:
        print("No movies found.")
    
    conn.close()

def add_movie(title, desc, date, director, genre):
    """Adds a new movie to the database."""
    conn = get_connection()
    c = conn.cursor()
    
    # Execute SQL query to insert new movie details into 'movies' table
    c.execute('INSERT INTO movies (title, description, release_date, director, genre) VALUES (?, ?, ?, ?, ?)', (title, desc, date, director, genre))
    
    conn.commit()
    conn.close()
    
    # Print success message
    print("Movie added successfully.")

def mark_favorite(movie_id):
    """Marks a movie as favorite."""
    conn = get_connection()
    c = conn.cursor()

    # Check if the movie is already marked as favorite
    c.execute('SELECT * FROM favorites WHERE movie_id = ?', (movie_id,))
    movie = c.fetchone()
    
    if movie:
        print("Movie already marked as favorite.")
    else:
        # If movie is not in favorites, insert it into 'favorites' table
        c.execute('INSERT INTO favorites (movie_id) VALUES (?)', (movie_id,))
        print("Movie marked as favorite.")
    
    conn.commit()
    conn.close()

def categorize_movies(category):
    """Retrieves and categorizes movies based on the specified category."""
    conn = get_connection()
    c = conn.cursor()
    
    if category == 'liked':
        # Fetch top 5 movies that are marked as favorites
        c.execute('''SELECT m.id, m.title, m.description, m.release_date, m.director, m.genre
                     FROM movies m
                     JOIN favorites f ON m.id = f.movie_id
                     LIMIT 5''')
    elif category == 'newest':
        # Fetch top 5 newest movies based on release date in descending order
        c.execute('SELECT * FROM movies ORDER BY release_date DESC LIMIT 5')
    else:
        # Fetch top 5 movies in the specified genre
        c.execute('SELECT * FROM movies WHERE genre = ? LIMIT 5', (category,))
    
    movies = c.fetchall()
    
    if movies:
        # Print details of each movie found in the category
        for movie in movies:
            print(f"ID: {movie[0]}, Title: {movie[1]}, Description: {movie[2]}, Release Date: {movie[3]}, Director: {movie[4]}, Genre: {movie[5]}")
    else:
        print("No movies found.")
    
    conn.close()
