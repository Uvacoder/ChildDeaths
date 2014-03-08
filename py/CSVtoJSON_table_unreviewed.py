#! /usr/bin/env python
import csv
import json
from collections import OrderedDict as ordereddict
#this file will convert csv to its json equivalent, but note that order will not be mantained
# Open the CSV
f = open( '../data/unreviewed cases - Sheet 1.csv', 'rU' )

#reader = csv.DictReader( f, fieldnames = ( "school","fiscyear","tuitionfees","hopepays","studentowes","source","notes" )) #doing it this way will put row 1 into your data - exclude fieldnames to use row 1 as fieldnames
reader = csv.reader( f, dialect='excel')
reader.next() 

headers = [
	[
		"Age", "County", "Date of death", "Cause of death", "Manner of death", "Previous DFCS case?"
	]
]
footers = "clone"
rows = []
for row in reader:
	rows.append(row)

# Parse the CSV into JSON
tree = { "headers": headers, "footers": footers, "rows": rows }
out = json.dumps(tree)

print "JSON parsed!"

# Save the JSON
f = open( '../data/unreviewed_table.json', 'w')
f.write(out)
print "JSON saved!"