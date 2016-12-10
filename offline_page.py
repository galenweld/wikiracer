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

	Once the Wikipedia_Extractor has built a directory structure, an
	index needs to be built. For help with this, see the included build_index
	module.

	Once this prep work has been done, update the file paths below.

	authored by Galen Weld, December 2016 """

from bs4 import BeautifulSoup 
from os.path import join
import urllib
import time
import csv
import re

wikipedia_index_file = "/Users/galenweld/Wikipedia/index.csv"
wikipedia_base_directory = "/Users/galenweld/Wikipedia"
              # make sure there's no final slash here ^


############################## BUILD THE INDEX ##############################

def load_index():
	""" loads the wikipedia article index from wikipedia_index_file and
		returns it as a python dictionary """
	print "Offline Wikipedia: Loading Index\nThis may take a bit..."
	index = {}
	num_entries = 0
	start_time = time.time()

	with open(wikipedia_index_file) as index_file:
		csvreader = csv.reader(index_file, delimiter=',')

		for line in csvreader:
			index[line[0].lower()] = join(wikipedia_base_directory, line[1])
			num_entries += 1

	print "Loaded " + str(num_entries) + " index entries in " + \
			str(time.time() - start_time) + " seconds."
	return index

index = load_index()

#############################################################################

class Page(object):
	""" constructs and returns a page object with the given title
		throws a NameError if there is no matching page """
	def __init__(self, page_title):
		file_path = index.get(page_title.lower())
		if file_path == None: raise NameError("page with title " + page_title + " was not found")

		data = BeautifulSoup(open(file_path), 'html.parser')
		doc = data.find(title=re.compile(page_title, re.IGNORECASE))
		if doc == None: raise KeyError("error in index was detected when loading " + page_title)
			# note: if we're seeing a lot of these errors, it's probably a case snesitivity thing

		self.title = str(doc['title'])
		self.id = int(doc['id'])
		self.url = str(doc['url'])
		self.body = doc.get_text()

		self.list_of_links = [urllib.unquote(x['href'].encode('ascii', 'replace')) for x in doc.find_all('a')]

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
		

p = Page("Seattle")
print p.links()