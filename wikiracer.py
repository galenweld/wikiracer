import operator
from offline_page import Page
import tf_idf

debug = False

def make_possiblities(current_page):
	""" Builds a list of pages linked to by current_page """
	print "fetching linked pages"
	possibilities = []

	for title in current_page.links():
		try:
			if debug: print "fetching " + str(title) 
			possibilities.append(Page(title))
		except Exception, msg:
			print "caught an error: " + str(msg)
	return possibilities


def compute_scores(destination, possibilities):
	""" Goes through all possiblites and adds a score field to them. """
	print "computing scores"

	for possible_page in possibilities:
		score =	tf_idf.distance(destination.list_of_words(), possible_page.list_of_words())
		if debug: print possible_page.title() + " gets score " + str(score)
		possible_page.score = score


def best_guess(possibilities, path_so_far):
	""" Given a scored set of possibilities, return the possiblity with the
		lowest score
		by looking at path_so_far, ignores pages we've already visited"""
	best_yet = possibilities[0]
	for possible_page in possibilities:
		if (possible_page.score < best_yet.score) and not possible_page in path_so_far:
			best_yet = possible_page
	return best_yet


def navigate(origin_title, destination_title):
	""" Navigates from origin_title to destination_title, trying to find the
		shortest path. Returns a list of pages visited.
		At least, it'll do this eventually"""

	# Get set up to start
	origin = Page(origin_title)
	destination = Page(destination_title)
	current_page = origin
	path = [origin]

	print "starting at " + current_page.title()

	# Search through pages
	while current_page != destination:
		possibilities = make_possiblities(current_page)

		# Check if we've found it
		if destination in possibilities:
			print "found destination page"
			path.append(destination)
			return path

		print "not at destination yet"
		compute_scores(destination, possibilities)

		current_page = best_guess(possibilities, path)
		path.append(current_page)
		print "clicking on " + current_page.title()


print navigate("Arthur H. Rosenfeld", "Star Trek")