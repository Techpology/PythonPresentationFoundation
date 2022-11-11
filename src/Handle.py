from tkinterweb import HtmlFrame
import tkinter as tk

import json

from Route import Route

class Handle:
	def __init__(self, _title="pypf app"):
		self.win	= tk.Tk()
		self.title	= _title

		self.config = self.getConfig("./config.json")

		self.routes = Route()

		self.frame	= HtmlFrame(self.win)
		self.frame.load_website(self.config["url"])
		self.frame.on_url_change(self.routes.getEvent)
		self.frame.pack(fill="both", expand=True)
		
		self.win.title(self.title)
		self.win.overrideredirect(1)
		self.win.mainloop()
	
	def getConfig(self, _path):
		return json.loads(_path)
