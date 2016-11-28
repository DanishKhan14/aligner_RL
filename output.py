#!/usr/bin/python
import csv
import sys

def main(inputFile):
    wordCount = {}
    f = open(inputFile, 'r')
    for line in f.readlines():
        if line.split('\t')[0] not in wordCount:
            wordCount[line.split('\t')[0]] = 1
        else:
            wordCount[line.split('\t')[0]]+=1
    f.close()

    with open(inputFile, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in wordCount.items():
            writer.writerow([key, value])

    
if __name__ == "__main__":
    main(sys.argv[1])