import requests
import json


NUM_PEOPLE = 88
NUM_STARSHIPS = 37
NUM_PLANETS = 61
NUM_FILMS = 7



def getJsonDict(model,numModel):
	jsondict = {}
	for i in range(1,numModel):
		url = "http://swapi.co/api/{0}/{1}".format(model,i) 	
		r = requests.get(url)
		jsondict[i]=r.json()
	return jsondict


peopleDict = getJsonDict("people",NUM_PEOPLE)
starshipDict = getJsonDict("starships",NUM_STARSHIPS)
filmDict = getJsonDict("films",NUM_FILMS)
planetDict = getJsonDict("planets",NUM_PLANETS)


with open('allPeople.json', 'w') as outfile:  
    json.dump(peopleDict, outfile)
with open('allStarships.json', 'w') as outfile:  
    json.dump(starshipDict, outfile)
with open('allFilms.json', 'w') as outfile:  
    json.dump(filmDict, outfile)
with open('allPlanets.json', 'w') as outfile:  
    json.dump(planetDict, outfile)
