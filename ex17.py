from os.path import exists
from_file='ex15_sample.txt'
to_file='ex16_sample.txt'
print "Copying from %s to %s"%(from_file,to_file)
in_file=open(from_file)
indata=in_file.read()
print "Does the output file exists? %r"%exists(to_file)
raw_input("Press RETURN")
out_file=open(to_file,'w')
out_file.write(indata)
print "Done"
out_file.close()
in_file.close()
