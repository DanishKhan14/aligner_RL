#!/bin/bash

mkdir ~/aligner
cd ~/aligner

wget https://sourceforge.net/projects/bowtie-bio/files/bowtie/1.1.2/bowtie-1.1.2-macos-x86_64.zip && unzip bowtie-1.1.2-macos-x86_64.zip
rm -rf bowtie-1.1.2-macos-x86_64.zip
mv bowtie-1.1.2 bowtie

cd bowtie

#if [[ -d ~/bowtie/aligner_RL ]]
#then
    git clone https://github.com/DanishKhan14/aligner_RL.git
    cp ./aligner_RL/align.py ./
    cp ./aligner_RL/align.py ./
    cp ./aligner_RL/create_db.py ./
    cp ./aligner_RL/output.py ./
#    exit;
#fi
