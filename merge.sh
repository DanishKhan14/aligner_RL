#!/usr/bin/env bash

for f in "$@"
do
    (cat "$f"; echo) >> 'mergedFile.csv'
done
