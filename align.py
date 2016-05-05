#!/usr/bin/python

import os
import sys
import glob
import subprocess


opt = raw_input("Select an option: \n 1 - run aligner \n 2 - show results \n 3 - plot graph \n 4 - exit\n")

'''
if opt not in ['1','2','3','4']:
	print("Please enter a valid number choice\n")
	opt = raw_input("Select an option: \n 1 - run aligner \n 2 - show results \n 3 - plot graph \n 4 - exit")
'''
def runAligner():
    print "Running Bowtie Aligner \n"
    fatqFile = raw_input("Enter the fstq file path...\n")
    db = raw_input("Enter the community db file path...\n")
    outfile = raw_input("Enter the output file path...\n")
    print "Running Command:\n"
    print "~/bowtie/bowtie-1.1.2$ ./bowtie -v 2 -a -m 3 --best --strata Community_db --suppress 1,2,4,5,6,7 fastqFile.fastq > outPutFile"

    cmdList = ['bowtie','--strata',db,'--suppress','1,2,4,5,6,7',fastqFile,'>',outfile]    
    subprocess.call(cmdList) 

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
