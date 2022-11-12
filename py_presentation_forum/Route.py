
class Route:
	def __init__(self, _hnwd):
		self.events = {}
		self.onDone	= {}
		self.doneTrigger = lambda: print("")
	
	def newEvent(self, _c, _fn):
		new = getattr(_c, _fn)
		self.events[_fn] = new
	
	def newOnDone(self, _c, _fn):
		new = getattr(_c, _fn)
		self.onDone[_fn] = new
	
	def getEvent(self, _fn):
		if(";" in _fn):
			_parsed = _fn.split(";")
			if(_parsed[1] in self.events):
				self.events[_parsed[1]](_parsed[1:])
				print(self.onDone)
				if(_parsed[1] + "_done" in self.onDone):
					self.doneTrigger = lambda: self.onDone[_parsed[1] + "_done"](_parsed[1:])
				else:
					self.doneTrigger = lambda: print("")
	
	def getOnDone(self):
		self.doneTrigger()
