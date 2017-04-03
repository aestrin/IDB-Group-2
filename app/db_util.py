from app.models import Film, Character, Planet, Species
from app import db


def get_film(id):
    film = db.session.query(Film).get(id)
    return film


def get_character(id):
    character = db.session.query(Character).get(id)
    return character


def get_planet(id):
    planet = db.session.query(Planet).get(id)
    return planet


def get_species(id):
    species = db.session.query(Species).get(id)
    return species


def get_films():
    films = Film.query.all()
    return films


def get_characters():
    characters = Character.query.all()
    return characters


def get_planets():
    planets = Planet.query.all()
    return planets


def get_all_species():
    species = Species.query.all()
    return species

