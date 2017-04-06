def toNum(value):
	if value.lower() == "unknown" or value.lower() == "n/a" or value.lower() == "none":
		return float("inf")
	# find numeric substring
	index = 0
	for c in value:
		if c.isdigit() or c == ".":
			index += 1
		else:
			break
	if index == 0:
		return float("inf")
	return float(value[:index])


numeric_fields = {"gravity", "population", "birth_year", "height", "weight", "release_date", "average_height"}

# convert from string to correct type
def correctVal(value):
	# remove "units"
	pass

class MatchFilter:
	def __init__(self, filtAtr):
		self.filtAtr = filtAtr

	def __call__(self, items, value):
		return [a for a in items if hasattr(a, self.filtAtr) and getattr(a, self.filtAtr) == value]


class RangeFilter:
	def __init__(self, filtAtr):
		self.filtAtr = filtAtr

	def __call__(self, items, rangestr):
		lo = float(rangestr[:rangestr.index("-")])
		hi = float(rangestr[rangestr.index("-") + 1:])
		return [a for a in items if hasattr(a, self.filtAtr) and getattr(a, self.filtAtr) != "unknown" and float(getattr(a, self.filtAtr)) >= lo and float(getattr(a, self.filtAtr)) <= hi]

def NameFilter(items, rangestr):
		lo = rangestr[:rangestr.index("-")].lower()
		hi = rangestr[rangestr.index("-") + 1:].lower()
		return [a for a in items if hasattr(a, "name") and a.name.lower() >= lo and a.name.lower() <= hi]

filters = {"height" : RangeFilter("height"), "mass" : RangeFilter("mass"), "avg height" : RangeFilter("average_height"), "population": RangeFilter("population"), "name" : NameFilter, "director" : MatchFilter("director")}