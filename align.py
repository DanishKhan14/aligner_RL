#!/usr/bin/python

import os
import sys
import glob
import subprocess

def runAligner():
    print "Running Bowtie Aligner \n"
    index = raw_input("Enter the microbe name ...\n")
    fatqFile = raw_input("Enter the fastq file path...\n")
    outfile = raw_input("Enter the output file path...\n")
    
    print "Running Command:\n"
    print "~/bowtie/bowtie-1.1.2/bowtie -v 2 -a -m 3 --best --strata Community_db --suppress 1,2,4,5,6,7 fastqFile.fastq > outPutFile"

    cmdList = ['./bowtie', '-v', '2', '-a', '-m', '3', '--best', '--strata', index,'--suppress','1,2,4,5,6,7',fatqFile, outfile]    
    subprocess.call(cmdList)

