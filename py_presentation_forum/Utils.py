
import json

class Utils:
	def getConfig(self, _path):
		with open(_path, "r") as f:
			return json.loads(f.read())