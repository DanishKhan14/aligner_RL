#!/usr/bin/python

import os
import sys
import csv
import glob
import subprocess

def main(argv):
    db = argv[0]
    for readFile in argv[1:]:
        baseName = os.path.basename(readFile)
        outfile = "output/" + os.path.splitext(baseName)[0]+".csv"
        umfile = "unmatched/" + os.path.splitext(baseName)[0]+".txt"
        suppressfile = "suppressed/" + os.path.splitext(baseName)[0]+".txt"
        runAligner(db, readFile, outfile, umfile, suppressfile)
        print "Now running nomralization ... \n"
        normFactor = getNormalizationFactor(db)
        formatOutput(outfile, normFactor)


def formatOutput(fileName, normFactor):
    wordCount = {}
    f = open(fileName, 'r')
    for line in f.readlines():
        if line.split('\t')[0] not in wordCount:
            wordCount[line.split('\t')[0]] = 1
        else:
            wordCount[line.split('\t')[0]]+=1
    f.close()

    totalNormCount = 0.0
    for key, value in wordCount.items():
        totalNormCount+=value*normFactor[key]

    with open(fileName, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Genome','Raw Count','Norm Count','Fraction', 'Percentage'])
        for key, value in wordCount.items():
            normCount = value*normFactor[key]
            writer.writerow([key, value, normCount, normCount/totalNormCount, (normCount/totalNormCount)*100])

def getNormalizationFactor(db):
    normFactor = {}
    cmdList = ['./bowtie-inspect', '-s', db]    
    output = subprocess.check_output(cmdList)

    genomes = output.split('\n')[3:]
    avgGenomeSize = sum([int(i.split('\t')[-1]) for i in genomes if i])/len(genomes)
    print avgGenomeSize

    for genome in genomes:
        if genome:
            normFactor[genome.split('\t')[1]] = round(float(genome.split('\t')[-1])/avgGenomeSize, 4)

    print normFactor
    return normFactor


def runAligner(index, readFile, outfile, umfile, suppressfile):
    print "Running Bowtie Aligner \n"
    fatqFile = readFile
    
    print "Running Command:\n"
    print "~/bowtie/bowtie-1.1.2/bowtie -v 2 -a -m 3 --best --strata Community_db --suppress 1,2,4,5,6,7 fastqFile.fastq > outPutFile"

    cmdList = ['./bowtie', '-v', '2', '-a', '-m', '3', '--best', '--strata', '--un', umfile, '--max', suppressfile, index,'--suppress','1,2,4,5,6,7',fatqFile, outfile]    
    subprocess.call(cmdList)


if __name__ == "__main__":
    main(sys.argv[1:])
