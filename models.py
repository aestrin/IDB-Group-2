from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = ".....TBD....."

db = SQLAlchemy(app)


film_character_table = db.Table('film_character_table',
    db.Column('film_id', db.Integer, db.ForeignKey('film.id'), nullable=False),
    db.Column('character_id', db.Integer, db.ForeignKey('character.id'), nullable=False),
    db.PrimaryKeyConstraint('film_id', 'character_id')
)

film_planet_table = db.Table('film_planet_table',
    db.Column('film_id', db.Integer, db.ForeignKey('film.id'), nullable=False),
    db.Column('planet_id', db.Integer, db.ForeignKey('planet.id'), nullable=False),
    db.PrimaryKeyConstraint('film_id', 'planet_id')
)


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)

    title = db.Column(db.String(120), nullable=False)
    director = db.Column(db.String(120), nullable=False)
    producer = db.Column(db.String(120), nullable=False)
    episode_no = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.String(120), nullable=False)
    img_url = db.Column(db.String(5000), nullable=False)

    characters = db.relationship('Character', secondary=film_character_table, backref='film')
    planets = db.relationship('Planet', secondary=film_planet_table, backref='film')

    def __init__(self, title, director, producer, episode_no, release_date, img_url):
        self.title = title
        self.director = director
        self.producer = producer
        self.episode_no = episode_no
        self.release_date = release_date
        self.img_url = img_url


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)

    name = db.Column(db.String(120), nullable=False)
    birth_year = db.Column(db.String(120), nullable=False)
    height = db.Column(db.String(120), nullable=False)
    mass = db.Column(db.String(120), nullable=False)
    img_url = db.Column(db.String(5000), nullable=False)

    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))

    def __init__(self, name, birth_year, height, mass, img_url):
        self.name = name
        self.birth_year = birth_year
        self.height = height
        self.mass = mass
        self.img_url = img_url


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)

    name = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(120), nullable=False)
    population = db.Column(db.String(120), nullable=False)
    gravity = db.Column(db.String(120), nullable=False)
    terrain = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(5000), nullable=False)

    # Planet to Character is One to Many
    characters = db.relationship('Character', backref='planet', lazy='dynamic')

    def __init__(self, name, climate, population, gravity, terrain, img_url):
        self.name = name
        self.climate = climate
        self.population = population
        self.gravity = gravity
        self.terrain = terrain
        self.img_url = img_url

