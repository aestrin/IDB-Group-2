# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-many-arguments
# pylint: disable = bad-continuation
# pylint: disable = too-few-public-methods
# pylint: disable = no-member
# pylint: disable = redefined-builtin
# pylint: disable = locally-disabled


import os
import json
from unittest import TestCase, main
from app.models import Film, Character, Planet, Species
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
application = Flask(__name__, static_url_path='/app/static')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://awsuser_idb_test:pushkariscool@starwars-idb.ceczpdhwgqiv.us-east-1.rds.amazonaws.com:5432/postgres'
test_db = SQLAlchemy(application)

f_name = os.path.join(APP_ROOT, "app/scraper", "TestSpecies.json")
with open(f_name) as f:
     speciesdata = json.load(f)
f_name = os.path.join(APP_ROOT, "app/scraper", "TestPlanets.json")
with open(f_name) as f:
     planetdata = json.load(f)
f_name = os.path.join(APP_ROOT, "app/scraper", "TestPeople.json")
with open(f_name) as f:
            peopledata = json.load(f)
f_name = os.path.join(APP_ROOT, "app/scraper", "TestFilms.json")
with open(f_name) as f:
            filmdata = json.load(f)

class TestModel (TestCase):

    def test_species_1(self):
        """Test querying the database by attribute using simple keywords"""
        data = speciesdata
        d = data['24']
        id = 24
        species = Species(id, d['name'], d['classification'], d['language'], d['average_height'], d['eye_colors'], "https://s3.amazonaws.com/tf.images/reduced-ban16554.jpg")
        test_db.session.add(species)
        s =test_db.session.query(Species).all()
        count = len(s)
        self.assertEqual(1,count)
        test_db.session.delete(species)
        test_db.session.commit()

    def test_species_model_2(self):
        data = speciesdata
        d = data['24']
        d2 = data['25']
        id = 24
        id2 = 25
        species = Species(id, d['name'], d['classification'], d['language'], d['average_height'], d['eye_colors'], "https://s3.amazonaws.com/tf.images/reduced-ban16554.jpg")
        species2 = Species(id2, d2['name'], d2['classification'], d2['language'], d2['average_height'], d2['eye_colors'], "https://s3.amazonaws.com/tf.images/reduced-ban16554.jpg")
        test_db.session.add(species)
        test_db.session.add(species2)
        s = test_db.session.query(Species).all()
        count = len(s)
        self.assertEqual(2,count)
        test_db.session.delete(species)
        test_db.session.delete(species2)
        test_db.session.commit()

    def test_species_model_3(self):
        data = speciesdata
        d = data['24']
        d2 = data['25']
        id = 24
        id2 = 25
        species = Species(id, d['name'], d['classification'], d['language'], d['average_height'], d['eye_colors'], "https://s3.amazonaws.com/tf.images/reduced-ban16554.jpg")
        species2 = Species(id2, d2['name'], d2['classification'], d2['language'], d2['average_height'], d2['eye_colors'], "https://s3.amazonaws.com/tf.images/reduced-ban16554.jpg")
        test_db.session.add(species)
        test_db.session.add(species2)
        s = test_db.session.query(Species).first()
        sclass = s.classification
        self.assertEqual(d['classification'],sclass)
        test_db.session.delete(species)
        test_db.session.delete(species2)
        test_db.session.commit()

    def test_species_model_4(self):
        data = speciesdata
        d = data['24']
        d2 = data['25']
        id = 24
        id2 = 25
        species = Species(id, d['name'], d['classification'], d['language'], d['average_height'], d['eye_colors'], "https://s3.amazonaws.com/tf.images/reduced-ban16554.jpg")
        species2 = Species(id2, d2['name'], d2['classification'], d2['language'], d2['average_height'], d2['eye_colors'], "https://s3.amazonaws.com/tf.images/reduced-ban16554.jpg")
        test_db.session.add(species)
        test_db.session.add(species2)
        s = test_db.session.query(Species).get(str(id2))
        s_lang = s.language
        self.assertEqual(d2['language'],s_lang)
        test_db.session.delete(species)
        test_db.session.delete(species2)
        test_db.session.commit()

    def test_planet_model_1(self):
        """Test querying the database by attribute using simple keywords"""
        data = planetdata
        d = data['1']
        id = 1
        planet = Planet(id, d['name'], d['climate'], d['population'], d['gravity'], d['terrain'], "http://overmental.com/wp-content/uploads/2015/07/Naboo-TPM-790x336.jpg")
        test_db.session.add(planet)
        s =test_db.session.query(Planet).all()
        count = len(s)
        self.assertEqual(1,count)
        test_db.session.delete(planet)
        test_db.session.commit()

    def test_planet_model_2(self):
        data = planetdata
        d = data['1']
        d2 = data['2']
        id = 1
        id2 = 2
        planet = Planet(id, d['name'], d['climate'], d['population'], d['gravity'], d['terrain'], "http://overmental.com/wp-content/uploads/2015/07/Naboo-TPM-790x336.jpg")
        planet2 = Planet(id2, d2['name'], d2['climate'], d2['population'], d2['gravity'], d2['terrain'], "http://overmental.com/wp-content/uploads/2015/07/Naboo-TPM-790x336.jpg")
        test_db.session.add(planet)
        test_db.session.add(planet2)
        s = test_db.session.query(Planet).all()
        count = len(s)
        self.assertEqual(2,count)
        test_db.session.delete(planet)
        test_db.session.delete(planet2)
        test_db.session.commit()

    def test_planet_model_3(self):
        data = planetdata
        d = data['1']
        d2 = data['2']
        id = 1
        id2 = 2
        planet = Planet(id, d['name'], d['climate'], d['population'], d['gravity'], d['terrain'], "http://overmental.com/wp-content/uploads/2015/07/Naboo-TPM-790x336.jpg")
        planet2 = Planet(id2, d2['name'], d2['climate'], d2['population'], d2['gravity'], d2['terrain'], "http://overmental.com/wp-content/uploads/2015/07/Naboo-TPM-790x336.jpg")
        test_db.session.add(planet)
        test_db.session.add(planet2)
        s = test_db.session.query(Planet).first()
        sclass = s.population
        self.assertEqual(d['population'],sclass)
        test_db.session.delete(planet)
        test_db.session.delete(planet2)
        test_db.session.commit()

    def test_planet_model_4(self):
        data = planetdata
        d = data['1']
        d2 = data['2']
        id = 1
        id2 = 2
        planet = Planet(id, d['name'], d['climate'], d['population'], d['gravity'], d['terrain'], "http://overmental.com/wp-content/uploads/2015/07/Naboo-TPM-790x336.jpg")
        planet2 = Planet(id2, d2['name'], d2['climate'], d2['population'], d2['gravity'], d2['terrain'], "http://overmental.com/wp-content/uploads/2015/07/Naboo-TPM-790x336.jpg")
        test_db.session.add(planet)
        test_db.session.add(planet2)
        s = test_db.session.query(Planet).get(str(2))
        climate = s.climate
        self.assertEqual(d2['climate'],climate)
        test_db.session.delete(planet)
        test_db.session.delete(planet2)
        test_db.session.commit()
    def test_character_model_1(self):
        """Test querying the database by attribute using simple keywords"""
        data = peopledata
        d = data['1']
        id = 1
        character = Character(id, d['name'], d['gender'], d['birth_year'], d['height'], d['mass'], "http://starwarscardtraderapp.com/wp-content/uploads/2015/12/99-1-7-Award-Luke-Skywalker.png")    
        test_db.session.add(character)
        s = test_db.session.query(Character).all()
        count = len(s)
        self.assertEqual(1,count)
        test_db.session.delete(character)
        test_db.session.commit()

    def test_character_model_2(self):
        data = peopledata
        d = data['1']
        d2 = data['2']
        id = 1
        id2 = 2
        character = Character(id, d['name'], d['gender'], d['birth_year'], d['height'], d['mass'], "http://starwarscardtraderapp.com/wp-content/uploads/2015/12/99-1-7-Award-Luke-Skywalker.png")  
        character2 = Character(id2, d2['name'], d2['gender'], d2['birth_year'], d2['height'], d2['mass'], "http://starwarscardtraderapp.com/wp-content/uploads/2015/12/99-1-7-Award-Luke-Skywalker.png")
        test_db.session.add(character)
        test_db.session.add(character2)
        s = test_db.session.query(Character).all()
        count = len(s)
        self.assertEqual(2,count)
        test_db.session.delete(character)
        test_db.session.delete(character2)
        test_db.session.commit()

    def test_character_model_3(self):
        data = peopledata
        d = data['1']
        d2 = data['2']
        id = 1
        id2 = 2
        character = Character(id, d['name'], d['gender'], d['birth_year'], d['height'], d['mass'], "http://starwarscardtraderapp.com/wp-content/uploads/2015/12/99-1-7-Award-Luke-Skywalker.png") 
        character2 = Character(id2, d2['name'], d2['gender'], d2['birth_year'], d2['height'], d2['mass'], "http://starwarscardtraderapp.com/wp-content/uploads/2015/12/99-1-7-Award-Luke-Skywalker.png")
        test_db.session.add(character)
        test_db.session.add(character2)
        s = test_db.session.query(Character).first()
        name = s.name
        self.assertEqual(d['name'],name)
        test_db.session.delete(character)
        test_db.session.delete(character2)
        test_db.session.commit()

    def test_character_model_4(self):
        data = peopledata
        d = data['1']
        d2 = data['2']
        id = 1
        id2 = 2
        character = Character(id, d['name'], d['gender'], d['birth_year'], d['height'], d['mass'], "http://starwarscardtraderapp.com/wp-content/uploads/2015/12/99-1-7-Award-Luke-Skywalker.png")
        character2 = Character(id2, d2['name'], d2['gender'], d2['birth_year'], d2['height'], d2['mass'], "http://starwarscardtraderapp.com/wp-content/uploads/2015/12/99-1-7-Award-Luke-Skywalker.png")
        test_db.session.add(character)
        test_db.session.add(character2)
        s = test_db.session.query(Character).get(str(2))
        name = s.name
        self.assertEqual(d2['name'],name)
        test_db.session.delete(character)
        test_db.session.delete(character2)
        test_db.session.commit()
    def test_film_model_1(self):
        """Test querying the database by attribute using simple keywords"""
        data = filmdata
        d = data['1']
        id = 1
        film = Film(id, d['title'], d['director'], d['producer'], d['episode_id'], d['release_date'], "http://cdn2us.denofgeek.com/sites/denofgeekus/files/starwars-iv.jpg")
        test_db.session.add(film)
        s = test_db.session.query(Film).all()
        count = len(s)
        self.assertEqual(1,count)
        test_db.session.delete(film)
        test_db.session.commit()

    def test_film_model_2(self):
        data = filmdata
        d = data['1']
        d2 = data['2']
        id = 1
        id2 = 2
        film = Film(id, d['title'], d['director'], d['producer'], d['episode_id'], d['release_date'], "http://cdn2us.denofgeek.com/sites/denofgeekus/files/starwars-iv.jpg")
        film2 = Film(id2, d2['title'], d2['director'], d2['producer'], d2['episode_id'], d2['release_date'], "http://cdn2us.denofgeek.com/sites/denofgeekus/files/starwars-iv.jpg")
        test_db.session.add(film)
        test_db.session.add(film2)
        s = test_db.session.query(Film).all()
        count = len(s)
        self.assertEqual(2,count)
        test_db.session.delete(film)
        test_db.session.delete(film2)
        test_db.session.commit()

    def test_film_model_3(self):
        data = filmdata
        d = data['1']
        d2 = data['2']
        id = 1
        id2 = 2
        film = Film(id, d['title'], d['director'], d['producer'], d['episode_id'], d['release_date'], "http://cdn2us.denofgeek.com/sites/denofgeekus/files/starwars-iv.jpg")
        film2 = Film(id2, d2['title'], d2['director'], d2['producer'], d2['episode_id'], d2['release_date'], "http://cdn2us.denofgeek.com/sites/denofgeekus/files/starwars-iv.jpg")
        test_db.session.add(film)
        test_db.session.add(film2)
        s = test_db.session.query(Film).first()
        title = s.title
        self.assertEqual(d['title'],title)
        test_db.session.delete(film)
        test_db.session.delete(film2)
        test_db.session.commit()

    def test_film_model_4(self):
        data = filmdata
        d = data['1']
        d2 = data['2']
        id = 1
        id2 = 2
        film = Film(id, d['title'], d['director'], d['producer'], d['episode_id'], d['release_date'], "http://cdn2us.denofgeek.com/sites/denofgeekus/files/starwars-iv.jpg")
        film2 = Film(id2, d2['title'], d2['director'], d2['producer'], d2['episode_id'], d2['release_date'], "http://cdn2us.denofgeek.com/sites/denofgeekus/files/starwars-iv.jpg")
        test_db.session.add(film)
        test_db.session.add(film2)
        s = test_db.session.query(Film).get(str(2))
        director = s.director
        self.assertEqual(d2['director'],director)
        test_db.session.delete(film)
        test_db.session.delete(film2)
        test_db.session.commit()
      
      
if __name__ == "__main__":  # pragma: no cover
    main()
