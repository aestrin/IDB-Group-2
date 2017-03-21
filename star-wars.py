from flask import Flask, render_template
from db_mock import MockDB

app = Flask(__name__)

# for persistence throughout app lifetime
# required for linking between instances
db = MockDB(app.static_folder)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/films/<film_id>')
def film(film_id):
    film_id = int(film_id)
    return render_template('film_instance.html', film=db.get_film(film_id))


@app.route('/films')
def films():
    return render_template('films.html', films=enumerate(db.get_films()))


@app.route('/characters/<character_id>')
def character(character_id):
    character_id = int(character_id)
    return render_template('character_instance.html', character=db.get_character(character_id))


@app.route('/characters')
def characters():
    return render_template('characters.html', characters=enumerate(db.get_characters()))


@app.route('/planets/<planet_id>')
def planet(planet_id):
    planet_id = int(planet_id)
    return render_template('planet_instance.html', planet=db.get_planet(planet_id))


@app.route('/planets')
def planets():
    return render_template('planets.html', planets=enumerate(db.get_planets()))

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)


# TODO: Where am I supposed to use SQLAlchemy for phase 0?
# TODO: Grab images from Bing Image search api, instead of hardcoding
# TODO: Phase 2: Sort all models by their url id before adding to the DB, to make for consistent and retrievable IDs

