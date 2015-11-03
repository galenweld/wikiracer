import operator
import page
import tf_idf

origin_title = "Daniel S. Weld"
destination_title = "Seattle"

origin = page.Page(origin_title)
destination = page.Page(destination_title)

current_page = origin
print "starting at " + current_page.title()

while current_page != destination:
	possibilities = []
	for title in current_page.links():
		try:
			#print "appending " + str(title) + " to possibilities" 
			possibilities.append(page.Page(title))
		except Exception, msg:
			print "caught an error: " + str(msg)

	print "computing scores"
	scores = []
	for possible_page in possibilities:
		if possible_page = destination: current_page = possible_page
		else
			score = tf_idf.distance(destination.list_of_words(), possible_page.list_of_words())
			print possible_page.title() + " gets score " + str(score)
			scores.append(score)

	best_page = possibilities[scores.index(min(scores))]
	print "clicking on " + best_page.title()
	current_page = best_page

print "made it to " + current_page.title()