#! /usr/bin/env python
#this script will convert csv to a json file formatted for tablesorter.js

import csv
import json

# Open the CSV
f = open( '../data/unreviewed cases - Sheet 1.csv', 'rU' )

reader = csv.reader( f, dialect='excel')

#skip the header row since we're setting those up manually
reader.next() 

#column headers - you can customize each label by creating an object for it like this: { "text": "First Name", "class": "fname", "width": "20%" }
headers = [
	[
		{ "text": "Age", "class": "age", "data-sorter": "false" }, { "text": "Date of death", "class": "death", "data-sorter": "false"}, "County", { "text": "Cause of death", "class": "cause", "data-sorter": "false"}, "Manner of death", { "text": "Previous DFCS case?", "class": "dfcs", "data-sorter": "false"}
	]
]

#set footer property to clone the headers
footers = "clone"

#push rows into an array
rows = []
for row in reader:
	rows.append(row)

#create object with key:value pairs
tree = { "headers": headers, "footers": footers, "rows": rows }

#convert to json
out = json.dumps(tree)
print "JSON parsed!"

# Save the JSON
f = open( '../data/unreviewed_table.json', 'w')
f.write(out)
print "JSON saved!"