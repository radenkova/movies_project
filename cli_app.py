import sys
from db_setup import setup_database
import movies

def main():
    # Set up the database when the app starts
    setup_database()

    # Check if a command is provided
    if len(sys.argv) < 2:
        print("Usage: <command> [options]")
        return
    
    command = sys.argv[1]
    
    if command == 'movlst':
        # Call function to list all movies
        movies.list_movies()
    elif command == 'movdt':
        if len(sys.argv) == 3:
            movie_id = sys.argv[2]
            # Call function to show movie details for a specific movie ID
            movies.movie_details(movie_id)
        else:
            print("Usage: movdt <movie_id>")
    elif command == 'movsrch':
        if len(sys.argv) == 3:
            query = sys.argv[2]
            # Call function to search for movies based on a query
            movies.search_movies(query)
        else:
            print("Usage: movsrch <query>")
    elif command == 'movadd':
        if len(sys.argv) == 7:
            # Gather parameters for adding a new movie
            title = sys.argv[2]
            desc = sys.argv[3]
            date = sys.argv[4]
            director = sys.argv[5]
            genre = sys.argv[6]
            movies.add_movie(title, desc, date, director, genre)
        else:
            print("Usage: movadd <title> <desc> <date> <director> <genre>")
    elif command == 'movfv':
        if len(sys.argv) == 3:
            movie_id = sys.argv[2]
            # Call function to mark a movie as favorite
            movies.mark_favorite(movie_id)
        else:
            print("Usage: movfv <movie_id>")
    elif command == 'movcat':
        if len(sys.argv) == 3:
            category = sys.argv[2]
            # Call function to categorize movies
            movies.categorize_movies(category)
        else:
            print("Usage: movcat <category>")
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
