# create a mapping of state to abbreviation
states = {
	'Orgeon' : 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '_' * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

# print some states
print '_' * 10
print "Michigan's abbrevation is: ", states['Michigan']
print "Florida's abbrevation is: ", states['Florida']

# do it by using the state then cities dict
print "_" * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print "_" * 10
for state, abbrev in states.items():
	print "%s is abbreviated as %s" % (state, abbrev)

# print every city in state
print "_" * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (state, abbrev)

# now do both at the same time
print '_' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '_' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX','Does not Exists')
print "The city for the state 'TX' is: %s" % city