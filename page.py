import wikipedia
import tf_idf

class Page(object):
	""" A class which extends wikipedia.wikipedia.WikipediaPage.
	Adds methods that are useful to wikiracer.
	Currently just wraps the WikipediaPage class instead of actually
	extending it since I can't get that to work."""
	def __init__(self, page_title):
		self.wikipage_obj = wikipedia.page(page_title)
		self.score = None

	def __eq__(self, other):
		return self.wikipage_obj.__eq__(other.wikipage_obj)

	def __str__(self):
		return self.wikipage_obj.title

	def __repr__(self):
		return self.wikipage_obj.__repr__()

	def list_of_words(self):
		content = self.wikipage_obj.content

		string = content.encode('ascii', 'replace')

		ls = str.split(string)
		return ls

	def title(self):
		return str(self.wikipage_obj.title.encode('ascii', 'replace'))

	def links(self):
		return self.wikipage_obj.links
