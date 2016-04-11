#!/usr/bin/python

import os
import sys
import glob

opt = raw_input("Select an option: \n 1 - run aligner \n 2 - show results \n 3 - plot graph \n 4 - exit\n")

'''
if opt not in ['1','2','3','4']:
	print("Please enter a valid number choice\n")
	opt = raw_input("Select an option: \n 1 - run aligner \n 2 - show results \n 3 - plot graph \n 4 - exit")
'''
def runAligner():
    print "Running Bowtie Aligner \n"

def showResults():
    print "Counts from given aligner results \n"
    
    path = raw_input("Enter the input directory ... \n")

    for file in glob.glob(os.path.join(path, '*.fasta')):
        #run per file freq count and display result
        print ("To be done....\n")

def plotGraph():
    print "Plotting Graph... \n "

if opt == "1":	
    runAligner()
elif opt == "2":
    showResults()
elif opt == "3":
    plotGraph()
elif opt == "4":
    exit()
else:
    print("Please enter a valid number choice\n")
    opt = raw_input("Select an option: \n 1 - run aligner \n 2 - show results \n 3 - plot graph \n 4 - exit")
