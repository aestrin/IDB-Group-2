class MatchFilter:
	def __init__(self, filtAtr):
		self.filtAtr = filtAtr

	def __call__(self, items, value):
		return [a for a in items if hasattr(a, filtAtr) and getattr(a, filtAtr) == value]


class RangeFilter:
	def __init__(self, filtAtr):
		self.filtAtr = filtAtr

	def __call__(self, items, rangestr):
		lo = float(rangestr[:rangestr.index("-")])
		hi = float(rangestr[rangestr.index("-") + 1:])
		return [a for a in items if hasattr(a, filtAtr) and getattr(a, filtAtr) != "unknown" and float(getattr(a, filtAtr)) >= lo and float(getattr(a, filtAtr)) <= hi]

def NameFilter(items, rangestr):
		lo = rangestr[:rangestr.index("-")].lower()
		hi = rangestr[rangestr.index("-") + 1:].lower()
		return [a for a in items if hasattr(a, "name") and a.name.lower() >= lo and a.name.lower() <= hi]



filters = {"height" : RangeFilter("height"), "mass" : RangeFilter("mass"), "avg height" : RangeFilter("average_height"), "population": RangeFilter("population"), "name" : NameFilter, "director" : MatchFilter("director")}