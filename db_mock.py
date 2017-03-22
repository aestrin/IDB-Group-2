from mock_models import Film, Character, Planet
import json
import os

# TODO: Phase 2: instead of using self.xxx, need to use DB for persistence. Use queries to retrieve model instances.


# TODO: In phase 2, Link object is not required. The retreived film/character/planet objects from the DB should have
# the id already in it, so you can simply pass the full object into the render_template, to get name/id on the HTML
# side
class Link:

    def __init__(self, description, index):
        self.description = description
        self.index = index


class MockDB:

    def __init__(self, static_folder):
        # Phase 2: Remove self.p, self.c, self.f
        self.p = ["Tatooine","Naboo","Bespin"]
        self.c = ["Luke Skywalker","Lobot","R2-D2"]
        self.f = ["A New Hope","Return of the Jedi", "The Empire Strikes Back"]
        self.static_folder = static_folder
        self.films = self.init_films()
        self.characters = self.init_characters()
        self.planets = self.init_planets()

    def get_film(self, index):
        return self.films[index]

    def get_character(self, index):
        return self.characters[index]

    def get_planet(self, index):
        return self.planets[index]

    def get_films(self):
        return self.films

    def get_characters(self):
        return self.characters

    def get_planets(self):
        return self.planets

    def init_films(self):
        f_name = os.path.join(self.static_folder, 'Films.json')
        with open(f_name) as f:
            data = json.load(f)

        d = data['results']
        f1 = Film(d[0]['title'], d[0]['director'], d[0]['producer'], d[0]['episode_id'], d[0]['release_date'], "http://cdn2us.denofgeek.com/sites/denofgeekus/files/starwars-iv.jpg",
                  [Link(self.c[0], 0), Link(self.c[2], 2)], [Link(self.p[0], 0)])
        f2 = Film(d[1]['title'], d[1]['director'], d[1]['producer'], d[1]['episode_id'], d[1]['release_date'], "https://i.ytimg.com/vi/jDIHiIxUGEY/maxresdefault.jpg",
                  [Link(self.c[0], 0), Link(self.c[2], 2)], [Link(self.p[0], 0), Link(self.p[1], 1)])
        f3 = Film(d[2]['title'], d[2]['director'], d[2]['producer'], d[2]['episode_id'], d[2]['release_date'], "http://static.dolimg.com/lucas/movies/starwars/starwars_epi5_01-de788d5a9549.jpg",
                  [Link(self.c[0], 0), Link(self.c[1], 1), Link(self.c[2], 2)], [Link(self.p[2], 2)])

        return [f1, f2, f3]

    def init_characters(self):
        f_name = os.path.join(self.static_folder, 'Characters.json')
        with open(f_name) as f:
            data = json.load(f)

        d = data['results']
        c1 = Character(d[0]['name'], d[0]['birth_year'], d[0]['height'], d[0]['mass'], "http://starwarscardtraderapp.com/wp-content/uploads/2015/12/99-1-7-Award-Luke-Skywalker.png",
                       [Link(self.f[0], 0), Link(self.f[1], 1), Link(self.f[2], 2)], [Link(self.p[0], 0)])
        c2 = Character(d[1]['name'], d[1]['birth_year'], d[1]['height'], d[1]['mass'], "https://lumiere-a.akamaihd.net/v1/images/databank_lobot_01_169_8a50d7ae.jpeg?region=0%2C0%2C1560%2C878&width=768",
                       [Link(self.f[2], 2)], [Link(self.p[2], 2)])
        c3 = Character(d[2]['name'], d[2]['birth_year'], d[2]['height'], d[2]['mass'], "http://rcysl.com/wp-content/uploads/2017/03/R2d2-Wallpaper-In-High-Definition-.jpg",
                       [Link(self.f[0], 0), Link(self.f[1], 1), Link(self.f[2], 2)], [Link(self.p[1], 1)])

        return [c1, c2, c3]

    def init_planets(self):
        f_name = os.path.join(self.static_folder, 'Planets.json')
        with open(f_name) as f:
            data = json.load(f)

        d = data['results']
        p1 = Planet(d[0]['name'], d[0]['climate'], d[0]['population'], d[0]['gravity'], d[0]['terrain'], "https://img.clipartfox.com/92129e5d25a3b8557820a8e286ee002e_chott-el-jerid-wookieepedia-star-wars-tatooine-clipart_1900-815.jpeg",
                    [Link(self.f[0], 0), Link(self.f[1], 1)], [Link(self.c[0], 0)])
        p2 = Planet(d[1]['name'], d[1]['climate'], d[1]['population'], d[1]['gravity'], d[1]['terrain'], "http://overmental.com/wp-content/uploads/2015/07/Naboo-TPM-790x336.jpg",
                    [Link(self.f[1], 1)], [Link(self.c[2], 2)])
        p3 = Planet(d[2]['name'], d[2]['climate'], d[2]['population'], d[2]['gravity'], d[2]['terrain'], "http://cdn.segmentnext.com/wp-content/uploads/2016/05/Star-Wars-Battlefront-Bespin-DLC-1.jpg",
                    [Link(self.f[2], 2)], [Link(self.c[1], 1)])
        return [p1, p2, p3]
