from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print "Copying %s to %s..." % (from_file, to_file)

#in_file = open(from_file)
#in_data = in_file.read()
in_data = open(from_file).read()

#print "The input file is %s bytes long." % len(in_data)

#print "Does the output file exist? %r" % exists(to_file)
#print "Press [ENTER] to continue or [CTL]+C to abort."
#raw_input()

out_file = open(to_file, 'w')
out_file.write(in_data) 

#print "Alright, all done."

out_file.close()
#in_file.close()
