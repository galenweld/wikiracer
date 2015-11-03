import wikipedia
import tf_idf

class page(object):
	""" A class which extends wikipedia.wikipedia.WikipediaPage.
	Adds methods that are useful to wikiracer.
	Currently just wraps the WikipediaPage class instead of actually
	extending it since I can't get that to work."""
	def __init__(self, page_title):
		self.wikipage_obj = wikipedia.page(title)

	def __eq__(self, other):
		return self.wikipage_obj = other.wikipage_obj

	def list_of_words(self):
		string = (self.wikipage_obj.content(self)).encode('ascii', 'replace')
		return str.split(string)
