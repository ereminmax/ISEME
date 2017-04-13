filename='ex16_sample.txt'
print "We're going to erase %r."%filename
print "If you don't want that, hit CTRL-C"
print "If you do want that, hit RETURN"
raw_input(">")
print "Opening the file..."
target=open(filename,'w')
print "Truncating..."
target.truncate()
print "Now I'm going to ask you for three lines"
l1=raw_input(">")
l2=raw_input('>')
l3=raw_input('>')
target.write(l1)
target.write(l2)
target.write(l3)
print "Writing..."
target.close()
