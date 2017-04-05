from flask import render_template, redirect, request
from app import application
from app.db_util import get_film, get_films, get_planet, get_planets, get_character, get_characters, get_species, get_all_species
from app.filters import filters
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

# TODO: Add routes for species


@application.route('/about')
def about():
    return render_template('about.html')


@application.route('/report')
def report():
    return render_template('report.html')
@application.route('/species/<species_id>')
def species(species_id):
    species_id = int(species_id)
    return render_template('species_instance.html',species=get_species(species_id))

# api stuff

@application.route('/api')
def api():
    return "Our API starts here!"

@application.route('/api/planets')
def api_planets():
    return redirect('/api/planets/?page=1')

@application.route('/api/planets/')
def api_planet_query():
    return process_query(get_planets())

@application.route('/api/species')
def api_species():
    return redirect('/api/species/?page=1')

@application.route('/api/species/')
def api_species_query():
    return process_query(get_species())

@application.route('/api/films')
def api_films():
    return redirect('/api/films/?page=1')

@application.route('/api/films/')
def api_film_query():
    return process_query(get_films())

@application.route('/api/characters')
def api_characters():
    return redirect('/api/characters/?page=1')

@application.route('/api/characters/')
def api_character_query():
    return process_query(get_characters())


def process_query(mylist):
    page = request.args.get('page')
    filtBy = request.args.get('filterBy')
    filt = request.args.get('filter')
    sort = request.args.get('sortUp')
    # process raw setting
    raw = request.args.get('raw')
    if raw != None:
        raw = True
    else:
        raw = False

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
        mylist.sort(key= lambda a: getattr(a, sort), reverse=rev)
    mylist = paginate(mylist, 5, int(page))
    """
    if not raw:
        planet_list = clean_data(deepcopy(planet_list))
    """
    mylist = jsonpickle.encode(mylist)
    """"
    if not raw:
        planet_list = clean_json(planet_list)"""
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
        for atr in (a for a in dir(i) if not a.startswith('__')):
            if atr != 'name':
                delattr(i, atr)
    return data

def to_json(data):
    return clean_json(jsonpickle.encode(data))

def clean_json(data):
    json_data = json.loads(data)
    print(json_data)
    for i in json_data:
        if 'py/object' in i:
           i.pop('py/object', None)
    return json.dumps(json_data)


# TODO: Grab images from Bing Image search api, instead of hardcoding
# TODO: Python version issue. Using 2.7 but should be using 3.6 :(