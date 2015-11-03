import operator
import page
import tf_idf

origin_title = "Hood Canal"
destination_title = "Seattle"

origin = page.page(origin_title)
destination = page.page(destination_title)

current_page = origin
print "starting at " + current_page.title

while current_page != destination:
	possibilities = []
	for title in current_page.links:
		try:
			print "appending " + str(title) + " to possibilities" 
			possibilities.append(page.page(title))
		except Exception:
			print "caught an error: " + str(Exception)

	print "computing scores"
	scores = []
	for page in possibilities:
		score = tf_idf.distance(destination.list_of_words, page.list_of_words)
		print page.title + " gets score " + str(score)
		scores.append(score)

	best_page = possibilities[scores.index(min(scores))]
	print "clicking on " + best_page.title
	current_page = best_page

print "made it to " + current_page.title