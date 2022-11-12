
class Route:
	def __init__(self):
		self.events = {}
	
	def newEvent(self, _c, _fn):
		new = getattr(_c, _fn)
		self.events[_fn] = new
	
	def getEvent(self, _fn):
		_parsed = _fn.split(";")

		if(_parsed[1] in self.events):
			self.events[_fn](_parsed[1:])