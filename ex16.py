from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you don't wat to do that, press [CTL]+C."
print "If you want to do that, press [ENTER]."

raw_input("> ")

print "Opening the file..."
target = open(filename, 'w')

#print "Truncating the file. Goodbye, file!"
#target.truncate()

print "Now, I'm going to as you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

target.write("%s\n%s\n%s\n" % (line1, line2, line3))
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "Now, I'll close the file."
target.close()

