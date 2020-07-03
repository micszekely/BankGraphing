import sys
import csv
import matplotlib.pyplot as plt


try:                                                    #Open CSV
	filename = sys.argv[1]
	csv_file = open(filename, "r")
	next(csv_file)										#Skipping over column headers
except FileNotFoundError:
	print("File not found, exiting program")
	sys.exit(1)
reader = csv.reader(csv_file)

row_col = []
category = []
runningTotal = 0
catDict = {}

for row in reader:										#Appending data from CSV to arrays
	row_col.append(row)
	category.append(row[3])								#Generating list of category names (with duplicates)
csv_file.close()

uniqueCats = set(category)								#'Set' removes duplicates from array
uniqueCats.remove("")									#Blank category represents paying off CC

for cat in uniqueCats:									#catDict = total spend per category
	catDict[cat] = 0									#initializing dict

for row in row_col:										#Assigining transactions to category
	cat = row[3]
	if cat is "":										#Don't assign paying off CC to a category
		continue
	amount = row[5]
	amount = float(amount)
	catDict[cat] = catDict[cat] + amount

totalSpent = sum(list(catDict.values()))
percentDict = {}

for cat in catDict:										# % total needed for pie chart
	percentDict[cat] = catDict[cat] / totalSpent


fig1, ax1 = plt.subplots()
ax1.pie(list(percentDict.values()), labels=uniqueCats, autopct='%1.1f%%',		#pass arguments
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()