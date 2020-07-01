import sys
import csv

# Open the file
try:
	filename = sys.argv[1]
	csv_file = open(filename, "r")
except FileNotFoundError:
	print("File not found, exiting program")
	sys.exit(1)

reader = csv.reader(csv_file)        #asdfasf