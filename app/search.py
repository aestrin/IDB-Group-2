from app.models import Film, Character, Planet, Species
from app.db_util import get_film, get_films, get_planet, get_planets, get_character, get_characters, get_species, get_all_species
from sqlalchemy.orm.attributes import InstrumentedAttribute
from app import db

def contextOf(match, searchTerm):
	items = match.split(searchTerm)
	count = len(items) - 1;
	contexts = "";
	for i in range(count):
		context = "["
		# show up to 3 words before
		wordsbefore = items[i].split(" ")
		for w in wordsbefore[-3:]:
				context+= w+" "
		context += searchTerm
		# show up to 3 words after
		wordsafter = items[i].split(" ")
		for w in wordsafter[-3:]:
				context+= w+" "
		contexts += context + "]..."
	return contexts, count



def combinecontext(a, b):
	together = set(a.split("..."))
	together = together | set(b.split("..."))
	ret = ""
	for s in together:
		if s != "":
			ret += s+"..."
	return ret

def combine(a, b):
	for r in b:
		if r in a:
			a[r][0] += b[r][0]
			a[r][1] = combinecontext(a[r][1], b[r][1])
			a[r][2] += b[r][2]
		else:
			a[r] = b[r]

def searchterm (words):
	results = {}
	for term in words.split(" "):
		result = {}
		result.update(searchModel(Film, term))
		result.update(searchModel(Character, term))
		result.update(searchModel(Species, term))
		result.update(searchModel(Planet, term))
		combine(results, result)
	return results

def searchModel (model, term):
	myQuery = db.session.query(model)
	queryParams = None
	for attr in model.__table__.columns.keys():
		if "id" in attr or "url" in attr:
			continue
		col = getattr(model, attr)
		if queryParams is None:
			queryParams = col.ilike('%'+term+'%')
		else:
			queryParams = queryParams | col.ilike('%'+term+'%')
	results = myQuery.filter(queryParams).all()
	summary = {}
	for r in results:
		count = 0
		context = ""
		for attr in model.__table__.columns.keys():
			if "id" not in attr and "url" not in attr and term.lower() in getattr(r, attr).lower().split(): 
				count += getattr(r, attr).lower().count(term.lower())
				# title and name attributes are worth triple
				if attr == "title" or attr == "name":
					count += getattr(r, attr).lower().count(term.lower()) * 2
				context += str(attr)+": " + getattr(r, attr) + "..."
			# if attribute matches title or name, count it towards its connections
			if (attr == "title" or attr == "name") and term.lower() in getattr(r, attr).lower().split():
				reflist = []
				if model is Species:
					reflist += r.characters
				if model is Character:
					if r.planet_id is not None:
						reflist += [get_planet(r.planet_id)];
					if r.species_id is not None:
						reflist += [get_species(r.species_id)];
				if model is Film:
					reflist += r.characters
					reflist += r.planets
					reflist += r.species
				if model is Planet:
					reflist += r.characters
				for ref in reflist:
					url = ref.model_url+"/"+str(ref.id)
					if url in summary:
						summary[url][0] += getattr(r, attr).lower().count(term.lower())
						addstr = r.model_name+": "+getattr(r, attr)+"..."
						if addstr not in summary[url][1]:
							summary[url][1] += addstr
					else:
						summary[url] = [getattr(r, attr).lower().count(term.lower()), r.model_name+": "+getattr(r, attr)+"...", 1, ref.img_url]
		if count > 0:
			summary[model.model_url+"/"+str(r.id)] = [count, context, 1, r.img_url]
	return summary
