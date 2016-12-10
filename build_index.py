from bs4 import BeautifulSoup
from os.path import join
import os
import csv 

#####################################################

base_dir = '/Volumes/Vesper/wiki_extracted'

output_file_path = '/Volumes/Vesper/wiki_extracted/new_index.csv'

#####################################################

""" This file builds a CSV index of all wikipedia pages contained in
	an extracted Wikipedia dump that can be created using Wikipedia_Extractor

	It constructs a CSV where each article's title as associated with the
	path to the file (relative to the base_dir) containing its text.

	If this causes trouble, try deleting anything at output_file_path, and
	if your terminal yells at you, create a black file there with
	touch output_file_path

	authored by Galen Weld, December 2016 """

output_file = open(output_file_path, 'wb')
writer = csv.writer(output_file, delimiter=',')

for root, dirs, files in os.walk(base_dir):
	for filename in files:
		path = join(root, filename)
		relative_path = path[len(base_dir):]

		if filename[0] != '.':
			file_obj = open(path)
			data = BeautifulSoup(file_obj, 'html.parser')

			for doc in data.find_all('doc'):
				pid = int(doc['id'])
				title = doc['title'].encode('ascii', 'replace')
				print str(pid) + ":" + title + " at " + path
				writer.writerow([title, relative_path])

			file_obj.close()

output_file.close()