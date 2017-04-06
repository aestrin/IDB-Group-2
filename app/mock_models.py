class Film:
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

    def __init__(self, id, title, director, producer, episode_no, release_date, img_url):
        self.id = id
        self.title = title
        self.director = director
        self.producer = producer
        self.episode_no = episode_no
        self.release_date = release_date
        self.img_url = img_url


class Character:
    """
        Character model
        Contains the following attributes:
            DB id
            name
            gender
            birth year
            height
            mass
            image URL

        Contains the following relations:
            Films (many-to-many)
            Planets (one-to-one)
            Species (one-to-one)
    """

    def __init__(self, id, name, gender, birth_year, height, mass, img_url):
        self.id = id
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.height = height
        self.mass = mass
        self.img_url = img_url


class Planet:
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

    def __init__(self, id, name, climate, population, gravity, terrain, img_url):
        self.id = id
        self.name = name
        self.climate = climate
        self.population = population
        self.gravity = gravity
        self.terrain = terrain
        self.img_url = img_url


class Species:
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

    def __init__(self, id, name, climate, population, gravity, terrain, img_url):
        self.id = id
        self.name = name
        self.climate = climate
        self.population = population
        self.gravity = gravity
        self.terrain = terrain
        self.img_url = img_url
