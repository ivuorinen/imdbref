#!/usr/bin/env bash

FILENAME=$(date +%Y-%m-%d);
# process and create .dot
python imdbref.py > $FILENAME.dot
# remove old
rm $FILENAME.png
# do the image from the .dot
twopi $FILENAME.dot -Tpng -v -o $FILENAME.png
