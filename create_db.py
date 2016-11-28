#!/usr/bin/python

import os
import sys
import glob
import subprocess

def main(argv):
    indexName = argv[-1]
    files = []
    for f in argv:
        filePath = os.path.abspath(f)
        if os.path.exists(filePath):
            files.append(filePath)
        else:
            print "File does not exist: " + f

    #TODO: Create Path  Objects for each file. List of path objects
    
    genomeFileList = ",".join(argv[:-1])
    print genomeFileList

    #Cocat and Rename
    renameHeaders(argv[:-1])

    #Create DB
    print "Creating combined database for entered genomes .... \n"
    createIndex(genomeFileList, indexName)


def renameHeaders(fileList):
    #TODO: Might go pythonic way to make platform independent
    for seqFile in fileList:
        #Removing all headers to create one single sequence
        cmd =  'grep -v ">" ' + seqFile + ' > temp; mv temp ' + seqFile
        cmdList = [cmd]
        subprocess.call(cmd, shell=True) 

        #Adding the modified header
        #cmd = 'sed -i.bu \"1i ' + seqFile.rsplit( ".", 1 )[ 0 ] + "\" " + seqFile   
        #print cmd
        #subprocess.call(cmd, shell=True)f = open("path_to_file", "r")
        f = open(seqFile, "r")
        contents = f.readlines()
        f.close()

        header = os.path.basename(seqFile)

        print header

        contents.insert(0, (">" + header.rsplit( ".", 1 )[ 0 ]+"\n"))

        f = open(seqFile, "w")
        contents = "".join(contents)
        f.write(contents)
        f.close()

    print "Done Renaming Headers ... \n"

def createIndex(genomeFileList, indexName):

    cmdList = ['./bowtie-build', genomeFileList, indexName]   
    subprocess.call(cmdList) 

    print "Index was created successfully for " + indexName

if __name__ == "__main__":
    main(sys.argv[1:])