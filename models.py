# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-many-arguments
# pylint: disable = bad-continuation
# pylint: disable = too-few-public-methods
# pylint: disable = no-member
# pylint: disable = import-error
# pylint: disable = redefined-builtin

# from app import db

from db import Table, Column, PrimaryKeyConstraint, ForeignKey, Model, Integer, String, Relationship

film_character_table = Table('film_character_table',
                                Column('film_id', Integer, ForeignKey(
                                    'film.id'), nullable=False),
                                Column('character_id', Integer, ForeignKey(
                                    'character.id'), nullable=False),
                                PrimaryKeyConstraint(
                                    'film_id', 'character_id')
                                )

film_planet_table = Table('film_planet_table',
                             Column('film_id', Integer, ForeignKey(
                                 'film.id'), nullable=False),
                             Column('planet_id', Integer, ForeignKey(
                                 'planet.id'), nullable=False),
                             PrimaryKeyConstraint('film_id', 'planet_id')
                             )

film_species_table = Table('film_species_table',
                              Column('film_id', Integer, ForeignKey(
                                  'film.id'), nullable=False),
                              Column('species_id', Integer, ForeignKey(
                                  'species.id'), nullable=False),
                              PrimaryKeyConstraint('film_id', 'species_id')
                              )


class Film(Model):
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

    model_url = "http://www.thesweawakens.me/films"
    model_name = "film"

    id = Column(Integer, primary_key=True, nullable=False)

    title = Column(String(120), nullable=False)
    director = Column(String(120), nullable=False)
    producer = Column(String(120), nullable=False)
    episode_no = Column(String(120), nullable=False)
    release_date = Column(String(120), nullable=False)
    img_url = Column(String(5000), nullable=False)

    characters = Relationship(
        'Character', secondary=film_character_table, backref='films')
    planets = Relationship(
        'Planet', secondary=film_planet_table, backref='films')
    species = Relationship(
        'Species', secondary=film_species_table, backref='films')

    def __init__(self, id, title, director, producer, episode_no, release_date, img_url):
        assert len(title) < 5000
        assert len(director) < 5000
        assert len(producer) < 5000
        self.id = id
        self.title = title
        self.director = director
        self.producer = producer
        self.episode_no = episode_no
        self.release_date = release_date
        self.img_url = img_url


    def get_descriptor(self):
        return self.title

    def __repr__(self):
        return '<Film %r>' % self.title

    def has_name(self, search):
        return self.episode_no == search


class Character(Model):
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

    model_url = "http://www.thesweawakens.me/characters"
    model_name = "character"

    id = Column(Integer, primary_key=True, nullable=False)

    name = Column(String(120), nullable=False)
    gender = Column(String(120), nullable=False)
    birth_year = Column(String(120), nullable=False)
    height = Column(String(120), nullable=False)
    mass = Column(String(120), nullable=False)
    img_url = Column(String(5000), nullable=False)

    # One to one
    planet_id = Column(Integer, ForeignKey('planet.id'))

    # One to one
    species_id = Column(Integer, ForeignKey('species.id'))

    def __init__(self, id, name, gender, birth_year, height, mass, img_url):
        assert len(name) < 5000
        assert len(gender) < 5000
        self.id = id
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.height = height
        self.mass = mass
        self.img_url = img_url

    def get_descriptor(self):
        return self.name

    def __repr__(self):
        return '<Character %r>' % self.name

    def has_name(self, search):
        return self.name == search


class Planet(Model):
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
    """

    model_url = "http://www.thesweawakens.me/planets"
    model_name = "planet"

    id = Column(Integer, primary_key=True, nullable=False)

    name = Column(String(120), nullable=False)
    climate = Column(String(120), nullable=False)
    population = Column(String(120), nullable=False)
    gravity = Column(String(120), nullable=False)
    terrain = Column(String(500), nullable=False)
    img_url = Column(String(5000), nullable=False)

    # Planet to Character is One to Many
    characters = Relationship('Character', backref='planet', lazy='dynamic')

    def __init__(self, id, name, climate, population, gravity, terrain, img_url):
        assert len(name) < 5000
        assert len(climate) < 5000
        assert len(terrain) < 5000
        self.id = id
        self.name = name
        self.climate = climate
        self.population = population
        self.gravity = gravity
        self.terrain = terrain
        self.img_url = img_url

    def get_descriptor(self):
        return self.name

    def __repr__(self):
        return '<Planet %r>' % self.name

    def has_name(self, search):
        return self.name == search


class Species(Model):
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
    """

    model_url = "http://www.thesweawakens.me/species"
    model_name = "species"

    id = Column(Integer, primary_key=True, nullable=False)

    name = Column(String(120), nullable=False)
    classification = Column(String(120), nullable=False)
    language = Column(String(120), nullable=False)
    average_height = Column(String(120), nullable=False)
    eye_colors = Column(String(1200), nullable=False)
    img_url = Column(String(5000), nullable=False)

    # Species to Character is One to Many
    characters = Relationship(
        'Character', backref='species', lazy='dynamic')

    def __init__(self, id, name, classification, language, average_height, eye_colors, img_url):
        assert len(name) < 5000
        assert len(classification) < 5000
        assert len(language) < 5000
        self.id = id
        self.name = name
        self.classification = classification
        self.language = language
        self.average_height = average_height
        self.eye_colors = eye_colors
        self.img_url = img_url

    def get_descriptor(self):
        return self.name

    def __repr__(self):
        return '<Species %r>' % self.name

    def has_name(self, search):
        return self.name == search
