from unittest import TestCase

from app.views import application
from models import Film, Character, Planet
from models import db


class TestModel (TestCase):

    def test(self):
        self.assertEqual(1, 1)

    def test_planet_model_1(self):
        """Test querying the database by attribute using simple keywords"""

        with app.test_request_context():
            example1 = Planet("Tatooine", "arid", "1 standard", "desert",
                              "https://img.clipartfox.com/92129e5d25a3b8557820a8e286ee002e_chott-el-jerid-wookieepedia-star-wars-tatooine-clipart_1900-815.jpeg")

            db.session.add(example1)
            db.session.commit()

            planet = db.session.query(Planet).filter_by(
                name="Tatooine").first()
            self.assertEqual(planet.climate, "arid")
            self.assertEqual(planet.gravity, "1 standard")

            db.session.delete(example1)
            db.session.commit()

    def test_planet_model_2(self):
        with application.test_request_context():
            example1 = Planet("Tatooine", "200000", "arid", "1 standard", "desert",
                              "https://img.clipartfox.com/92129e5d25a3b8557820a8e286ee002e_chott-el-jerid-wookieepedia-star-wars-tatooine-clipart_1900-815.jpeg")

            db.session.add(example1)
            db.session.commit()

            planet = db.session.query(Planet).filter_by(climate="arid").first()
            self.assertEqual(planet.name, "Tatooine")
            self.assertEqual(planet.gravity, "d")

            db.session.delete(example1)
            db.session.commit()

    def test_planet_model_3(self):
        with application.test_request_context():
            example1 = Planet("Tatooine", "arid", "1 standard", "desert",
                              "https://img.clipartfox.com/92129e5d25a3b8557820a8e286ee002e_chott-el-jerid-wookieepedia-star-wars-tatooine-clipart_1900-815.jpeg")

            example2 = Planet("Naboo", "temperate", "4500000000", "1 standard", "grassy hills, swamps, forests, mountains",
                              "http://overmental.com/wp-content/uploads/2015/07/Naboo-TPM-790x336.jpg")

            db.session.add(example1)
            db.session.add(example2)
            db.session.commit()

            planet = db.session.query(Planet).filter_by(name="Naboo")
            self.assertEqual(planet.climate, "temperate")
            self.assertEqual(planet.gravity, "1 standard")

            db.session.delete(example1)
            db.session.delete(example2)
            db.session.commit()

    def test_missing_planet(self):
        with application.test_request_context():
            planet = db.session.query(Planet).filter_by(name="Naboo")
            self.assertEqual(planet, None)

    def test_missing_char(self):
        with application.test_request_context():
            char = db.session.query(Character).filter_by(name="Luke")
            self.assertEqual(char, None)

    def test_character_model_1(self):
        with application.test_request_context():
            example1 = Character("Luke", "19BBY", "172", "77",
                                 "http://starwarscardtraderapplication.com/wp-content/uploads/2015/12/99-1-7-Award-Luke-Skywalker.png")

            db.session.add(example1)
            db.session.commit()

            character = db.session.query(
                Character).filter_by(name="Luke").first()
            self.assertEqual(character.name, "Luke")
            self.assertEqual(character.weight, "172")

            db.session.delete(example1)
            db.session.commit()

    def test_character_multiple_model_2(self):
        with application.test_request_context():
            example1 = Character("Luke", "19BBY", "172", "77",
                                 "http://starwarscardtraderapplication.com/wp-content/uploads/2015/12/99-1-7-Award-Luke-Skywalker.png")

            example2 = Planet("Naboo", "temperate", "4500000000", "1 standard", "grassy hills, swamps, forests, mountains",
                              "http://overmental.com/wp-content/uploads/2015/07/Naboo-TPM-790x336.jpg")

            db.session.add(example1)
            db.session.add(example2)
            db.session.commit()

            planet = db.session.query(Character).filter_by(name="Luke").first()
            self.assertEqual(planet.weight, "172")
            self.assertEqual(planet.birth_year, "19BBY")

            db.session.delete(example1)
            db.session.delete(example2)
            db.session.commit()

    def test_films_1(self):
        """Test querying the database by attribute using simple keywords"""

        with application.test_request_context():
            example1 = Film("A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum", "4", "1977-05-25",
                            "http://cdn2us.denofgeek.com/sites/denofgeekus/files/starwars-iv.jpg")

            db.session.add(example1)
            db.session.commit()

            planet = db.session.query(Planet).filter_by(
                name="A New Hope").first()
            self.assertEqual(planet.episode_no, "4")
            self.assertEqual(planet.release_date, "1977-05-25")

            db.session.delete(example1)
            db.session.commit()

    def test_films_2(self):
        """Test querying the database by attribute using simple keywords"""

        with application.test_request_context():
            example1 = Film("Return of the Jedi", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "6", "1983-05-25"
                            "https://i.ytimg.com/vi/jDIHiIxUGEY/maxresdefault.jpg")

            db.session.add(example1)
            db.session.commit()

            planet = db.session.query(Planet).filter_by(
                name="Return of the Jedi").first()
            self.assertEqual(planet.episode_no, "6")
            self.assertEqual(planet.release_date, "1983-05-25")

            db.session.delete(example1)
            db.session.commit()

    def test_films_3(self):
        """Test querying the database by attribute using simple keywords"""

        with application.test_request_context():
            example1 = Film("The Empire Strikes Back", "Irvin Kershner", "Gary Kutz, Rick McCallum", "5", "1980-05-17"
                            "http://static.dolimg.com/lucas/movies/starwars/starwars_epi5_01-de788d5a9549.jpg")

            db.session.add(example1)
            db.session.commit()

            planet = db.session.query(Planet).filter_by(
                name="The Empire Strikes Back").first()
            self.assertEqual(planet.episode_no, "5")
            self.assertEqual(planet.release_date, "1980-05-17")

            db.session.delete(example1)
            db.session.commit()
