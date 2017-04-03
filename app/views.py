from flask import render_template
from app import application
from db_mock import MockDB

import jsonpickle



# for persistence throughout app lifetime
# required for linking between instances
db_util = MockDB(application.static_folder)


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/films/<film_id>')
def film(film_id):
    film_id = int(film_id)
    return render_template('film_instance.html', film=db_util.get_film(film_id))


@application.route('/films')
def films():
    data = jsonpickle.encode(db_util.get_films())
    return render_template('films.html', films=data)


@application.route('/characters/<character_id>')
def character(character_id):
    character_id = int(character_id)
    return render_template('character_instance.html', character=db_util.get_character(character_id))


@application.route('/characters')
def characters():
    data = jsonpickle.encode(db_util.get_characters())
    return render_template('characters.html', characters=data)


@application.route('/planets/<planet_id>')
def planet(planet_id):
    planet_id = int(planet_id)
    return render_template('planet_instance.html', planet=db_util.get_planet(planet_id))


@application.route('/planets')
def planets():
    data = jsonpickle.encode(db_util.get_planets())
    return render_template('planets.html', planets=data)

# TODO: Add routes for species


@application.route('/about')
def about():
    # db_util.add_to_db_no_relationships()
    return render_template('about.html')


@application.route('/report')
def report():
    return render_template('report.html')


# TODO: Where am I supposed to use SQLAlchemy for phase 0?
# TODO: Grab images from Bing Image search api, instead of hardcoding
# TODO: Phase 2: Sort all models by their url id before adding to the DB,
# TODO: Get character gender from DB!
# to make for consistent and retrievable IDs
