import operator
import page
import tf_idf

def navigate(origin_title, destination_title):
	origin = page.Page(origin_title)
	destination = page.Page(destination_title)

	current_page = origin
	print "starting at " + current_page.title()

	while current_page != destination:
		possibilities = []
		for title in current_page.links():
			try:
				print "fetching " + str(title) 
				possibilities.append(page.Page(title))
			except Exception, msg:
				print "caught an error: " + str(msg)

		print "computing scores"
		for possible_page in possibilities:
			if possible_page == destination: current_page = possible_page
			else:
				score =	tf_idf.distance(destination.list_of_words(), possible_page.list_of_words())
				print possible_page.title() + " gets score " + str(score)
				possible_page.score = score

		best_yet = possibilities[0]
		for possible_page in possibilities:
			if possible_page.score < best_yet.score:
				best_yet = possible_page
		print "clicking on " + best_yet.title()
		current_page = best_yet

	print "made it to " + current_page.title()

navigate("Daniel S. Weld", "University of Washington")