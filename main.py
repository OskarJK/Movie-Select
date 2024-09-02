import mysql.connector
import random

# Zrobić wybór filmu na podstawie roku produkcji, rodzaju filmu (animacja/live-action).


def main():
    connection = mysql.connector.connect(
        host="127.0.0.1", user="root", password="root", database="python_movies"
    )
    mycursor = connection.cursor()

    while True:
        choice = input(
            "Hello there! What do you want to do? \n 1. Add a movie to database \n 2. Remove movie from database \n 3. End program \n Your choice: "
        )
        if choice == "1":
            add_movie(mycursor, connection)
        elif choice == "2":
            remove_movie(mycursor, connection)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please enter your choice")
    connection.close()


def add_movie(mycursor, connection):
    name = input("What is the name of the movie: ")
    while True:
        try:
            year = int(input("When was the movie made: "))
            break
        except ValueError:
            print("Please enter correct year e.g. 2012")
    while True:
        type_of_movie = input(
            "What type of movie is it (animation or live-action): "
        ).lower()
        if type_of_movie in ["animation", "live-action"]:
            break
        else:
            print("Please enter either 'animation' or 'live-action'.")
    query = "INSERT INTO movies (movie_name, year, type_of_movie) VALUES (%s, %s, %s)"
    values = (name, year, type_of_movie)
    mycursor.execute(query, values)
    connection.commit()
    print(mycursor.rowcount, "record(s) inserted successfully")


def remove_movie(mycursor, connection):
    query = "SELECT * FROM movies"
    mycursor.execute(query)
    for row in mycursor:
        print(row)
    while True:
        try:
            movie_remove = int(
                input("Choose the ID of the movie you want to remove: "))
            break
        except ValueError:
            print("Please enter correct value from ID(e.g. 4)")
    query_remove = "DELETE FROM movies WHERE id = %s"
    value = (movie_remove,)
    mycursor.execute(query_remove, value)
    connection.commit()
    print(mycursor.rowcount, "record(s) deleted successfully")


if __name__ == "__main__":
    main()
