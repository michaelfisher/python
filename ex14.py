from sys import argv

script, fn, ln = argv
prompt = '$> '

print "Hi, %s %s! I'm the %s script." % (fn, ln, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % fn
likes = raw_input(prompt)

print "Where do you live, %s?" % fn
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print '''
Alright, you said %r about liking me.
You live in %r. Not sure where that is.
And, you have a %r...Nice
''' % (likes, lives, computer)