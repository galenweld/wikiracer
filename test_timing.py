#from offline_page import Page
from page import Page
import time

titles = ['Seattle','Cornell University','Africa','Computer science','Sahara']
num_reps = 10

start_time =  time.time()

for title in titles:
	p = Page(title)

print "ran in " + str(time.time()-start_time) + " seconds"