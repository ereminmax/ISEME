states={
    'Oregon': 'OR',
    'Florida': 'FL'
}
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
cities['NY']='New York'
cities['OR']='Portland'
print '-'*10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

print '-'*5
print "Oregon has: ", cities[states['Oregon']]
print "Florida has: ", cities[states['Florida']]

for state, abbrev in states.items():
    print state, abbrev

for abbrev, city in cities.items():
    print abbrev, city

for state, abbrev in states.items():
    print state, abbrev, cities[abbrev]

state = states.get('Saratov')

if not state:
    print "Sorry, no Saratov"

city = cities.get('SA', 'Does not exist')
print city
