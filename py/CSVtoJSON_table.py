#! /usr/bin/env python
import csv
import json
from collections import OrderedDict as ordereddict
#this file will convert csv to its json equivalent, but note that order will not be mantained
# Open the CSV
f = open( '../data/CFR Cases - online.csv', 'rU' )

#reader = csv.DictReader( f, fieldnames = ( "school","fiscyear","tuitionfees","hopepays","studentowes","source","notes" )) #doing it this way will put row 1 into your data - exclude fieldnames to use row 1 as fieldnames
reader = csv.reader( f, dialect='excel')
reader.next() 

headers = [
	[
		"Age", "Date of death", "County", "Months before review", "Details of death", "Recommendation by child fatality review committee", "Previous contact by family with government agency?", "Family history with DFCS?", "Review find abuse or neglect caused death?", "Review find abuse or neglect contributed to death?", "Death result in action by DFCS?", "If yes, were other children taken into protective custody?", "Were criminal charges filed?",  "Reasons committees cited for incomplete reviews"
	]
]
footers = "clone"
rows = []
for row in reader:
	rows.append(row)
	#print row
# Parse the CSV into JSON
tree = {"headers": headers, "footers": footers, "rows": rows}
out = json.dumps(tree)
#obj = { "total_rows": 0, "headers": ["Time before final report (months)", "No.", , "Name", ], "rows": out }
print "JSON parsed!"
print out

# Save the JSON
f = open( '../data/CFR_table.json', 'w')
f.write(out)
print "JSON saved!"