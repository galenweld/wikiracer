#from offline_page import Page
from page import Page

class Path(object):
	""" a simple class to compute stats on a path
		constructor takes list of page objects"""
	def __init__(self, list_of_articles):
		""" takes a list of page objects or titles and produces a path """
		self.articles = []
		for elt in list_of_articles:
			if type(elt) == str: self.articles.append(Page(elt))
			elif type(elt) == Page: self.articles.append(elt)
			else: raise TypeError("list may only contain titles or pages")
		self.num_nodes = len(list_of_articles)
		self.titles = [x.title() for x in list_of_articles]

	def __str__(self):
		""" returns pretty string of page titles """
		s = ''
		for title in self.titles[:-1]:
			s += title + " -> "
		return s + self.titles[-1]

	def __repr__(self):
		""" returns ugly string of page titles """
		return "<PathObj:" + str(self.articles) + ">"

	def __len__(self):
		""" returns number of edges in path """
		return self.num_nodes - 1

	def origin(self):
		""" returns the first article in the path """
		return self.articles[0]

	def destination(self):
		""" returns the last article in the path """
		return self.articles[-1]

	def branching_factor(self):
		""" returns the average branching_factor of
			the pages contained within the path """
		branches = 0
		for p in self.articles:
			branches += len(p.links())
		return float(branches)/self.num_nodes