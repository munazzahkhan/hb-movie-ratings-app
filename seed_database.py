"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())


movies_in_db = []
for movie in movie_data:
    
    title = movie['title']
    overview = movie['overview']
    poster_path = movie['poster_path']
    release_date = movie['release_date']

    format = '%Y-%m-%d'
    date = datetime.strptime(release_date, format)

    new_movie = crud.create_movie(title, overview, date, poster_path)

    movies_in_db.append(new_movie)

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    new_user = crud.create_user(email, password)

    for i in range(10):
        random_movie = choice(movies_in_db)
        random_score = randint(1,5)
        crud.create_rating(new_user, random_movie, random_score)

