# Movie Database CLI Application

## Overview

Movie Database CLI application - it uses SQLite as the database and provides features for listing, viewing, searching, adding, and categorizing movies.

## Setup

1. Make sure you have Python installed.
2. Clone the repository and navigate to the project directory.

## Usage

To run the application, use the following command:
python cli_app.py <command> [options]

### Commands

- `movlst`: List all movies, e.g. `python cli_app.py movlst`
- `movdt <movie_id>`: View details of a specific movie, e.g. `python cli_app.py movlst 1`
- `movsrch <query>`: Search for movies by title, e.g. `python cli_app.py movsrch "Interstellar"`
- `movadd <title> <desc> <date> <director> <genre>`: Add a new movie, e.g. `python cli_app.py movadd "Interstellar" "A space exploration journey" "2014-11-07" "Christopher Nolan" "Sci-Fi"`
- `movfv <movie_id>`: Mark a movie as a favorite
- `movcat <category>`: List movies by category (liked, newest, genre)

#### Example Workflow

1. Add New Movies:

```
python cli_app.py movadd "Interstellar" "A space exploration journey" "2014-11-07" "Christopher Nolan" "Sci-Fi"
python cli_app.py movadd "The Dark Knight" "Batman battles against the Joker" "2008-07-18" "Christopher Nolan" "Action"
```

- Output:

```
Movie added successfully.
Movie added successfully.
```

2. List All Movies:

`python cli_app.py movlst`

- Output:

```
ID: 1, Title: Interstellar, Description: A space exploration journey, Release Date: 2014-11-07, Director: Christopher Nolan, Genre: Sci-Fi
ID: 2, Title: The Dark Knight, Description: Batman battles against the Joker, Release Date: 2008-07-18, Director: Christopher Nolan, Genre: Action
```

3. View Movie Details:

`python cli_app.py movdt 1`

- Output:

`ID: 1, Title: Interstellar, Description: A space exploration journey, Release Date: 2014-11-07, Director: Christopher Nolan, Genre: Sci-Fi`

4. Search for Movies:

`python cli_app.py movsrch "The Dark Knight"`

- Output:

`ID: 2, Title: The Dark Knight, Description: Batman battles against the Joker, Release Date: 2008-07-18, Director: Christopher Nolan, Genre: Action`

5. Mark as Favourite:

`python cli_app.py movfv 1`

- Output:

`Movie marked as favorite.`

6. Categorise Movies:

6.1. Liked:

`python cli_app.py movcat liked`

- Output:

`ID: 1, Title: Interstellar, Description: A space exploration journey, Release Date: 2014-11-07, Director: Christopher Nolan, Genre: Sci-Fi`

6.2. Genre:

`python cli_app.py movcat Action`

- Output:

`ID: 2, Title: The Dark Knight, Description: Batman battles against the Joker, Release Date: 2008-07-18, Director: Christopher Nolan, Genre: Action`