""" A python file containing methods to access wikipedia pages without
	needing an internet connection. The wikipedia.xml is intended
	to be created from a wikipedia database dump, available online
	at https://meta.wikimedia.org/wiki/Data_dumps
	These XML files should then be cleaned using the Wikipedia_Extractor
	available at http://medialab.di.unipi.it/wiki/Wikipedia_Extractor

	Make sure to preseve links (the -l flag) when using Wikipedia_Extractor
	This process took approximately 6 hours running on my 2014 Macbook
	Pro	to convert ~4.5 million articles from a 2014 dump of only the
	current revisions of the English language Wikipedia.

	The resulting files are then easily concatenated into a single
	large XML wile with cat */*wiki_* > wikipedia.xml

	This wikipedia.xml file should be formatted as defined here:
	http://medialab.di.unipi.it/wiki/Document_Format

	authored by Galen Weld, December 2016 """

from bs4 import BeautifulSoup
import re

point_this_to_your_wikipedia_xml = "/Users/galenweld/Wikipedia/wikipedia.xml"

wiki = BeautifulSoup(open(point_this_to_your_wikipedia_xml), 'html.parser')


class Page(object):
	""" constructs and returns a page object with the given title
		throws a NameError if there is no matching page """
	def __init__(self, page_title):
		tag = wiki.find(title=page_title) # this part may take a while
		if tag == None: raise NameError("page with title " + page_title + " was not found")

		self.title = str(tag['title'])
		self.id = int(tag['id'])
		self.url = str(tag['url'])
		self.body = tag.get_text()

		self.list_of_links = [x.string.encode('ascii', 'replace') for x in tag.find_all('a')]



	def __eq__(self, other):
		return self.id == other.id

	def __str__(self):
		return self.title

	def __repr__(self):
		return "Page_id:" + str(self.id) + '_' + self.title

	def list_of_words(self):
		""" returns a list of strings contained within the text of the page
			all non alphanumeric characters, including all punctuation, are
			removed"""
		return str.split(re.sub(r'\W+', ' ', self.body.encode('ascii', 'replace')))

	def links(self):
		""" returns a list of strings, where each string is the title of a 
		wikipedia page linked to in this page """
		return self.list_of_links
		


# tag = wiki.find(title="Achilles")

# print [x.string.encode('ascii', 'replace') for x in tag.find_all('a')]

p = Page("University of Washington")
print p.links()