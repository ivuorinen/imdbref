#!/usr/bin/env bash

# if no movie-links.list then download from
# ftp://ftp.funet.fi//.m/mirrors1l/ftp.imdb.com/pub/movie-links.list.gz
# and decompress

FILENAME=$(date +%Y-%m-%d);
# process and create .dot
python imdbref.py > $FILENAME.dot
# remove old
rm $FILENAME.png
# do the image from the .dot
twopi $FILENAME.dot -Tpng -v -o $FILENAME.png
