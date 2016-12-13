

def similarity(destCats,currentCats):
	'''
		given two lists of categories associated with two pages
	returns a similarity index based on the number of 
	categories two pages have in common
	'''
	sim = 0.0
	for cat in destCats:
		if cat in currentCats:
			sim += 1
	return sim