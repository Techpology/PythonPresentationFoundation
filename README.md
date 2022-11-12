# PythonPresentationFoundation

##### Description:
Python Presentation Foundation allows the use of html and css to design and style UI for the purpose of use within tkinter.
The binding between both html and tkinter is done using tkinterweb. All events are currently handled by url requests.
An event system built in to the `py_presentation_forum.Handle` class allows to bind python functions to urls.
Arguments can be passed through the requests from the html side.

## Installation
```
pip install py-presentation-foundation
```
https://pypi.org/project/py-presentation-foundation/#description

## Getting started
Create a directory with two files, a `main.py`, and a `config.json`. Create a directory for your html files to keep things clean.
Create an index.html file within
```
Directory|
         |-->main.py
         |-->config.json
         |-->Design|
                   |-->index.html
```

```python
# main.py
from py_presentation_forum import Handle
from py_presentation_forum.Utils import Utils

global hnwd
global conf
conf = Utils().getConfig("./config.json")
hnwd = Handle(conf)

hnwd.win.mainloop()
```
```json
{
  "url": "file:///C:/{...path}/Design/index.html"
}
```
You can aquire the `[url]` path by viewing the html file in a browser and proceeding to copy the link from the url bar.

## Events
There are two type of events, one that is triggered when the request is sent, and one that is triggered after the request has finished rendering.

We can test this by using this script:
```python
from py_presentation_forum import Handle
from py_presentation_forum.Utils import Utils

from tkinter import messagebox

global hnwd
global conf
conf = Utils().getConfig("./config.json")
hnwd = Handle(conf)

class evnts:
	def alert(args):
		messagebox.showwarning(args[1], args[2])
	
	def alert_done(args):
		global hnwd
		global conf
		hnwd.frame.load_file(conf["url"])

hnwd.routes.newEvent(evnts, "alert")
hnwd.routes.newOnDone(evnts, "alert_done")

hnwd.win.mainloop()
```

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
	</head>
	
	<body>
		<a href=";alert;test;hello world" class="button is-info">Info</a>
	</body>
</html>
```

Request paths must contain a semi column `;`.
In this case we want to call an event called `alert`.
Therefore we can call the function by using a hyperlink specifying the request route.
for example:
```html
<a href=";alert">Test</a>
```
This would call the alert function.
If we need to pass arguments to the alert function, we can do so as such:
```html
<a href=";alert;arg1;arg2">Test</a>
```

if an `onDone` event has been passed with the prefix of the primary functions name, then the `onDone` event will be called automatically.
In the examples case, we use alert to show a warning box, and the alert_done to redirect back to the home page `index.html`
