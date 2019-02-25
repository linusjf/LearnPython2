name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 * 2.54  # cms
weight = 180.0/2.205 # kgs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %0.2f cms tall." % height
print "He's %0.2f kilos  heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it 
# exactly right
print "If I add %d, %0.2f, and %0.2f I get %0.2f." % (age, height, weight, age + height + weight)
