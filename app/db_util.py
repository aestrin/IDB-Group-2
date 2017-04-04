from app.models import Film, Character, Planet, Species
from app import db
import json
import os


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


def add_images_to_db():
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))

    # films
    # f_name = os.path.join(APP_ROOT, "scraper", "allFilms.json")
    # with open(f_name) as infile:
    #     data = json.load(infile)
    # films = get_films()
    # for f in films:
    #     f.img_url = data[str(f.id)]['img_url']

    # # characters
    # f_name = os.path.join(APP_ROOT, "scraper", "allPeople.json")
    # with open(f_name) as infile:
    #     data = json.load(infile)
    # characters = get_characters()
    # for c in characters:
    #     c.img_url = data[str(c.id)]['img_url']
    #
    # # planets
    # f_name = os.path.join(APP_ROOT, "scraper", "allPlanets.json")
    # with open(f_name) as infile:
    #     data = json.load(infile)
    # planets = get_planets()
    # for p in planets:
    #     p.img_url = data[str(p.id)]['img_url']
    #
    # # species
    # f_name = os.path.join(APP_ROOT, "scraper", "allSpecies.json")
    # with open(f_name) as infile:
    #     data = json.load(infile)
    # species = get_all_species()
    # for s in species:
    #     s.img_url = data[str(s.id)]['img_url']

    # db.session.commit()
    print "DONE"



