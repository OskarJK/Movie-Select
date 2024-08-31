import mysql.connector
import random

# Zrobić wybór filmu na podstawie roku produkcji, rodzaju filmu (animacja/zwykły).


def main():
    connection = mysql.connector.connect(
        host="127.0.0.1", user="root", password="root", database="python_movies"
    )
    mycursor = connection.cursor()

    while True:
        choice = input(
            "Hello there! What do you want to do? \n 1. Add a movie to database \n 2. Nothing \n Your choice: "
        )
        if choice == "1":
            add_movie(mycursor, connection)
        elif choice == "2":
            print("Nothing to do here.")
            break
        else:
            print("Please enter your choice")
    connection.close()


def add_movie(mycursor, connection):
    name = input("What is the name of the movie: ")
    year = int(input("When was the movie made: "))
    type_of_movie = input("What type of movie is it (animation or live-action): ")

    query = "INSERT INTO movies (movie_name, year, type_of_movie) VALUES (%s, %s, %s)"
    values = (name, year, type_of_movie)
    mycursor.execute(query, values)
    connection.commit()

    print(mycursor.rowcount, "record(s) inserted successfully")


if __name__ == "__main__":
    main()
