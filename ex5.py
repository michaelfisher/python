my_name = 'Michael L. Fisher'
my_age = 30 #Years
my_height = 74 #Inches
my_height_feet = my_height / 12
my_height_feet_inches = my_height % 12
my_height_centimeters = my_height * 2.54
my_height_meters = my_height_centimeters / 100.0
my_weight = 195 #Pounds
my_weight_kilograms = my_weight * 0.453592
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "That's", my_height_feet, "feet", my_height_feet_inches, "inches tall."
print "That's %d centimeters tall." % my_height_centimeters
print "That's %.2f meters tall" % my_height_meters
print
print "He weighs %d pounds." % my_weight
print "That's %.2f kilograms." % my_weight_kilograms
print
print "He's got %s eyes, and %s hair." % ( my_eyes, my_hair )
print "His teeth are usually %s, depending on how much coffee he's consumed." % my_teeth
print