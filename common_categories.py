import operator
import offline_page
import page
from path import Path
import category
import wikipedia as wiki

debug = False

def make_possiblities(current_page):
	""" Builds a list of pages linked to by current_page """
	print "fetching linked pages"
	possibilities = []

	for title in current_page.links():
		try:
			if debug: print "fetching " + str(title) 
			possibilities.append(offline_page.Page(title))
		except Exception, msg:
			if debug: print "caught an error: " + str(msg)
	return possibilities


def compute_scores(dest_cats, possibilities):
	""" Goes through all possiblites and adds a score field to them. """
	print "computing scores"

	for possible_page in possibilities:
		try:
			possible_page_cats = wiki.page(possible_page.page_title).categories
		except:
			possible_page_cats = []

		score =	category.similarity(dest_cats, possible_page_cats)
		if debug: print possible_page.title() + " gets score " + str(score)
		possible_page.score = score


def best_guess(possibilities, path_so_far):
	""" Given a scored set of possibilities, return the possiblity with the
		lowest score
		by looking at path_so_far, ignores pages we've already visited"""
	best_yet = possibilities[0]
	for possible_page in possibilities:
		if (possible_page.score > best_yet.score) and not possible_page in path_so_far:
			best_yet = possible_page
	return best_yet


def navigate(origin_title, destination_title):
	""" Navigates from origin_title to destination_title, trying to find the
		shortest path. Returns a Path from the start to end.
		At least, it'll do this eventually"""

	# Get set up to start
	origin = offline_page.Page(origin_title)
	destination = offline_page.Page(destination_title)
	current_page = origin
	path = [origin]

	print "starting at " + current_page.title()

	try:
		dest_cats = wiki.page(destination.page_title).categories
	except:
		dest_cats = []

	# Search through pages
	clicks = 0
	while current_page != destination:
		possibilities = make_possiblities(current_page)

		# Check if we've found it
		if destination in possibilities:
			print "found destination page"
			path.append(destination)
			return Path(path)
		elif clicks >= 20:
			print "TIMEOUT_ERROR: Path exceeded 20 nodes. Failed to find destination page."
			return Path(path)

		print "not at destination yet"
		compute_scores(dest_cats, possibilities)

		current_page = best_guess(possibilities, path)
		path.append(current_page)
		print "clicking on " + current_page.title()
		clicks += 1

