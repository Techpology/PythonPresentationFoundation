
class Route:
	def __init__(self):
		self.events = {}
	
	def newEvent(self, _c, _fn):
		new = getattr(_c, _fn)
		self.events[_fn] = new
	
	def getEvent(self, _fn):
		if(_fn in self.events):
			self.events[_fn]()