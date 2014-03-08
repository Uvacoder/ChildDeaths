#! /usr/bin/env python
#this script will convert csv to a json file formatted for tablesorter.js

import csv
import json

# Open the CSV
f = open( '../data/CFR Cases - online.csv', 'rU' )

reader = csv.reader( f, dialect='excel')

#skip the header row since we're setting those up manually
reader.next() 

#column headers - you can customize each label by creating an object for it like this: { "text": "First Name", "class": "fname", "width": "20%" }
headers = [
	[
		"Age", "Date of death", "County", "Months before review", "Details of death", "Recommendation by child fatality review committee", "Previous contact by family with government agency?", "Family history with DFCS?", "Review find abuse or neglect caused death?", "Review find abuse or neglect contributed to death?", "Death result in action by DFCS?", "If yes, were other children taken into protective custody?", "Were criminal charges filed?",  "Reasons committees cited for incomplete reviews"
	]
]

#set footer property to clone the headers
footers = "clone"

#push rows into an array
rows = []
for row in reader:
	rows.append(row)

#create object with key:value pairs
tree = {"headers": headers, "footers": footers, "rows": rows}

#convert to json
out = json.dumps(tree)
print "JSON parsed!"

# Save the JSON
f = open( '../data/CFR_table.json', 'w')
f.write(out)
print "JSON saved!"