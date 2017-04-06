from flask import render_template, redirect, request
from app import application
from app.db_util import get_film, get_films, get_planet, get_planets, get_character, get_characters, get_species, get_all_species
from app.filters import filters, numeric_fields, toNum
import json
from copy import deepcopy   

import jsonpickle


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/films/<film_id>')
def film(film_id):
    film_id = int(film_id)
    return render_template('film_instance.html', film=get_film(film_id))


@application.route('/films')
def films():
    data = jsonpickle.encode(get_films())
    return render_template('films.html', films=data)


@application.route('/characters/<character_id>')
def character(character_id):
    character_id = int(character_id)
    return render_template('character_instance.html', character=get_character(character_id))


@application.route('/characters')
def characters():
    data = jsonpickle.encode(get_characters())
    return render_template('characters.html', characters=data)


@application.route('/planets/<planet_id>')
def planet(planet_id):
    planet_id = int(planet_id)
    return render_template('planet_instance.html', planet=get_planet(planet_id))


@application.route('/planets')
def planets():
    data = jsonpickle.encode(get_planets())
    return render_template('planets.html', planets=data)


@application.route('/species/<species_id>')
def species(species_id):
    species_id = int(species_id)
    return render_template('species_instance.html',species=get_species(species_id))


@application.route('/species')
def all_species():
    data = jsonpickle.encode(get_all_species())
    return render_template('species.html', species=data)


@application.route('/about')
def about():
    return render_template('about.html')


@application.route('/report')
def report():
    return render_template('report.html')


# api stuff

def fix_film(f):
    f.planet_list = ["http://www.thesweawakens.me/api/planets/{}".format(p.id) for p in f.planets]
    f.species_list = ["http://www.thesweawakens.me/api/species/{}".format(p.id) for p in f.species]
    f.character_list = ["http://www.thesweawakens.me/api/characters/{}".format(p.id) for p in f.characters]
    return f

def fix_planet(p):
    p.character_list = ["http://www.thesweawakens.me/api/characters/{}".format(x.id) for x in p.characters]
    p.film_list = ["http://www.thesweawakens.me/api/films/{}".format(x.id) for x in p.films]
    return p

def fix_species(s):
    s.character_list = ["http://www.thesweawakens.me/api/characters/{}".format(x.id) for x in s.characters]
    s.film_list = ["http://www.thesweawakens.me/api/films/{}".format(x.id) for x in s.films]
    return s

def fix_character(c):
    c.home_planet = "http://www.thesweawakens.me/api/characters/{}".format(c.planet_id)
    c.film_list = ["http://www.thesweawakens.me/api/films/{}".format(x.id) for x in c.films]
    return c

@application.route('/api')
def api():
    return "Our API starts here!"


""" PLANETS API """


@application.route('/api/planets')
def api_planets():
    return redirect('/api/planets/?page=1')


@application.route('/api/planets/')
def api_planet_query():
    return process_query(get_planets(), model='planet')


@application.route('/api/planets/<planet_id>')
def api_planet(planet_id):
    return process_query([get_planet(int(planet_id))], model='planet')


""" SPECIES API """


@application.route('/api/species')
def api_all_species():
    return redirect('/api/species/?page=1')


@application.route('/api/species/')
def api_all_species_query():
    return process_query(get_all_species(), model='species')


@application.route('/api/species/<species_id>')
def api_species(species_id):
    return process_query([get_species(int(species_id))], model='species')


""" FILMS API """


@application.route('/api/films')
def api_films():
    return redirect('/api/films/?page=1')


@application.route('/api/films/')
def api_film_query():
    return process_query(get_films(), model='film')


@application.route('/api/films/<film_id>')
def api_film(film_id):
    return process_query([get_film(int(film_id))], model='film')


""" CHARACTERS API """


@application.route('/api/characters')
def api_characters():
    return redirect('/api/characters/?page=1')


@application.route('/api/characters/')
def api_character_query():
    return process_query(get_characters(), model='character')


@application.route('/api/characters/<character_id>')
def api_character(character_id):
    return process_query([get_character(int(character_id))], model='character')


def process_query(mylist, model):
    page = request.args.get('page')
    if page is None:
        page = 1
    filtBy = request.args.get('filterBy')
    filt = request.args.get('filter')
    sort = request.args.get('sortUp')
    # process raw setting
    raw = request.args.get('raw')
    if raw != None:
        raw = True
    else:
        raw = False

    if not raw:
        # fix the list
        if model == 'film':
            for f in mylist:
                fix_film(f)
        elif model == 'planet':
            for p in mylist:
                fix_planet(p)
        elif model == 'character':
            for c in mylist:
                fix_character(c)
        elif model == 'species':
            for s in mylist:
                fix_species(s)

    # determine if sort should be backwards
    if sort != None:
        rev = False
    else:
        sort = request.args.get('sortDown')
        rev = True

    # filter
    # get filter
    if filtBy != None and filtBy in filters:
        myFilter = filters[filtBy]
        if myFilter != None:
            mylist = myFilter(mylist, filt)
    # sort
    if sort != None:
        if sort.lower() in numeric_fields:
            mylist.sort(key= lambda a: toNum(getattr(a, sort)), reverse=rev)
        else:
            mylist.sort(key= lambda a: getattr(a, sort).lower(), reverse=rev)
    mylist = paginate(mylist, 6, int(page))
    """
    if not raw:
        mylist = clean_data(deepcopy(mylist))"""

    mylist = jsonpickle.encode(mylist)

    if not raw:
        mylist = clean_json(mylist)
    # return jsonpickle.encode(db.get_planets())

    return mylist



def make_page(data, type, page):
    json_data = json.loads(data)
    page_data = {}
    page_data['count'] = len(json_data)
    if page > 1:
        page_data['previous'] = '/api/planets/?page='+str(page -1)
    else:
        page_data['previous'] = None
    page_data['next'] = '/api/planets/?page='+str(page +1)
    page_data['results'] = json_data
    return json.dumps(page_data)


def paginate(data, size, page):
    page_data = []
    print(data)
    for i in range((page-1)*size, min(page*size, len(data))):
        page_data += [data[i]]
    return page_data

def clean_data(data):
    for i in data:
        for atr in (a for a in dir(i) if not a.startswith('_')):
            if atr != 'name':
                delattr(i, atr)
    return data

def to_json(data):
    return clean_json(jsonpickle.encode(data))

def clean_json(data):
    json_data = json.loads(data)
    for i in json_data:
        if "py/object" in i:
            i.pop("py/object")
        if "_sa_instance_state" in i:
            i.pop("_sa_instance_state")
        if "py/state" in i:
            i.pop("py/state")
        if "planets" in i:
            i.pop("planets")
        if "planet" in i:
            i.pop("planet")
        if "films" in i:
            i.pop("films")
        if "characters" in i:
            i.pop("characters")
        if "species" in i:
            i.pop("species")
    return json.dumps(json_data)


# TODO: Grab images from Bing Image search api, instead of hardcoding
# TODO: Python version issue. Using 2.7 but should be using 3.6 :(