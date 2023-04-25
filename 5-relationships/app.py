import datetime

from database import (
    create_tables,
    add_movie,
    get_movies,
    watch_movie,
    get_watched_movies,
    add_user,
    search_movies
)


menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add user.
7) Search for a movie.
8) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
create_tables()

def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    add_movie(title, timestamp)


def print_movie_list(heading, movies):
    print(f"-- {heading} Movies --")
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{_id}: {title} on {human_date}")
        print("---- \n")


def prompt_watch_movie():
    username = input("Username: ")
    movie_id = input("Movie ID: ")
    watch_movie(username, movie_id)


def prompt_add_user():
    username = input("Username: ")
    add_user(username)


def prompt_search_movies():
    search_term = input("Enter partial movie title: ")
    movies = search_movies(search_term)
    if movies:
        print_movie_list("Search Results", movies)
    else:
        print("No matches found.")


while (user_input := input(menu)) != "8":
    if user_input == "1":
        prompt_add_movie()

    elif user_input == "2":
        movies = get_movies(True)
        print_movie_list("Upcoming", movies)

    elif user_input == "3":
        movies = get_movies()
        print_movie_list("All", movies)

    elif user_input == "4":
        prompt_watch_movie()

    elif user_input == "5":
        username = input("Username: ")
        movies = get_watched_movies(username)
        if movies:
            print_movie_list(f"{username}'s watched movies", movies)
        else:
            print("That user has watched no movies yet!")

    elif user_input == "6":
        prompt_add_user()

    elif user_input == "7":
        prompt_search_movies()

    else:
        print("Invalid input, please try again!")