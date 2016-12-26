#!/bin/bash

echo "Installing COPRO-Seq Pipeline in current working directory ..."

unamestr=`uname`
if [[ -d ./bowtie ]]; then
    echo "Bowtie Already Exists ...Updating Wrapper Scripts Only ...."
elif [[ "$unamestr" == 'Linux' ]]; then
    wget https://sourceforge.net/projects/bowtie-bio/files/bowtie/1.1.2/bowtie-1.1.2-macos-x86_64.zip && unzip bowtie-1.1.2-macos-x86_64.zip
    rm -rf bowtie-1.1.2-macos-x86_64.zip
    mv bowtie-1.1.2 bowtie
elif [[ "$unamestr" == 'Darwin' ]]; then
    wget https://sourceforge.net/projects/bowtie-bio/files/bowtie/1.1.2/bowtie-1.1.2-macos-x86_64.zip && unzip bowtie-1.1.2-macos-x86_64.zip
    rm -rf bowtie-1.1.2-macos-x86_64.zip
    mv bowtie-1.1.2 bowtie
fi

cd bowtie

if ! [[ -d ./aligner_RL ]]; then
    git clone https://github.com/DanishKhan14/aligner_RL.git
    cp ./aligner_RL/align.py ./
    cp ./aligner_RL/align.py ./
    cp ./aligner_RL/create_db.py ./
    cp ./aligner_RL/output.py ./
    exit;
fi

mkdir output stats suppressed unmatched


