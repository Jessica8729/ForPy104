# create a mapping of state to abbreviation
states = {
	'Oregan': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'

# print out some cities
print (cities ['MI'])
print (states ['New York'])
