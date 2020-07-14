#!/usr/bin/env bash

if [ -n "$1" ]; then

	FROM=iso-8859-1
	TO=UTF-8
	iconv -f $FROM -t $TO $1 > $1.utf8

	# process and create .dot
	python process.py -f $1.utf8 > $1.dot

	# do the image from the .dot
	#dot $1.dot -Tpng -v -o $1.png

	# iconv -f original_charset -t utf-8 originalfile > newfile
else
	echo "source needed"
fi
