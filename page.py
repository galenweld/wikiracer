import wikipedia

class page(wikipedia.wikipedia.WikipediaPage):
	""" A class which extends wikipedia.wikipedia.WikipediaPage.
	Adds methods that are useful to wikiracer. """
	def __init__(self, title):
		wikipedia.wikipedia.WikipediaPage.__init__(self, title=title)
	
	