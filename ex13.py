# argc hold variable you pass to the python script
from sys import argv

# next line does unpacking
# Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order.
script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third