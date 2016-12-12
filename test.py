import time
from page import Page
from path import Path
from informed_greedy import navigate

pairs = [
('Seattle','San Francisco'),
('Cornell University','Antarctica'),
('Computer Science','Sumo'),
('Trilobite','London'),
('Arthur H. Rosenfeld','International Space Station')]

paths = []
times = []

for origin, destination in pairs:
	start_time = time.time()
	p = navigate(origin, destination)
	times.append(time.time()-start_time)
	paths.append(p)

for i in range(len(pairs)):
	print "Origin-Destination Pair "+str(i)+":"
	print "Origin:\t" + paths[i].origin()
	print "Destination:\t" + paths[i].destination()
	print "(generated in "+str(times[i])+ "sec)"
