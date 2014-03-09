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
		{ "text": "Age", "class": "age", "data-sorter": "false" }, { "text": "Date of death", "class": "death", "data-sorter": "false" }, "County", "Months before review", { "text": "Details of death", "class": "cause", "data-sorter": "false" }, { "text": "Recommendation by child fatality review committee", "class": "recommendation", "data-sorter": "false" }, { "text":  "Family history with DFCS?", "class": "dfcs", "data-sorter": "false" }, { "text":  "Review find abuse or neglect caused death?", "class": "caused-death", "data-sorter": "false" }, { "text":  "Review find abuse or neglect contributed to death?", "class": "contributed", "data-sorter": "false" }, { "text":  "Death result in action by DFCS?", "class": "action", "data-sorter": "false" }, { "text":  "If yes, were other children taken into protective custody?", "class": "custody", "data-sorter": "false" }, { "text":  "Were criminal charges filed?", "class": "charges", "data-sorter": "false" },  { "text":  "Reasons committees cited for incomplete reviews", "class": "reasons", "data-sorter": "false" }
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