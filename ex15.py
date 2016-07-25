from sys import argv

# Get file name from the command prompt
script, filename = argv

# Open the file reture file object
txt = open(filename)

print "Here's your file %r:" % filename
# Read the contents of the file
print txt.read()

# closing the file object
txt.close()

print "Type the filename again:"
file_again = raw_input('> ')

txt_again = open(file_again)

print txt_again.read()

txt_again.close()