#Building more complicated data structures

'''This exercise takes various parts of a name and then returns a dicionary.'''

def build_person(first_name, last_name):
	'''Return a dictionary of information about a person'''
	person = {'first': first_name, 'last': last_name}
	return person

musician = build_person('jimi','hendrix')
print(musician)

'''If we know the keys, can we format better?'''

print(musician['first'].title() + " " + musician['last'].title())