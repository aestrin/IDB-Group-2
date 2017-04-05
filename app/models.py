# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-many-arguments
# pylint: disable = bad-continuation
# pylint: disable = too-few-public-methods
# pylint: disable = no-member
# pylint: disable = import-error

from app import db

film_character_table = db.Table('film_character_table',
                                db.Column('film_id', db.Integer, db.ForeignKey(
                                    'film.id'), nullable=False),
                                db.Column('character_id', db.Integer, db.ForeignKey(
                                    'character.id'), nullable=False),
                                db.PrimaryKeyConstraint(
                                    'film_id', 'character_id')
                                )

film_planet_table = db.Table('film_planet_table',
                             db.Column('film_id', db.Integer, db.ForeignKey(
                                 'film.id'), nullable=False),
                             db.Column('planet_id', db.Integer, db.ForeignKey(
                                 'planet.id'), nullable=False),
                             db.PrimaryKeyConstraint('film_id', 'planet_id')
                             )

film_species_table = db.Table('film_species_table',
                              db.Column('film_id', db.Integer, db.ForeignKey(
                                  'film.id'), nullable=False),
                              db.Column('species_id', db.Integer, db.ForeignKey(
                                  'species.id'), nullable=False),
                              db.PrimaryKeyConstraint('film_id', 'species_id')
                              )


class Film(db.Model):
    """
        Film model
        Contains the following attributes:
            DB id
            title
            director
            episode number
            release date
            image URL

        Contains the following relations:
            Planets (many-to-many)
            Characters (many-to-many)
            Species (many-to-many)
    """

    id = db.Column(db.Integer, primary_key=True, nullable=False)

    title = db.Column(db.String(120), nullable=False)
    director = db.Column(db.String(120), nullable=False)
    producer = db.Column(db.String(120), nullable=False)
    episode_no = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.String(120), nullable=False)
    img_url = db.Column(db.String(5000), nullable=False)

    characters = db.relationship(
        'Character', secondary=film_character_table, backref='films')
    planets = db.relationship(
        'Planet', secondary=film_planet_table, backref='films')
    species = db.relationship(
        'Species', secondary=film_species_table, backref='films')

    def __init__(self, id, title, director, producer, episode_no, release_date, img_url):
        self.id = id
        self.title = title
        self.director = director
        self.producer = producer
        self.episode_no = episode_no
        self.release_date = release_date
        self.img_url = img_url

    def __repr__(self):
        return '<Film %r>' % self.title

    def has_name(search):
        return self.episode_no == search


class Character(db.Model):
    """
        Character model
        Contains the following attributes:
            DB id
            name
            birth year
            height
            mass
            image URL

        Contains the following relations:
            Films (many-to-many)
            Planets (one-to-one)
            Species (one-to-one)
    """

    id = db.Column(db.Integer, primary_key=True, nullable=False)

    name = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    birth_year = db.Column(db.String(120), nullable=False)
    height = db.Column(db.String(120), nullable=False)
    mass = db.Column(db.String(120), nullable=False)
    img_url = db.Column(db.String(5000), nullable=False)

    # One to one
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))

    # One to one
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))

    def __init__(self, id, name, gender, birth_year, height, mass, img_url):
        self.id = id
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.height = height
        self.mass = mass
        self.img_url = img_url

    def __repr__(self):
        return '<Character %r>' % self.name

    def has_name(search):
        return self.name == search


class Planet(db.Model):
    """
        Planet model
        Contains the following planets:
            DB id
            name
            climate
            population
            gravity
            terrain
            image URL

        Contains the following relations:
            Films (many-to-many)
            Characters (one-to-many)
            Species (one-to-many)
    """

    id = db.Column(db.Integer, primary_key=True, nullable=False)

    name = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(120), nullable=False)
    population = db.Column(db.String(120), nullable=False)
    gravity = db.Column(db.String(120), nullable=False)
    terrain = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(5000), nullable=False)

    # Planet to Character is One to Many
    characters = db.relationship('Character', backref='planet', lazy='dynamic')

    def __init__(self, id, name, climate, population, gravity, terrain, img_url):
        self.id = id
        self.name = name
        self.climate = climate
        self.population = population
        self.gravity = gravity
        self.terrain = terrain
        self.img_url = img_url

    def __repr__(self):
        return '<Planet %r>' % self.name

    def has_name(search):
        return self.name == search


class Species(db.Model):
    """
        Species model
        Contains the following planets:
            DB id
            name
            classification
            language
            average_height
            eye_colors

        Contains the following relations:
            Films (many-to-many)
            Characters (one-to-many)
            Planets (one-to-one)
    """

    id = db.Column(db.Integer, primary_key=True, nullable=False)

    name = db.Column(db.String(120), nullable=False)
    classification = db.Column(db.String(120), nullable=False)
    language = db.Column(db.String(120), nullable=False)
    average_height = db.Column(db.String(120), nullable=False)
    eye_colors = db.Column(db.String(1200), nullable=False)
    img_url = db.Column(db.String(5000), nullable=False)

    # Species to Character is One to Many
    characters = db.relationship('Character', backref='species', lazy='dynamic')

    def __init__(self, id, name, classification, language, average_height, eye_colors, img_url):
        self.id = id
        self.name = name
        self.classification = classification
        self.language = language
        self.average_height = average_height
        self.eye_colors = eye_colors
        self.img_url = img_url

    def __repr__(self):
        return '<Species %r>' % self.name

    def has_name(search):
        return self.name == search
