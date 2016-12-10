""" needed to remove extra '/' at beginning of index entry """

import os
import csv

inp = '/Users/galenweld/Wikipedia/index.csv'

outp = '/Users/galenweld/Wikipedia/new_index.csv'

inf = file(inp, 'rb')
outf = file(outp, 'wb')

reader = csv.reader(inf)
writer = csv.writer(outf)



for line in reader:
	path = line[1]
	writer.writerow([line[0], path[1:]])








inf.close()
outf.close()