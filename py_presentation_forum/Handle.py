from tkinterweb import HtmlFrame
import tkinter as tk

import json

from py_presentation_forum.Route import Route

class Handle:
	def __init__(self, _conf={}, _title="pypf app"):
		self.win	= tk.Tk()
		self.title	= _title

		self.config = _conf

		self.routes = Route()

		self.frame	= HtmlFrame(self.win)
		self.frame.load_file(self.config["url"])
		self.frame.on_url_change(self.routes.getEvent)
		self.frame.pack(fill="both", expand=True)
		
		self.win.title(self.title)
		self.win.mainloop()
