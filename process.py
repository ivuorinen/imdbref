import codecs, re, sys

print "graph imdblinks {" # start the project
print

f = codecs.open( 'movie-links.list.utf8', encoding='utf-8' )
for line in f:
    
    line = line.encode('utf-8', 'replace')
    
    if line[0] == "\"":
        if re.search("{", line): # Skip TV-episodes
            pass
        else:
            #title = repr(line)
            title = line
    elif re.search("referenced in", line):
        if re.search("{", line): # Skip TV-episodes
            pass
        else:
            title = title.replace("\"", "")
            title = title.replace("\"", "")
            refer = line.replace("referenced in", "")
            refer = refer.replace("(", "", 1)
            refer = refer.replace("))", ")")
            refer = refer.replace("\"", "")
            
            title = "\"" + title.strip() + "\""
            refer = "\"" + refer.strip() + "\""
            
            print "\t"+title, "--", refer+";"
    else:
        pass

print
print "}"
