import sys, optparse, errno, re, codecs, os

def imdbref(argv):
	"""
	create a .dot-file from imdb's movie-links.list
	"""

	parser = optparse.OptionParser(
		usage='Usage: %prog [options]',
		description="create a .dot-file from imdb's movie-links.list",
		version="%prog 0.1"
	)
	parser.add_option(	"-f", "--file", default="movie-links.list", help="file to process [default: %default]")

	(options, args) = parser.parse_args(argv[1:])

	if options.file == None:
		parser.print_help()
		sys.exit(-1)

	else:
		names = []
		lines = []
		connections = []

		# generate {movie list file}.utf8
		os.system("iconv -f iso-8859-1 -t UTF-8 "+options.file+" > "+options.file+".utf8")

		f = codecs.open( options.file +'.utf8', encoding='utf-8' )
		for line in f:
			line = line.encode('utf-8', 'replace')
			if line[0] == "\"":
				if re.search("{", line): # Skip TV-episodes
					pass
				elif re.search("\(TV\)", line): # Skip (TV)
					pass
				else:
					#title = repr(line)
					title = line
			elif re.search("referenced in", line):
				if re.search("{", line): # Skip TV-episodes
					pass
				elif re.search("\(TV\)", line): # Skip (TV)
					pass
				elif re.search("\(V\)", line): # Skip (V)
					pass
				elif re.search("\(VG\)", line): # Skip (VG)
					pass
				elif re.search("lgyi\-show \(1991\)", line): # Skip (VG)
					pass
				else:
					title = title.replace("\"", "")
					title = title.replace("\"", "")
					refer = line.replace("referenced in", "")
					refer = refer.replace("(", "", 1)
					refer = refer.replace("))", ")")
					refer = refer.replace("\"", "")

					# Titles and referers into the names-list
					title = title.strip()
					refer = refer.strip()

					if title not in names:
						names.append(title)
					if refer not in names:
						names.append(refer)

					names = sort2(names) # remove duplicates, the hard way

					# Let's get the title and refer index number from the names-list
					id_title = names.index(title)
					id_refer = names.index(refer)


					# We use the already defined names list to make the file smaller
					normal_line = "\t"+str(id_title)+" <- "+str(id_refer)+";"
					revers_line = "\t"+str(id_refer)+" <- "+str(id_title)+";"
					if revers_line or normal_line not in lines: # no dublicates
						if id_title is not id_refer and normal_line is not revers_line:
							if id_title != 6025 and id_refer != 6025:
								# We get occurances
								connections.append( id_title )
								connections.append( id_refer )
								# Add the line itself
								lines.append(normal_line)
			else:
				pass
		else:
			pass


		os.remove( options.file +'.utf8' ) # We get rid of the temp file


		used = []

		if True:
			print "graph imdb {" # start the project
			print '    node [shape=plaintext fontsize="7" fontname="Arial"]'

			# loop the names
			for i, name in enumerate(names):
				c = connections.count(i)
				if c > 10:
					print "    " + str(i) + ' [label="' + str(name) + '" priority="' + str(c) + '"];'
					used.append( i )

			print
			print "// used: " + str(used)
			print
			# loop the connections
			for i, line in enumerate(lines):
				s = re.findall("([0-9]+)", line)
				if any(x in s for x in used): # wtf?
					print "//", s, 'not found in used'
				else:
					print line

			print "}"




def sort2(seq): # Dave Kirby
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]



if __name__ == '__main__':
	imdbref(sys.argv)