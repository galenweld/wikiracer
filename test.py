import time
from page import Page
from path import Path
from informed_greedy import navigate

pairs = [
('Seattle','San Francisco'),
('Cornell University','Antarctica'),
('Computer Science','Sumo'),
('Trilobite','London Underground'),
('Arthur H. Rosenfeld','International Space Station')]


def compute_test_results(list_of_pairs):
	""" prints out the results of computing the paths between
		a whole bunch of start/end pairs, provided as a list.
		For formatting, see the above list."""
	paths = []
	times = []

	for origin, destination in pairs:
		start_time = time.time()
		p = navigate(origin, destination)
		times.append(time.time()-start_time)
		paths.append(p)

	for i in range(len(pairs)):
		print "Origin-Destination Pair "+str(i)+":"
		print "Origin:\t" + str(paths[i].origin())
		print "Destination:\t" + str(paths[i].destination())
		print "Path:\t" + str(paths[i])
		print "Path Length\t" + str(len(paths[i]))
		print "(generated in "+str(times[i])+ "sec)"
