from sys import argv, exit
import csv
from cs50 import get_string
import copy

#Compare new DNA with DNA in existing database

if len(argv) != 3:
    print ("Missing command-line argument")
    exit(1)

# Open first file and read to memory

with open(argv[1], newline='') as csvfile:
    reader = list(csv.DictReader(csvfile))

# Open second file and read to memory

file = open(argv[2],"r")
dna = file.read ()

# Close file
file.close()

# Create a new dictionary

new_dna = {}
new_dna = reader[0].copy()
new_dna.pop('name')


# Store STR values as a variable and add value to dictionary
for dnatype in new_dna:
    for n in range(len(dna)):
        if dnatype*n not in dna:
	        total = n-1
	        new_dna[dnatype] = total
	        break;


no_match = 0
match = False;

# Determine if DNA matches any of the previous participants
for n in range(0, len(reader)):
    for dnastrand, value in new_dna.items():
        if new_dna[dnastrand] != int(reader[n][dnastrand]):
            no_match = reader[n]
            break;
    if reader[n] != no_match:
        match = True
        print (reader[n]['name'])
        break;
if match == False:
    print("No Match")



