"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import User, Rating, Movie, connect_to_db, db
from server import app
from datetime import datetime

def load_users():
    """Load users from u.user into database."""

    users_file = open("seed_data/u.user")

    for line in users_file:
        user_info = line.rstrip().split('|')

        id = int(user_info[0])
        age = int(user_info[1])
        zipcode = user_info[4]

        id = User(user_id=id, age=age, zipcode=zipcode)
        db.session.add(id)
        print "Added User %s" % id

    db.session.commit()

def load_movies():
    """Load movies from u.item into database."""

    movies_file = open("seed_data/u.item")

    for line in movies_file:
        movie_info = line.rstrip().split('|')

        id = int(movie_info[0])
        title = movie_info[1]
        title = title[:-7]
        title = title.decode("latin-1")

        if movie_info[2] == '':
            continue
        else:
            released = datetime.strptime(movie_info[2], "%d-%b-%Y")

        imdb = movie_info[4]

        id = Movie(movie_id = id, title = title, released_at = released, imdb_url = imdb)
        db.session.add(id)
        print "Added Movie %s" % title
 
    db.session.commit()

def load_ratings():
    """Load ratings from u.data into database."""

    ratings_file = open("seed_data/u.data")

    for line in ratings_file:
        ratings_info = line.rstrip().split('\t')

        user_id = int(ratings_info[0])
        movie_id = int(ratings_info[1])
        score = int(ratings_info[2])

        id = Rating(movie_id=movie_id, user_id=user_id, score=score)
        db.session.add(id)
        print "Added new rating for Movie %s" % movie_id
    
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    load_users()
    load_movies()
    load_ratings()
