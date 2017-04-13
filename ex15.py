from sys import argv
sc, fi =argv
txt =open(fi)
print "That's what inside the %r file"%fi
print txt.read()
